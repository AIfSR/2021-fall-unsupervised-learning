import unittest
from features.Features import Features
from features.ZFeatureCreator import ZFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points

class ZFeatureCreatorTest (unittest.TestCase):

    def test_get_features(self):
        """Tests getting features from the Z Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        xFeatureCreator = ZFeatureCreator(points)

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(3)
        solutionFeatures.add_feature_val(7)
        solutionFeatures.add_feature_val(11)
        
        self.assertEquals(xFeatureCreator.get_features(), solutionFeatures)