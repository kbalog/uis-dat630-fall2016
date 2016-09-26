Practicum 4
===========

See [this document](../Practicum.md) for general information about the practicums.

Learning objectives:

  - Implementing K-Means and Bisecting K-Means clustering algorithms
  - Implementing Hierarchical Agglomerative Clustering using different cluster proximities
  - Visualizing clusters (scatterplots and dendrograms)


## Task 1. Implementing K-Means clustering

  - A set of 2D data points are given (generated artificially)
  - Select the centroids initially randomly from the data points
  - Repeat until the cluster assignments change for less than 1% of the data points
  - Visualize the cluster assignments and centroids after each iteration


## Task 2. Implementing Bisecting K-Means clustering

  - Solve the previous task using the bisecting variant of K-Means
  - Measure the quality of the resulting clustering in terms of Sum of Squared Error (SSE)
    * How does it compare to the SSE of the 'true' clustering?


## Task 3. Implementing Hierarchical Agglomerative Clustering

  - Cluster the "Italian cities" dataset (from the lecture) using Hierarchical Agglomerative Clustering
  - Implement the Single link (MIN), Complete link (MAX), and Group average methods for comparing cluster proximities
  - Bonus: visualize the different clusterings using dendrograms
