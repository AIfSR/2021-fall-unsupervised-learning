import unittest
from abc import ABC, abstractmethod
from features.EpisodesFeatureCreatorBase import EpisodesFeatureCreatorBase
from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
import random

class EpisodesFeatureCreatorTestBase (unittest.TestCase):

    @abstractmethod
    def get_feature_creator(self) -> EpisodesFeatureCreatorBase:
        """Gets the feature creator being tested"""
        pass

    def test_length_of_feature(self):
        """Tests that the length of the features and length of points are the same"""
        episodes = Episodes()
        for i in range(random.randint(20,30)):
            episodes.addEpisode("WK",Episode(random.random()*10,random.random()*10,i))

        feature = self.get_feature_creator().get_features(episodes)
        self.assertEquals(len(feature), len(episodes))

