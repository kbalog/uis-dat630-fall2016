"""Class for computing background language model probabilities for a given field.

Note that you can get the collection statistics by setting term_statistics=True when 
asking for the term vector of any document. However, if we are interested in the
collection statistics of term X, we can only get it from a document that contains term X.
Therefore, we first issue a search with term X as the query and get the first matching
document (since the query is a single term, we know that this document contains term X
for sure). We can then ask for the term vector of that document with term_statistics=True.

Note that statistics are computed per shard, not per index.
Therefore, make sure you use a single shard for Elasticsearch.

@author: Krisztian Balog
"""

from elasticsearch import Elasticsearch

INDEX_NAME = "aquaint"
DOC_TYPE = "doc"


class BackgroundLM(object):
    def __init__(self, es, field):
        self._es = es
        self._field = field

    def get_prob(self, term):
        """Returns the probability of the term given the field LM."""
        # first need to find a document that contains the term
        hits = self._es.search(index=INDEX_NAME, q=term, df=self._field, _source=False, size=1).get("hits", {}).get(
            "hits", {})
        doc_id = hits[0]["_id"] if len(hits) > 0 else None
        if doc_id is not None:
            # ask for global term statistics when requesting the term vector of that doc
            tv = self._es.termvectors(index=INDEX_NAME, doc_type=DOC_TYPE, id=doc_id, fields=self._field,
                                      term_statistics=True)["term_vectors"][self._field]
            ttf = tv["terms"].get(term, {}).get("ttf", 0)  # total term count in the collection (in that field)
            sum_ttf = tv["field_statistics"]["sum_ttf"]
            return ttf / sum_ttf

        return None


if __name__ == "__main__":
	es = Elasticsearch()
	bg_lm = BackgroundLM(es, "content")
	print(bg_lm.get_prob("ever"))
	print(bg_lm.get_prob("science"))