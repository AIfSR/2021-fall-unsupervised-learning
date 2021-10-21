
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class EWAFeatureCreator (FeatureCreatorBase):

    def __init__(self, featureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, points:Points) -> Features:
        origFeatures = self._featureCreator.get_features(points)
        features = Features()
        prevVal = 0
        beta = 0.9999
        count = 1
        for featureVal in origFeatures:
            val = (beta * prevVal + (1 - beta) * featureVal) #/ (1 - beta**count)
            features.add_feature_val(val)
            count += 1
            prevVal = val

        return features

    def __str__(self) -> str:
        return "Non0:" + str(self._featureCreator)
