from typing import List, Tuple

from matplotlib import pyplot as plt
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.XFeatureCreator import XFeatureCreator
from plotting.ComparePlotsBase import ComparePlotsBase
from tckfilereader.Points import Points

class SinglePointCompareTrajectories (ComparePlotsBase):

    def _get_average_of_feature(self, feature:Features) -> float:
        """Gets the average of a feature"""
        count = 0
        sum = 0
        for featureVal in feature:
            sum += featureVal
            count += 1
        return sum / count

    def _get_max_of_feature(self, feature:Features) -> float:
        """Gets the maximum value of a feature"""
        return max(feature)

    def _get_median_of_feature(self, feature:Features) -> float:
        """Gets the median value of a feature"""
        sortedListFeature = sorted(feature.to_list())
        return sortedListFeature[len(sortedListFeature) // 2]

    def _get_std_dev_of_feature(self, feature:Features) -> float:
        """Gets the standard deviation of a feature"""
        avg = self._get_average_of_feature(feature)
        sum = 0
        count = 0
        for featureVal in feature:
            sum += (featureVal - avg)**2
            count +=1
        stdDev = (sum/count)**0.5
        return stdDev

    def display_plots(self, featuresList:List[Tuple[Features, Features]], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays plots comparing the average of a feature for each category"""
        for yFeatureGenerator, xFeatureGenerator in featuresList:
            categoryCount = 0
            xFeatureGenerator = xFeatureGenerator or LineFeatureCreator()
            for name, allFilesPoints in categories:
                if(type(xFeatureGenerator) == LineFeatureCreator):
                    xFeatureGenerator.increment()
                categoryCount += 1
                xPointsAverages = []
                yPointsAverages = []
                for trajectoryPoints in allFilesPoints:
                    xFeature = xFeatureGenerator.get_features(trajectoryPoints)
                    yFeature = yFeatureGenerator.get_features(trajectoryPoints)
                    xAvgOfFeature = self._get_average_of_feature(xFeature)
                    yAvgOfFeature = self._get_average_of_feature(yFeature)
                    xPointsAverages.append(xAvgOfFeature)
                    yPointsAverages.append(yAvgOfFeature)
                plt.scatter(xPointsAverages, yPointsAverages, label=name)
            
            title = ""
            for name, allFilesPoints in categories:
                title += name + ", "
            if not type(xFeatureGenerator) == LineFeatureCreator:
                plt.xlabel("Average: " + str(xFeatureGenerator))
                title += str(yFeatureGenerator) + " vs. " + str(xFeatureGenerator) + " comparison"
            else:
                title += str(yFeatureGenerator)
                
            plt.ylabel("Average: " + str(yFeatureGenerator))
            plt.title(title)
            plt.legend()
            plt.show()
        
class LineFeatureCreator (FeatureCreatorBase):

    def __init__(self) -> None:
        super().__init__()
        self._val = 0.0

    def increment(self):
        self._val += 1

    def get_features(self, points:Points) -> Features:
        """Creates a feature with only 0s so the scatter plot is a strait line"""
        feature = Features()
        for point in points:
            feature.add_feature_val(self._val)
        return feature

    def __str__(self) -> str:
        return ""

