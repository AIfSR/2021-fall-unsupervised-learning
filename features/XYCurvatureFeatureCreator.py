from features.FeatureCreatorBase import FeatureCreatorBase
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.Features import Features
from tckfilereader.Points import Points

class XYCurvatureFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that gets the XY curvature of the points as calculated 
    according to this website:
    https://math24.net/curvature-radius.html
    """

    def get_features(self, points:Points) -> Features:
        """Gets all the curvature values as features"""
        xVelocity = RateOfChangeFeatureCreator(XFeatureCreator()).get_features(points)
        yVelocity = RateOfChangeFeatureCreator(YFeatureCreator()).get_features(points)
        xAcceleration = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())).get_features(points)
        yAcceleration = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())).get_features(points)
        features = Features()
        for xVel, yVel, xAcc, yAcc in zip(xVelocity, yVelocity, xAcceleration, yAcceleration):
            if xVel == 0.0 and yVel == 0.0:
                curvature = 0.0
            else:
                curvature = abs(xVel * yAcc - yVel * xAcc) / (xVel**2 + yVel**2)**1.5
            features.add_feature_val(curvature)

        return features

    def __str__(self) -> str:
        """This is a feature for curvature"""
        return "Curvature"