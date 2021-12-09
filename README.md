# 2021-fall-unsupervised-learning

This code base was created to analyze the trajectories of nanodiamonds being tracked within macrophages. The points are read in from tck files, useful features are extracted from them, and then these features are reduced to single values that can be plotted to visually show the difference between trajectories. The data is read in by a TCKFileReader object which is located in the tckfilereader directory to generate a Points object. From there the Points object is passed to various feature creators which are all located in the features directory. These feature creators create Features objects which are the data structure that holds all of the values associated with the data constructed. From there each Features instance is passed to a FeatureToSingleValBase object which are all located in the featuretosingleval directory. These objects reduce the Features object to a single value that is representative of all of the feature values in order to plot that single value. From that point the resulting single value that is created is passed to an object that will plot that single value against all of the other trajectory’s single value representations. A list of all of these steps is detailed below:

1. A TCK file is passed to a TCKFileReader object to create a Points object
2. A Points object is passed to various FeatureCreatorBase objects to create various Features objects
3. A Features object is passed to a featurestosingleval object to reduce the those Features values down to one value to be plotted
4. The result of the featurestosingleval object is plotted against other Features objects that have been reduced down to a single value.
5. This process is repeated for all of the trajectories in order to plot each trajectory against one another.

A concrete example of these steps is detailed below:

1. The tck file name MyTrajectory.tck is passed to a tckfilereader object to create Points object called myPoints
myPoints is passed to an XFeatureCreator object which then creates a Features object that contains all of the X values from my trajectory. This Features object is called myXFeatures
2. myXFeatures is passed to an AverageOfFeature object to take the average of all of the X values. This is the single value that will be plotted.
3. The average that is taken of all of the X values is plotted.

The code corresponding with the preceding example is shown below.

from tckfilereader.TCKFileReader import TCKFileReader 
from features.XFeatureCreator import XFeatureCreator 
from featuretosingleval.AverageOfFeature import AverageOfFeature 
 
tckFileReader = TCKFileReader() 
myPoints = tckFileReader.get_points("MyTrajectory.tck") 
xFeatureCreator = XFeatureCreator() 
myXFeatures = xFeatureCreator.get_features(myPoints) 
averageOfFeature = AverageOfFeature() 
averageX = averageOfFeature.get_val(myXFeatures) 
#averageX is then plotted 

In practice the user only needs to create objects for the Points, the FeatureCreatorBase(s), the FeaturesToSingleValBase(s) and pass these objects into a plotting object and it will go through the process detailed above. The data structure called GraphParameters which is located in the plotting directory is intended to store each of the above mentioned objects for each graph intended to be created.
 
 
