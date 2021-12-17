from typing import List
from features.genericfeatures.MarkWhenFeatureValuesChange import MarkWhenFeatureValuesChange
from features.genericfeatures.OutlierFeatureCreator import OutlierFeatureCreator
from features.genericfeatures.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator 
from features.genericfeatures.ABSFeatureCreator import ABSFeatureCreator
from features.genericfeatures.EWAFeatureCreator import EWAFeatureCreator
from features.genericfeatures.EliminatePointsOutsideRangeFeatureCreator import EliminatePointsOutsideRangeFeatureCreator
from features.FeatureCreatorBase import FeatureCreatorBase
from features.episodesfeatures.PercentageFeatureCreator import PercentageFeatureCreator
from features.pointsfeatures.PhiFeatureCreator import PhiFeatureCreator
from features.pointsfeatures.PointsAngleFeatureCreator import PointsAngleFeatureCreator
from features.genericfeatures.RaiseToPowerFeatureCreator import RaiseToPowerFeatureCreator
from features.genericfeatures.SignChangeFeatureCreator import SignChangeFeatureCreator
from features.pointsfeatures.SpreadFeatureCreator import SpreadFeatureCreator
from features.pointsfeatures.ThetaFeatureCreator import ThetaFeatureCreator
from features.pointsfeatures.XYSpeedFeatureCreator import XYSpeedFeatureCreator
from features.pointsfeatures.XYZSpeedFeatureCreator import XYZSpeedFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from featuretosingleval.MedianOfFeature import MedianOfFeature
from plotting.GraphParameters import GraphParameters
from plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories
from plotting.singlepointcomparetrajectories.SinglePointCompareTrajectoriesFactory import SinglePointCompareTrajectoriesFactory
import numpy
import matplotlib.pyplot as plt

from features.pointsfeatures.XFeatureCreator import XFeatureCreator
from features.pointsfeatures.YFeatureCreator import YFeatureCreator
from features.pointsfeatures.ZFeatureCreator import ZFeatureCreator
from features.pointsfeatures.TFeatureCreator import TFeatureCreator
from features.genericfeatures.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.pointsfeatures.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from features.pointsfeatures.PointsDisplacementFeatureCreator import PointsDisplacementFeatureCreator
from tckfilereader.Points import Points
from tckfilereader.TCKFileReader import TCKFileReader

import FilePaths as FP
from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.XLSXFileReader import XLSXFileReader

def getEpisodesFromFilePaths(filePaths:List[str]) -> List[Episodes]:
    """Gets valid Episodes from a list of file paths"""
    episodesList = []
    for file in filePaths:
        episodes = xlsxFileReader.get_episodes(file)
        episodesList.append(episodes)
    return episodesList

def getValidPointsFromFilePaths(filePaths:List[str]) -> List[Points]:
    """Gets valid Points from a list of file paths"""
    pointsList = []
    for file in filePaths:
        points = tckFileReader.get_points(file)
        if len(points) > 50:
            pointsList.append(points)
    return pointsList

if __name__ == "__main__":
    # A TCKFileReader object reads in .tck files and creates Points objects which are usable in this code base.
    tckFileReader = TCKFileReader()

    xlsxFileReader = XLSXFileReader()

    # PlotFeatures stores all of the GraphParameters associated with each desired graph. 
    # In this case there will be 5 graphs, the first one will plot the average X speed 
    # against the average Y speed of the trajectories passed in in a scatterplot, and the next two will 
    # plot similar 2 dimensional graphs but with different features for the X and Y axes.
    # The fourth GraphParameters object only has an xFeatureCreator set which means it will only 
    # plot one dimension in the form of a boxplot. The final GraphParameters object similarly only 
    # plots one dimension in the form of a boxplot but in this case it is taking the median value of 
    # the angle between points as opposed to the average value
    plotFeatures = [
        # GraphParameters(
        #     xFeatureCreator=XFeatureCreator(),
        # ),
        GraphParameters(
            xFeatureCreator=PercentageFeatureCreator("WK"),
            yFeatureCreator=PercentageFeatureCreator("SWS"),
            xLabel="Percentage of WK",
            yLabel="Percentage of SWS"),
        GraphParameters(
            xFeatureCreator=PercentageFeatureCreator("WK"),
            yFeatureCreator=PercentageFeatureCreator("PS"),
            xLabel="Percentage of WK",
            yLabel="Percentage of PS"),
        GraphParameters(
            xFeatureCreator=PercentageFeatureCreator("SWS"),
            yFeatureCreator=PercentageFeatureCreator("PS"),
            xLabel="Percentage of SWS",
            yLabel="Percentage of PS"),
        GraphParameters(
            xFeatureCreator=PercentageFeatureCreator("WK")),
        GraphParameters(
            xFeatureCreator=PercentageFeatureCreator("SWS")),
        GraphParameters(
            xFeatureCreator=PercentageFeatureCreator("PS")),

    ]
    
    m0Points = getValidPointsFromFilePaths(FP.m0FilePaths)
    m1Points = getValidPointsFromFilePaths(FP.m1FilePaths)
    m2Points = getValidPointsFromFilePaths(FP.m2FilePaths)
    
    # Specifies the three different categories of trajectories that are to be 
    # compared and the points list of points associated with each of these treajectory categories
    stageCategories = [
        ("M0", m0Points),
        ("M1", m1Points),
        ("M2", m2Points),
    ]

    ControlEpisodes = getEpisodesFromFilePaths(FP.ControlFilePaths)
    ResilientEpisodes = getEpisodesFromFilePaths(FP.ResilientFilePaths)
    SusceptibleEpisodes = getEpisodesFromFilePaths(FP.SusceptibleFilePaths)

    mouseCategories = [
        ("Control", ControlEpisodes),
        ("Resilient", ResilientEpisodes),
        ("Susceptible", SusceptibleEpisodes),
    ]

    # Takes all of the points and categories specified above in the stageCategories variable, 
    # and all of the different types of graphs specified above in the plotFeatures variable and 
    # creates all of the desired graphs one at a time.
    singlePoint2DCompareTrajectoriesFactory = SinglePointCompareTrajectoriesFactory()
    singlePoint2DCompareTrajectoriesFactory.display_plots(plotFeatures, mouseCategories)


