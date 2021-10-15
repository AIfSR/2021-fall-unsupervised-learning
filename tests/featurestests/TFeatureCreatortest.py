import unittest
from features.Features import Features
from features.TFeatureCreator import TFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points

class TFeatureCreatorTest (unittest.TestCase):

    def test_get_features(self):
        """Tests getting features from the T Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        tFeatureCreator = TFeatureCreator(points)

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(4)
        solutionFeatures.add_feature_val(8)
        solutionFeatures.add_feature_val(12)
        
        self.assertEquals(tFeatureCreator.get_features(), solutionFeatures)