

from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class PointsDistanceFeatureCreator (FeatureCreatorBase):

    def get_features(self) -> Features:
        """Creates a feature that gets the euclidean distance between every 
        point"""

        for i in range(len(self._points)-1):
            currentPoint = self._points[i]
            nextPoint = self._points[i + 1]

            xdifference = nextPoint.get_x() - currentPoint.get_x()
            ydifference = nextPoint.get_y() - currentPoint.get_y()
            zdifference = nextPoint.get_z() - currentPoint.get_z()
            distance = (xdifference**2 + ydifference**2 + zdifference**2)**0.5

            self._features.add_feature_val(distance) 
        if len(self._points) > 1:
            self._features.add_feature_val(distance) 
            # this line needs to be here so that there are an equal amount of 
            # feature values as points passed in
        return self._features
