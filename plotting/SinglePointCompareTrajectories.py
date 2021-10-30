from typing import List, Tuple

from matplotlib import pyplot as plt
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
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

    def display_plots(self, features:Tuple[Features, Features], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays a plot comparing the average of a feature for each category"""
        for name, allFilesPoints in categories:
            xPointsAverages = []
            yPointsAverage = []
            for trajectoryPoints in allFilesPoints:
                xfeature = features[0].get_features(trajectoryPoints)
                yfeature = features[1].get_features(trajectoryPoints)
                xAvgOfFeature = self._get_average_of_feature(xfeature)
                yAvgOfFeature = self._get_average_of_feature(yfeature)
                xPointsAverages.append(xAvgOfFeature)
                yPointsAverage.append(yAvgOfFeature)
            plt.scatter(xPointsAverages, yPointsAverage, label=name)
        
        title = ""
        for name, allFilesPoints in categories:
            title += name + ", "
        title += str(features[0]) + str(features[1]) + " comparison"
        plt.title(title)
        plt.xlabel(str(features[0]))
        plt.ylabel(str(features[1]))
        plt.legend()
        plt.show()
        