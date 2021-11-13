import unittest
from features.Features import Features
from features.OutlierFeatureCreator import OutlierFeatureCreator
from features.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class OutlierFeatureCreatorTest (FeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the OutlierFeatureCreator to test"""
        return OutlierFeatureCreator(XFeatureCreator(),1.5)

    def test_get_features(self):
        """Tests getting features from the OutlierFeatureCreator Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(1,6,7,8),
            Point(1,10,11,12),
            Point(100,10,11,12),
            Point(1,10,11,12),
            Point(1,10,11,12),
            Point(-100,10,11,12),
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val(1)
        
        self.assertEquals(featureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "X Outliers: 1.5")