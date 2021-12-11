import unittest
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.MedianOfFeature import MedianOfFeature
from plotting.GraphParameters import GraphParameters
from plotting.singleepisodecomparetrajectories.SingleEpisode1DCompareTrajectories import SingleEpisode1DCompareTrajectories
from plotting.singleepisodecomparetrajectories.SingleEpisode2DCompareTrajectories import SingleEpisode2DCompareTrajectories

from plotting.singleepisodecomparetrajectories.SingleEpisodeCompareTrajectoriesFactory import SingleEpisodeCompareTrajectoriesFactory

class SingleEpisodeCompareTrajectoriesFactoryTest (unittest.TestCase):

    def test_get_single_episode_compare_trajectory(self):
        """Tests that _get_single_episode_compare_trajectory gets the right instance of 
        each SingleEpisodeCompareTrajectories depending on the parameters"""
        singleEpisodeCompareTrajectoresFactory = SingleEpisodeCompareTrajectoriesFactory()
        
        twoDGraphParameters = GraphParameters(XFeatureCreator())
        self.assertTrue(type(singleEpisodeCompareTrajectoresFactory._get_single_episode_compare_trajectory(twoDGraphParameters)) == SingleEpisode1DCompareTrajectories)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator())
        self.assertTrue(type(singleEpisodeCompareTrajectoresFactory._get_single_episode_compare_trajectory(twoDGraphParameters)) == SingleEpisode2DCompareTrajectories)

    def test_update_graph_parameters(self):
        """Tests that _update_graph_parameters updates the labels for twoDGraphParameters"""
        singleEpisodeCompareTrajectoresFactory = SingleEpisodeCompareTrajectoriesFactory()

        twoDGraphParameters = GraphParameters(XFeatureCreator())
        solution = GraphParameters(XFeatureCreator(), xLabel="Average X", featuresToSingleVal=AverageOfFeature())
        singleEpisodeCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator())
        solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="Average X", yLabel="Average Y", featuresToSingleVal=AverageOfFeature())
        singleEpisodeCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this")
        solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel="Average Y", featuresToSingleVal=AverageOfFeature())
        singleEpisodeCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel="that")
        solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel="that", featuresToSingleVal=AverageOfFeature())
        singleEpisodeCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), featuresToSingleVal=MedianOfFeature())
        solution = GraphParameters(XFeatureCreator(), xLabel="Median X", featuresToSingleVal=MedianOfFeature())
        singleEpisodeCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)
