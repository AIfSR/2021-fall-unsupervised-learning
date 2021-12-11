from typing import List, Tuple
from featuretosingleval.AverageOfFeature import AverageOfFeature
from plotting.ComparePlotsBase import ComparePlotsBase
from plotting.GraphParameters import GraphParameters
from plotting.singlepointcomparetrajectories.SinglePoint1DCompareTrajectories import SinglePoint1DCompareTrajectories
from plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories
from tckfilereader.Points import Points


class SinglePointCompareTrajectoriesFactory (ComparePlotsBase):

    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]):
        """Goes through all of the graph parameters and creates the correct graphing objects and plot them."""
        for graphParameter in graphParameters:
            self._update_graph_parameters(graphParameter)
            singlePointCompareTrajectory = self._get_single_point_compare_trajectory(graphParameter)
            singlePointCompareTrajectory.display_plots([graphParameter], categories)

    def _get_single_point_compare_trajectory(self, graphParameter:GraphParameters) -> ComparePlotsBase:
        """Gets the right object to display the plots passed in."""
        if graphParameter.yFeatureCreator is None:
            return SinglePoint1DCompareTrajectories()
        return SinglePoint2DCompareTrajectories()

    def _update_graph_parameters(self, graphParameter:GraphParameters) -> None:
        """Updates the graph parameters with the necessary information it may not have."""
        if graphParameter.featuresToSingleVal is None:
            graphParameter.featuresToSingleVal = AverageOfFeature()
        if graphParameter.xLabel is None:
            graphParameter.xLabel = str(graphParameter.featuresToSingleVal) + " " + str(graphParameter.xFeatureCreator)
        if graphParameter.yFeatureCreator is not None and graphParameter.yLabel is None:
            graphParameter.yLabel = str(graphParameter.featuresToSingleVal) + " " + str(graphParameter.yFeatureCreator)
        

        
