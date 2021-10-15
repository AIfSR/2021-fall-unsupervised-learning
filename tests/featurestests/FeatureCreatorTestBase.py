import unittest
from abc import ABC, abstractmethod
from features.FeatureCreatorBase import FeatureCreatorBase
from tckfilereader.Point import Point
from tckfilereader.Points import Points
import random

class FeatureCreatorTestBase (unittest.TestCase):

    @abstractmethod
    def get_feature_creator(self) -> FeatureCreatorBase:
        """Gets the feature creator being tested"""
        pass

    def test_length_of_feature(self):
        """Tests that the length of the features and length of points are the same"""
        points = Points()
        for i in range(random.randint(2,10)):
            points.addPoint(Point(random.random()*10,random.random()*10,random.random()*10,i))

        feature = self.get_feature_creator().get_features(points)
        self.assertEquals(len(feature), len(points))

