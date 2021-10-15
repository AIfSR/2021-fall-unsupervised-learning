import unittest
from features.Features import Features
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points

class RateOfChangeFeatureCreatorTest (unittest.TestCase):

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        rateOfChangeFeatureCreator = RateOfChangeFeatureCreator(points, XFeatureCreator(points))

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val((5-1) / (8-4))
        solutionFeatures.add_feature_val((9-5) / (12-8))
        
        self.assertEquals(rateOfChangeFeatureCreator.get_features(), solutionFeatures)