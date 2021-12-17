from features.genericfeatures.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Point import Point
from tckfilereader.Points import Points
import unittest

import unittest

class DummyFeatureCreator (FeatureCreatorBase):
    
    def get_features(self, points:Points) -> Features:
        """Gets a set of features with values 1, 2, 3, 4"""
        features = Features()
        for i in range(len(points)):
            features.add_feature_val(i)
        return features
    
    def __str__(self) -> str:
        return "DummyFeatureCreator"

class DeltaFromStartFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self) -> FeatureCreatorBase:
        """Gets the DeltaFromStartFeatureCreator to test"""
        return DeltaFromStartFeatureCreator(DummyFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the DeltaFromStartFeatureCreator"""
        solution = Features()
        solution.add_feature_val(0)
        solution.add_feature_val(1)
        solution.add_feature_val(2)
        solution.add_feature_val(3)
        featureCreator = self.get_feature_creator()
        points = Points([Point(0,0,0,0), Point(0,0,0,0),Point(0,0,0,0),Point(0,0,0,0),])
        self.assertEquals(featureCreator.get_features(points), solution)

    def test_string(self):
        """Tests the name generated from a DeltaFromStartFeatureCreator"""
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "DfS:DummyFeatureCreator")


