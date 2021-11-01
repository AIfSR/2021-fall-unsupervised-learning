from typing import Tuple
import Main
from features.ABSFeatureCreator import ABSFeatureCreator
from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator
from features.DeviationsFromMeanFeatureCreator import DeviationsFromMeanFeatureCreator
from features.DisplacementDirectionContribution import DisplacementDirectionContribution
from features.EliminatePointsOutsideRangeFeatureCreator import EliminatePointsOutsideRangeFeatureCreator
from features.Features import Features
import itertools
import numpy as np
import random
from features.MarkWhenFeatureValuesChange import MarkWhenFeatureValuesChange
from features.MaxMinDifferenceOfFeature import MaxMinDifferenceOfFeature
from features.OutlierFeatureCreator import OutlierFeatureCreator
from features.PhiFeatureCreator import PhiFeatureCreator
from features.PointsAngleFeatureCreator import PointsAngleFeatureCreator
from features.PointsDisplacementFeatureCreator import PointsDisplacementFeatureCreator
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.SignChangeFeatureCreator import SignChangeFeatureCreator
from features.SpeedOverDistanceFeatureCreator import SpeedOverDistanceFeatureCreator
from features.SpreadFeatureCreator import SpreadFeatureCreator
from features.ThetaFeatureCreator import ThetaFeatureCreator
from features.XFeatureCreator import XFeatureCreator
from features.XYCurvatureFeatureCreator import XYCurvatureFeatureCreator
from features.XYSpeedFeatureCreator import XYSpeedFeatureCreator
from features.XYZSpeedFeatureCreator import XYZSpeedFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator

independentFeatureCreators = [
    XFeatureCreator(),
    YFeatureCreator(),
    ZFeatureCreator(),
    ThetaFeatureCreator(),
    PhiFeatureCreator(),
    DisplacementDirectionContribution(),
    PointsAngleFeatureCreator(),
    PointsDistanceFeatureCreator(),
    SpeedOverDistanceFeatureCreator(),
    SpreadFeatureCreator(),
    XYCurvatureFeatureCreator(),
    XYSpeedFeatureCreator(),
    XYZSpeedFeatureCreator(),
]
dependentFeatureCreators = [
    ABSFeatureCreator,
    DeltaFromStartFeatureCreator,
    DeviationsFromMeanFeatureCreator,
    MarkWhenFeatureValuesChange,
    MaxMinDifferenceOfFeature,
    RateOfChangeFeatureCreator,
    SignChangeFeatureCreator,
]
specialFeatureCreators = [
    OutlierFeatureCreator,
    EliminatePointsOutsideRangeFeatureCreator,
    PointsDisplacementFeatureCreator,
]

def create_all_feature_creators():
    allFeatureCreators = independentFeatureCreators[:]
    for dependentFeatureCreator in dependentFeatureCreators:
        for nonDependentFeatureCreator in independentFeatureCreators:
            allFeatureCreators.append(dependentFeatureCreator(nonDependentFeatureCreator))
    for specialFeatureCreator in specialFeatureCreators:
        for nonDependentFeatureCreator in independentFeatureCreators:
            if specialFeatureCreator == OutlierFeatureCreator:
                outlierVals = [1.5, 2.0]
                for val in outlierVals:
                    allFeatureCreators.append(OutlierFeatureCreator(nonDependentFeatureCreator, val))
            if specialFeatureCreator == EliminatePointsOutsideRangeFeatureCreator:
                ranges = [(0.0, 0.5), (0.5, 1.0), (0.25, 0.75)]
                for range in ranges:
                    allFeatureCreators.append(EliminatePointsOutsideRangeFeatureCreator(range[0], range[1], nonDependentFeatureCreator))
            if specialFeatureCreator == PointsDisplacementFeatureCreator:
                allFeatureCreators.append(PointsDisplacementFeatureCreator())

    return allFeatureCreators

allFeatureCreators = create_all_feature_creators()


def _get_average_of_feature(feature:Features) -> float:
    """Gets the average of a feature"""
    count = 0
    sum = 0
    for featureVal in feature:
        sum += featureVal
        count += 1
    if count == 0:
        print("Uh oh")
    return sum / count

class LabeledVector:
    def __init__(self, label, vector) -> None:
        self.label = label
        self.vector = vector

    def __eq__(self, o: object) -> bool:
        return self.label == o.label and np.array_equiv(self.vector, o.vector)
    
    def __repr__(self) -> str:
        return self.label + ": " + str(self.vector)

def get_list_of_all_combinations_of_i_creators(i):
    return list(itertools.combinations(allFeatureCreators, i))

def create_labeled_vector(combinationOfCreators, name, points):
    lst = []
    for featureCreator in combinationOfCreators:
        features = featureCreator.get_features(points)
        pointAverage = _get_average_of_feature(features)
        lst.append(pointAverage)
    vector = np.array(lst)
    return LabeledVector(name, vector)

def contents_of_lists_the_same(list1, list2):
    if not len(list1) == len(list2):
        return False
    for val in list1:
        if not val in list2:
            return False
    for val in list2:
        if not val in list1:
            return False
    return True

def calculate_mean(groupOfLabeledVectors):
    if len(groupOfLabeledVectors) == 0:
        return 0
    sum = np.zeros(groupOfLabeledVectors[0].vector.shape)
    count = 0
    for labeledVector in groupOfLabeledVectors:
        sum += labeledVector.vector
        count += 1
    return sum / count

def get_m0_m1_m2_score(groups:Tuple) -> float:
    total = len(groups[0]) + len(groups[1]) + len(groups[2])
    numCorrect = 0
    for labeledVector in groups[0]:
        if labeledVector.label == "M0":
            numCorrect += 1
    for labeledVector in groups[1]:
        if labeledVector.label == "M1":
            numCorrect += 1
    for labeledVector in groups[2]:
        if labeledVector.label == "M2":
            numCorrect += 1
    return numCorrect / total


def get_stage_groups(groupOne, groupTwo, groupThree):
    groupsList = [groupOne, groupTwo, groupThree]
    permutations = list(itertools.permutations(groupsList))
    scores = [get_m0_m1_m2_score(permutation) for permutation in permutations]
    maxScore = max(scores)
    index = scores.index(maxScore)
    return permutations[index]

def predictTrajectoryGroupsUsingKMeans(allLabeledVectors, name=""):
    groupOne = []
    groupTwo = []
    groupThree = []
    centers = random.sample(allLabeledVectors, 3)
    centerOne = centers[0].vector
    centerTwo = centers[1].vector
    centerThree = centers[2].vector
    done = False
    loops = 0
    while not done:
        newGroupOne = []
        newGroupTwo = []
        newGroupThree = []
        for labeledVector in allLabeledVectors:
            centerOneDistance = np.linalg.norm(labeledVector.vector - centerOne)
            centerTwoDistance = np.linalg.norm(labeledVector.vector - centerTwo)
            centerThreeDistance = np.linalg.norm(labeledVector.vector - centerThree)
            if centerOneDistance <= centerTwoDistance and centerOneDistance <= centerThreeDistance:
                newGroupOne.append(labeledVector)
            elif centerTwoDistance <= centerOneDistance and centerTwoDistance <= centerThreeDistance:
                newGroupTwo.append(labeledVector)
            else:
                newGroupThree.append(labeledVector)
        if(contents_of_lists_the_same(groupOne, newGroupOne) and contents_of_lists_the_same(newGroupTwo, groupTwo) and contents_of_lists_the_same(newGroupThree, groupThree)):
            done = True
        groupOne = newGroupOne
        groupTwo = newGroupTwo
        groupThree = newGroupThree

        centerOne = calculate_mean(groupOne)
        centerTwo = calculate_mean(groupTwo)
        centerThree = calculate_mean(groupThree)

        #Very messy code to take care of what to do if one group becomes completely empty
        if len(groupOne) == 0:
            if len(groupTwo) == 0:
                centerOne = centerThree
            centerOne = centerTwo
        if len(groupTwo) == 0:
            if len(groupThree) == 0:
                centerTwo = centerOne
            centerTwo = centerThree
        if len(groupThree) == 0:
            if len(groupOne) == 0:
                centerThree = centerTwo
            centerThree = centerOne

        loops += 1
        if(loops % 500 == 0):
            print(name)
            print("Loops: " + str(loops))
    
    m0group, m1group, m2group = get_stage_groups(groupOne, groupTwo, groupThree)
    return m0group, m1group, m2group


if __name__ == "__main__":
    for index in range(1, 6):
        listOfAllCombinationsOfICreators = get_list_of_all_combinations_of_i_creators(index)
        scoresDict = {}
        count = 0 
        total = len(listOfAllCombinationsOfICreators)
        printCount = total // 25
        for combinationOfCreators in listOfAllCombinationsOfICreators:
            nameList = [str(featureCreator) for featureCreator in combinationOfCreators]
            name = ""
            for elem in nameList:
                name += elem + ", "
            allLabeledVectors = []
            for stageName, listOfPoint in Main.stageCategories:
                for points in listOfPoint:
                    allLabeledVectors.append(create_labeled_vector(combinationOfCreators, stageName, points))
            bestProportionCorrect = 0.0
            for j in range(3):
                trajectoryGroups = predictTrajectoryGroupsUsingKMeans(allLabeledVectors, name)
                proportionCorrect = get_m0_m1_m2_score(trajectoryGroups)
                if proportionCorrect > bestProportionCorrect:
                    bestProportionCorrect = proportionCorrect
            
            scoresDict[name] = bestProportionCorrect
            if count % printCount == 0:
                print(str(count) + "/" + str(total))
            count +=1
        maxScore = scoresDict[name]
        maxScoreName = name
        for comboName in scoresDict:
            if scoresDict[comboName] > maxScore:
                maxScoreName = comboName
                maxScore = scoresDict[comboName]
        
        print("For i = " + str(index))
        print("The best combo was: " + maxScoreName)
        print("with a percent correct of: " + str(maxScore))
        print("----------------")