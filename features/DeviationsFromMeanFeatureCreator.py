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

    def get_mean(features:Features) -> float:
        """Gets the mean of all of the feature values"""
        sum = 0
        count = 0
        for featureVal in features:
            sum += featureVal
            count += 1
        return sum / count
    
    def get_std_dev(features:Features) -> float:
        """Gets the standard deviation of all the feature values"""
        sum = 0
        count =0
        mean = DeviationsFromMeanFeatureCreator.get_mean(features)
        for featureVal in features:
            sum += (featureVal - mean)**2
            count += 1
        return (sum/count)**0.5

    def get_features(self, points:Points) -> Features:
        """Gets all the Y values as features"""
        origFeatures = self._origFeatureCreator.get_features(points)
        features = Features()
        mean = DeviationsFromMeanFeatureCreator.get_mean(origFeatures)
        std_dev = DeviationsFromMeanFeatureCreator.get_std_dev(origFeatures)
        for featureVal in origFeatures:
            if not std_dev == 0:
                z = (featureVal - mean) / std_dev
            else:
                z = 0
            features.add_feature_val(z)

        return features

    def __str__(self) -> str:
        """This is a feature for std. deviation"""
        return "std_dev:" + str(self._origFeatureCreator)