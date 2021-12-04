import unittest
from xlsxfilereader.Episode import Episode


class TestEpisodeMethods(unittest.TestCase):
    def test_episode_init(self):
        episode = Episode("WK",1,2,3)
        self.assertEquals(episode.type, "WK")
        self.assertEquals(episode.n, 1)
        self.assertEquals(episode.occ, 2)
        self.assertEquals(episode.duration, 3)

    def test_episode_str(self):
        episode = Episode("WK",1,2,3)
        self.assertEquals(str(episode),"Episode(WK,1.0,2.0,3.0)")

    def test_episode_eq(self):
        episode = Episode("WK",1,2,3)
        episode2 = Episode("WK",1,2,3)
        self.assertEquals(episode, episode2)
