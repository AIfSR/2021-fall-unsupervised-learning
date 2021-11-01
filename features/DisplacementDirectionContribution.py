from features.FeatureCreatorBase import FeatureCreatorBase
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from features.DeviationsFromMeanFeatureCreator import DeviationsFromMeanFeatureCreator

from features.Features import Features
from tckfilereader.Points import Points

class DisplacementDirectionContribution (FeatureCreatorBase):
    """Finds a vector between all points and determines the contribution of that 
    vector towards the center of the entire trajectory"""

    def get_features(self, points:Points) -> Features:
        """Gets the contributions to the center value as features"""
        xFeature = XFeatureCreator().get_features(points)
        yFeature = YFeatureCreator().get_features(points)
        zFeature = ZFeatureCreator().get_features(points)
        xMean = DeviationsFromMeanFeatureCreator.get_mean(xFeature)
        yMean = DeviationsFromMeanFeatureCreator.get_mean(yFeature)
        zMean = DeviationsFromMeanFeatureCreator.get_mean(zFeature)
        prevPoint = points[0]

        features = Features()
        for i in range(1, len(points)):
            currentPoint = points[i]
            directionX = currentPoint.get_x() - prevPoint.get_x()
            directionY = currentPoint.get_y() - prevPoint.get_y()
            directionZ = currentPoint.get_z() - prevPoint.get_z()

            displacementX = currentPoint.get_x() - xMean
            displacementY = currentPoint.get_y() - yMean
            displacementZ = currentPoint.get_z() - zMean
            displacementDistance = (displacementX**2 + displacementY**2 + displacementZ**2)**0.5
            
            unitDisplacementX = displacementX / displacementDistance
            unitDisplacementY = displacementY / displacementDistance
            unitDisplacementZ = displacementZ / displacementDistance

            contribution = directionX * unitDisplacementX + directionY*unitDisplacementY + directionZ * unitDisplacementZ
            features.add_feature_val(contribution)
            prevPoint = currentPoint

        return features

    def __str__(self) -> str:
        """This is a feature for contributions to mean"""
        return "Contributions"


