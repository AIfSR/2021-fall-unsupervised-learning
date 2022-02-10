import unittest
import numpy as np
from features.Features import Features
from features.MSDFeatureCreator import MSDFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return MeanSquaredDisplacementFeatureCreator(XFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Points([
            Point(0,2,3,0),
            Point(1,2,3,1),
            Point(2,2,3,2),
            Point(0,2,3,3),
        ])
        rateOfChangeFeatureCreator = MSDFeatureCreator(XFeatureCreator())

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(6/3)
        solutionFeatures.add_feature_val(5/2)
        solutionFeatures.add_feature_val(0)
        self.assertEquals(rateOfChangeFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = MSDFeatureCreator(XFeatureCreator())
        self.assertEquals(str(featureCreator), "MSD:X")
        featureCreator = MSDFeatureCreator(MSDFeatureCreator(XFeatureCreator()))
        self.assertEquals(str(featureCreator), "MSD^2:X")
        featureCreator = MSDFeatureCreator(MSDFeatureCreator(MSDFeatureCreator(XFeatureCreator())))
        self.assertEquals(str(featureCreator), "MSD^3:X")

        featureCreator = XFeatureCreator()
        for i in range(200):
            featureCreator = MSDFeatureCreator(featureCreator)

        self.assertEquals(str(featureCreator), "MSD^200:X")
