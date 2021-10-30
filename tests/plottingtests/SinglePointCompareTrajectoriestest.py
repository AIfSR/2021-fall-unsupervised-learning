import unittest

from features.Features import Features
from plotting.SinglePointCompareTrajectories import SinglePointCompareTrajectories
from plotting.SinglePointCompareTrajectories import LineFeatureCreator
from tckfilereader.Point import Point
from tckfilereader.Points import Points

class SinglePointCompareTrajectoriesTest (unittest.TestCase):

    def test_get_average_of_feature(self) -> None:
        """Tests the method that gets the average of a feature"""
        feature = Features()
        lst = [1,2,3,5,2.7,4.6,2.3]
        for val in lst:
            feature.add_feature_val(val)
        solution = sum(lst) / len(lst)
        singlePointCompareTrajectories = SinglePointCompareTrajectories()
        self.assertEquals(singlePointCompareTrajectories._get_average_of_feature(feature), solution)

    def test_line_feature_creator(self) -> None:
        """Tests creating the feature creator base that is just a line for 
        plotting purposes"""

        lineFeatureCreator = LineFeatureCreator()
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        solutionFeature = Features()
        solutionFeature.add_feature_val(0.0)
        solutionFeature.add_feature_val(0.0)
        solutionFeature.add_feature_val(0.0)
        
        self.assertEquals(lineFeatureCreator.get_features(points), solutionFeature)
        self.assertEquals(str(lineFeatureCreator), "")


