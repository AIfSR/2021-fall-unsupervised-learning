from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class YDistanceFeatureCreator (FeatureCreatorBase):

    def get_features(self, points:Points) -> Features:
        """Creates a feature that gets the euclidean distance between every
        point"""
        features = Features()

        for i in range(len(points)-1):
            currentPoint = points[i]
            nextPoint = points[i + 1]
            distance = abs(nextPoint.get_y() - currentPoint.get_y())
            features.add_feature_val(distance)
        return features

    def __str__(self) -> str:
        """This is a feature for the distance between points"""
        return "PointsDistance"
