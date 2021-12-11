import unittest

from features.Features import Features
from plotting.singleepisodecomparetrajectories.SingleEpisode2DCompareTrajectories import SingleEpisode2DCompareTrajectories
from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes

class SingleEpisode2DCompareTrajectoriesTest (unittest.TestCase):

    def test_calculate_hist_height(self) -> None:
        """Tests calculating the height for each histogram"""

        solution = (1.0 - (SingleEpisode2DCompareTrajectories.BOTTOM * 2 + SingleEpisode2DCompareTrajectories.HEIGHT + 2 * SingleEpisode2DCompareTrajectories.SPACING)) / 2
        singleEpisodeCompareTrajectories = SingleEpisode2DCompareTrajectories()
        self.assertAlmostEquals(solution, singleEpisodeCompareTrajectories._calculate_hist_height(2))


