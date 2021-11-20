from typing import List, Tuple
from features.Features import Features
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from plotting.ComparePlotsBase import ComparePlotsBase
from plotting.GraphParameters import GraphParameters
from tckfilereader.Points import Points
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


class SinglePoint1DCompareTrajectories (ComparePlotsBase):

    def __init__(self) -> None:
        super().__init__()

    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all of the 1 dimentsional plots passed in."""
        for graphParameter in graphParameters:
            plt.close()
            ax = self.setup_fig()
            names = []
            data = []
            for name, pointsList in categories:
                pointAverages = []
                names.append(name)
                for points in pointsList:
                    features = graphParameter.xFeatureCreator.get_features(points)
                    singleVal = graphParameter.featuresToSingleVal.get_val(features)
                    pointAverages.append(singleVal)
                data.append(pointAverages)

            ax.boxplot(data, patch_artist = True, vert = 0)
            ax.set_yticklabels(names, fontdict = {'fontsize':16})
            plt.title(self.get_title(graphParameter, categories), fontsize=20)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
            ax.set_xlabel(graphParameter.xLabel, fontsize=16)
            plt.show()


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

