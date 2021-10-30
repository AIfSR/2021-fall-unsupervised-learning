from typing import List, Tuple
from features.Features import Features
from plotting.ComparePlotsBase import ComparePlotsBase
from tckfilereader.TCKFileReader import TCKFileReader
import matplotlib
import matplotlib.pyplot as plt
import numpy
from matplotlib.widgets import Slider
import sys
import random
from tckfilereader.Points import Points
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import (
                        QWidget,
                        QApplication,
                        QMainWindow,
                        QVBoxLayout,
                        QScrollArea,
                    )

from matplotlib.backends.backend_qt5agg import (
                        FigureCanvasQTAgg as FigCanvas,
                        NavigationToolbar2QT as NabToolbar,
                    )
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class TwoDComparePlots (ComparePlotsBase):

    def __init__(self) -> None:
        super().__init__()

    def display_plots(self, plotFeatures: List[Tuple[Features, Features]], filepaths: List[Tuple[str, List[str]]]) -> None:
        """Displays all of the plots passed in in two dimensions"""
        tckFileReader = TCKFileReader()

        m0Points = []
        for file in filepaths[0][1]:
            m0Points.append(tckFileReader.get_points(file))

        m1Points = []
        for file in filepaths[1][1]:
            m1Points.append(tckFileReader.get_points(file))

        m2Points = []
        for file in filepaths[2][1]:
            m2Points.append(tckFileReader.get_points(file))

        categories = [("M0",m0Points),("M1",m1Points),("M2",m2Points)]
        all_graphs = []
        for featureCreators in plotFeatures:
            graphs_of_feature = []
            xFeatureCreator = featureCreators[0]
            yFeatureCreator = featureCreators[1]
            for category in categories:
                graphs_of_category = []
                for point in category[1]:
                    xValues = []
                    yValues = []
                    x = xFeatureCreator.get_features(point)
                    y = yFeatureCreator.get_features(point)
                    xValues.append(x)
                    yValues.append(y)
                    a = []
                    for i in xValues:
                        for j in i:
                            a.append(str(j))
                    convertedxValues = [float(x) for x in a]
                    b = []
                    for i in yValues:
                        for j in i:
                            b.append(str(j))
                    convertedyValues = [float(x) for x in b]
                    convertedxValuesarr = numpy.array(convertedxValues)
                    convertedyValuesarr = numpy.array(convertedyValues)
                    one_graph = []
                    one_graph.append(convertedxValuesarr)
                    one_graph.append(convertedyValuesarr)
                    graphs_of_category.append(one_graph)
                graphs_of_feature.append(graphs_of_category)
            all_graphs.append(graphs_of_feature)

        for i in range(len(plotFeatures)):
            new_file_names = []
            fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16, ax17, ax18)) = plt.subplots(3, 6, sharex=True, sharey=True)
            # fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16, ax17, ax18)) = plt.subplots(3, 6)
            fig.suptitle(str(plotFeatures[i][0]) + " / " + str(plotFeatures[i][1]), fontsize=16)

            m0_x_values = []
            for point in m0Points:
                m0_x_feature_creator = plotFeatures[i][0]
                x = m0_x_feature_creator.get_features(point)
                m0_x_values.append(x)
            a = []
            for value in m0_x_values:
                for j in value:
                    a.append(str(j))
            convertedm0xValues = [float(x) for x in a]
            minimum_m0_x = min(convertedm0xValues)
            maximum_m0_x = max(convertedm0xValues)

            m0_y_values = []
            for point in m0Points:
                m0_y_feature_creator = plotFeatures[i][1]
                y = m0_y_feature_creator.get_features(point)
                m0_y_values.append(y)
            a = []
            for value in m0_y_values:
                for j in value:
                    a.append(str(j))
            convertedm0yValues = [float(y) for y in a]
            minimum_m0_y = min(convertedm0yValues)
            maximum_m0_y = max(convertedm0yValues)

            m1_x_values = []
            for point in m1Points:
                m1_x_feature_creator = plotFeatures[i][0]
                x = m1_x_feature_creator.get_features(point)
                m1_x_values.append(x)
            a = []
            for value in m1_x_values:
                for j in value:
                    a.append(str(j))
            convertedm1xValues = [float(x) for x in a]
            minimum_m1_x = min(convertedm1xValues)
            maximum_m1_x = max(convertedm1xValues)

            m1_y_values = []
            for point in m1Points:
                m1_y_feature_creator = plotFeatures[i][1]
                y = m1_y_feature_creator.get_features(point)
                m1_y_values.append(y)
            a = []
            for value in m1_y_values:
                for j in value:
                    a.append(str(j))
            convertedm1yValues = [float(y) for y in a]
            minimum_m1_y = min(convertedm1yValues)
            maximum_m1_y = max(convertedm1yValues)

            m2_x_values = []
            for point in m2Points:
                m2_x_feature_creator = plotFeatures[i][0]
                x = m2_x_feature_creator.get_features(point)
                m2_x_values.append(x)
            a = []
            for value in m2_x_values:
                for j in value:
                    a.append(str(j))
            convertedm2xValues = [float(x) for x in a]
            minimum_m2_x = min(convertedm2xValues)
            maximum_m2_x = max(convertedm2xValues)

            m2_y_values = []
            for point in m1Points:
                m2_y_feature_creator = plotFeatures[i][1]
                y = m2_y_feature_creator.get_features(point)
                m2_y_values.append(y)
            a = []
            for value in m2_y_values:
                for j in value:
                    a.append(str(j))
            convertedm2yValues = [float(y) for y in a]
            minimum_m2_y = min(convertedm2yValues)
            maximum_m2_y = max(convertedm2yValues)

            minimums_of_x = [minimum_m0_x,minimum_m1_x,minimum_m2_x]
            minimums_of_y = [minimum_m0_y,minimum_m1_y,minimum_m2_y]
            minimum_of_x = min(minimums_of_x)
            minimum_of_y = min(minimums_of_y)

            maximums_of_x = [maximum_m0_x,maximum_m1_x,maximum_m2_x]
            maximums_of_y = [maximum_m0_y,maximum_m1_y,maximum_m2_y]
            maximum_of_x = max(maximums_of_x)
            maximum_of_y = max(maximums_of_y)
            # print(convertedm0xValues)
            custom_xlim = (minimum_of_x, maximum_of_x)
            custom_ylim = (minimum_of_y, maximum_of_y)

            # plt.setp(ax1, xlim=custom_ylim, ylim=custom_xlim)

            for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
	            label.set_fontsize(5)
            ax1.plot(all_graphs[i][0][0][1], all_graphs[i][0][0][0])
            ax1_title = filepaths[0][1][0]
            first_chars = ax1_title[0:10]
            if first_chars == "data/0_4h/":
                ax1_title_changed = ax1_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax1_title_changed = ax1_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax1_title_changed = ax1_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax1_title_changed = ax1_title.replace("data/24h_24h/","").replace("_.tck","")
            ax1.set_title(ax1_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
	            label.set_fontsize(5)
            ax2.plot(all_graphs[i][0][1][1], all_graphs[i][0][1][0])
            ax2_title = filepaths[0][1][1]
            first_chars = ax2_title[0:10]
            if first_chars == "data/0_4h/":
                ax2_title_changed = ax2_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax2_title_changed = ax2_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax2_title_changed = ax2_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax2_title_changed = ax2_title.replace("data/24h_24h/","").replace("_.tck","")
            ax2.set_title(ax2_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax3.get_xticklabels() + ax3.get_yticklabels()):
	            label.set_fontsize(5)
            ax3.plot(all_graphs[i][0][2][1], all_graphs[i][0][2][0])
            ax3_title = filepaths[0][1][2]
            first_chars = ax3_title[0:10]
            if first_chars == "data/0_4h/":
                ax3_title_changed = ax3_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax3_title_changed = ax3_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax3_title_changed = ax3_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax3_title_changed = ax3_title.replace("data/24h_24h/","").replace("_.tck","")
            ax3.set_title(ax3_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax4.get_xticklabels() + ax4.get_yticklabels()):
	            label.set_fontsize(5)
            ax4.plot(all_graphs[i][0][3][1], all_graphs[i][0][3][0])
            ax4_title = filepaths[0][1][3]
            first_chars = ax4_title[0:10]
            if first_chars == "data/0_4h/":
                ax4_title_changed = ax4_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax4_title_changed = ax4_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax4_title_changed = ax4_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax4_title_changed = ax4_title.replace("data/24h_24h/","").replace("_.tck","")
            ax4.set_title(ax4_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax5.get_xticklabels() + ax5.get_yticklabels()):
	            label.set_fontsize(5)
            ax5.plot(all_graphs[i][0][4][1], all_graphs[i][0][4][0])
            ax5_title = filepaths[0][1][4]
            first_chars = ax5_title[0:10]
            if first_chars == "data/0_4h/":
                ax5_title_changed = ax5_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax5_title_changed = ax5_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax5_title_changed = ax5_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax5_title_changed = ax5_title.replace("data/24h_24h/","").replace("_.tck","")
            ax5.set_title(ax5_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax6.get_xticklabels() + ax6.get_yticklabels()):
	            label.set_fontsize(5)
            ax6.plot(all_graphs[i][0][5][1], all_graphs[i][0][5][0])
            ax6_title = filepaths[0][1][5]
            first_chars = ax6_title[0:10]
            if first_chars == "data/0_4h/":
                ax6_title_changed = ax6_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax6_title_changed = ax6_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax6_title_changed = ax6_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax6_title_changed = ax6_title.replace("data/24h_24h/","").replace("_.tck","")
            ax6.set_title(ax6_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax7.get_xticklabels() + ax7.get_yticklabels()):
	            label.set_fontsize(5)
            ax7.plot(all_graphs[i][1][0][1], all_graphs[i][1][0][0])
            ax7_title = filepaths[1][1][0]
            first_chars = ax7_title[0:10]
            if first_chars == "data/0_4h/":
                ax7_title_changed = ax7_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax7_title_changed = ax7_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax7_title_changed = ax7_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax7_title_changed = ax7_title.replace("data/24h_24h/","").replace("_.tck","")
            ax7.set_title(ax7_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax8.get_xticklabels() + ax8.get_yticklabels()):
	            label.set_fontsize(5)
            ax8.plot(all_graphs[i][1][1][1], all_graphs[i][1][1][0])
            ax8_title = filepaths[1][1][1]
            first_chars = ax8_title[0:10]
            if first_chars == "data/0_4h/":
                ax8_title_changed = ax8_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax8_title_changed = ax8_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax8_title_changed = ax8_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax8_title_changed = ax8_title.replace("data/24h_24h/","").replace("_.tck","")
            ax8.set_title(ax8_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax9.get_xticklabels() + ax9.get_yticklabels()):
	            label.set_fontsize(5)
            ax9.plot(all_graphs[i][1][2][1], all_graphs[i][1][2][0])
            ax9_title = filepaths[1][1][2]
            first_chars = ax9_title[0:10]
            if first_chars == "data/0_4h/":
                ax9_title_changed = ax9_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax9_title_changed = ax9_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax9_title_changed = ax9_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax9_title_changed = ax9_title.replace("data/24h_24h/","").replace("_.tck","")
            ax9.set_title(ax9_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax10.get_xticklabels() + ax10.get_yticklabels()):
	            label.set_fontsize(5)
            ax10.plot(all_graphs[i][1][3][1], all_graphs[i][1][3][0])
            ax10_title = filepaths[1][1][3]
            first_chars = ax10_title[0:10]
            if first_chars == "data/0_4h/":
                ax10_title_changed = ax10_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax10_title_changed = ax10_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax10_title_changed = ax10_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax10_title_changed = ax10_title.replace("data/24h_24h/","").replace("_.tck","")
            ax10.set_title(ax10_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax11.get_xticklabels() + ax11.get_yticklabels()):
	            label.set_fontsize(5)
            ax11.plot(all_graphs[i][1][4][1], all_graphs[i][1][4][0])
            ax11_title = filepaths[1][1][4]
            first_chars = ax11_title[0:10]
            if first_chars == "data/0_4h/":
                ax11_title_changed = ax11_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax11_title_changed = ax11_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax11_title_changed = ax11_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax11_title_changed = ax11_title.replace("data/24h_24h/","").replace("_.tck","")
            ax11.set_title(ax11_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax12.get_xticklabels() + ax12.get_yticklabels()):
	            label.set_fontsize(5)
            ax12.plot(all_graphs[i][1][5][1], all_graphs[i][1][5][0])
            ax12_title = filepaths[1][1][5]
            first_chars = ax12_title[0:10]
            if first_chars == "data/0_4h/":
                ax12_title_changed = ax12_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax12_title_changed = ax12_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax12_title_changed = ax12_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax12_title_changed = ax12_title.replace("data/24h_24h/","").replace("_.tck","")
            ax12.set_title(ax12_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax13.get_xticklabels() + ax13.get_yticklabels()):
	            label.set_fontsize(5)
            ax13.plot(all_graphs[i][2][0][1], all_graphs[i][2][0][0])
            ax13_title = filepaths[2][1][0]
            first_chars = ax13_title[0:10]
            if first_chars == "data/0_4h/":
                ax13_title_changed = ax13_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax13_title_changed = ax13_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax13_title_changed = ax13_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax13_title_changed = ax13_title.replace("data/24h_24h/","").replace("_.tck","")
            ax13.set_title(ax13_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax14.get_xticklabels() + ax14.get_yticklabels()):
	            label.set_fontsize(5)
            ax14.plot(all_graphs[i][2][1][1], all_graphs[i][2][1][0])
            ax14_title = filepaths[2][1][1]
            first_chars = ax14_title[0:10]
            if first_chars == "data/0_4h/":
                ax14_title_changed = ax14_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax14_title_changed = ax14_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax14_title_changed = ax14_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax14_title_changed = ax14_title.replace("data/24h_24h/","").replace("_.tck","")
            ax14.set_title(ax14_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax15.get_xticklabels() + ax15.get_yticklabels()):
	            label.set_fontsize(5)
            ax15.plot(all_graphs[i][2][2][1], all_graphs[i][2][2][0])
            ax15_title = filepaths[2][1][2]
            first_chars = ax15_title[0:10]
            if first_chars == "data/0_4h/":
                ax15_title_changed = ax15_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax15_title_changed = ax15_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax15_title_changed = ax15_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax15_title_changed = ax15_title.replace("data/24h_24h/","").replace("_.tck","")
            ax15.set_title(ax15_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax16.get_xticklabels() + ax16.get_yticklabels()):
	            label.set_fontsize(5)
            ax16.plot(all_graphs[i][2][3][1], all_graphs[i][2][3][0])
            ax16_title = filepaths[2][1][3]
            first_chars = ax16_title[0:10]
            if first_chars == "data/0_4h/":
                ax16_title_changed = ax16_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax16_title_changed = ax16_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax16_title_changed = ax16_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax16_title_changed = ax16_title.replace("data/24h_24h/","").replace("_.tck","")
            ax16.set_title(ax16_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax17.get_xticklabels() + ax17.get_yticklabels()):
	            label.set_fontsize(5)
            ax17.plot(all_graphs[i][2][4][1], all_graphs[i][2][4][0])
            ax17_title = filepaths[2][1][4]
            first_chars = ax17_title[0:10]
            if first_chars == "data/0_4h/":
                ax17_title_changed = ax17_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax17_title_changed = ax17_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax17_title_changed = ax17_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax17_title_changed = ax17_title.replace("data/24h_24h/","").replace("_.tck","")
            ax17.set_title(ax17_title_changed, fontsize=3, fontstyle='italic')

            for label in (ax18.get_xticklabels() + ax18.get_yticklabels()):
	            label.set_fontsize(5)
            ax18.plot(all_graphs[i][2][5][1], all_graphs[i][2][5][0])
            ax18_title = filepaths[2][1][5]
            first_chars = ax18_title[0:10]
            if first_chars == "data/0_4h/":
                ax18_title_changed = ax18_title.replace("data/0_4h/","").replace("_.tck","")
            elif first_chars == "data/0_24h":
                ax18_title_changed = ax18_title.replace("data/0_24h/","").replace("_.tck","")
            elif first_chars == "data/24h_4":
                ax18_title_changed = ax18_title.replace("data/24h_4h/","").replace("_.tck","")
            elif first_chars == "data/24h_2":
                ax18_title_changed = ax18_title.replace("data/24h_24h/","").replace("_.tck","")
            ax18.set_title(ax18_title_changed, fontsize=3, fontstyle='italic')
            plt.figure(i)
            # barpos = plt.axes([0.18, 0.05, 0.55, 0.03], facecolor="skyblue")
            # slider = Slider(barpos, 'Barpos', 0, len(plotFeatures)-2, valinit=0)
            # slider.on_changed(plt)
            # bar(0)
        plt.show()

    # def comparison_of_time(self, plotFeature: Tuple[Features, Features], filepaths: List[Tuple[str, List[str]]]) -> None:
    #     """Given a Plot feature, display all of the plots organized by time interval"""
    #     tckFileReader = TCKFileReader()
    #
    #     # zero4m0POints = []
    #     # for i in filepaths:
    #     #     for j in i[1]:
    #     #         if "" in j
    #
    #     m0Points = []
    #     for file in filepaths[0][1]:
    #         m0Points.append(tckFileReader.get_points(file))
    #
    #     m1Points = []
    #     for file in filepaths[1][1]:
    #         m1Points.append(tckFileReader.get_points(file))
    #
    #     m2Points = []
    #     for file in filepaths[2][1]:
    #         m2Points.append(tckFileReader.get_points(file))
    #
    #     categories = [("M0",m0Points),("M1",m1Points),("M2",m2Points)]
    #     all_graphs = []
    #     for featureCreators in plotFeatures:
    #         graphs_of_feature = []
    #         xFeatureCreator = featureCreators[0]
    #         yFeatureCreator = featureCreators[1]
    #         for category in categories:
    #             graphs_of_category = []
    #             for point in category[1]:
    #                 xValues = []
    #                 yValues = []
    #                 x = xFeatureCreator.get_features(point)
    #                 y = yFeatureCreator.get_features(point)
    #                 xValues.append(x)
    #                 yValues.append(y)
    #                 a = []
    #                 for i in xValues:
    #                     for j in i:
    #                         a.append(str(j))
    #                 convertedxValues = [float(x) for x in a]
    #                 b = []
    #                 for i in yValues:
    #                     for j in i:
    #                         b.append(str(j))
    #                 convertedyValues = [float(x) for x in b]
    #                 convertedxValuesarr = numpy.array(convertedxValues)
    #                 convertedyValuesarr = numpy.array(convertedyValues)
    #                 one_graph = []
    #                 one_graph.append(convertedxValuesarr)
    #                 one_graph.append(convertedyValuesarr)
    #                 graphs_of_category.append(one_graph)
    #             graphs_of_feature.append(graphs_of_category)
    #         all_graphs.append(graphs_of_feature)
    #
    #     for i in range(len(plotFeatures)):
    #         new_file_names = []
    #         # fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16, ax17, ax18)) = plt.subplots(3, 6, sharex=True, sharey=True)
    #         fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16, ax17, ax18)) = plt.subplots(3, 6)
    #         fig.suptitle(str(plotFeatures[i][0]) + " / " + str(plotFeatures[i][1]), fontsize=16)
    #
    #         m0_x_values = []
    #         for point in m0Points:
    #             m0_x_feature_creator = plotFeatures[i][0]
    #             x = m0_x_feature_creator.get_features(point)
    #             m0_x_values.append(x)
    #         a = []
    #         for value in m0_x_values:
    #             for j in value:
    #                 a.append(str(j))
    #         convertedm0xValues = [float(x) for x in a]
    #         minimum_m0_x = min(convertedm0xValues)
    #         maximum_m0_x = max(convertedm0xValues)
    #
    #         m0_y_values = []
    #         for point in m0Points:
    #             m0_y_feature_creator = plotFeatures[i][1]
    #             y = m0_y_feature_creator.get_features(point)
    #             m0_y_values.append(y)
    #         a = []
    #         for value in m0_y_values:
    #             for j in value:
    #                 a.append(str(j))
    #         convertedm0yValues = [float(y) for y in a]
    #         minimum_m0_y = min(convertedm0yValues)
    #         maximum_m0_y = max(convertedm0yValues)
    #
    #         m1_x_values = []
    #         for point in m1Points:
    #             m1_x_feature_creator = plotFeatures[i][0]
    #             x = m1_x_feature_creator.get_features(point)
    #             m1_x_values.append(x)
    #         a = []
    #         for value in m1_x_values:
    #             for j in value:
    #                 a.append(str(j))
    #         convertedm1xValues = [float(x) for x in a]
    #         minimum_m1_x = min(convertedm1xValues)
    #         maximum_m1_x = max(convertedm1xValues)
    #
    #         m1_y_values = []
    #         for point in m1Points:
    #             m1_y_feature_creator = plotFeatures[i][1]
    #             y = m1_y_feature_creator.get_features(point)
    #             m1_y_values.append(y)
    #         a = []
    #         for value in m1_y_values:
    #             for j in value:
    #                 a.append(str(j))
    #         convertedm1yValues = [float(y) for y in a]
    #         minimum_m1_y = min(convertedm1yValues)
    #         maximum_m1_y = max(convertedm1yValues)
    #
    #         m2_x_values = []
    #         for point in m2Points:
    #             m2_x_feature_creator = plotFeatures[i][0]
    #             x = m2_x_feature_creator.get_features(point)
    #             m2_x_values.append(x)
    #         a = []
    #         for value in m2_x_values:
    #             for j in value:
    #                 a.append(str(j))
    #         convertedm2xValues = [float(x) for x in a]
    #         minimum_m2_x = min(convertedm2xValues)
    #         maximum_m2_x = max(convertedm2xValues)
    #
    #         m2_y_values = []
    #         for point in m1Points:
    #             m2_y_feature_creator = plotFeatures[i][1]
    #             y = m2_y_feature_creator.get_features(point)
    #             m2_y_values.append(y)
    #         a = []
    #         for value in m2_y_values:
    #             for j in value:
    #                 a.append(str(j))
    #         convertedm2yValues = [float(y) for y in a]
    #         minimum_m2_y = min(convertedm2yValues)
    #         maximum_m2_y = max(convertedm2yValues)
    #
    #         minimums_of_x = [minimum_m0_x,minimum_m1_x,minimum_m2_x]
    #         minimums_of_y = [minimum_m0_y,minimum_m1_y,minimum_m2_y]
    #         minimum_of_x = min(minimums_of_x)
    #         minimum_of_y = min(minimums_of_y)
    #
    #         maximums_of_x = [maximum_m0_x,maximum_m1_x,maximum_m2_x]
    #         maximums_of_y = [maximum_m0_y,maximum_m1_y,maximum_m2_y]
    #         maximum_of_x = max(maximums_of_x)
    #         maximum_of_y = max(maximums_of_y)
    #         # print(convertedm0xValues)
    #         custom_xlim = (minimum_of_x, maximum_of_x)
    #         custom_ylim = (minimum_of_y, maximum_of_y)
    #
    #         # plt.setp(ax1, xlim=custom_ylim, ylim=custom_xlim)
    #
    #         for label in (ax1.get_xticklabels() + ax1.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax1.plot(all_graphs[i][0][0][1], all_graphs[i][0][0][0])
    #         ax1_title = filepaths[0][1][0]
    #         first_chars = ax1_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax1_title_changed = ax1_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax1_title_changed = ax1_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax1_title_changed = ax1_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax1_title_changed = ax1_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax1.set_title(ax1_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax2.get_xticklabels() + ax2.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax2.plot(all_graphs[i][0][1][1], all_graphs[i][0][1][0])
    #         ax2_title = filepaths[0][1][1]
    #         first_chars = ax2_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax2_title_changed = ax2_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax2_title_changed = ax2_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax2_title_changed = ax2_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax2_title_changed = ax2_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax2.set_title(ax2_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax3.get_xticklabels() + ax3.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax3.plot(all_graphs[i][0][2][1], all_graphs[i][0][2][0])
    #         ax3_title = filepaths[0][1][2]
    #         first_chars = ax3_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax3_title_changed = ax3_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax3_title_changed = ax3_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax3_title_changed = ax3_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax3_title_changed = ax3_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax3.set_title(ax3_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax4.get_xticklabels() + ax4.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax4.plot(all_graphs[i][0][3][1], all_graphs[i][0][3][0])
    #         ax4_title = filepaths[0][1][3]
    #         first_chars = ax4_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax4_title_changed = ax4_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax4_title_changed = ax4_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax4_title_changed = ax4_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax4_title_changed = ax4_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax4.set_title(ax4_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax5.get_xticklabels() + ax5.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax5.plot(all_graphs[i][0][4][1], all_graphs[i][0][4][0])
    #         ax5_title = filepaths[0][1][4]
    #         first_chars = ax5_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax5_title_changed = ax5_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax5_title_changed = ax5_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax5_title_changed = ax5_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax5_title_changed = ax5_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax5.set_title(ax5_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax6.get_xticklabels() + ax6.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax6.plot(all_graphs[i][0][5][1], all_graphs[i][0][5][0])
    #         ax6_title = filepaths[0][1][5]
    #         first_chars = ax6_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax6_title_changed = ax6_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax6_title_changed = ax6_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax6_title_changed = ax6_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax6_title_changed = ax6_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax6.set_title(ax6_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax7.get_xticklabels() + ax7.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax7.plot(all_graphs[i][1][0][1], all_graphs[i][1][0][0])
    #         ax7_title = filepaths[1][1][0]
    #         first_chars = ax7_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax7_title_changed = ax7_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax7_title_changed = ax7_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax7_title_changed = ax7_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax7_title_changed = ax7_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax7.set_title(ax7_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax8.get_xticklabels() + ax8.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax8.plot(all_graphs[i][1][1][1], all_graphs[i][1][1][0])
    #         ax8_title = filepaths[1][1][1]
    #         first_chars = ax8_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax8_title_changed = ax8_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax8_title_changed = ax8_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax8_title_changed = ax8_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax8_title_changed = ax8_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax8.set_title(ax8_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax9.get_xticklabels() + ax9.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax9.plot(all_graphs[i][1][2][1], all_graphs[i][1][2][0])
    #         ax9_title = filepaths[1][1][2]
    #         first_chars = ax9_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax9_title_changed = ax9_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax9_title_changed = ax9_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax9_title_changed = ax9_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax9_title_changed = ax9_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax9.set_title(ax9_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax10.get_xticklabels() + ax10.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax10.plot(all_graphs[i][1][3][1], all_graphs[i][1][3][0])
    #         ax10_title = filepaths[1][1][3]
    #         first_chars = ax10_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax10_title_changed = ax10_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax10_title_changed = ax10_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax10_title_changed = ax10_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax10_title_changed = ax10_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax10.set_title(ax10_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax11.get_xticklabels() + ax11.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax11.plot(all_graphs[i][1][4][1], all_graphs[i][1][4][0])
    #         ax11_title = filepaths[1][1][4]
    #         first_chars = ax11_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax11_title_changed = ax11_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax11_title_changed = ax11_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax11_title_changed = ax11_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax11_title_changed = ax11_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax11.set_title(ax11_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax12.get_xticklabels() + ax12.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax12.plot(all_graphs[i][1][5][1], all_graphs[i][1][5][0])
    #         ax12_title = filepaths[1][1][5]
    #         first_chars = ax12_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax12_title_changed = ax12_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax12_title_changed = ax12_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax12_title_changed = ax12_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax12_title_changed = ax12_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax12.set_title(ax12_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax13.get_xticklabels() + ax13.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax13.plot(all_graphs[i][2][0][1], all_graphs[i][2][0][0])
    #         ax13_title = filepaths[2][1][0]
    #         first_chars = ax13_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax13_title_changed = ax13_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax13_title_changed = ax13_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax13_title_changed = ax13_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax13_title_changed = ax13_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax13.set_title(ax13_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax14.get_xticklabels() + ax14.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax14.plot(all_graphs[i][2][1][1], all_graphs[i][2][1][0])
    #         ax14_title = filepaths[2][1][1]
    #         first_chars = ax14_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax14_title_changed = ax14_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax14_title_changed = ax14_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax14_title_changed = ax14_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax14_title_changed = ax14_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax14.set_title(ax14_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax15.get_xticklabels() + ax15.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax15.plot(all_graphs[i][2][2][1], all_graphs[i][2][2][0])
    #         ax15_title = filepaths[2][1][2]
    #         first_chars = ax15_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax15_title_changed = ax15_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax15_title_changed = ax15_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax15_title_changed = ax15_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax15_title_changed = ax15_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax15.set_title(ax15_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax16.get_xticklabels() + ax16.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax16.plot(all_graphs[i][2][3][1], all_graphs[i][2][3][0])
    #         ax16_title = filepaths[2][1][3]
    #         first_chars = ax16_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax16_title_changed = ax16_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax16_title_changed = ax16_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax16_title_changed = ax16_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax16_title_changed = ax16_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax16.set_title(ax16_title_changed, fontsize=3, fontstyle='italic')
    #
    #         for label in (ax17.get_xticklabels() + ax17.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax17.plot(all_graphs[i][2][4][1], all_graphs[i][2][4][0])
    #         ax17_title = filepaths[2][1][4]
    #         first_chars = ax17_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax17_title_changed = ax17_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax17_title_changed = ax17_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax17_title_changed = ax17_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax17_title_changed = ax17_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax17.set_title(ax17_title_changed, fontsize=3, fontstyle='italic')
    #
    #
    #         for label in (ax18.get_xticklabels() + ax18.get_yticklabels()):
	#             label.set_fontsize(5)
    #         ax18.plot(all_graphs[i][2][5][1], all_graphs[i][2][5][0])
    #         ax18_title = filepaths[2][1][5]
    #         first_chars = ax18_title[0:10]
    #         if first_chars == "data/0_4h/":
    #             ax18_title_changed = ax18_title.replace("data/0_4h/","").replace("_.tck","")
    #         elif first_chars == "data/0_24h":
    #             ax18_title_changed = ax18_title.replace("data/0_24h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_4":
    #             ax18_title_changed = ax18_title.replace("data/24h_4h/","").replace("_.tck","")
    #         elif first_chars == "data/24h_2":
    #             ax18_title_changed = ax18_title.replace("data/24h_24h/","").replace("_.tck","")
    #         ax18.set_title(ax18_title_changed, fontsize=3, fontstyle='italic')
    #
    #         plt.figure(i)
    #         # barpos = plt.axes([0.18, 0.05, 0.55, 0.03], facecolor="skyblue")
    #         # slider = Slider(barpos, 'Barpos', 0, len(plotFeatures)-2, valinit=0)
    #         # slider.on_changed(plt)
    #         # bar(0)
    #     plt.show()



