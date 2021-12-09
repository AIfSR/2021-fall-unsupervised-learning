import unittest
from features.Features import Features
from features.PointsDisplacementFeatureCreator import PointsDisplacementFeatureCreator
from tckfilereader.Point import Point
from tckfilereader.Points import Points
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase


class PointsDistanceFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return PointsDisplacementFeatureCreator()

    def test_get_features(self):
        """Tests getting the features from the PointsDistanceFeatureCreator"""
        points = Points([
            Point(0,0,0,1),
            Point(1,0,0,2),
            Point(1,1,0,3),
            Point(0,0,0,4),
            Point(1,1,1,5),
        ])
        pointsDistanceFeatureCreator = PointsDisplacementFeatureCreator()
        solutionFeatures = Features()
        solutionFeatures.add_feature_val(3.0**0.5)
        # solutionFeatures.add_feature_val(3.0**0.5)

        self.assertEquals(pointsDistanceFeatureCreator.get_features(points), solutionFeatures)

    def test_string(self):
        featureCreator = PointsDisplacementFeatureCreator()
        self.assertEquals(str(featureCreator), "PointsDisplacement")


