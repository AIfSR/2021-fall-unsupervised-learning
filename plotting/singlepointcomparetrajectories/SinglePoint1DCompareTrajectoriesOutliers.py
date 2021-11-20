from typing import List, Tuple
from features.Features import Features
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from plotting.ComparePlotsBase import ComparePlotsBase
from plotting.GraphParameters import GraphParameters
from tckfilereader.Points import Points
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


class SinglePoint1DCompareTrajectoriesOutliers (ComparePlotsBase):

    def __init__(self) -> None:
        super().__init__()

    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all of the 1 dimentsional plots passed in."""
        outliers = []
        indexes_of_outliers = []
        def make_labels(ax, boxplot):
            # Grab the relevant Line2D instances from the boxplot dictionary
            iqr = boxplot['boxes'][0]
            caps = boxplot['caps']
            med = boxplot['medians'][0]
            fly = boxplot['fliers'][0]

            # The x position of the median line
            xpos = med.get_xdata()

            # Lets make the text have a horizontal offset which is some
            # fraction of the width of the box
            xoff = 0.10 * (xpos[1] - xpos[0])

            # The x position of the labels
            xlabel = xpos[1] + xoff

            # The median is the y-position of the median line
            median = med.get_ydata()[1]

            # The 25th and 75th percentiles are found from the
            # top and bottom (max and min) of the box
            pc25 = iqr.get_ydata().min()
            pc75 = iqr.get_ydata().max()

            # The caps give the vertical position of the ends of the whiskers
            capbottom = caps[0].get_ydata()[0]
            captop = caps[1].get_ydata()[0]

            # Make some labels on the figure using the values derived above
            ax.text(xlabel, median,
                    'Median = {:6.3g}'.format(median), va='center')
            ax.text(xlabel, pc25,
                    '25th percentile = {:6.3g}'.format(pc25), va='center')
            ax.text(xlabel, pc75,
                    '75th percentile = {:6.3g}'.format(pc75), va='center')
            ax.text(xlabel, capbottom,
                    'Bottom cap = {:6.3g}'.format(capbottom), va='center')
            ax.text(xlabel, captop,
                    'Top cap = {:6.3g}'.format(captop), va='center')

            # Many fliers, so we loop over them and create a label for each one
            fliers = []
            for flier in fly.get_ydata():
                ax.text(1 + xoff, flier,
                        'Flier = {:6.3g}'.format(flier), va='center')
                fliers.append(flier)
            return fliers
        for graphParameter in graphParameters:
            plt.close()
            # ax = self.setup_fig()
            names = []
            data = []
            for name, pointsList in categories:
                pointAverages = []
                names.append(name)
                for points in pointsList:
                    features = graphParameter.xFeatureCreator.get_features(points)
                    # feature_creator = str(graphParameter.xFeatureCreator)
                    singleVal = graphParameter.featuresToSingleVal.get_val(features)
                    pointAverages.append(singleVal)
                data.append(pointAverages)
            red_diamond = dict(markerfacecolor='r', marker='D')
            fig3, ax3 = plt.subplots()
            ax3.set_title(self.get_title(graphParameter, categories), fontsize=20)

            # Create the boxplot and store the resulting python dictionary
            my_boxes = ax3.boxplot(data, flierprops=red_diamond)

            # Call the function to make labels

            outliers.append(make_labels(ax3, my_boxes))
            # print(len(pointAverages))
            # print(len(categories[0][1]))
            # print(outliers)
            if outliers[0] != None:
                for i in outliers[0]:
                    for j in pointAverages:
                        if i == j:
                            indexes_of_outliers.append(pointAverages.index(i))
            else:
                indexes_of_outliers.append(None)
            print(str(graphParameter.xFeatureCreator) + ": " + str(indexes_of_outliers))
            ax3.get_xaxis().tick_bottom()
            ax3.get_yaxis().tick_left()
            ax3.set_ylabel(graphParameter.xLabel, fontsize=16)
            ax3.set_xticklabels(names, fontdict = {'fontsize':16})
            # plt.show()


    def setup_fig(self) -> Axes:
        """Sets up the figure with the right dimensions."""
        fig = plt.figure(figsize=(16, 7.5))
        ax = fig.add_subplot(111)
        return ax

    def get_title(self, graphParameter:GraphParameters, categories:List[Tuple[str,List[Points]]]) ->str:
        """Gets the name of the graph"""
        title = ""
        for name, _ in categories:
            title += name + " "
        title += str(graphParameter.featuresToSingleVal) + " " + str(graphParameter.xFeatureCreator) + " Comparison"
        return title

