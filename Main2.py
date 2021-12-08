from typing import List
from features.MarkWhenFeatureValuesChange import MarkWhenFeatureValuesChange
from features.OutlierFeatureCreator import OutlierFeatureCreator
from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator
from features.EpisodesABSFeatureCreator import EpisodesABSFeatureCreator
from features.EWAFeatureCreator import EWAFeatureCreator
# from features.EliminateEpisodesOutsideRangeFeatureCreator import EliminateEpisodesOutsideRangeFeatureCreator
from features.FeatureCreatorBase import FeatureCreatorBase
from features.PhiFeatureCreator import PhiFeatureCreator
# from features.EpisodesAngleFeatureCreator import EpisodesAngleFeatureCreator
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
from plotting.singleepisodecomparetrajectories.SingleEpisode2DCompareTrajectories import SingleEpisode2DCompareTrajectories
from plotting.TwoDComparePlots import TwoDComparePlots
from plotting.singleepisodecomparetrajectories.SingleEpisodeCompareTrajectoriesFactory import SingleEpisodeCompareTrajectoriesFactory

import numpy
import matplotlib.pyplot as plt

from features.NFeatureCreator import NFeatureCreator
from features.OccFeatureCreator import OccFeatureCreator
from features.DurationFeatureCreator import DurationFeatureCreator
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.EpisodesRateOfChangeFeatureCreator import EpisodesRateOfChangeFeatureCreator
# from features.EpisodesDistanceFeatureCreator import EpisodesDistanceFeatureCreator
# from features.EpisodesDisplacementFeatureCreator import EpisodesDisplacementFeatureCreator
from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.XLSXFileReader import XLSXFileReader
Control_Dark_postFilePaths = [
    "data/Data_MS3/Control_Dark_post/M1EEGVIII_Dark_post.xlsx",
    "data/Data_MS3/Control_Dark_post/M2EEGII_Dark_post.xlsx",
    "data/Data_MS3/Control_Dark_post/M2EEGIV_Dark_post.xlsx",
    "data/Data_MS3/Control_Dark_post/M2EEGVIII_Dark_post.xlsx",
    "data/Data_MS3/Control_Dark_post/M3EEGIV_Dark_post.xlsx",
    "data/Data_MS3/Control_Dark_post/M4EEGV_Dark_post.xlsx",
]
Control_Dark_preFilePaths = [
    "data/Data_MS3/Control_Dark_pre/M1EEGI_Dark_pre.xlsx",
    "data/Data_MS3/Control_Dark_pre/M1EEGVIII_Dark_pre.xlsx",
    "data/Data_MS3/Control_Dark_pre/M2EEGII_Dark_pre.xlsx",
    "data/Data_MS3/Control_Dark_pre/M2EEGIV_Dark_pre.xlsx",
    "data/Data_MS3/Control_Dark_pre/M2EEGVIII_Dark_pre.xlsx",
    "data/Data_MS3/Control_Dark_pre/M3EEGIV_Dark_pre.xlsx",
    "data/Data_MS3/Control_Dark_pre/M4EEGV_Dark_pre.xlsx"
]

Control_Light_postFilePaths = [
    "data/Data_MS3/Control_Light_post/M1EEGI_Light_post.xlsx",
    "data/Data_MS3/Control_Light_post/M1EEGVIII_Light_post.xlsx",
    "data/Data_MS3/Control_Light_post/M2EEGII_Light_post.xlsx",
    "data/Data_MS3/Control_Light_post/M2EEGIV_Light_post.xlsx",
    "data/Data_MS3/Control_Light_post/M2EEGVIII_Light_post.xlsx",
    "data/Data_MS3/Control_Light_post/M3EEGIV_Ligtht_post.xlsx",
    "data/Data_MS3/Control_Light_post/M4EEGV_Light_post.xlsx"
]

Control_Light_preFilePaths = [
    "data/Data_MS3/Control_Light_pre/M1EEGI_Light_pre.xlsx",
    "data/Data_MS3/Control_Light_pre/M1EEGVIII_Light_pre.xlsx",
    "data/Data_MS3/Control_Light_pre/M2EEGII_Light_pre.xlsx",
    "data/Data_MS3/Control_Light_pre/M2EEGIV_Light_pre.xlsx",
    "data/Data_MS3/Control_Light_pre/M2EEGVIII_Light_pre.xlsx",
    "data/Data_MS3/Control_Light_pre/M3EEGIV_Light_pre.xlsx",
    "data/Data_MS3/Control_Light_pre/M4EEGV_Light_pre.xlsx",
]

ControlFilePaths = Control_Dark_postFilePaths[:]
ControlFilePaths.extend(Control_Dark_preFilePaths[:])
ControlFilePaths.extend(Control_Light_postFilePaths[:])
ControlFilePaths.extend(Control_Light_preFilePaths[:])

Resilient_Dark_postFilePaths = [
    "data/Data_MS3/Resilient_Dark_post/EEGVM3_Dark_post.xlsx",
    "data/Data_MS3/Resilient_Dark_post/M1EEGIII_Dark_post.xlsx",
    "data/Data_MS3/Resilient_Dark_post/M2EEGV_Dark_post.xlsx",
    "data/Data_MS3/Resilient_Dark_post/Mouse1EEGVII_Darkpost.xlsx",
    "data/Data_MS3/Resilient_Dark_post/Pilot1_Dark_post.xlsx",
]

Resilient_Dark_preFilePaths = [
    "data/Data_MS3/Resilient_Dark_pre/EEGVM3_Dark_pre.xlsx",
    "data/Data_MS3/Resilient_Dark_pre/M1EEGIII_Dark_pre.xlsx",
    "data/Data_MS3/Resilient_Dark_pre/M1EEGVII_Dark_pre.xlsx",
    "data/Data_MS3/Resilient_Dark_pre/M2EEGI_Dark_pre.xlsx",
    "data/Data_MS3/Resilient_Dark_pre/M2EEGV_Dark_pre.xlsx",
    "data/Data_MS3/Resilient_Dark_pre/M3EEGI_Dark_pre.xlsx",
    "data/Data_MS3/Resilient_Dark_pre/M4EEGI_Dark_pre.xlsx",
]

Resilient_Light_postFilePaths = [
    "data/Data_MS3/Resilient_Light_post/M1EEGIII_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/M1EEGVII_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/M2EEGI_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/M2EEGV_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/M3EEGI_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/M3EEGV_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/M4EEGI_Light_post.xlsx",
    "data/Data_MS3/Resilient_Light_post/Pilot1_Light_post.xlsx",
]

Resilient_Light_preFilePaths = [
    "data/Data_MS3/Resilient_Light_pre/EEGVM3_Light_pre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/M1EEGIII_Light_pre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/M1EEGVII_Light_pre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/M2EEGI_Light_pre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/M2EEGV_Light_pre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/M3EEGI_LightPre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/M4EEGI_Light_pre.xlsx",
    "data/Data_MS3/Resilient_Light_pre/Pilot1_Light_pre.xlsx"
]

ResilientFilePaths = Resilient_Dark_postFilePaths[:]
ResilientFilePaths.extend(Resilient_Dark_preFilePaths[:])
ResilientFilePaths.extend(Resilient_Light_postFilePaths[:])
ResilientFilePaths.extend(Resilient_Light_preFilePaths[:])

Susceptible_Dark_postFilePaths = [
    "data/Data_MS3/Susceptible_Dark_post/M1EEGII_Dark_post.xlsx",
    "data/Data_MS3/Susceptible_Dark_post/M1EEGIV_Dark_post.xlsx",
    "data/Data_MS3/Susceptible_Dark_post/M1EEGVI_Dark_post.xlsx",
    "data/Data_MS3/Susceptible_Dark_post/M2EEGVI_Dark_post.xlsx",
    "data/Data_MS3/Susceptible_Dark_post/M2EEGVII_Dark_post.xlsx",
    "data/Data_MS3/Susceptible_Dark_post/M3EEGII_Dark_post.xlsx",
    "data/Data_MS3/Susceptible_Dark_post/Pilot2_Dark_post.xlsx",
]

Susceptible_Dark_preFilePaths = [
    "data/Data_MS3/Susceptible_Dark_pre/M1EEGII_Dark_pre.xlsx",
    "data/Data_MS3/Susceptible_Dark_pre/M1EEGIV_Dark_pre.xlsx",
    "data/Data_MS3/Susceptible_Dark_pre/M1EEGVI_Dark_pre.xlsx",
    "data/Data_MS3/Susceptible_Dark_pre/M2EEGVI_Dark_pre.xlsx",
    "data/Data_MS3/Susceptible_Dark_pre/M2EEGVII_Dark_pre.xlsx",
    "data/Data_MS3/Susceptible_Dark_pre/M3EEGII_Dark_pre.xlsx",
    "data/Data_MS3/Susceptible_Dark_pre/Pilot2_Dark_pre.xlsx",
]

Susceptible_Light_postFilePaths = [
    "data/Data_MS3/Susceptible_Light_post/M1EEGII_Light_post.xlsx",
    "data/Data_MS3/Susceptible_Light_post/M1EEGIV_Light_post.xlsx",
    "data/Data_MS3/Susceptible_Light_post/M1EEGVI_Light_post.xlsx",
    "data/Data_MS3/Susceptible_Light_post/M2EEGVI_Light_post.xlsx",
    "data/Data_MS3/Susceptible_Light_post/M2EEGVII_Light_post.xlsx",
    "data/Data_MS3/Susceptible_Light_post/M3EEGII_Light_post.xlsx",
    "data/Data_MS3/Susceptible_Light_post/Pilot2_Light_post.xlsx"
]

Susceptible_Light_preFilePaths = [
    "data/Data_MS3/Susceptible_Light_pre/M1EEGII_Light_pre.xlsx",
    "data/Data_MS3/Susceptible_Light_pre/M1EEGIV_Light_pre.xlsx",
    "data/Data_MS3/Susceptible_Light_pre/M1EEGVI_Light_pre.xlsx",
    "data/Data_MS3/Susceptible_Light_pre/M2EEGVI_Light_pre.xlsx",
    "data/Data_MS3/Susceptible_Light_pre/M2EEGVII_Light_pre.xlsx",
    "data/Data_MS3/Susceptible_Light_pre/M3EEGII_Light_pre.xlsx",
    "data/Data_MS3/Susceptible_Light_pre/Pilot2_Light_pre.xlsx",
]

SusceptibleFilePaths = Susceptible_Dark_postFilePaths[:]
SusceptibleFilePaths.extend(Susceptible_Dark_preFilePaths[:])
SusceptibleFilePaths.extend(Susceptible_Light_postFilePaths[:])
SusceptibleFilePaths.extend(Susceptible_Light_preFilePaths[:])

filePathsDark = Control_Dark_postFilePaths[:]
filePathsDark.extend(Control_Dark_preFilePaths[:])
filePathsDark.extend(Resilient_Dark_postFilePaths[:])
filePathsDark.extend(Resilient_Dark_preFilePaths[:])
filePathsDark.extend(Susceptible_Dark_postFilePaths[:])
filePathsDark.extend(Susceptible_Dark_preFilePaths[:])

filePathsLight = Control_Light_postFilePaths[:]
filePathsLight.extend(Control_Light_preFilePaths[:])
filePathsLight.extend(Resilient_Light_postFilePaths[:])
filePathsLight.extend(Resilient_Light_preFilePaths[:])
filePathsLight.extend(Susceptible_Light_postFilePaths[:])
filePathsLight.extend(Susceptible_Light_preFilePaths[:])

filePathspre = Control_Dark_preFilePaths[:]
filePathspre.extend(Control_Light_preFilePaths[:])
filePathspre.extend(Resilient_Dark_preFilePaths[:])
filePathspre.extend(Resilient_Light_preFilePaths[:])
filePathspre.extend(Susceptible_Dark_preFilePaths[:])
filePathspre.extend(Susceptible_Light_preFilePaths[:])

filePathspost = Control_Dark_postFilePaths[:]
filePathspost.extend(Control_Light_postFilePaths[:])
filePathspost.extend(Resilient_Dark_postFilePaths[:])
filePathspost.extend(Resilient_Light_postFilePaths[:])
filePathspost.extend(Susceptible_Dark_postFilePaths[:])
filePathspost.extend(Susceptible_Light_postFilePaths[:])

Control_DarkfilePaths = Control_Dark_postFilePaths[:]
Control_DarkfilePaths.extend(Control_Dark_preFilePaths[:])

Control_LightfilePaths = Control_Light_postFilePaths[:]
Control_LightfilePaths.extend(Control_Light_preFilePaths[:])

Resilient_DarkfilePaths = Resilient_Dark_postFilePaths[:]
Resilient_DarkfilePaths.extend(Resilient_Dark_preFilePaths[:])

Resilient_LightfilePaths = Resilient_Light_postFilePaths[:]
Resilient_LightfilePaths.extend(Resilient_Light_preFilePaths[:])

Susceptible_DarkfilePaths = Susceptible_Dark_postFilePaths[:]
Susceptible_DarkfilePaths.extend(Susceptible_Dark_preFilePaths[:])

Susceptible_LightfilePaths = Susceptible_Light_postFilePaths[:]
Susceptible_LightfilePaths.extend(Susceptible_Light_preFilePaths[:])


# def printAverageVelocity(files:List, title=""):
#     def getAverageOfAbsFeature(feature):
#         count = 0
#         sum = 0
#         for featureVal in feature:
#             sum += abs(featureVal)
#             count += 1
#         return sum / count
#     fileCount = 0
#     xSpeedAvgs = []
#     ySpeedAvgs = []
#     zSpeedAvgs = []
#     distanceAvgSum = 0
#     displacementAvgSum = 0
#     for file in files:
#         episodes = xlsxFileReader.get_episodes(file)
#         if len(episodes) < 50:
#             continue
#         xVelocity = RateOfChangeFeatureCreator(XFeatureCreator()).get_features(episodes)
#         yVelocity = RateOfChangeFeatureCreator(YFeatureCreator()).get_features(episodes)
#         zVelocity = RateOfChangeFeatureCreator(ZFeatureCreator()).get_features(episodes)
#         distance = EpisodesDistanceFeatureCreator().get_features(episodes)
#         displacement = EpisodesDisplacementFeatureCreator().get_features(episodes)
#         fileCount += 1
#         xSpeedAvgs.append(getAverageOfAbsFeature(xVelocity))
#         ySpeedAvgs.append(getAverageOfAbsFeature(yVelocity))
#         zSpeedAvgs.append(getAverageOfAbsFeature(zVelocity))
#         distanceAvgSum += getAverageOfAbsFeature(distance)
#         displacementAvgSum += getAverageOfAbsFeature(displacement)
#     xSpeedAvg = sum(xSpeedAvgs) / fileCount
#     ySpeedAvg = sum(ySpeedAvgs) / fileCount
#     zSpeedAvg = sum(zSpeedAvgs) / fileCount
#     print("Average X speed: " + str(xSpeedAvg))
#     print("Average Y speed: " + str(ySpeedAvg))
#     print("Average Z speed: " + str(zSpeedAvg))
#     print("Average Total Speed (X,Y): " + str((xSpeedAvg**2 + ySpeedAvg**2)**0.5))
#     print("Distance Average: " + str(distanceAvgSum / fileCount))
#     print("Displacement Average: " + str(displacementAvgSum / fileCount))
#
#     print("-----------------------")

if __name__ == "__main__":
    xlsxFileReader = XLSXFileReader()
    beta = 0.9
    outlier = 2.0
    power = 3
    plotFeatures = [
        GraphParameters(
            xFeatureCreator=EpisodesABSFeatureCreator(EpisodesRateOfChangeFeatureCreator(OccFeatureCreator())),
            yFeatureCreator=EpisodesABSFeatureCreator(EpisodesRateOfChangeFeatureCreator(DurationFeatureCreator())),
            xLabel="Occ",
            yLabel="N"),
        GraphParameters(
            xFeatureCreator=EpisodesABSFeatureCreator(EpisodesRateOfChangeFeatureCreator(OccFeatureCreator())),
            yFeatureCreator=EpisodesABSFeatureCreator(EpisodesRateOfChangeFeatureCreator(DurationFeatureCreator())),
            featuresToSingleVal=MedianOfFeature()),
        # GraphParameters(
        #     xFeatureCreator=EpisodesAngleFeatureCreator(),
        #     yFeatureCreator=RateOfChangeFeatureCreator(EpisodesDistanceFeatureCreator())),
        # GraphParameters(
        #     xFeatureCreator=EpisodesAngleFeatureCreator()),
        GraphParameters(
            xFeatureCreator=NFeatureCreator(),
            featuresToSingleVal=MedianOfFeature()),
    ]

    # twoDPlotFeatures = [
    #     (EliminateEpisodesOutsideRangeFeatureCreator(0, 0.5, DeltaFromStartFeatureCreator(YFeatureCreator())), EliminateEpisodesOutsideRangeFeatureCreator(0, 0.5, DeltaFromStartFeatureCreator(XFeatureCreator()))),
    #     (EliminateEpisodesOutsideRangeFeatureCreator(0.5, 1.0, DeltaFromStartFeatureCreator(YFeatureCreator())), EliminateEpisodesOutsideRangeFeatureCreator(0.5, 1.0, DeltaFromStartFeatureCreator(XFeatureCreator()))),
    #     (EliminateEpisodesOutsideRangeFeatureCreator(0.25, 0.75, DeltaFromStartFeatureCreator(YFeatureCreator())), EliminateEpisodesOutsideRangeFeatureCreator(0.25, 0.75, DeltaFromStartFeatureCreator(XFeatureCreator()))),
    # ]

    def getEpisodesFromFilePaths(filePaths:List[str]) -> List[Episodes]:
        """Gets valid Episodes from a list of file paths"""
        episodesList = []
        for file in filePaths:
            episodes = xlsxFileReader.get_episodes(file)
            if len(episodes) > 50:
                episodesList.append(episodes)
        return episodesList

    ControlEpisodes = getEpisodesFromFilePaths(ControlFilePaths)
    ResilientEpisodes = getEpisodesFromFilePaths(ResilientFilePaths)
    SusceptibleEpisodes = getEpisodesFromFilePaths(SusceptibleFilePaths)

    episodesDark = getEpisodesFromFilePaths(filePathsDark)
    episodesLight = getEpisodesFromFilePaths(filePathsLight)
    episodesPre = getEpisodesFromFilePaths(filePathspre)
    episodesPost = getEpisodesFromFilePaths(filePathspost)

    stageCategories = [
        ("Control", ControlEpisodes),
        ("Resilient", ResilientEpisodes),
        ("Susceptible", SusceptibleEpisodes),
    ]

    LightCategories = [
        ("Dark", episodesDark),
        ("Light", episodesLight)
    ]

    time = [
        ("Pre", episodesPre),
        ("Post", episodesPost)
    ]

    allCategories = [
        ("Control_Dark_post", getEpisodesFromFilePaths(Control_Dark_postFilePaths)),
        ("Control_Dark_pre", getEpisodesFromFilePaths(Control_Dark_preFilePaths)),
        ("Control_Light_post", getEpisodesFromFilePaths(Control_Light_postFilePaths)),
        ("Control_Light_pre", getEpisodesFromFilePaths(Control_Light_preFilePaths)),

        ("Resilient_Dark_post", getEpisodesFromFilePaths(Resilient_Dark_postFilePaths)),
        ("Resilient_Dark_pre", getEpisodesFromFilePaths(Resilient_Dark_preFilePaths)),
        ("Resilient_Light_post", getEpisodesFromFilePaths(Resilient_Light_postFilePaths)),
        ("Resilient_Light_pre", getEpisodesFromFilePaths(Resilient_Light_preFilePaths)),

        ("Susceptible_Dark_post", getEpisodesFromFilePaths(Susceptible_Dark_postFilePaths)),
        ("Susceptible_Dark_pre", getEpisodesFromFilePaths(Susceptible_Dark_preFilePaths)),
        ("Susceptible_Light_post", getEpisodesFromFilePaths(Susceptible_Light_postFilePaths)),
        ("Susceptible_Light_pre", getEpisodesFromFilePaths(Susceptible_Light_preFilePaths)),
    ]

    twoDComparePlots = TwoDComparePlots()
    # twoDComparePlots.display_plots(twoDPlotFeatures, stageCategories)
    singleEpisode2DCompareTrajectoriesFactory = SingleEpisodeCompareTrajectoriesFactory()
    singleEpisode2DCompareTrajectoriesFactory.display_plots(plotFeatures, stageCategories)
    # SingleEpisode1DCompareTrajectories = SingleEpisode1DCompareTrajectories()
    # singleEpisodeCompareTrajectories.display_plots(plotFeatures, allCategories)
    # singleEpisodeCompareTrajectories.display_plots(plotFeatures, treatmentCategories)
    # print("M0")
    # printAverageVelocity(m0FilePaths, "M0")
    # print("M1")
    # printAverageVelocity(m1FilePaths, "M1")
    # print("M2")
    # printAverageVelocity(m2FilePaths, "M2")


