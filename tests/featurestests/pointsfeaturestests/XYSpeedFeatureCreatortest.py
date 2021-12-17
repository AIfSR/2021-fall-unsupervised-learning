import unittest
from features.Features import Features
from features.pointsfeatures.XYSpeedFeatureCreator import XYSpeedFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
# import unittest

class XYSpeedFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self):
        """Gets the XYSpeedFeatureCreator to test"""
        return XYSpeedFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the XYSpeedFeatureCreator"""
        points = Points([
            Point(1,2,3,4),
            Point(-3,6,7,8),
            Point(5,14,11,12),
        ])
        xFeatureCreator = self.get_feature_creator()

        solutionFeatures = Features()

        firstSpeed = (2)**0.5
        secondSpeed = (8)**0.5

        # solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(firstSpeed)
        solutionFeatures.add_feature_val(secondSpeed)

        features = xFeatureCreator.get_features(points)
        self.assertEquals(len(features), len(solutionFeatures))
        for speed, solutionSpeed in zip(features, solutionFeatures):
            self.assertAlmostEquals(speed, solutionSpeed, delta=0.0001)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "XYSpeed")
