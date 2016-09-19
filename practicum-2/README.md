Practicum 2
===========

See [this document](../../Practicum.md) for general information about the practicums.

Learning objectives:

  - Naive Bayes classifier


## Task 1: Implement a Naive Bayes classifier

  - Load the Iris dataset and divide it into to 2/3 training and 1/3 test sets.  
  - Implement a Naive Bayes classifier
    * a) Use categorical attributes by discretize each attribute into three equally-sized bins: low, medium, high.
    * b) Use continuous attributes and assume a Gaussian (normal) distribution. Estimate the parameters of the distribution (mean and variance) from the training data (you'll have different parameters for each attribute)!
  - Compare the performance of the two solutions in terms of accuracy and error rate. Fill in the results in the following table:

| Arrribute handling | Accuracy | Error rate |
| ------------------ | -------- | ---------- |
| Discretization     |          |            |
| Gaussian distr.    |          |            |


## References
  - [Numpy](http://www.python-course.eu/numpy.php)
    * [Numpy arrays](http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array)
    * [Numpy statistics](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)
