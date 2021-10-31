import unittest
from features.Features import Features
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return RateOfChangeFeatureCreator(XFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        rateOfChangeFeatureCreator = RateOfChangeFeatureCreator(XFeatureCreator())

        solutionFeatures = Features()
        # solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val((5-1) / (8-4))
        solutionFeatures.add_feature_val((9-5) / (12-8))
        
        self.assertEquals(rateOfChangeFeatureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = RateOfChangeFeatureCreator(XFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC:X")
        featureCreator = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator()))
        self.assertEquals(str(featureCreator), "RoC^2:X")
        featureCreator = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())))
        self.assertEquals(str(featureCreator), "RoC^3:X")

        featureCreator = XFeatureCreator()
        for i in range(200):
            featureCreator = RateOfChangeFeatureCreator(featureCreator)

        self.assertEquals(str(featureCreator), "RoC^200:X")
