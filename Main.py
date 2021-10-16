from plotting.SimpleComparePlots import TwoDComparePlots
from features.XFeatureCreator import XFeatureCreator
from features.YFeatureCreator import YFeatureCreator
from features.ZFeatureCreator import ZFeatureCreator
from features.TFeatureCreator import TFeatureCreator
from features.RateOfChangeFeatureCreator import RateOfChangeFeatureCreator
from features.PointsDistanceFeatureCreator import PointsDistanceFeatureCreator

if __name__ == "__main__":
    plotFeatures = [
        (XFeatureCreator(), TFeatureCreator()),
        (YFeatureCreator(), TFeatureCreator()),
        (ZFeatureCreator(), TFeatureCreator()),
        (RateOfChangeFeatureCreator(XFeatureCreator()), TFeatureCreator()),
        (RateOfChangeFeatureCreator(YFeatureCreator()), TFeatureCreator()),
        (RateOfChangeFeatureCreator(ZFeatureCreator()), TFeatureCreator()),
        (RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(XFeatureCreator())), TFeatureCreator()),
        (RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(YFeatureCreator())), TFeatureCreator()),
        (RateOfChangeFeatureCreator(RateOfChangeFeatureCreator(ZFeatureCreator())), TFeatureCreator()),
        (PointsDistanceFeatureCreator(), TFeatureCreator())
        
    ]
    simpleComparePlots = TwoDComparePlots(plotFeatures)