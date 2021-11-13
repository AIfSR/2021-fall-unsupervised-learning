
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class PointsAngleFeatureCreator (FeatureCreatorBase):

    def get_features(self, points:Points) -> Features:
        """Creates a feature that gets the euclidean angle between every
        point"""
        features = Features()

        for i in range(len(points)-2):
            currentPoint = points[i]
            nextPoint = points[i + 1]
            nextofnextPoint= points[i + 2]

            xdifference = nextPoint.get_x() - currentPoint.get_x()
            ydifference = nextPoint.get_y() - currentPoint.get_y()
            zdifference = nextPoint.get_z() - currentPoint.get_z()
            nextxdifference = nextofnextPoint.get_x() - nextPoint.get_x()
            nextydifference = nextofnextPoint.get_y() - nextPoint.get_y()
            nextzdifference = nextofnextPoint.get_z() - nextPoint.get_z()
            distance = (xdifference ** 2 + ydifference ** 2 + zdifference ** 2) ** 0.5
            nextdistance = (nextxdifference ** 2 + nextydifference ** 2 + nextzdifference ** 2) ** 0.5

            angle = (xdifference*nextxdifference + ydifference*nextydifference + zdifference*nextzdifference)/(distance*nextdistance)
            # angle in cosine

            features.add_feature_val(angle)
        return features

    def __str__(self) -> str:
        """This is a feature for the angle between points"""
        return "PointsAngle"