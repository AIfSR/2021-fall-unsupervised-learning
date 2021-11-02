import unittest
import FindBestFeatures
from FindBestFeatures import LabeledVector
import numpy as np
import Main
from features.SpeedOverDistanceFeatureCreator import SpeedOverDistanceFeatureCreator
from features.DeviationsFromMeanFeatureCreator import DeviationsFromMeanFeatureCreator
from features.MaxMinDifferenceOfFeature import MaxMinDifferenceOfFeature
from features.PhiFeatureCreator import PhiFeatureCreator
from features.YFeatureCreator import YFeatureCreator
import pytest

class FindBestFeaturesTest (unittest.TestCase):
    def test_5(self):
        self.assertEquals(5, 5)

    def test_contents_of_lists_the_same(self):
        lst1 = [
            LabeledVector("M0", np.array([1,2,3])),
            LabeledVector("M2", np.array([4,5,6])),
            LabeledVector("M3", np.array([7,8,9])),
        ]

        lst2 = [
            LabeledVector("M2", np.array([4,5,6])),
            LabeledVector("M3", np.array([7,8,9])),
            LabeledVector("M0", np.array([1,2,3])),
        ]

        self.assertTrue(FindBestFeatures.contents_of_lists_the_same(lst1, lst2))

    def test_predictTrajectoryGroupsUsingKMeans(self):
        allLabeledVectors = []
        combinationOfCreators = (DeviationsFromMeanFeatureCreator(SpeedOverDistanceFeatureCreator()), MaxMinDifferenceOfFeature((PhiFeatureCreator())))
        for stageName, listOfPoint in Main.stageCategories:
            for points in listOfPoint:
                allLabeledVectors.append(FindBestFeatures.create_labeled_vector(combinationOfCreators, stageName, points))
        nameList = [str(featureCreator) for featureCreator in combinationOfCreators]
        name = ""
        for elem in nameList:
            name += elem + ", "
        for i in range(5):
            FindBestFeatures.predictTrajectoryGroupsUsingKMeans(allLabeledVectors, name)
        
        self.assertEquals(name, "std_dev:SpeedOverDistance, Range:Phi, ")

