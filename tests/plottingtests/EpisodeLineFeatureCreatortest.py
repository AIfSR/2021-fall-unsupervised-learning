import unittest

from plotting.singleepisodecomparetrajectories.LineFeatureCreator import LineFeatureCreator
from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes

class EpisodeLineFeatureCreatorTest (unittest.TestCase):

    def test_get_features(self) -> None:
        """Tests that the features created are all one number so that they are plotted along the same line"""

        lineFeatureCreator = LineFeatureCreator()
        episodes = Episodes()
        episodes.addEpisode(Episode("WK",2,3,4))
        episodes.addEpisode(Episode("WK",2,3,4))
        episodes.addEpisode(Episode("WK",2,3,4))
        episodes.addEpisode(Episode("WK",2,3,4))
        episodes.addEpisode(Episode("WK",2,3,4))
        episodes.addEpisode(Episode("WK",2,3,4))

        features = lineFeatureCreator.get_features(episodes)
        self.assertEquals(len(episodes), len(features))
        for val in features:
            self.assertAlmostEquals(0.0, val)

    def test_increment(self) -> None:
        """Tests incrementing the line that all of the features are plotted along within the line feature creator"""
        
        lineFeatureCreator = LineFeatureCreator()
        episodes1 = Episodes()
        episodes1.addEpisode(Episode("WK",2,3,4))
        episodes1.addEpisode(Episode("WK",2,3,4))
        episodes1.addEpisode(Episode("WK",2,3,4))
        episodes2 = Episodes()
        episodes2.addEpisode(Episode("WK",2,3,4))
        episodes2.addEpisode(Episode("WK",2,3,4))
        episodes2.addEpisode(Episode("WK",2,3,4))

        features1 = lineFeatureCreator.get_features(episodes1)
        lineFeatureCreator.increment()
        features2 = lineFeatureCreator.get_features(episodes2)
        self.assertEquals(len(episodes1), len(features1))
        for val in features1:
            self.assertAlmostEquals(0.0, val)

        self.assertEquals(len(episodes2), len(features2))
        for val in features2:
            self.assertAlmostEquals(1.0, val)

    def test_str(self) -> None:
        """Tests that the string representation of a line feature creator is nothing"""

        lineFeatureCreator = LineFeatureCreator()
        self.assertEquals(str(lineFeatureCreator), "")
