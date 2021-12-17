import unittest
from features.pointsfeatures.XFeatureCreator import XFeatureCreator
from features.pointsfeatures.YFeatureCreator import YFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.MedianOfFeature import MedianOfFeature
from plotting.GraphParameters import GraphParameters
from plotting.singlepointcomparetrajectories.SinglePoint1DCompareTrajectories import SinglePoint1DCompareTrajectories
from plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories

from plotting.singlepointcomparetrajectories.SinglePointCompareTrajectoriesFactory import SinglePointCompareTrajectoriesFactory

class SinglePointCompareTrajectoriesFactoryTest (unittest.TestCase):

    def test_get_single_point_compare_trajectory(self):
        """Tests that _get_single_point_compare_trajectory gets the right instance of 
        each SinglePointCompareTrajectories depending on the parameters"""
        singlePointCompareTrajectoresFactory = SinglePointCompareTrajectoriesFactory()
        
        twoDGraphParameters = GraphParameters(XFeatureCreator())
        self.assertTrue(type(singlePointCompareTrajectoresFactory._get_single_point_compare_trajectory(twoDGraphParameters)) == SinglePoint1DCompareTrajectories)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator())
        self.assertTrue(type(singlePointCompareTrajectoresFactory._get_single_point_compare_trajectory(twoDGraphParameters)) == SinglePoint2DCompareTrajectories)

    def test_update_graph_parameters(self):
        """Tests that _update_graph_parameters updates the labels for twoDGraphParameters"""
        singlePointCompareTrajectoresFactory = SinglePointCompareTrajectoriesFactory()

        twoDGraphParameters = GraphParameters(XFeatureCreator())
        solution = GraphParameters(XFeatureCreator(), xLabel="Average X", featuresToSingleVal=AverageOfFeature())
        singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator())
        solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="Average X", yLabel="Average Y", featuresToSingleVal=AverageOfFeature())
        singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this")
        solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel="Average Y", featuresToSingleVal=AverageOfFeature())
        singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel="that")
        solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel="that", featuresToSingleVal=AverageOfFeature())
        singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)

        twoDGraphParameters = GraphParameters(XFeatureCreator(), featuresToSingleVal=MedianOfFeature())
        solution = GraphParameters(XFeatureCreator(), xLabel="Median X", featuresToSingleVal=MedianOfFeature())
        singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
        self.assertEquals(twoDGraphParameters, solution)
