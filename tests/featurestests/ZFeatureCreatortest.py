import unittest
from features.Features import Features
from features.pointsfeatures.ZFeatureCreator import ZFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class ZFeatureCreatorTest (FeatureCreatorTestBase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return ZFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the Z Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        zFeatureCreator = ZFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(3)
        solutionFeatures.add_feature_val(7)
        solutionFeatures.add_feature_val(11)
        
        self.assertEquals(zFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = ZFeatureCreator()
        self.assertEquals(str(featureCreator), "Z")