import unittest
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.MedianOfFeature import MedianOfFeature
from plotting.GraphParameters import GraphParameters
from plotting.singlepointcomparetrajectories.SinglePoint1DCompareTrajectories import SinglePoint1DCompareTrajectories
from plotting.singlepointcomparetrajectories.SinglePoint2DCompareTrajectories import SinglePoint2DCompareTrajectories

from plotting.singlepointcomparetrajectories.SinglePointCompareTrajectoriesFactory import SinglePointCompareTrajectoriesFactory

singlePointCompareTrajectoresFactory = SinglePointCompareTrajectoriesFactory()
twoDGraphParameters = GraphParameters(XFeatureCreator())
solution = GraphParameters(XFeatureCreator(), xLabel=str(XFeatureCreator()), featuresToSingleVal=AverageOfFeature())
singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
print(twoDGraphParameters)
print(solution)

twoDGraphParameters = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this")
solution = GraphParameters(XFeatureCreator(), yFeatureCreator=YFeatureCreator(), xLabel="this", yLabel=str(YFeatureCreator()), featuresToSingleVal=AverageOfFeature())
singlePointCompareTrajectoresFactory._update_graph_parameters(twoDGraphParameters)
print(twoDGraphParameters)
print(solution)
