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

    def display_plots(self, featureCreator:FeatureCreatorBase, categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays a plot comparing the average of a feature for each category"""
        for name, allFilesPoints in categories:
            pointsAverages = []
            for trajectoryPoints in allFilesPoints:
                feature  = featureCreator.get_features(trajectoryPoints)
                avgOfFeature = self._get_average_of_feature(feature)
                pointsAverages.append(avgOfFeature)
            plt.scatter(range(len(pointsAverages)), pointsAverages, label=name)
        
        title = ""
        for name, allFilesPoints in categories:
            title += name + ", "
        title += str(featureCreator) + " comparison"
        plt.title(title)
        plt.ylabel(str(featureCreator))
        plt.legend()
        plt.show()
        