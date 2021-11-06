import unittest
from features.Features import Features
from features.XDisplacementFeatureCreator import XDisplacementFeatureCreator
from tckfilereader.Point import Point
from tckfilereader.Points import Points
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase


class XDisplacementFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return XDisplacementFeatureCreator()

    def test_get_features(self):
        """Tests getting the features from the PointsDistanceFeatureCreator"""
        points = Points([
            Point(0,0,0,1),
            Point(1,0,0,2),
            Point(1,1,0,3),
            Point(0,0,0,4),
            Point(1,1,1,5),
        ])
        xDisplacementFeatureCreator = XDisplacementFeatureCreator()
        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1)
        # solutionFeatures.add_feature_val(3.0**0.5)

        self.assertEquals(xDisplacementFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = XDisplacementFeatureCreator()
        self.assertEquals(str(featureCreator), "PointsDistance")


