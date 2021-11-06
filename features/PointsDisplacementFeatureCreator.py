

from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class PointsDisplacementFeatureCreator (FeatureCreatorBase):

    def get_features(self, points:Points) -> Features:
        """Creates a feature that gets the euclidean distance between every
        point"""
        features = Features()
        firstPoint = points[0]
        finalPoint = points[len(points)-1]
        xdifference = finalPoint.get_x() - firstPoint.get_x()
        ydifference = finalPoint.get_y() - firstPoint.get_y()
        zdifference = finalPoint.get_z() - firstPoint.get_z()
        displacement= (xdifference**2 + ydifference**2 + zdifference**2)**0.5
        features.add_feature_val(displacement)
        # if len(points) > 1:
        #     features.add_feature_val(displacement)
            # this line needs to be here so that there are an equal amount of
            # feature values as points passed in
        return features

    def __str__(self) -> str:
        """This is a feature for the distance between points"""
        return "PointsDisplacement"
