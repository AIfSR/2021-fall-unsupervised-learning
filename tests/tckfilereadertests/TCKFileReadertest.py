import unittest
from tckfilereader.TCKFileReader import TCKFileReader
from tckfilereader.Points import Points
from tckfilereader.Point import Point

class TCKFileReaderTest (unittest.TestCase):

    def test_get_points(self):
        """Tests getting points from a tck file"""
        path = "tests/tckfilereadertests/testfile2.tck"
        tckFileReader = TCKFileReader()
        solutionPoints = Points()
        solutionPoints.addPoint(Point(1,6,11,16))
        solutionPoints.addPoint(Point(2,7,12,17))
        solutionPoints.addPoint(Point(3,8,13,18))
        solutionPoints.addPoint(Point(4,9,14,19))
        solutionPoints.addPoint(Point(5,10,15,20))
        testPoints = tckFileReader.get_points(path)
        self.assertEquals(testPoints, solutionPoints)

