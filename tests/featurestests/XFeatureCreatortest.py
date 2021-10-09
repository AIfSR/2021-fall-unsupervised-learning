import unittest
from features.Features import Features
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points

class XFeatureCreatorTest (unittest.TestCase):

    def test_get_features(self):
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        xFeatureCreator = XFeatureCreator(points)

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(5)
        solutionFeatures.add_feature_val(9)
        
        self.assertEquals(xFeatureCreator.get_features(), solutionFeatures)