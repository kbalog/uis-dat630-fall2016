# Assignment 3

## Recent updates

  - The final results are available [here](Final_results.md).


## Task

This assignment is about solving a document retrieval problem.
The task involves the following four main steps:

  1. Index the document collection using Elasticsearch.
    - See [this document](../Elasticsearch.md) for help on Elasticsearch.
    - Use two fields, title and content.
  2. Perform a baseline retrieval using the default retrieval model in Elasticsearch and evaluate its performance.
    - Search only in the content field.
    - Return the top 100 documents for each query and measure Mean Average Precision (MAP).
    - You should get a MAP score around 0.048 if you use TF/IDF and around 0.064 if you use BM25.
  3. Implement the Mixture of Language Models (MLM) approach with two fields (title and content).
    - For each query, obtain the top 200 documents using the default Elasticsearch model (using the "content" field only), then re-rank these documents by computing the MLM score for each (and then return the top 100).
    - Find the field weights, smoothing method, and smoothing parameter that yield the best performance.
    - You need to reach a **MAP score of minimum 0.07** in order to pass this assignment.
    - The best performing team (each team member) will get 5 bonus points at the final exam. There will be no live leaderboard for this assignment.
  4. Write a report.
    - Present a results table with Mean Average Precision scores for baseline Elasticsearch (TF/IDF or BM25) and you MLM models.
    - Explain how did you choose the LM field weights and smoothing configuration.
    - Make a plot showing which queries were improved and which were hurt when moving from the default Elasticsearch model to MLM.
    - The report should be max 2 (A4) pages long, written in English, and in pdf format.

You may use any programming language/environment of your choice, but you are required to submit the complete source code that produced your output.


## Data

### Document collection

The AQUAINT document collection consists of newswire text data in English, drawn from three sources: the Xinhua News Service (`xie`), the New York Times News Service (`nyt`), and the Associated Press Worldstream News Service (`apw`). It has been used in official benchmark evaluations conducted by National Institute of Standards and Technology (NIST).

The text data are separated into directories by source (`apw`, `nyt`, `xie`); within each source, data files are subdivided by year, and within each year, there is one file per date of collection. Each file contains a stream of SGML-tagged text, i.e., blocks of text bounded by `<DOC>` and `</DOC>` tags.  Create an index with *title* (inside `<HEADING>`) and *content* fields (inside `<TEXT>`) and use `<DOCNO>` as the document identifier (docID).

The collection is 1.1GB compressed and can be dowloaded from here: http://www.ux.uis.no/~balog/dat630/aquaint.zip

Upon successful indexing, the index should contain 1,033,461 documents. (Assuming your index is called "aquaint", you can check it at http://localhost:9200/aquaint/_stats.)

You are requested to delete the collection after this assignment.


### Queries

The [queries.txt](data/queries.txt) file contains 50 queries in total.  Each line starts with a 3-digit queryID, followed by the query string.  E.g.,

```
336 Black Bear Attacks
341 Airport Security
...
```


### Relevance judgments

The [qrels2.csv](data/qrels2.csv) file contains the relevance judgments for all queries. Each line contains a queryID and the set of docIDs. The queryID and docIDs are separated by a comma, the docIDs are separated by spaces. (Note that relevance is binary, so the order in which these documents are listed does not matter.)

The new qrels file (qrels2.csv) contains only 45 queries, i.e., for 5 queries there are no relevance assessments. Just ignore those queries that are not in qrels2.csv when computing the MAP scores.

```
queryID,docIDs
303,APW19980610.1778 APW19990525.0223 APW19990602.0039  ...
307,APW19980602.0026 APW19980603.0021 APW19980810.1038 ...
...
```


### Output file format

For every query in queries.txt, the output file should contain two columns: queryID and docIDs (i.e., the same format that is used in the qrels.csv file).  The docIDs are space separated and need to be in ranked order (the one with the highest relevance score first).  You may return up to 100 documents for each query.

The file should contain a header and have the following format:

```
queryID,docIDs
303,XIE19970211.0115 XIE20000522.0056 XIE19970513.0108 ...
307,XIE19990501.0067 XIE19961203.0196 XIE19970621.0161 ...
...
```


## Code

  - [indexer.py](code/indexer.py) parses and (bulk) indexes the contents of a single file
  - [background_lm.py](code/background_lm.py) computes background language model probabilities (for a given field)
  - [mlm_ranking.ipynb](code/mlm_ranking.ipynb) is the pseudo code for MLM scoring


## Hints and notes

#### BM25 scoring

The default retrieval model depends on your Elasticsearch version; for 2.x it is TF/IDF, for 5.x it is BM25.  

You can change the default to BM25 in 2.x by adding this line to your `config/elasticsearch.yml` file (under your elasticsearch folder):

```
index.similarity.default.type: BM25
```

You will need to restart Elasticsearch and rebuild the index.

#### MLM implementation

  - You need to compute the background language model on the entire collection. Using only the top-ranked documents is wrong, and solutions that do that won't be accepted. A class that computes the background LM probabilities is already [provided](code/background_lm.py).
  - Using Dirichlet smoothing should perform better than Jelinek-Mercer smoothing. When using Dirichlet smoothing, you can set the average field length as the value of the smoothing parameter for each field.
  - Use a single shard for the Elasticsearch index (otherwise the term statistics you get may be wrong); you need to set it before building the index.
  - You need to make sure that the same preprocessing is applied to queries that was used for indexing the documents.  Use `es.indices.analyze()` or the [Analyze API endpoint](https://www.elastic.co/guide/en/elasticsearch/reference/2.4/indices-analyze.html).
  - See the provided [skeleton code](code/mlm_ranking.ipynb).

#### Indexing

If you change the number of shards or the default similarity, you need to rebuild the index.  For that, you will first need to delete the old index.


## Submission

  * Each team must **sign up** before the deadline here: https://goo.gl/forms/KMddcPaJjJb0hQZ93
    - A team can be 2 or 3 people. Single-person teams are also possible (even though not recommended).
    - It is possible to form different teams for each assignment.
  * **Send your report, output file, and source code in email** to the student assistant Darío Garigliotti <dario.garigliotti@uis.no>
    - The subject of the email should be `[DAT630] {teamname} Assignment 3`
    - There should be two output files: `{teamname_bm25.out}` and `{teamname_mlm.out}`, and these should be zip-ed.
    - The code should be zip-ed and contain a short README file explaining instructions on how to run it. Running this code should produce the exact same output that you attached to the email.
    - The report should be max 2 pages (A4) and in pdf format.
  * The deadline for submitting all files is **2 Nov, 16:00**.
  * Late submissions will not be allowed!


## FAQ

  - **So kaggle is not used after all for this assignment?**
  That's correct. It was not possible to set up this task as a competition on the kaggle platform.
  - **Will there bonus points be awarded for the best performing team?** Yes. However, there won't be a live leaderboard. So you need to submit your best performing run and we'll make a ranking of all teams in the end.
  - **What resources can be used?**
  Everything can be used. It is OK to look at online tutorials and examples, and to re-use them, but you will need to be able to explain every line of code you submit.
  - **Any advice on which programming language to use?** We are using Python (v3.5) during the practical sessions in the course, so Python is a good choice (but it is merely and advice, not a requirement).
  - **Should each member of the team write a separate report?** No, there is a single report from the team.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.
