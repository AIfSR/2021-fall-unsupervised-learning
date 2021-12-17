from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points
import math

class ThetaFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the theta coordinates of the vectors between points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the theta values as features"""
        features = Features()
        prevPoint = points[0]
        for i in range(1, len(points)):
            point = points[i]
            xDiff = point.get_x() - prevPoint.get_x()
            yDiff = point.get_y() - prevPoint.get_y()
            theta = math.atan2(yDiff, xDiff)
            features.add_feature_val(theta)
            prevPoint = point

        return features

    def __str__(self) -> str:
        """This is a feature for thetas"""
        return "Theta"