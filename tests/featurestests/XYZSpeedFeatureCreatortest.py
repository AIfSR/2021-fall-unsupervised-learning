import unittest
from features.Features import Features
from features.XYZSpeedFeatureCreator import XYZSpeedFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class XYZSpeedFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self):
        """Gets the XYZSpeedFeatureCreatorTest to test"""
        return XYZSpeedFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the X Feature Creator"""
        points = Points([
            Point(0,0,0,1),
            Point(1,1,1,2),
            Point(2,2,1,3),
        ])
        xFeatureCreator = self.get_feature_creator()

        solutionFeatures = Features()

        firstSpeed = (3)**0.5
        secondSpeed = (2)**0.5

        solutionFeatures.add_feature_val(firstSpeed)
        solutionFeatures.add_feature_val(secondSpeed)

        features = xFeatureCreator.get_features(points)
        self.assertEquals(len(features), len(solutionFeatures))
        for speed, solutionSpeed in zip(features, solutionFeatures):
            print("------------")
            print("speed: " + str(speed))
            print("solutionSpeed: " + str(solutionSpeed))
            print("------------")
            self.assertAlmostEquals(speed, solutionSpeed, delta=0.0001)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "XYZSpeed")
