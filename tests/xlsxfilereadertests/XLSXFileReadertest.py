import unittest
from xlsxfilereader.XLSXFileReader import XLSXFileReader
from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.Episode import Episode

class XLSXFileReaderTest (unittest.TestCase):

    def test_get_episodes(self):
        """Tests getting episodes from a xlsx file"""
        path = "tests/xlsxfilereadertests/testfile2.xlsx"
        xlsxFileReader = XLSXFileReader()
        solutionWKEpisodes = Episodes()
        solutionSWSEpisodes = Episodes()
        solutionPSEpisodes = Episodes()
        solutionWKEpisodes.addEpisode(Episode("WK",1,2,3))
        solutionSWSEpisodes.addEpisode(Episode("SWS",4,5,6))
        solutionPSEpisodes.addEpisode(Episode("PS",7,8,9))
        testEpisodes = xlsxFileReader.get_episodes(path)
        self.assertEquals(testEpisodes, (solutionWKEpisodes,solutionSWSEpisodes,solutionPSEpisodes))

