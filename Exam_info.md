# Exam Information

last updated: 22/11/2016 — final

## Rules

### Can be used

  * Calculator
  * All written (printed) material
  * All electronic material brought on a pendrive (PDFs, slides, MS Excel files, python code, etc.)
    - Slides in PDF format are available [here](slides/)
  * Pre-approved programs available on the PCs (MS Excel, MS Word, Adobe Acrobat, Notepad, Calculator)
  * **No online resources**

### Grading

  * Multiple choice questions:
    - 2 or 3 points if correct
    - 0 if unanswered
    - -1 if incorrectly answered
  * Total points: 100+N, where N is the number of multiple choice questions
  * Grading
    - 0-39	F
    - 40-49	E
    - 50-59	D
    - 60-79	C
    - 80-89	B
    - 90+	A

## Topics

### Data Mining

book chapters 1–3, 5, 8, and everything from the lectures and practicums

  * Types of attributes (properties, transformations)
  * Types of data sets
  * Data quality problems
  * Data preprocessing
  * Proximity measures
    - Similarity vs. distance
    - Normalization (min-max)
    - Similarity/distance for single attributes (depending on attr. type)
    - Similarity/distance between data objects
        * Numerical attributes: Eucledian, Minkowski, Cosine
        * Binary attributes: Simple Matching Coefficient, Jaccard
  * Summary statistics
    - Frequency, mode, percentiles, mean, median, range, variance, std. deviation
    - Absolute Average Deviation, Median Absolute Deviation, Interquartile Range
  * Visualization
  * Supervised vs. unsupervised learning
  * Classification
    - Decision trees
        * Tree induction, how to split, impurity measures, stopping criteria
    - Rule-based classifiers
        * Rule sets and their properties, creating a rule-based classifier from a decision tree
    - Nearest neighbors
    - Naive Bayes
        * Conditional probabilities for different attribute types, smoothing
    - Main ideas behind Support Vector Machines and Ensemble Methods
    - Underfitting and overfitting
    - Evaluation
        * Confusion matrix
        * Evaluation measures (accuracy, precision, recall, F1, true/false positive/negative rate)
    - Multiclass classification
        * One-against-rest and one-against-one approaches
        * Micro- and macro-averaging
  * Clustering
    - Types of clusterings
    - K-means clustering (basic and bisecting)
    - Hierarchical agglomerative clustering
    - Clustering evaluation


### Information Retrieval

book chapters 1, 2, 4—9, and everything from the lectures and practicums

  * Text preprocessing (tokenization, stopword removal, stemming)
  * Term vectors, measuring the similarity of term vectors
  * Search engine architecture
  * Inverted index
    - With term frequency or with position information
  * Boolean retrieval
  * Vector space model
  * TFIDF term weighting
  * BM25 scoring
  * Language models
    - Different smoothing methods (Jelinek-Mercer, Dirichlet)
  * Fielded retrieval models
  * Anchor text
  * Pagerank
  * Evaluation
    - Precision, recall, (mean) average precision, (mean) reciprocal rank, NDCG
  * Entity retrieval
    - Knowledge bases, RDF, DBpedia
    - Fielded entity representations
  * Entity linking
