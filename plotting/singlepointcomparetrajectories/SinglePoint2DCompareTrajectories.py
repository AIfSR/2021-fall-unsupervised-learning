from typing import Dict, List, Tuple
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.XFeatureCreator import XFeatureCreator
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from plotting.ComparePlotsBase import ComparePlotsBase
from plotting.GraphParameters import GraphParameters
from tckfilereader.Points import Points
from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator

class SinglePoint2DCompareTrajectories (ComparePlotsBase):

    LEFT = 0.065
    WIDTH = 0.615
    BOTTOM = 0.05
    HEIGHT = 0.6
    SPACING = 0.025

    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays plots comparing single point values of a feature for each category"""
        for graphParameter in graphParameters:
            plt.close()
            self._plot_features(categories, graphParameter.yFeatureCreator, graphParameter.xFeatureCreator, graphParameter.yLabel, graphParameter.xLabel, graphParameter.featuresToSingleVal)
            plt.show()

    def _plot_features(self, categories:List[Tuple[str,List[Points]]], yFeatureCreator:FeatureCreatorBase, xFeatureCreator:FeatureCreatorBase, yLabel:str, xLabel:str, featuresToSingleVal:FeatureToSingleValBase) -> None:
        """Takes the two feature creator bases and plots the single point values 
        of their features against one another for every trajectory"""
        fig = plt.figure(figsize=(16, 7.5))
        ax_scatter, histogramDict = self._create_graph_and_histogram_sections(categories)
        histBinsDict = self._plot_2D_data_and_hists(categories, ax_scatter, histogramDict, xFeatureCreator, yFeatureCreator, featuresToSingleVal)
        self._set_hist_size_and_labels(histBinsDict, histogramDict, ax_scatter)
        ax_scatter.set_ylabel(yLabel)
        ax_scatter.set_xlabel(xLabel)
        fig.suptitle(self._get_graph_title(categories, yLabel, xLabel))
        fig.legend(prop={"size":20})
        

    def _create_graph_and_histogram_sections(self, categories:List[Tuple[str,List[Points]]]) -> Tuple[Axes, Dict]:
        """Creates the sections of the figure for the graphs and for the histograms. 
        Returns the scatter plot axis and a dictionary with all of the histograms created"""

        histDict = {}
        left = SinglePoint2DCompareTrajectories.LEFT
        bottom = SinglePoint2DCompareTrajectories.BOTTOM
        width = SinglePoint2DCompareTrajectories.WIDTH
        height = SinglePoint2DCompareTrajectories.HEIGHT
        
        rect_scatter = [left, bottom, width, height]
        ax_scatter = plt.axes(rect_scatter)
        ax_scatter.tick_params(direction='in', top=True, right=True)

        numberOfHistsPerAxis = len(categories)
        i = 0
        histHeight = self._calculate_hist_height(numberOfHistsPerAxis)
        for name, _ in categories:
            histDict[name + " X"] = self._create_hist_section("X", i, histHeight, ax_scatter)
            histDict[name + " Y"] = self._create_hist_section("Y", i, histHeight, ax_scatter)
            i += 1

        return ax_scatter, histDict

    def _create_hist_section(self, axis:str, i:int, histHeight:float, ax_scatter:Axes) -> Axes:
        """Creates the section of the figure for the histogram"""
        left = SinglePoint2DCompareTrajectories.LEFT
        bottom = SinglePoint2DCompareTrajectories.BOTTOM
        width = SinglePoint2DCompareTrajectories.WIDTH
        height = SinglePoint2DCompareTrajectories.HEIGHT
        spacing = SinglePoint2DCompareTrajectories.SPACING
        if axis == "X":
            rect_hist = [left, bottom + height + (spacing * (i + 1)) + (histHeight * i), width, histHeight]
            ax_hist = plt.axes(rect_hist, sharex=ax_scatter)
            ax_hist.tick_params(direction='in', labelbottom=False)
        else:
            rect_hist = [left + width + (spacing * (i + 1)) + (histHeight * i), bottom, histHeight, height]
            ax_hist = plt.axes(rect_hist, sharey=ax_scatter)
            ax_hist.tick_params(direction='in', labelleft=False)
        return ax_hist

    def _calculate_hist_height(self, numberOfHistsPerAxis:int) -> float:
        """Calculated the height of each histogram so that they fit within the figure."""
        bottom = SinglePoint2DCompareTrajectories.BOTTOM
        height = SinglePoint2DCompareTrajectories.HEIGHT
        spacing = SinglePoint2DCompareTrajectories.SPACING
        spaceForHists = 1.0 - bottom * 2 - height
        spaceForSingleHist = spaceForHists / numberOfHistsPerAxis
        height = spaceForSingleHist - spacing
        return height

    def _plot_2D_data_and_hists(self, categories:List[Tuple[str,List[Points]]], ax_scatter:Axes, histogramDict:Dict,  xFeatureCreator:FeatureCreatorBase, yFeatureCreator:FeatureCreatorBase, featuresToSingleVal) -> Dict:
        """Plots the data passed in in two dimensions on the scatterplot, and the histograms"""
        histBinsDict = {}
        pointsPlotted = []
        for name, allFilesPoints in categories:
            xPointsAverages = []
            yPointsAverages = []
            for trajectoryPoints in allFilesPoints:
                xFeature = xFeatureCreator.get_features(trajectoryPoints)
                yFeature = yFeatureCreator.get_features(trajectoryPoints)
                xAvgOfFeature = featuresToSingleVal.get_val(xFeature)
                yAvgOfFeature = featuresToSingleVal.get_val(yFeature)
                xPointsAverages.append(xAvgOfFeature)
                yPointsAverages.append(yAvgOfFeature)
            
            s = ax_scatter.scatter(xPointsAverages, yPointsAverages, label=name)
            pointsPlotted.append((name, xPointsAverages, yPointsAverages, s.get_ec()))
        
        for name, xPointsAverages, yPointsAverages, color in pointsPlotted:
            xHistAxis = histogramDict[name + " X"]
            yHistAxis = histogramDict[name + " Y"]
            histBinsDict[name + " X"] = xHistAxis.hist(xPointsAverages, color = color, bins=ax_scatter.get_xticks()[1:-1])
            histBinsDict[name + " Y"] = yHistAxis.hist(yPointsAverages, orientation='horizontal', color = color,bins=ax_scatter.get_yticks()[1:-1])

        return histBinsDict

    def _set_hist_size_and_labels(self, histBinsDict:Dict, histogramDict:Dict, ax_scatter:Axes) -> None:
        """Sets the labels for each of the histograms"""
        xRange, yRange = self._get_max_hist_bin_heights(histBinsDict)
        self._set_max_hist_bin_heights_and_labels(histogramDict, ax_scatter, xRange, yRange)

    def _get_max_hist_bin_heights(self, histBinsDict:Dict) -> Tuple[float, float]:
        """Get the maximum bin heights for the x and y bins"""
        xRanges = []
        yRanges = []
        for histName in histBinsDict:
            binHeights, _, _ = histBinsDict[histName]
            maxBinVal = max(binHeights)
            if(histName[-1:] == "X"):
                xRanges.append(maxBinVal) 
            else:
                yRanges.append(maxBinVal)
        return (max(xRanges), max(yRanges))

    def _set_max_hist_bin_heights_and_labels(self, histogramDict:Dict, ax_scatter:Axes, xRange:float, yRange:float) -> None:
        """Sets all of the histogram bin heights so that they fit comfortably within the graph"""
        for histName in histogramDict:
            hist = histogramDict[histName]
            if(histName[-1:] == "X"):
                hist.set_ylabel("Trajectories", fontsize = 8)
                hist.set_ylim([0, xRange + 1])
            else:
                hist.set_xlabel("Trajectories", fontsize = 8)
                hist.set_xlim([0, yRange + 1])
        pass

    def _get_graph_title(self, categories:List[Tuple[str,List[Points]]], yLabel:str, xLabel:str) -> str:
        """Gets the name of the graph."""
        title = ""
        for name, _ in categories:
            title += name + ", "
        
        title += str(yLabel) + " vs. " + str(xLabel) + " comparison"
        return title

        

