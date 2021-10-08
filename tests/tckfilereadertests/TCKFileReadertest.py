import unittest
from tckfilereader.TCKFileReader import TCKFileReader
from tckfilereader.Points import Points
from tckfilereader.Point import Point

class TCKFileReaderTest (unittest.TestCase):

    def test_5(self):
        self.assertEquals(5, 5)

    def test_get_points(self):
        path = "tests/tckfilereadertests/testfile.tck"
        tckFileReader = TCKFileReader()

        solutionPoints = Points()
        solutionPoints.addPoint(Point(1,6,11,15))
        solutionPoints.addPoint(Point(2,7,12,16))
        solutionPoints.addPoint(Point(3,8,13,17))
        solutionPoints.addPoint(Point(4,9,14,18))
        solutionPoints.addPoint(Point(5,10,15,19))
        
        self.assertEquals(tckFileReader.get_points(path), solutionPoints)
