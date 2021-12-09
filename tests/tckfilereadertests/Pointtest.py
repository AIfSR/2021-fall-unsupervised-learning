import unittest
from tckfilereader.Point import Point


class TestPointMethods(unittest.TestCase):
    def test_point_init(self):
        point = Point(1,2,3,4)
        self.assertEquals(point.x, 1)
        self.assertEquals(point.y, 2)
        self.assertEquals(point.z, 3)
        self.assertEquals(point.t, 4)

    def test_point_str(self):
        point = Point(1,2,3,4)
        self.assertEquals(str(point),"Point(1.0,2.0,3.0,4.0)")

    def test_point_eq(self):
        point = Point(1,2,3,4)
        point2 = Point(1,2,3,4)
        self.assertEquals(point, point2)
