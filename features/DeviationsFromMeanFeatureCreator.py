from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class DeviationsFromMeanFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that takes the mean and standard devaition of the 
    original feature and calculates the devations away from the mean of all the 
    points"""
    def __init__(self, origFeatureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._origFeatureCreator = origFeatureCreator

    def _get_mean(self, points) -> float:
        """Gets the mean of all of the feature values"""
        sum = 0
        count = 0
        features = self._origFeatureCreator.get_features(points)
        for featureVal in features:
            sum += featureVal
            count += 1
        return sum / count
    
    def _get_std_dev(self, points) -> float:
        """Gets the standard deviation of all the feature values"""
        sum = 0
        count =0
        mean = self._get_mean(points)
        features = self._origFeatureCreator.get_features(points)
        for featureVal in features:
            sum += (featureVal - mean)**2
            count += 1
        return (sum/count)**0.5

    def get_features(self, points:Points) -> Features:
        """Gets all the Y values as features"""
        origFeatures = self._origFeatureCreator.get_features(points)
        features = Features()
        mean = self._get_mean(points)
        std_dev = self._get_std_dev(points)
        for featureVal in origFeatures:
            z = (featureVal - mean) / std_dev
            features.add_feature_val(z)

        return features

    def __str__(self) -> str:
        """This is a feature for std. deviation"""
        return "std_dev:" + str(self._origFeatureCreator)