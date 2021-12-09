

import unittest
from features.Features import Features
from features.EliminatePointsOutsideRangeFeatureCreator import EliminatePointsOutsideRangeFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
import math

class PhiFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self):
        """Gets the EliminatePointsOutsideRangeFeatureCreator to test"""
        return EliminatePointsOutsideRangeFeatureCreator(0.3, 0.6, XFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the EliminatePointsOutsideRange Feature Creator"""
        points = Points([
            Point(4,0,0,4),
            Point(1,1,0,8),
            Point(6,1,-1,12),
            Point(3,0,0,4),
            Point(4,1,0,8),
            Point(-1,1,-1,12),
            Point(-2,0,0,4),
            Point(1,1,0,8),
            Point(9,1,-1,12),
            Point(-99,1,-1,12),
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(6.0)
        solutionFeatures.add_feature_val(3.0)
        solutionFeatures.add_feature_val(4.0)
        solutionFeatures.add_feature_val(-1.0)

        feature = featureCreator.get_features(points)
        self.assertEquals(len(feature), len(solutionFeatures))
        for featureVal, solutionVal in zip(feature, solutionFeatures):
            self.assertEquals(featureVal, solutionVal)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "X Kept: 0.3-0.6")