import unittest
from features.Features import Features
from features.genericfeatures.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.pointsfeatures.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
from features.pointsfeatures.TFeatureCreator import TFeatureCreator
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return RateOfChangeFeatureCreator(XFeatureCreator(), TFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Points([
            Point(1,2,3,4),
            Point(5,6,7,8),
            Point(9,10,11,12),
        ])
        rateOfChangeFeatureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        # solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val((5-1) / (8-4))
        solutionFeatures.add_feature_val((9-5) / (12-8))
        
        self.assertEquals(rateOfChangeFeatureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = RateOfChangeFeatureCreator(XFeatureCreator(), TFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC:X")
        featureCreator = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator(), TFeatureCreator()), TFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC^2:X")
        featureCreator = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator(), TFeatureCreator()), TFeatureCreator()), TFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC^3:X")

        featureCreator = XFeatureCreator()
        timeFeatureCreator = TFeatureCreator()
        for i in range(200):
            featureCreator = RateOfChangeFeatureCreator(featureCreator, timeFeatureCreator)

        self.assertEquals(str(featureCreator), "RoC^200:X")
