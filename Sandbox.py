import unittest
from xlsxfilereader.XLSXFileReader import XLSXFileReader
from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.Episode import Episode

path = "tests/xlsxfilereadertests/testfile2.xlsx"
xlsxFileReader = XLSXFileReader()
solutionEpisodes = Episodes()
solutionEpisodes.addEpisode(Episode("WK",1,2,3))
solutionEpisodes.addEpisode(Episode("SWS",7,5,6))
solutionEpisodes.addEpisode(Episode("PS",4,11,9))
testEpisodes = xlsxFileReader.get_episodes(path)
for i in testEpisodes:
    print(i)
for i in solutionEpisodes:
    print(i)
