from typing import Dict, List, Tuple
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.XFeatureCreator import XFeatureCreator
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from plotting.ComparePlotsBase import ComparePlotsBase
from tckfilereader.Points import Points
from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator

class SinglePointCompareTrajectories (ComparePlotsBase):

    LEFT = 0.065
    WIDTH = 0.615
    BOTTOM = 0.05
    HEIGHT = 0.6
    SPACING = 0.005

    def __init__(self, featureToSingleVal:FeatureToSingleValBase) -> None:
        super().__init__()
        self._featureToSingleVal = featureToSingleVal

    def display_plots(self, featuresList:List[Tuple[Features, Features]], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays plots comparing the average of a feature for each category"""
        for features in featuresList:
            plt.close()
            if not self.is_labels_included(features):
                yFeatureGenerator, xFeatureGenerator = features
                yLabel = "Average: " + str(yFeatureGenerator)
                xLabel = "Average: " + str(xFeatureGenerator)
            else:
                yFeatureGenerator, xFeatureGenerator, yLabel, xLabel = features
            
            if self.is_data_one_dimension(xFeatureGenerator):
                self.plot_one_dimention_feature(categories, yFeatureGenerator, yLabel)
            else:
                self.plot_two_dimention_features(categories, yFeatureGenerator, xFeatureGenerator, yLabel, xLabel)

    def is_labels_included(self, features:Tuple):
        """Gets whether the labels for each feature are included in the tuple"""
        return len(features) == 4
    
    def is_data_one_dimension(self, xFeatureGenerator:FeatureCreatorBase):
        """If the xFeature generator is not None that means that the data is two dimensional"""
        return xFeatureGenerator is None or type(xFeatureGenerator) == LineFeatureCreator
    
    def get_rid_of_x_ticks(self) -> None:
        """Gets rid of the ticks along the x Axis for graphs that are not two dimensional"""
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False
        )
    def plot_one_dimention_feature(self, categories:List[Tuple[str,List[Points]]], featureCreator:FeatureCreatorBase, label:str) -> None:
        """Takes the feature creator base and plots the averages of 
        this feature for every trajectory"""


    def plot_two_dimention_features(self, categories:List[Tuple[str,List[Points]]], yFeatureCreator:FeatureCreatorBase, xFeatureCreator:FeatureCreatorBase, yLabel:str, xLabel:str) -> None:
        """Takes the two feature creator bases and plots the averages 
        of there features against one another for every trajectory"""
        fig = plt.figure(figsize=(16, 7.5))
        ax_scatter, histogramDict = self.create_graph_and_histogram_sections(categories)
        histBinsDict = self.plot_2D_data_and_hists(categories, ax_scatter, histogramDict, xFeatureCreator, yFeatureCreator)
        self.set_hist_size_and_labels(histBinsDict, histogramDict, ax_scatter)
        ax_scatter.set_ylabel(yLabel)
        ax_scatter.set_xlabel(xLabel)
        fig.suptitle(self.get_graph_title(categories, yLabel, xLabel))
        fig.legend(prop={"size":20})
        plt.show()

    def create_graph_and_histogram_sections(self, categories:List[Tuple[str,List[Points]]]) -> Tuple[Axes, Dict]:
        """Creates the sections of the figure for the graphs and for the histograms. 
        Returns the scatter plot axis and a dictionary with all of the histograms created"""

        histDict = {}
        left = SinglePointCompareTrajectories.LEFT
        bottom = SinglePointCompareTrajectories.BOTTOM
        width = SinglePointCompareTrajectories.WIDTH
        height = SinglePointCompareTrajectories.HEIGHT
        spacing = SinglePointCompareTrajectories.SPACING
        
        rect_scatter = [left, bottom, width, height]
        ax_scatter = plt.axes(rect_scatter)
        ax_scatter.tick_params(direction='in', top=True, right=True)

        numberOfHistsPerAxis = len(categories)
        i = 0
        histHeight = self.calculate_hist_height(numberOfHistsPerAxis)
        for name, _ in categories:
            rect_hist_x = [left, bottom + height + (spacing * (i + 1)) + (histHeight * i), width, histHeight]
            rect_hist_y = [left + width + (spacing * (i + 1)) + (histHeight * i), bottom, histHeight, height]
            ax_hist_x = plt.axes(rect_hist_x)
            ax_hist_x.tick_params(direction='in', labelbottom=False)
            ax_hist_y = plt.axes(rect_hist_y)
            ax_hist_y.tick_params(direction='in', labelleft=False)
            histDict[name + " X"] = ax_hist_x
            histDict[name + " Y"] = ax_hist_y
            i += 1

        return ax_scatter, histDict

    def calculate_hist_height(self, numberOfHistsPerAxis):
        bottom = SinglePointCompareTrajectories.BOTTOM
        height = SinglePointCompareTrajectories.HEIGHT
        spacing = SinglePointCompareTrajectories.SPACING
        spaceForHists = 1.0 - bottom * 2 - height
        spaceForSingleHist = spaceForHists / numberOfHistsPerAxis
        height = spaceForSingleHist - spacing
        return height


    def plot_2D_data_and_hists(self, categories:List[Tuple[str,List[Points]]], ax_scatter:Axes, histogramDict:Dict,  xFeatureCreator:FeatureCreatorBase, yFeatureCreator:FeatureCreatorBase) -> Dict:
        """Plots the data passed in in two dimensions on the scatterplot, and the histograms"""
        histBinsDict = {}
        for name, allFilesPoints in categories:
            xPointsAverages = []
            yPointsAverages = []
            for trajectoryPoints in allFilesPoints:
                xFeature = xFeatureCreator.get_features(trajectoryPoints)
                yFeature = yFeatureCreator.get_features(trajectoryPoints)
                xAvgOfFeature = self._featureToSingleVal.get_val(xFeature)
                yAvgOfFeature = self._featureToSingleVal.get_val(yFeature)
                xPointsAverages.append(xAvgOfFeature)
                yPointsAverages.append(yAvgOfFeature)
            
            s = ax_scatter.scatter(xPointsAverages, yPointsAverages, label=name)
            
            histBinsDict[name + " X"] = histogramDict[name + " X"].hist(xPointsAverages, color = s.get_ec())
            histBinsDict[name + " Y"] = histogramDict[name + " Y"].hist(yPointsAverages, orientation='horizontal', color = s.get_ec())
        return histBinsDict

    def set_hist_size_and_labels(self, histBinsDict:Dict, histogramDict:Dict, ax_scatter:Axes) -> None:
        """Sets the labels for each of the histograms"""
        xRanges = []
        yRanges = []
        for histName in histBinsDict:
            binHeights, _, _ = histBinsDict[histName]
            maxBinVal = max(binHeights)
            if(histName[-1:] == "X"):
                xRanges.append(maxBinVal) 
            else:
                yRanges.append(maxBinVal)
        xRange = max(xRanges)
        yRange = max(yRanges)
        for histName in histogramDict:
            hist = histogramDict[histName]
            if(histName[-1:] == "X"):
                hist.set_ylabel("Trajectories", fontsize = 8)
                hist.set_ylim([0,xRange + 1])
                hist.set_xlim(ax_scatter.get_xlim())
            else:
                hist.set_xlabel("Trajectories", fontsize = 8)
                hist.set_xlim([0,yRange + 1])
                hist.set_ylim(ax_scatter.get_ylim())

    def get_graph_title(self, categories:List[Tuple[str,List[Points]]], yLabel:str, xLabel:str) -> str:
        """Gets the name of the graph."""
        title = ""
        for name, allFilesPoints in categories:
            title += name + ", "
        
        title += str(yLabel) + " vs. " + str(xLabel) + " comparison"
        return title

        

