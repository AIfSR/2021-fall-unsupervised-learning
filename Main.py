from typing import List
from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator
from features.EWAFeatureCreator import EWAFeatureCreator
from features.SignChangeFeatureCreator import SignChangeFeatureCreator
from features.XYSpeedFeatureCreator import XYSpeedFeatureCreator
from plotting.SinglePointCompareTrajectories import SinglePointCompareTrajectories
from plotting.TwoDComparePlots import TwoDComparePlots
import numpy
import matplotlib.pyplot as plt

from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from tckfilereader.Points import Points
from tckfilereader.TCKFileReader import TCKFileReader

m0FilePaths = [
    "data/0_4h/M0/2020-08-05_16-45-01,168_.tck",
    "data/0_4h/M0/2020-08-05_17-21-46,888_.tck",
    "data/0_4h/M0/2020-08-05_18-11-44,490_.tck",
    "data/0_4h/M0/2020-12-02_14-49-41,154_.tck",
    "data/0_4h/M0/2020-12-02_15-58-23,371_.tck",
    "data/0_4h/M0/2020-12-02_16-41-18,342_.tck",

    "data/0_24h/M0/2020-12-17_10-20-56,683_.tck",
    "data/0_24h/M0/2020-12-17_13-02-13,789_.tck",
    "data/0_24h/M0/2020-12-17_11-07-35,778_.tck",

    "data/24h_4h/M0/2020-09-24_15-31-22,100_.tck",
    "data/24h_4h/M0/2020-09-24_17-00-57,463_.tck",
    "data/24h_4h/M0/2020-09-24_16-16-27,474_.tck",
    "data/24h_4h/M0/2020-11-12_16-12-49,016_.tck",

    "data/24h_24h/M0/2020-10-23_18-48-03,252_.tck",
    "data/24h_24h/M0/2020-10-23_19-16-43,054_.tck",
    "data/24h_24h/M0/2020-11-13_09-56-18,599_.tck",
]


m1FilePaths = [
    "data/0_4h/M1/2020-08-05_18-51-50,514_.tck",
    "data/0_4h/M1/2020-08-05_19-18-08,801_.tck",
    "data/0_4h/M1/2020-08-05_20-12-39,857_.tck",
    "data/0_4h/M1/2020-08-05_20-44-17,610_.tck",
    "data/0_4h/M1/2020-08-05_21-48-48,900_.tck",
    "data/0_4h/M1/2020-08-05_22-33-50,826_.tck",

    "data/0_24h/M1/2020-08-06_16-00-42,831_.tck",
    "data/0_24h/M1/2020-08-06_17-07-43,536_.tck",
    "data/0_24h/M1/2020-08-06_16-28-09,982_.tck",
    "data/0_24h/M1/2020-08-06_17-44-38,166_.tck",

    "data/24h_4h/M1/2020-11-12_20-01-59,972_.tck",
    "data/24h_4h/M1/2020-11-12_20-51-02,405_.tck",
    "data/24h_4h/M1/2020-11-12_21-23-17,103_.tck",

    "data/24h_24h/M1/2020-08-27_15-47-02,026_.tck",
    "data/24h_24h/M1/2020-08-27_17-07-16,954_.tck",
    "data/24h_24h/M1/2020-08-27_18-19-30,067_.tck",
    "data/24h_24h/M1/2020-11-05_18-18-55,017_.tck",
    "data/24h_24h/M1/2020-11-13_14-34-21,558_.tck",
]

m2FilePaths = [
    "data/0_4h/M2/2020-12-02_17-08-21,199_.tck",
    "data/0_4h/M2/2020-12-02_17-50-33,515_.tck",
    "data/0_4h/M2/2020-12-02_18-56-04,307_.tck",
    "data/0_4h/M2/2020-12-16_20-05-05,492_.tck",
    "data/0_4h/M2/2020-12-16_21-53-37,370_.tck",
    "data/0_4h/M2/2020-12-16_22-54-31,916_.tck",

    "data/0_24h/M2/2020-12-03_16-27-23,050_.tck",
    "data/0_24h/M2/2020-12-03_16-55-34,539_.tck",
    "data/0_24h/M2/2020-12-03_20-03-25,144_.tck",
    "data/0_24h/M2/2020-12-17_15-12-12,655_.tck",
    "data/0_24h/M2/2020-12-17_16-12-44,462_.tck",
    "data/0_24h/M2/2020-12-17_16-52-18,642_.tck",

    "data/24h_4h/M2/2020-12-10_19-19-16,045_.tck",
    "data/24h_4h/M2/2020-12-10_19-54-26,923_.tck",
    "data/24h_4h/M2/2020-12-10_21-40-27,025_.tck",
    "data/24h_4h/M2/2020-12-10_22-37-02,878_.tck",

    "data/24h_24h/M2/2020-12-11_18-08-48,051_.tck",
    "data/24h_24h/M2/2020-12-11_18-41-12,360_.tck",
    "data/24h_24h/M2/2020-12-11_19-15-07,942_.tck",
]

def printAverageVelocity(files:List, title=""):
    def getAverageOfAbsFeature(feature):
        count = 0
        sum = 0
        for featureVal in feature:
            sum += abs(featureVal)
            count += 1
        return sum / count
    fileCount = 0
    xSpeedAvgs = []
    ySpeedAvgs = []
    zSpeedAvgs = []
    distanceAvgSum = 0
    for file in files:
        points = tckFileReader.get_points(file)
        if len(points) < 50:
            continue
        xVelocity = RateOfChangeFeatureCreator(XFeatureCreator()).get_features(points)
        yVelocity = RateOfChangeFeatureCreator(YFeatureCreator()).get_features(points)
        zVelocity = RateOfChangeFeatureCreator(ZFeatureCreator()).get_features(points)
        distance = PointsDistanceFeatureCreator().get_features(points)
        fileCount += 1
        xSpeedAvgs.append(getAverageOfAbsFeature(xVelocity))
        ySpeedAvgs.append(getAverageOfAbsFeature(yVelocity))
        zSpeedAvgs.append(getAverageOfAbsFeature(zVelocity))
        distanceAvgSum += getAverageOfAbsFeature(distance)
    xSpeedAvg = sum(xSpeedAvgs) / fileCount
    ySpeedAvg = sum(ySpeedAvgs) / fileCount
    zSpeedAvg = sum(zSpeedAvgs) / fileCount
    distanceAvgSum = distanceAvgSum / fileCount
    print("Average X speed: " + str(xSpeedAvg))
    print("Average Y speed: " + str(ySpeedAvg))
    print("Average Z speed: " + str(zSpeedAvg))
    print("Average Total Speed (X,Y): " + str((xSpeedAvg**2 + ySpeedAvg**2)**0.5))
    print("Distance Average: " + str(distanceAvgSum / fileCount))
    
    print("-----------------------")

if __name__ == "__main__":
    tckFileReader = TCKFileReader()
    beta = 0.25
    plotFeatures = [
        # (RateOfChangeFeatureCreator(XFeatureCreator()), TFeatureCreator()),
        # (RateOfChangeFeatureCreator(YFeatureCreator()), TFeatureCreator()),
        # (RateOfChangeFeatureCreator(ZFeatureCreator()), TFeatureCreator()),
        # (EWAFeatureCreator(RateOfChangeFeatureCreator(PointsDistanceFeatureCreator())), TFeatureCreator()),
        # (EWAFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), EWAFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator()))),
        # (EWAFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator())), EWAFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator()))),
        # (EWAFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), EWAFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator()))),
        # (DeltaFromStartFeatureCreator(EWAFeatureCreator(XFeatureCreator(), beta)), TFeatureCreator()),
        # (DeltaFromStartFeatureCreator(EWAFeatureCreator(YFeatureCreator(), beta)), TFeatureCreator()),
        # (DeltaFromStartFeatureCreator(EWAFeatureCreator(ZFeatureCreator(), beta)), TFeatureCreator()),
        # (DeltaFromStartFeatureCreator(EWAFeatureCreator(YFeatureCreator(), beta)), DeltaFromStartFeatureCreator(EWAFeatureCreator(XFeatureCreator(), beta))),
        # (DeltaFromStartFeatureCreator(EWAFeatureCreator(ZFeatureCreator(), beta)), DeltaFromStartFeatureCreator(EWAFeatureCreator(XFeatureCreator(), beta))),
        # (DeltaFromStartFeatureCreator(EWAFeatureCreator(YFeatureCreator(), beta)), DeltaFromStartFeatureCreator(EWAFeatureCreator(ZFeatureCreator(), beta))),
        # (ZFeatureCreator(), TFeatureCreator()),
        # (DeltaFromStartFeatureCreator(XFeatureCreator()), TFeatureCreator()),
        # (DeltaFromStartFeatureCreator(YFeatureCreator()), TFeatureCreator()),
        (XYSpeedFeatureCreator(), None),
        # (SignChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())), None),
        # (SignChangeFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), None),
        # (SignChangeFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator())), None),
        
        #(SignChangeFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), SignChangeFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator()))),
        #(SignChangeFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), SignChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator()))),
        #(SignChangeFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator())), SignChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator()))),

        # (XFeatureCreator(), YFeatureCreator()),
        # (DeltaFromStartFeatureCreator(XFeatureCreator()), DeltaFromStartFeatureCreator(YFeatureCreator())),
    ]
    def getPointsFromFilePaths(filePaths:List[str]) -> List[Points]:
        """Gets valid Points from a list of file paths"""
        pointsList = []
        for file in filePaths:
            points = tckFileReader.get_points(file)
            if len(points) > 50:
                pointsList.append(points)
        return pointsList
    
    m0Points = getPointsFromFilePaths(m0FilePaths)
    m1Points = getPointsFromFilePaths(m1FilePaths)
    m2Points = getPointsFromFilePaths(m2FilePaths)
    
    categories = [
        ("M0", m0Points),
        ("M1", m1Points),
        ("M2", m2Points),
    ]

    # twoDComparePlots = TwoDComparePlots()
    # twoDComparePlots.display_plots(plotFeatures, categories)
    singlePointCompareTrajectories = SinglePointCompareTrajectories()
    singlePointCompareTrajectories.display_plots(plotFeatures, categories)
    # print("M0")
    # printAverageVelocity(m0FilePaths, "M0")
    # print("M1")
    # printAverageVelocity(m1FilePaths, "M1")
    # print("M2")
    # printAverageVelocity(m2FilePaths, "M2")


