

from typing import List, Tuple
from featuretosingleval.AverageOfFeature import AverageOfFeature
from plotting.ComparePlotsBase import ComparePlotsBase
from plotting.GraphParameters import GraphParameters
from plotting.singleepisodecomparetrajectories.SingleEpisode1DCompareTrajectories import SingleEpisode1DCompareTrajectories
from plotting.singleepisodecomparetrajectories.SingleEpisode2DCompareTrajectories import SingleEpisode2DCompareTrajectories
from xlsxfilereader.Episodes import Episodes


class SingleEpisodeCompareTrajectoriesFactory (ComparePlotsBase):

    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Episodes]]]):
        """Goes through all of the graph parameters and creates the correct graphing objects and plot them."""
        for graphParameter in graphParameters:
            self._update_graph_parameters(graphParameter)
            singleEpisodeCompareTrajectory = self._get_single_episode_compare_trajectory(graphParameter)
            singleEpisodeCompareTrajectory.display_plots([graphParameter], categories)

    def _get_single_episode_compare_trajectory(self, graphParameter:GraphParameters) -> ComparePlotsBase:
        """Gets the right object to display the plots passed in."""
        if graphParameter.yFeatureCreator is None:
            return SingleEpisode1DCompareTrajectories()
        return SingleEpisode2DCompareTrajectories()

    def _update_graph_parameters(self, graphParameter:GraphParameters) -> None:
        """Updates the graph parameters with the necessary information it may not have."""
        if graphParameter.xLabel is None:
            graphParameter.xLabel = str(graphParameter.featuresToSingleVal) + " " + str(graphParameter.xFeatureCreator)
        if graphParameter.yFeatureCreator is not None and graphParameter.yLabel is None:
            graphParameter.yLabel = str(graphParameter.featuresToSingleVal) + " " + str(graphParameter.yFeatureCreator)
        if graphParameter.featuresToSingleVal is None:
            graphParameter.featuresToSingleVal = AverageOfFeature()

