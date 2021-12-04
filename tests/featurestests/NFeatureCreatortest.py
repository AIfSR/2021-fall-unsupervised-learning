import unittest
from features.Features import Features
from features.NFeatureCreator import NFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
from tests.featurestests.EpisodesFeatureCreatorTestBase import EpisodesFeatureCreatorTestBase

class NFeatureCreatorTest (EpisodesFeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the NFeatureCreator to test"""
        return NFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the N Feature Creator"""
        episodes = Episodes([
            Episode("WK",1,2,3),
            Episode("WK",5,6,7),
            Episode("WK",9,10,11),
        ])
        nFeatureCreator = NFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(5)
        solutionFeatures.add_feature_val(9)

        self.assertEquals(nFeatureCreator.get_features(episodes), solutionFeatures)

    def test_string(self):
        featureCreator = NFeatureCreator()
        self.assertEquals(str(featureCreator), "N")
