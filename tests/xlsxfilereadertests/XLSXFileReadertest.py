import unittest
from xlsxfilereader.XLSXFileReader import XLSXFileReader
from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.Episode import Episode

class XLSXFileReaderTest (unittest.TestCase):
    def test_get_episodes(self):
        """Tests getting episodes from a xlsx file"""
        path = "tests/xlsxfilereadertests/testfile2.xlsx"
        xlsxFileReader = XLSXFileReader()
        solutionEpisodes = Episodes()
        solutionEpisodes.addEpisode(Episode("WK",1,2,3))
        solutionEpisodes.addEpisode(Episode("PS",7,5,6))
        solutionEpisodes.addEpisode(Episode("SWS",4,11,9))
        testEpisodes = xlsxFileReader.get_episodes(path)
        self.assertEquals(testEpisodes, solutionEpisodes)

