import unittest
from features.Features import Features
from features.SignChangeFeatureCreator import SignChangeFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class SignChangeFeatureCreatorTest (FeatureCreatorTestBase):
    def get_feature_creator(self):
        """Gets the SignChangeFeatureCreator to test"""
        return SignChangeFeatureCreator(XFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the Y Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(-5,6,7,8),
            Point(-9,10,11,12),
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(0)
        
        self.assertEquals(featureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "SignChange:X")