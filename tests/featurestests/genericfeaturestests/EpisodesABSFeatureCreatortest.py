import unittest
from features.Features import Features
from features.genericfeatures.ABSFeatureCreator import ABSFeatureCreator
from features.episodesfeatures.NFeatureCreator import NFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
import unittest

class ABSFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return ABSFeatureCreator(NFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the Y Feature Creator"""
        episodes = Episodes([
            Episode("SWS",2,3,4),
            Episode("SWS",6,7,8),
            Episode("SWS",10,11,12),
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(2)
        solutionFeatures.add_feature_val(6)
        solutionFeatures.add_feature_val(10)
        
        self.assertEquals(featureCreator.get_features(episodes), solutionFeatures)

    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "ABS:N")
