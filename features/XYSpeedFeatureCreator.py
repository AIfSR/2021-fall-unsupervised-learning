from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.ABSFeatureCreator import ABSFeatureCreator
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from tckfilereader.Points import Points

class XYSpeedFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the speed of X and Y of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the XY speed of all of the points"""
        xSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())).get_features(points)
        ySpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())).get_features(points)
        features = Features()
        for xSpeed, ySpeed in zip(xSpeedFeatures, ySpeedFeatures):
            print()
            print("xSpeed: " + str(xSpeed))
            print("ySpeed: " + str(ySpeed))
            print()
            totalSpeed = (xSpeed**2 + ySpeed**2)**0.5
            features.add_feature_val(totalSpeed)

        return features

    def __str__(self) -> str:
        """This is a feature for XY Speed"""
        return "XYSpeed"