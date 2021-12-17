import unittest
from features.Features import Features
from features.genericfeatures.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.episodesfeatures.OccFeatureCreator import OccFeatureCreator
from features.episodesfeatures.NFeatureCreator import NFeatureCreator

from xlsxfilereader.Episode import Episode
from xlsxfilereader.Episodes import Episodes
# from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RateOfChangeFeatureCreatorTest (unittest.TestCase):
    def get_feature_creator(self):
        """Gets the XFeatureCreator to test"""
        return RateOfChangeFeatureCreator(OccFeatureCreator(), NFeatureCreator())

    def test_get_features(self):
        """Tests getting features from the RateOfChangeFeatureCreator"""
        points = Episodes([
            Episode("SWS",1,2,4),
            Episode("SWS",2,6,8),
            Episode("SWS",3,10,12),
        ])
        rateOfChangeFeatureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        # solutionFeatures.add_feature_val(0)
        solutionFeatures.add_feature_val((6-2) / 1)
        solutionFeatures.add_feature_val((10-6) / 1)
        
        self.assertEquals(rateOfChangeFeatureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = RateOfChangeFeatureCreator(OccFeatureCreator(), NFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC:Occ")
        featureCreator = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(OccFeatureCreator(), NFeatureCreator()), NFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC^2:Occ")
        featureCreator = RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(OccFeatureCreator(), NFeatureCreator()), NFeatureCreator()), NFeatureCreator())
        self.assertEquals(str(featureCreator), "RoC^3:Occ")

        featureCreator = OccFeatureCreator()
        nFeatureCreator = NFeatureCreator()
        for i in range(200):
            featureCreator = RateOfChangeFeatureCreator(featureCreator, nFeatureCreator)

        self.assertEquals(str(featureCreator), "RoC^200:Occ")
