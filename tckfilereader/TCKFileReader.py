from tckfilereader.Points import Points
from tckfilereader.Point import Point
import os


class TCKFileReader:
    
    def get_points(self, path_to_tck_file:str) -> Points:
        """Gets all of the points from the specified TCK file."""
        script = os.path.dirname(__file__)
        script1 = os.path.dirname(script)
        path = os.path.join(script1, path_to_tck_file)
        with open(path) as file:
            xLine = file.readline()
            xList = xLine.split()
            yLine = file.readline()
            yList = yLine.split()
            zLine = file.readline()
            zList = zLine.split()
            tLine = file.readline()
            tList = tLine.split()
        xList = [float(x.replace(',', '.')) for x in xList]
        yList = [float(y.replace(',', '.')) for y in yList]
        zList = [float(z.replace(',', '.')) for z in zList]
        tList = [float(t.replace(',', '.')) for t in tList]
        allPoints = Points()
        for i in range(len(xList)):
            allPoints.addPoint(Point(xList[i], yList[i], zList[i], tList[i]))
        return allPoints

