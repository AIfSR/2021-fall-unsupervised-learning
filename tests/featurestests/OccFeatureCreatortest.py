import unittest
from features.Features import Features
from features.episodesfeatures.OccFeatureCreator import OccFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
from tests.featurestests.EpisodesFeatureCreatorTestBase import EpisodesFeatureCreatorTestBase

class OccFeatureCreatorTest (EpisodesFeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the OccFeatureCreator to test"""
        return OccFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the Occ Feature Creator"""
        episodes = Episodes([
            Episode("WK",1,2,3),
            Episode("WK",5,6,7),
            Episode("WK",9,10,11),
        ])
        occFeatureCreator = OccFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(2)
        solutionFeatures.add_feature_val(6)
        solutionFeatures.add_feature_val(10)

        self.assertEquals(occFeatureCreator.get_features(episodes), solutionFeatures)

    def test_string(self):
        featureCreator = OccFeatureCreator()
        self.assertEquals(str(featureCreator), "Occ")
