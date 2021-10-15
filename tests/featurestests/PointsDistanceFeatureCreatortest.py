import unittest
from features.Features import Features
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from tckfilereader.Point import Point
from tckfilereader.Points import Points

class PointsDistanceFeatureCreatorTest (unittest.TestCase):
    def test_get_features(self):
        points = Points([
            Point(0,0,0,1),
            Point(1,0,0,2),
            Point(1,1,0,3),
            Point(0,0,0,4),
            Point(1,1,1,5),
        ])
        pointsDistanceFeatureCreator = PointsDistanceFeatureCreator(points)

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(2.0**0.5)
        solutionFeatures.add_feature_val(3.0**0.5)
        solutionFeatures.add_feature_val(3.0**0.5)
        
        self.assertEquals(pointsDistanceFeatureCreator.get_features(), solutionFeatures)


