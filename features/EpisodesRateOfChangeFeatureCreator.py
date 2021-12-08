

from features.EpisodesFeatureCreatorBase import EpisodesFeatureCreatorBase
from features.Features import Features
from features.NFeatureCreator import NFeatureCreator
from xlsxfilereader.Episodes import Episodes


class EpisodesRateOfChangeFeatureCreator (EpisodesFeatureCreatorBase):
    """Takes a feature and finds the rate of change over all of the values"""

    def __init__(self, featureCreator:EpisodesFeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, episodes: Episodes) -> Features:
        """Gets the rate of change of all the values in the feature created"""
        features = Features()

        timeFeature = NFeatureCreator().get_features(episodes)
        otherFeature = self._featureCreator.get_features(episodes)
        firstVal = True

        for val, time in zip(otherFeature, timeFeature):
            if firstVal:
                # features.add_feature_val(0.0)
                # # this line needs to be here so that there are an equal amount
                # # of feature values as points passed in
                firstVal = False
            else:
                valChange = val - prevVal
                tChange = 1
                features.add_feature_val(valChange / tChange)
            prevVal = val
            prevTime = time
        return features

    def __str__(self) -> str:
        """This is a feature for the Rate of change of another feature"""
        if not isinstance(self._featureCreator, EpisodesRateOfChangeFeatureCreator):
            return "RoC:" + str(self._featureCreator)
        
        featureString = str(self._featureCreator)
        stringWithoutRoc = featureString[3:]
        if stringWithoutRoc[0] == ":":
            return "RoC^2" + stringWithoutRoc
        
        for i in range(1, len(stringWithoutRoc)):
            if stringWithoutRoc[i] == ":":
                break
        number = stringWithoutRoc[1:i]
        return "RoC^" + str(int(number) + 1) + stringWithoutRoc[i:]
