import unittest

from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator
from tckfilereader.Point import Point
from tckfilereader.Points import Points

class LineFeatureCreatorTest (unittest.TestCase):

    def test_get_features(self) -> None:
        """Tests that the features created are all one number so that they are plotted along the same line"""

        lineFeatureCreator = LineFeatureCreator()
        points = Points()
        points.addPoint(Point(1,2,3,4))
        points.addPoint(Point(1,2,3,4))
        points.addPoint(Point(1,2,3,4))
        points.addPoint(Point(1,2,3,4))
        points.addPoint(Point(1,2,3,4))
        points.addPoint(Point(1,2,3,4))

        features = lineFeatureCreator.get_features(points)
        self.assertEquals(len(points), len(features))
        for val in features:
            self.assertAlmostEquals(0.0, val)

    def test_increment(self) -> None:
        """Tests incrementing the line that all of the features are plotted along within the line feature creator"""
        
        lineFeatureCreator = LineFeatureCreator()
        points1 = Points()
        points1.addPoint(Point(1,2,3,4))
        points1.addPoint(Point(1,2,3,4))
        points1.addPoint(Point(1,2,3,4))
        points2 = Points()
        points2.addPoint(Point(1,2,3,4))
        points2.addPoint(Point(1,2,3,4))
        points2.addPoint(Point(1,2,3,4))

        features1 = lineFeatureCreator.get_features(points1)
        lineFeatureCreator.increment()
        features2 = lineFeatureCreator.get_features(points2)
        self.assertEquals(len(points1), len(features1))
        for val in features1:
            self.assertAlmostEquals(0.0, val)

        self.assertEquals(len(points2), len(features2))
        for val in features2:
            self.assertAlmostEquals(1.0, val)

    def test_str(self) -> None:
        """Tests that the string representation of a line feature creator is nothing"""

        lineFeatureCreator = LineFeatureCreator()
        self.assertEquals(str(lineFeatureCreator), "")