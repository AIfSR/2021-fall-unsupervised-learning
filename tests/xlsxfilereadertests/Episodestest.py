import unittest
from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.Episode import Episode

class TestEpisodesMethods(unittest.TestCase):

    def test_episodes_init(self):
        episodesString = Episodes([])
        x = episodesString.episodesList
        self.assertEquals(x, [], "expected empty array")

    def test_episodes_append(self):
        episodesString1 = Episodes()
        episode1 = Episode("WK",1,2,3)
        episodesString1.addEpisode(episode1)
        self.assertEquals(episodesString1.episodesList[0], episode1)

    def test_episodes_str(self):
        episodesString2 = Episodes([Episode("WK",1,2,3)])
        self.assertEquals(str(episodesString2), "Episode(WK,1.0,2.0,3.0)")

    def test_episodes_iter(self):
        a_list=Episodes([])
        episode1 = Episode("WK",1,2,3)
        episode2 = Episode("PS",4,5,6)
        a_list.addEpisode(episode1)
        a_list.addEpisode(episode2)
        it1=iter(a_list)
        self.assertEquals(next(it1),episode1)
        self.assertEquals(next(it1),episode2)

    def test_episodes_eq(self):
        a_list=Episodes()
        b_list=Episodes()
        episode1 = Episode("WK",1,2,3)
        episode2 = Episode("WK",1,2,3)
        a_list.addEpisode(episode1)
        b_list.addEpisode(episode2)
        self.assertEquals(a_list,b_list)

    def test_inexing(self):
        """Tests indexing methods within Episodes"""
        a_list=Episodes()
        episode1 = Episode("WK",1,2,3)
        episode2 = Episode("WK",1,2,3)
        a_list.addEpisode(episode1)
        a_list.addEpisode(episode2)
        self.assertEquals(a_list[0], episode1)
        self.assertEquals(a_list[1], episode2)

    def test_length(self):
        a_list=Episodes()
        episode1 = Episode("WK",1,2,3)
        episode2 = Episode("WK",1,2,3)
        a_list.addEpisode(episode1)
        a_list.addEpisode(episode2)
        self.assertEquals(len(a_list), 2)

