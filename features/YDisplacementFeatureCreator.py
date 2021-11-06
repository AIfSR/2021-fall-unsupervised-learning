from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class YDisplacementFeatureCreator (FeatureCreatorBase):

    def get_features(self, points:Points) -> Features:
        """Creates a feature that gets the euclidean distance between every
        point"""
        features = Features()
        firstPoint = points[0]
        finalPoint = points[len(points)-1]
        displacement = finalPoint.get_y() - firstPoint.get_y()
        features.add_feature_val(displacement)
        return features

    def __str__(self) -> str:
        """This is a feature for the distance between points"""
        return "PointsDistance"
