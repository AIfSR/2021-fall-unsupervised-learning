from typing import List, Tuple
import numpy as np
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
        for features in featuresList:
            if len(features) == 2:
                yFeatureGenerator, xFeatureGenerator = features
                yLabel = "Average: " + str(yFeatureGenerator)
                xLabel = "Average: " + str(xFeatureGenerator)
            else:
                yFeatureGenerator, xFeatureGenerator, yLabel, xLabel = features
            plt.close()
            categoryCount = 0
            if xFeatureGenerator == None:
                xFeatureGenerator = LineFeatureCreator()
                plt.tick_params(
                    axis='x',          # changes apply to the x-axis
                    which='both',      # both major and minor ticks are affected
                    bottom=False,      # ticks along the bottom edge are off
                    top=False,         # ticks along the top edge are off
                    labelbottom=False)
            left, width = 0.1, 0.65
            bottom, height = 0.1, 0.65
            spacing = 0.005
            rect_scatter = [left, bottom, width, height]
            rect_histx = [left, bottom + height + spacing, width, 0.2]
            rect_histy = [left + width + spacing, bottom, 0.2, height]
            fig = plt.figure()
            ax_scatter = plt.axes(rect_scatter)
            ax_scatter.tick_params(direction='in', top=True, right=True)
            ax_histx = plt.axes(rect_histx)
            ax_histx.tick_params(direction='in', labelbottom=False)
            ax_histy = plt.axes(rect_histy)
            ax_histy.tick_params(direction='in', labelleft=False)
                  
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
            
                # plt.scatter(xPointsAverages, yPointsAverages, label=name)
                ax_scatter.scatter(xPointsAverages, yPointsAverages, label=name)
                
                binwidth = 0.25
                lim = np.ceil(np.abs([xPointsAverages, yPointsAverages]).max() / binwidth) * binwidth
                # ax_scatter.set_xlim((-lim, lim))
                # ax_scatter.set_ylim((-lim, lim))

                # bins = np.arange(-lim, lim + binwidth, binwidth)
                ax_histx.hist(xPointsAverages)
                ax_histy.hist(yPointsAverages, orientation='horizontal')
                ax_histx.set_ylabel("Number of Trajectories", fontsize = 8)
                ax_histy.set_xlabel("Number of Trajectories", fontsize = 8)

                # ax_histx.set_xlim(ax_scatter.get_xlim())
                # ax_histy.set_ylim(ax_scatter.get_ylim())

            title = ""
            for name, allFilesPoints in categories:
                title += name + ", "
            if not type(xFeatureGenerator) == LineFeatureCreator:
                # plt.xlabel(xLabel)
                ax_scatter.set_xlabel(xLabel)
                title += str(yFeatureGenerator) + " vs. " + str(xFeatureGenerator) + " comparison"
            else:
                title += str(yFeatureGenerator)

            # plt.ylabel(yLabel)
            ax_scatter.set_ylabel(yLabel)
            fig.suptitle(title)
            fig.legend()
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
