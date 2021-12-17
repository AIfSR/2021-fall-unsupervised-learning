from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.genericfeatures.ABSFeatureCreator import ABSFeatureCreator
from features.genericfeatures.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.pointsfeatures.TFeatureCreator import TFeatureCreator
from features.pointsfeatures.XFeatureCreator import XFeatureCreator
from features.pointsfeatures.YFeatureCreator import YFeatureCreator
from tckfilereader.Points import Points

class XYSpeedFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is the speed of X and Y of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the XY speed of all of the points"""
        xSpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator(), TFeatureCreator())).get_features(points)
        ySpeedFeatures = ABSFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator(), TFeatureCreator())).get_features(points)
        features = Features()
        for xSpeed, ySpeed in zip(xSpeedFeatures, ySpeedFeatures):
            totalSpeed = (xSpeed**2 + ySpeed**2)**0.5
            features.add_feature_val(totalSpeed)

        return features

    def __str__(self) -> str:
        """This is a feature for XY Speed"""
        return "XYSpeed"