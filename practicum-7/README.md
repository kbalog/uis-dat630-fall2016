Practicum 7
===========

## The DBpedia Entity Search Challenge

The task is to generate a ranking of entities from the DBpedia knowledge base in response to a [set of queries](data/queries_test.txt).

  * Form groups of 2 or 3; each group gets a secret key.
  * The knowledge base has already been indexed using Elasticsearch.
  * You need to generate a ranking for the [test queries](data/queries_test.txt) and upload them [here](http://gustav1.ux.uis.no/dat630/index.php?action=submit)
  * A set of training queries and relevance judgments can be found under [data](data/).
  * Each team is allowed to submit a ranking every 5 minutes. Only the last submission counts (i.e., overwrites the previous one). Submissions close at 10:00.
  * The leaderboard can be found at http://gustav1.ux.uis.no/dat630/
    * The first team that gets on the leaderboard with a min MAP score of 0.05 gets 2 bonus points at the exam (all members).
    * The team with the highest overall score at 10:00 gets 5 bonus points at the exam (all members).


### Elasticsearch

  * The Elasticsearch service is running at http://http://gustav1.ux.uis.no:8889
  * The index is called `dbpedia_fsdm_bm25`
  * You need to figure out what fields the index contains.
    * Hint: you need to get the [mapping](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/indices-get-field-mapping.html) used for the given index.


### Data format

The data format is the same as in Assignment 3.

Queries contain a queryID followed by the query text.

For every query, the output file should contain two columns: queryID and docIDs.  The docIDs are space separated and need to be in ranked order (the one with the highest relevance score first).  You may return up to 100 docIDs for each query (the docID is in the `_id` field in Elasticsearch).

The file should contain a header and have the following format:

```
queryID,docIDs
INEX_LD-2009074,<dbpedia:PageRank> <dbpedia:Topic-Sensitive_PageRank> <dbpedia:Google_Penguin>  ...
QALD2_tr-63,<dbpedia:Gus_Lewis> <dbpedia:Batman_Forever> <dbpedia:The_Joker_(The_Dark_Knight)>  ...
...
```
