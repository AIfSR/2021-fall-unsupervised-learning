from typing import List, Tuple
from features.Features import Features
from plotting.ComparePlotsBase import ComparePlotsBase
from tckfilereader.TCKFileReader import TCKFileReader
import matplotlib.pyplot as plt
import numpy
from tckfilereader.Points import Points



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
            fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16, ax17, ax18)) = plt.subplots(3, 6)
            fig.suptitle(str(plotFeatures[i][0]) + " / " + str(plotFeatures[i][1]), fontsize=16)

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
            ax1.set_title(ax1_title_changed, fontsize=7, fontstyle='italic')

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
            ax2.set_title(ax2_title_changed, fontsize=7, fontstyle='italic')

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
            ax3.set_title(ax3_title_changed, fontsize=7, fontstyle='italic')

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
            ax4.set_title(ax4_title_changed, fontsize=7, fontstyle='italic')

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
            ax5.set_title(ax5_title_changed, fontsize=7, fontstyle='italic')

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
            ax6.set_title(ax6_title_changed, fontsize=7, fontstyle='italic')


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
            ax7.set_title(ax7_title_changed, fontsize=7, fontstyle='italic')

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
            ax8.set_title(ax8_title_changed, fontsize=7, fontstyle='italic')

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
            ax9.set_title(ax9_title_changed, fontsize=7, fontstyle='italic')

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
            ax10.set_title(ax10_title_changed, fontsize=7, fontstyle='italic')

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
            ax11.set_title(ax11_title_changed, fontsize=7, fontstyle='italic')

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
            ax12.set_title(ax12_title_changed, fontsize=7, fontstyle='italic')


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
            ax13.set_title(ax13_title_changed, fontsize=7, fontstyle='italic')

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
            ax14.set_title(ax14_title_changed, fontsize=7, fontstyle='italic')

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
            ax15.set_title(ax15_title_changed, fontsize=7, fontstyle='italic')

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
            ax16.set_title(ax16_title_changed, fontsize=7, fontstyle='italic')

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
            ax17.set_title(ax17_title_changed, fontsize=7, fontstyle='italic')

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
            ax18.set_title(ax18_title_changed, fontsize=7, fontstyle='italic')


            plt.show()
