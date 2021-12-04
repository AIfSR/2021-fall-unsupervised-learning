import unittest
from features.Features import Features
from features.TypeFeatureCreator import TypeFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
from tests.featurestests.EpisodesFeatureCreatorTestBase import EpisodesFeatureCreatorTestBase

class TypeFeatureCreatorTest (EpisodesFeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the TypeFeatureCreator to test"""
        return TypeFeatureCreator()

    def test_get_features(self):
        """Tests getting features from the Type Feature Creator"""
        episodes = Episodes([
            Episode("WK",1,2,3),
            Episode("SWS",5,6,7),
            Episode("PS",9,10,11),
        ])
        typeFeatureCreator = TypeFeatureCreator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val("WK")
        solutionFeatures.add_feature_val("SWS")
        solutionFeatures.add_feature_val("PS")

        self.assertEquals(typeFeatureCreator.get_features(episodes), solutionFeatures)

    def test_string(self):
        featureCreator = TypeFeatureCreator()
        self.assertEquals(str(featureCreator), "Type")
