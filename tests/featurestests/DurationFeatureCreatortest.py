import unittest
from features.Features import Features
from features.episodesfeatures.DurationFeatureCreator import DurationFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
from tests.featurestests.EpisodesFeatureCreatorTestBase import EpisodesFeatureCreatorTestBase

class DurationFeatureCreatorTest (EpisodesFeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the DurationFeatureCreator to test"""
        return DurationFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the Duration Feature Creator"""
        episodes = Episodes([
            Episode("WK",1,2,3),
            Episode("WK",5,6,7),
            Episode("WK",9,10,11),
        ])
        durationFeatureCreator = DurationFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(3)
        solutionFeatures.add_feature_val(7)
        solutionFeatures.add_feature_val(11)

        self.assertEquals(durationFeatureCreator.get_features(episodes), solutionFeatures)

    def test_string(self):
        featureCreator = DurationFeatureCreator()
        self.assertEquals(str(featureCreator), "Duration")
