Practicum 1
===========

Learning objectives:

  - Setting up the programming environment (Python 3.5)
  - Attribute transformations (normalization, binarization, discretization)
  - Proximity calculations
  - Computing summary statistics (mean, median, range, variance, etc.)
  - Visualization (histograms, scatter plots, box plots)


## Task 0: Setting up local environment

  - Install python 3.5 ([Anaconda distribution](https://www.continuum.io/downloads)) on your personal computer.
  - For the university PCs, you can use the [WinPython](http://winpython.github.io/) portable distribution.
  - For local development, [PyCharm](https://www.jetbrains.com/pycharm/) is an excellent IDE.  It is available for all platforms (Windows, Linux, Mac). You can get a [free student license](https://www.jetbrains.com/student/).


## Task 1: Normalizing values between 0 and 1

  - Generate a random value that is the sum of rolling two six-sided dice.
  - Create a vector with n random values.
  - Plot the distribution of the values on a histogram.
  - Normalize the values between 0 and 1 using Min-Max normalization.
  - Plot the distribution of the normalized values on a histogram.


## Task 2: Computing the similarity of binary vectors

  - Create a binary representation of the records that have nominal and ordinal attributes.
  - Implement the functions that compute the Simple Matching Coefficient and Jaccard Coefficient for a given pair of records.
  - Find the most similar pair of records according to each similarity measure.


## Task 3: Discretization

  - Create an ordinal attribute "file size" with the following 5 possible values {tiny, small, medium, large, huge}.
  - Implement both the equal width and equal frequency methods.
  - Display the discretized values on a plot.


## Task 4: Finding k-nearest neighbors using Eucledian distance

  - Generate n=100 random points in a two dimensional space. Let both the x and y attributes be int values between 1 and 100.
  - Display these points on a scatterplot.
  - Select one of these points randomly (i.e., pick a random index).
  - Find the k closest neighbors of the selected record (i.e., the k records that are most similar to it) using the Eucledian distance. The value of k is given (i.e., hard-coded).
  - Display the selected record and its k closest neighbors in a distinctive manner on the plot (e.g., using different colors).


## Task 5: Computing summary statistics on the Iris dataset

  - Load the Iris dataset (`data/iris.data`)
  - Answer the following questions:
    * What is the mean `sepal length` for Iris Setosa?
    * What is the median `petal length` for Iris Virginica?
    * What is the range of `sepal width` for Iris Versicolour?
    * Which class (Setosa/Versicolour/Virginica) shows the highest variance in `petal width`?
    * What is the 70% percentile for `sepal length` and `sepal width` (for all classes together)?
    * Compute Absolute Average Deviation (AAD), Median Absolute Deviation (MAD), and Interquartile Range (IQR) for `petal length` (for all classes together).


## Task 6: Computing summary statistics using numpy

  - Load the Iris dataset into a 4x150 numpy array.
  - Answer the questions from Task 5 (except the last one) using numpy.
  - See reference at the bottom of the document.


## Task 7: Visualizing Iris data

  - Create two scatter plots: sepal length vs. width and petal length vs. width. Use different color/symbols for the different classes (Setosa/Versicolour/Virginica).
  - Create box plots for comparing the four attributes (for all classes). I.e., 4 box plots, one for each attribute.
  - Create box plots for comparing one of the attributes (e.g., sepal length) across the three classes. I.e., 3 box plots, one for each class.


## References
  - Python tutorials
    * [Python course on codecademy](https://www.codecademy.com/tracks/python)
    * [Official Python tutorial](https://docs.python.org/2/tutorial/index.html)
    * [Tutorialspoint](http://www.tutorialspoint.com/python/index.htm)
  - [Matplotlib plotting framework](http://matplotlib.org/api/pyplot_api.html)
    * [How to make beautiful data visualizations in Python with matplotlib](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
  - [Numpy](http://www.python-course.eu/numpy.php)
    * [Numpy arrays](http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array)
    * [Numpy statistics](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)
