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
            left, width = 0.05, 0.6
            bottom, height = 0.05, 0.6
            spacing = 0.005
            rect_scatter = [left, bottom, width, height]

            # rect_histx = [left, bottom + height + spacing, width, 0.095]
            rect_hist_m0_x = [left, bottom + height + spacing, width, 0.095]
            rect_hist_m1_x = [left, bottom + height + spacing + spacing + 0.095, width, 0.095]
            rect_hist_m2_x = [left, bottom + height + spacing + spacing + 0.095 + spacing + 0.095, width, 0.095]

            # rect_histy = [left + width + spacing, bottom, 0.095, height]
            rect_hist_m0_y = [left + width + spacing, bottom, 0.095, height]
            rect_hist_m1_y = [left + width + spacing + spacing + 0.095, bottom, 0.095, height]
            rect_hist_m2_y = [left + width + spacing + spacing + 0.095 + spacing + 0.095 , bottom, 0.095, height]

            fig = plt.figure()
            ax_scatter = plt.axes(rect_scatter)
            ax_scatter.tick_params(direction='in', top=True, right=True)

            ax_hist_m0_x = plt.axes(rect_hist_m0_x)
            ax_hist_m0_x.tick_params(direction='in', labelbottom=False)
            ax_hist_m1_x = plt.axes(rect_hist_m1_x)
            ax_hist_m1_x.tick_params(direction='in', labelbottom=False)
            ax_hist_m2_x = plt.axes(rect_hist_m2_x)
            ax_hist_m2_x.tick_params(direction='in', labelbottom=False)

            ax_hist_m0_y = plt.axes(rect_hist_m0_y)
            ax_hist_m0_y.tick_params(direction='in', labelleft=False)
            ax_hist_m1_y = plt.axes(rect_hist_m1_y)
            ax_hist_m1_y.tick_params(direction='in', labelleft=False)
            ax_hist_m2_y = plt.axes(rect_hist_m2_y)
            ax_hist_m2_y.tick_params(direction='in', labelleft=False)
                  
            for name, allFilesPoints in categories:
                if(type(xFeatureGenerator) == LineFeatureCreator):
                    xFeatureGenerator.increment()
                categoryCount += 1
                xPointsAverages = []
                yPointsAverages = []
                m0_xPointsAverages = []
                m0_yPointsAverages = []
                m1_xPointsAverages = []
                m1_yPointsAverages = []
                m2_xPointsAverages = []
                m2_yPointsAverages = []
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
                if name == "M0":
                    ax_hist_m0_x.hist(xPointsAverages)
                    ax_hist_m0_y.hist(yPointsAverages, orientation='horizontal')
                if name == "M1":
                    ax_hist_m1_x.hist(xPointsAverages, color="orange")
                    ax_hist_m1_y.hist(yPointsAverages, orientation='horizontal' , color="orange")
                if name == "M2":
                    ax_hist_m2_x.hist(xPointsAverages, color="green")
                    ax_hist_m2_y.hist(yPointsAverages, orientation='horizontal', color="green")

                ax_hist_m0_x.set_ylabel("Trajectories", fontsize = 8)
                ax_hist_m0_y.set_xlabel("Trajectories", fontsize = 8)
                ax_hist_m1_x.set_ylabel("Trajectories", fontsize = 8)
                ax_hist_m1_y.set_xlabel("Trajectories", fontsize = 8)
                ax_hist_m2_x.set_ylabel("Trajectories", fontsize = 8)
                ax_hist_m2_y.set_xlabel("Trajectories", fontsize = 8)

                # ax_histx.set_xlim(ax_scatter.get_xlim())
                # ax_histy.set_ylim(ax_scatter.get_ylim())
                # ax_hist_m0_x.set_xlim(ax_scatter.get_xlim())
                ax_hist_m0_x.set_ylim([0,8])
                ax_hist_m1_x.set_ylim([0,8])
                ax_hist_m2_x.set_ylim([0,8])
                ax_hist_m0_y.set_xlim([0,8])
                ax_hist_m1_y.set_xlim([0,8])
                ax_hist_m2_y.set_xlim([0,8])
                ax_hist_m0_x.set_xlim(ax_scatter.get_xlim())
                ax_hist_m0_y.set_ylim(ax_scatter.get_ylim())
                ax_hist_m1_x.set_xlim(ax_scatter.get_xlim())
                ax_hist_m1_y.set_ylim(ax_scatter.get_ylim())
                ax_hist_m2_x.set_xlim(ax_scatter.get_xlim())
                ax_hist_m2_y.set_ylim(ax_scatter.get_ylim())

            title = ""
            for name, allFilesPoints in categories:
                title += name + ", "
            if not type(xFeatureGenerator) == LineFeatureCreator:
                # plt.xlabel(xLabel)
                ax_scatter.set_xlabel(xLabel)
                # title += str(yFeatureGenerator) + " vs. " + str(xFeatureGenerator) + " comparison"
                title += str(yLabel) + " vs. " + str(xLabel) + " comparison"
            else:
                # title += str(yFeatureGenerator)
                title += str(yLabel)

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
