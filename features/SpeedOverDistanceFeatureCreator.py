from features.FeatureCreatorBase import FeatureCreatorBase
from features.XYSpeedFeatureCreator import XYSpeedFeatureCreator
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator
from features.Features import Features
from tckfilereader.Points import Points

class SpeedOverDistanceFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that where each value is the speed over the distance 
    traveled"""

    def get_features(self, points:Points) -> Features:
        """Gets all the Y values as features"""
        pointsDistance = PointsDistanceFeatureCreator().get_features(points)
        speeds = XYSpeedFeatureCreator().get_features(points)
        features = Features()
        for distance, speed in zip(pointsDistance, speeds):
            features.add_feature_val(speed / distance)

        return features

    def __str__(self) -> str:
        """This is a feature for SpeedOverDistance"""
        return "SpeedOverDistance"