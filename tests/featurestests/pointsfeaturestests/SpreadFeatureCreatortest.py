import unittest
from features.Features import Features
from features.pointsfeatures.SpreadFeatureCreator import SpreadFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
import unittest

class SpreadFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self):
        """Gets the spreadFeatureCreator to test"""
        return SpreadFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the spreadFeatureCreator"""
        points = Points([
            Point(1,2,3,4),
            Point(3,4,6,8),
            Point(5,6,9,12),
        ])
        xFeatureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val((4 + 4  + 9)**0.5)
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val((4 + 4  + 9)**0.5)
        
        self.assertEquals(xFeatureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "Spread")