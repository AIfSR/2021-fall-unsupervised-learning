

from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class PointsDistanceFeatureCreator (FeatureCreatorBase):

    def get_features(self, points:Points) -> Features:
        """Creates a feature that gets the euclidean distance between every 
        point"""
        features = Features()

        for i in range(len(points)-1):
            currentPoint = points[i]
            nextPoint = points[i + 1]

            xdifference = nextPoint.get_x() - currentPoint.get_x()
            ydifference = nextPoint.get_y() - currentPoint.get_y()
            zdifference = nextPoint.get_z() - currentPoint.get_z()
            distance = (xdifference**2 + ydifference**2 + zdifference**2)**0.5

            features.add_feature_val(distance) 
        return features

    def __str__(self) -> str:
        """This is a feature for the distance between points"""
        return "PointsDistance"
