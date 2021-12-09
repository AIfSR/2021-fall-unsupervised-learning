from features.DeltaFromStartFeatureCreator import DeltaFromStartFeatureCreator
from features.EWAFeatureCreator import EWAFeatureCreator
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Point import Point
from tckfilereader.Points import Points
import unittest

from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class DummyFeatureCreator (FeatureCreatorBase):
    
    def get_features(self, points:Points) -> Features:
        """Gets a set of features with values 1, 2, 3, 4"""
        features = Features()
        for i in range(len(points)):
            features.add_feature_val(i)
        return features
    
    def __str__(self) -> str:
        return "DummyFeatureCreator"

class EWAFeatureCreatorTest (FeatureCreatorTestBase):

    def get_feature_creator(self) -> FeatureCreatorBase:
        """Gets the EWAFeatureCreator to test"""
        return EWAFeatureCreator(DummyFeatureCreator(), beta=0.9, skipValues=0)

    def test_get_features(self):
        """Tests getting features from the EWAFeatureCreator"""
        solution = Features()
        solution.add_feature_val(0)
        solution.add_feature_val((1*0.1) / (1 - 0.9**2))
        featureCreator = self.get_feature_creator()
        points = Points([Point(0,0,0,0), Point(0,0,0,0)])
        self.assertEquals(featureCreator.get_features(points), solution)

    def test_string(self):
        """Tests the name generated from a EWAFeatureCreator"""
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "EWA:DummyFeatureCreator")


