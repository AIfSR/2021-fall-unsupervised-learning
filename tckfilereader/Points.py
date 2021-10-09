from typing import List
from tckfilereader.Point import Point

class Points:
    def __init__(self, pointsList:List[Point]=None) -> None:
        """A Points class stores all the points generated from a tck file"""
        self.pointsList = pointsList or []
        pass
    
    def addPoint(self, point:Point) -> None:
        """Adds the Point to the list of points"""