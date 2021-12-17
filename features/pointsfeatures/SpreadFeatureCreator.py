from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points


class SpreadFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that measures the distance each point is from the average"""

    def get_features(self, points: Points) -> Features:
        """Gets all the distances from the average of the x, y, and z values"""
        xSum = 0
        ySum = 0
        zSum = 0
        count = 0
        for point in points:
            xSum += point.get_x()
            ySum += point.get_y()
            zSum += point.get_z()
            count += 1
        xAvg = xSum / count
        yAvg = ySum / count
        zAvg = zSum / count
        features = Features()
        for point in points:
            distance = ((xAvg - point.get_x())**2 + (yAvg - point.get_y())**2 + (zAvg - point.get_z())**2)**0.5
            features.add_feature_val(distance)
        return features

    def __str__(self) -> str:
        """This is a feature for spread"""
        return "Spread"
