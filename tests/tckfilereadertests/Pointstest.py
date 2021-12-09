import unittest
from tckfilereader.Points import Points
from tckfilereader.Point import Point

class TestPointsMethods(unittest.TestCase):

    def test_points_init(self):
        pointsString = Points([])
        x = pointsString.pointsList
        self.assertEquals(x, [], "expected empty array")

    def test_points_append(self):
        pointsString1 = Points()
        point1 = Point(1,2,3,4)
        pointsString1.addPoint(point1)
        self.assertEquals(pointsString1.pointsList[0], point1)

    def test_points_str(self):
        pointsString2 = Points([Point(1,2,3,4)])
        self.assertEquals(str(pointsString2), "Point(1.0,2.0,3.0,4.0)")

    def test_points_iter(self):
        a_list=Points([])
        point1 = Point(1,2,3,4)
        point2 = Point(4,5,6,7)
        a_list.addPoint(point1)
        a_list.addPoint(point2)
        it1=iter(a_list)
        self.assertEquals(next(it1),point1)
        self.assertEquals(next(it1),point2)

    def test_points_eq(self):
        a_list=Points()
        b_list=Points()
        point1 = Point(1,2,3,4)
        point2 = Point(1,2,3,4)
        a_list.addPoint(point1)
        b_list.addPoint(point2)
        self.assertEquals(a_list,b_list)

    def test_inexing(self):
        """Tests indexing methods within Points"""
        a_list=Points()
        point1 = Point(1,2,3,4)
        point2 = Point(1,2,3,4)
        a_list.addPoint(point1)
        a_list.addPoint(point2)
        self.assertEquals(a_list[0], point1)
        self.assertEquals(a_list[1], point2)

    def test_length(self):
        a_list=Points()
        point1 = Point(1,2,3,4)
        point2 = Point(1,2,3,4)
        a_list.addPoint(point1)
        a_list.addPoint(point2)
        self.assertEquals(len(a_list), 2)

