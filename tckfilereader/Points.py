from typing import List
from tckfilereader.Point import Point

class PointsIterator:
    """Iterator class """
    def __init__(self, points):
        self._points = points
        self._index = 0

    def __next__(self):
        """Returns the next value from Points object's lists"""
        if self._index < (len(self._points.pointsList)):
            result = self._points.pointsList[self._index]
            self._index += 1
            return result
        raise StopIteration

class Points:
    def __init__(self, pointsList:List[Point]=None) -> None:
        """A Points class stores all the points generated from a tck file"""
        self.pointsList = pointsList or []
        pass
    
    def addPoint(self, point:Point) -> None:
        """Adds the Point to the list of points"""
        self.pointsList.append(point)

    def __str__(self) -> str:
        """displays array in a string"""
        _result = ""
        for counter in range(len(self.pointsList)-1):
            _result += "Point(%s,%s,%s,%s)," % (self.pointsList[counter].x, self.pointsList[counter].y, self.pointsList[counter].z, self.pointsList[counter].t)
        _result += "Point(%s,%s,%s,%s)" % (self.pointsList[len(self.pointsList)-1].x, self.pointsList[len(self.pointsList)-1].y, self.pointsList[len(self.pointsList)-1].z, self.pointsList[len(self.pointsList)-1].t)
        return _result

    def __iter__(self):
        """Returns the Iterator object"""
        return PointsIterator(self)




