from features.Features import Features
from features.genericfeatures.RaiseToPowerFeatureCreator import RaiseToPowerFeatureCreator
from features.pointsfeatures.XFeatureCreator import XFeatureCreator

from tckfilereader.Point import Point
from tckfilereader.Points import Points
from tests.featurestests.FeatureCreatorTestBase import FeatureCreatorTestBase

class RaiseToPowerFeatureCreatorTest (FeatureCreatorTestBase):

    def get_feature_creator(self):
        """Gets the RaiseToPowerFeatureCreator to test"""
        return RaiseToPowerFeatureCreator(XFeatureCreator(), 2)

    def test_get_features(self):
        """Tests getting features from the RaiseToPowerFeatureCreator Feature Creator"""
        points = Points([
            Point(1,2,3,4),
            Point(2,6,7,8),
            Point(3,10,11,12),
            Point(4,10,11,12),
            Point(5,10,11,12),
        ])
        featureCreator = self.get_feature_creator()

        solutionFeatures = Features()
        solutionFeatures.add_feature_val(1)
        solutionFeatures.add_feature_val(4)
        solutionFeatures.add_feature_val(9)
        solutionFeatures.add_feature_val(16)
        solutionFeatures.add_feature_val(25)
        
        self.assertEquals(featureCreator.get_features(points), solutionFeatures)
    
    def test_string(self):
        featureCreator = self.get_feature_creator()
        self.assertEquals(str(featureCreator), "Power: 2 of X")