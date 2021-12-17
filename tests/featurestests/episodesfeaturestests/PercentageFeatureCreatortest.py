import unittest
from features.Features import Features
from features.episodesfeatures.PercentageFeatureCreator import PercentageFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes

class PercentageFeatureCreatorTest (unittest.TestCase):

    def get_feature_creator(self):
        """Gets the OccFeatureCreator to test"""
        return PercentageFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the Occ Feature Creator"""
        episodes = Episodes([
            Episode("SWS",1,0,1),
            Episode("WK",3,1,1),
            Episode("PS",2,2,1),
            Episode("SWS",4,3,1),
        ])
        percentageFeatureCreator = PercentageFeatureCreator("PS")

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(0.25)

        self.assertEquals(percentageFeatureCreator.get_features(episodes), solutionFeatures)

    def test_string(self):
        featureCreator = PercentageFeatureCreator("SWS")
        self.assertEquals(str(featureCreator), "Percentage of SWS")
