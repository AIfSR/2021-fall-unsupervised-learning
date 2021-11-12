from typing import List, Tuple
from features.Features import Features
from plotting.ComparePlotsBase import ComparePlotsBase
import matplotlib.pyplot as plt
import numpy
from plotting.GraphParameters import GraphParameters
from tckfilereader.Points import Points


class TwoDComparePlots (ComparePlotsBase):

    def __init__(self) -> None:
        super().__init__()

    def display_plots(self, graphParameters:List[GraphParameters], categories: List[Tuple[str, List[Points]]]) -> None:
        """Displays all of the plots passed in in two dimensions"""

        all_graphs = []
        for graphParameter in graphParameters:
            graphs_of_feature = []
            xFeatureCreator = graphParameter.xFeatureCreator
            yFeatureCreator = graphParameter.yFeatureCreator
            for category in categories:
                # xValues = []
                # yValues = []
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

        for i in range(len(graphParameters)):
            fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16, ax17, ax18)) = plt.subplots(3, 6, sharex=True, sharey=True)
            fig.suptitle(graphParameters[i].xLabel + " / " + graphParameters[i].yLabel, fontsize=16)
            ax1.plot(all_graphs[i][0][0][1], all_graphs[i][0][0][0])
            ax1.set_title('M0/16-45-01,168', fontsize=7, fontstyle='italic')
            ax2.plot(all_graphs[i][0][1][1], all_graphs[i][0][1][0])
            ax2.set_title('M0/17-21-46,888.tck', fontsize=7, fontstyle='italic')
            ax3.plot(all_graphs[i][0][2][1], all_graphs[i][0][2][0])
            ax3.set_title('M0/18-11-44,490.tck', fontsize=7, fontstyle='italic')
            ax4.plot(all_graphs[i][0][3][1], all_graphs[i][0][3][0])
            ax4.set_title('M0/14-49-41,154.tck', fontsize=7, fontstyle='italic')
            ax5.plot(all_graphs[i][0][4][1], all_graphs[i][0][4][0])
            ax5.set_title('M0/15-58-23,371.tck', fontsize=7, fontstyle='italic')
            ax6.plot(all_graphs[i][0][5][1], all_graphs[i][0][5][0])
            ax6.set_title('M0/16-41-18,342.tck', fontsize=7, fontstyle='italic')

            ax7.plot(all_graphs[i][1][0][1], all_graphs[i][1][0][0])
            ax7.set_title('M1/18-51-50,514', fontsize=7, fontstyle='italic')
            ax8.plot(all_graphs[i][1][1][1], all_graphs[i][1][1][0])
            ax8.set_title('M1/19-18-08,801', fontsize=7, fontstyle='italic')
            ax9.plot(all_graphs[i][1][2][1], all_graphs[i][1][2][0])
            ax9.set_title('M1/20-12-39,857', fontsize=7, fontstyle='italic')
            ax10.plot(all_graphs[i][1][3][1], all_graphs[i][1][3][0])
            ax10.set_title('M1/20-44-17,610', fontsize=7, fontstyle='italic')
            ax11.plot(all_graphs[i][1][4][1], all_graphs[i][1][4][0])
            ax11.set_title('M1/21-48-48,900', fontsize=7, fontstyle='italic')
            ax12.plot(all_graphs[i][1][5][1], all_graphs[i][1][5][0])
            ax12.set_title('M1/22-33-50,826', fontsize=7, fontstyle='italic')

            ax13.plot(all_graphs[i][2][0][1], all_graphs[i][2][0][0])
            ax13.set_title('M2/17-08-21,199', fontsize=7, fontstyle='italic')
            ax14.plot(all_graphs[i][2][1][1], all_graphs[i][2][1][0])
            ax14.set_title('M2/17-50-33,515', fontsize=7, fontstyle='italic')
            ax15.plot(all_graphs[i][2][2][1], all_graphs[i][2][2][0])
            ax15.set_title('M2/18-56-04,307', fontsize=7, fontstyle='italic')
            ax16.plot(all_graphs[i][2][3][1], all_graphs[i][2][3][0])
            ax16.set_title('M2/20-05-05,492', fontsize=7, fontstyle='italic')
            ax17.plot(all_graphs[i][2][4][1], all_graphs[i][2][4][0])
            ax17.set_title('M2/21-53-37,370', fontsize=7, fontstyle='italic')
            ax18.plot(all_graphs[i][2][5][1], all_graphs[i][2][5][0])
            ax18.set_title('M2/22-54-31,916', fontsize=7, fontstyle='italic')

            plt.show()
