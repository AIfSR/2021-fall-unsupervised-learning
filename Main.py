from typing import List
from features.MarkWhenFeatureValuesChange import MarkWhenFeatureValuesChange
from features.OutlierFeatureCreator import OutlierFeatureCreator
from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator 
from features.ABSFeatureCreator import ABSFeatureCreator
from features.EWAFeatureCreator import EWAFeatureCreator
from features.EliminatePointsOutsideRangeFeatureCreator import EliminatePointsOutsideRangeFeatureCreator
from features.FeatureCreatorBase import FeatureCreatorBase
from features.PhiFeatureCreator import PhiFeatureCreator
from features.PointsAngleFeatureCreator import PointsAngleFeatureCreator
from features.RaiseToPowerFeatureCreator import RaiseToPowerFeatureCreator
from features.SignChangeFeatureCreator import SignChangeFeatureCreator
from features.SpreadFeatureCreator import SpreadFeatureCreator
from features.ThetaFeatureCreator import ThetaFeatureCreator
from features.XYSpeedFeatureCreator import XYSpeedFeatureCreator
from features.XYZSpeedFeatureCreator import XYZSpeedFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from featuretosingleval.MedianOfFeature import MedianOfFeature
from plotting.GraphParameters import GraphParameters
from plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories
from plotting.TwoDComparePlots import TwoDComparePlots
from plotting.singlepointcomparetrajectories.SinglePointCompareTrajectoriesFactory import SinglePointCompareTrajectoriesFactory
import numpy
import matplotlib.pyplot as plt

from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from features.PointsDisplacementFeatureCreator import PointsDisplacementFeatureCreator
from tckfilereader.Points import Points
from tckfilereader.TCKFileReader import TCKFileReader

import FilePaths as FP

if __name__ == "__main__":
    tckFileReader = TCKFileReader()
    plotFeatures = [
        GraphParameters(
            xFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())), 
            yFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), 
            yLabel = "Average: Y Speed",
            xLabel = "Average: X Speed"),
        GraphParameters(
            xFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())), 
            yFeatureCreator=ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), 
            featuresToSingleVal=MedianOfFeature()),
        GraphParameters(
            xFeatureCreator=PointsAngleFeatureCreator(),
            yFeatureCreator=RateOfChangeFeatureCreator(PointsDistanceFeatureCreator())),    
        GraphParameters(
            xFeatureCreator=PointsAngleFeatureCreator()),
        GraphParameters(
            xFeatureCreator=PointsAngleFeatureCreator(),
            featuresToSingleVal=MedianOfFeature()),
    ]
    
    def getPointsFromFilePaths(filePaths:List[str]) -> List[Points]:
        """Gets valid Points from a list of file paths"""
        pointsList = []
        for file in filePaths:
            points = tckFileReader.get_points(file)
            if len(points) > 50:
                pointsList.append(points)
        return pointsList
    
    m0Points = getPointsFromFilePaths(FP.m0FilePaths)
    m1Points = getPointsFromFilePaths(FP.m1FilePaths)
    m2Points = getPointsFromFilePaths(FP.m2FilePaths)
    
    stageCategories = [
        ("M0", m0Points),
        ("M1", m1Points),
        ("M2", m2Points),
    ]

    singlePoint2DCompareTrajectoriesFactory = SinglePointCompareTrajectoriesFactory()
    singlePoint2DCompareTrajectoriesFactory.display_plots(plotFeatures, stageCategories)


