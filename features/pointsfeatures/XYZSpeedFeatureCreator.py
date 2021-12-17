from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.genericfeatures.ABSFeatureCreator import ABSFeatureCreator
from features.genericfeatures.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.pointsfeatures.TFeatureCreator import TFeatureCreator
from features.pointsfeatures.XFeatureCreator import XFeatureCreator
from features.pointsfeatures.YFeatureCreator import YFeatureCreator
from features.pointsfeatures.ZFeatureCreator import ZFeatureCreator
from tckfilereader.Points import Points

class XYZSpeedFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the speed of X, Y and Z of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the XYZ speed of all of the points"""
        xSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator(), TFeatureCreator())).get_features(points)
        ySpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator(), TFeatureCreator())).get_features(points)
        zSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator(), TFeatureCreator())).get_features(points)
        features = Features()
        for xSpeed, ySpeed, zSpeed in zip(xSpeedFeatures, ySpeedFeatures, zSpeedFeatures):
            totalSpeed = (xSpeed**2 + ySpeed**2 + zSpeed**2)**0.5
            features.add_feature_val(totalSpeed)

        return features

    def __str__(self) -> str:
        """This is a feature for XYZ Speed"""
        return "XYZSpeed"