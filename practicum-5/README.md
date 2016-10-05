Practicum 5
===========

See [this document](../Practicum.md) for general information about the practicums.

Learning objectives:

  - Ranking documents using the Vector Space Model
  - Building an inverted index

## Task 1. Term weighting and vector space retrieval

  - Score a toy-sized document collection against a query using the vector space model (i.e., TFIDF term weighting and cosine similarity).


## Task 2. Building an inverted index

  - You are given a sample (1000 documents) from the [The Reuters-21578 data collection](http://www.daviddlewis.com/resources/testcollections/reuters21578/) in `data/reuters21578-000.xml`
  - The code that parses the XML and extract a list of preprocessed terms (tokenized, lowercased, stopwords removed) is already given.
  - You are also given an InvIndex class that manages the posting lists operations.
  - Build an inverted index from the input collection with the term frequencies stored.
  - Save the inverted index to a text file. E.g., `termID docID1:freq1 docID2:freq2 ...`.
