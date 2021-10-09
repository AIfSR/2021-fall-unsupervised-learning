import unittest
from features.Feature import Feature

class FeatureTest (unittest.TestCase):

    def test_add_feature(self):
        """Tests the add_feature_val method in Feature"""
        feature = Feature()
        solution = [1,2,3]
        feature.add_feature_val(solution[0])
        feature.add_feature_val(solution[1])
        feature.add_feature_val(solution[2])
        
        for val, solutionVal in zip(feature, solution):
            self.assertEquals(val, solutionVal)

    def test_equals(self):
        """Tests the equals operator for Feature instances"""
        feature1 = Feature()
        feature2 = Feature()
        feature3 = Feature()
        feature4 = Feature()

        feature1.add_feature_val(1)
        feature1.add_feature_val(2)
        
        feature2.add_feature_val(1)
        feature2.add_feature_val(2)
        
        feature3.add_feature_val(3)
        feature3.add_feature_val(2)
        
        feature4.add_feature_val(1)
        feature4.add_feature_val(2)
        feature4.add_feature_val(3)

        self.assertTrue(feature1 == feature2)
        self.assertFalse(feature1 == feature3)
        self.assertFalse(feature1 == feature4)

    def test_length(self):
        """Tests the len() operator on a Feature instance"""
        feature = Feature()
        self.assertEquals(len(feature), 0)
        feature.add_feature_val(1)
        feature.add_feature_val(2)

        self.assertEquals(len(feature), 2)