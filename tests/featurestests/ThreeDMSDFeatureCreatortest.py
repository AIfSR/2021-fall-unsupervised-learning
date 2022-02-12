import unittest
import numpy as np
from features.Features import Features
from features.ThreeDMSDFeatureCreator import ThreeDMSDFeatureCreator
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return ThreeDMSDFeatureCreator(XFeatureCreator(),YFeatureCreator(),ZFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Points([
            Point(0,2,3,0),
            Point(1,2,3,1),
            Point(2,2,3,2),
            Point(0,2,3,3),
        ])
        rateOfChangeFeatureCreator = ThreeDMSDFeatureCreator(XFeatureCreator(),YFeatureCreator(),ZFeatureCreator())

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(6/3)
        solutionFeatures.add_feature_val(5/2)
        solutionFeatures.add_feature_val(0)
        self.assertEquals(rateOfChangeFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = ThreeDMSDFeatureCreator(XFeatureCreator(),YFeatureCreator(),ZFeatureCreator())
        self.assertEquals(str(featureCreator), "3DMSD:XYZ")
