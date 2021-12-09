import unittest
from features.Features import Features
from features.PhiFeatureCreator import PhiFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
import math

class PhiFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return PhiFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the X Feature Creator"""
        points = Points([
            Point(0,0,0,4),
            Point(1,1,0,8),
            Point(1,1,-1,12),
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(math.pi / 2)
        solutionFeatures.add_feature_val(math.pi)
        feature = featureCreator.get_features(points)
        self.assertEquals(len(feature), len(solutionFeatures))
        for featureVal, solutionVal in zip(feature, solutionFeatures):
            self.assertEquals(featureVal, solutionVal)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "Phi")