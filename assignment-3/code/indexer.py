"""
Index builder for AQUAINT collection.

@author: Krisztian Balog
"""
import re
import gzip
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from elasticsearch import helpers

INDEX_NAME = "aquaint"
DOC_TYPE = "doc"

ELASTIC_SETTINGS = {
    "number_of_shards": 1,
    "number_of_replicas": 0
}


def add_docs_bulk(es, docs):
    """Adds a set of documents to the index in a bulk.

    :param docs: dictionary {doc_id: doc}
    """
    actions = []
    for doc_id, doc in docs.items():
        action = {
            "_index": INDEX_NAME,
            "_type": DOC_TYPE,
            "_id": doc_id,
            "_source": doc
        }
        actions.append(action)

    if len(actions) > 0:
        helpers.bulk(es, actions)


def index(es, file_name):
    print("Processing", file_name)
    with gzip.open(file_name, "rt") as fin:
        is_body = False
        docs = {}
        doc_id, body = None, None
        for line in fin:
            line = line.strip()
            if line.startswith("<DOCNO>"):  # get doc id
                doc_id = re.sub("<DOCNO> | </DOCNO>", "", line)
            elif line.startswith("<BODY>"):  # start to parse body
                is_body = True
                body = []
            elif line.startswith("</BODY>"):  # finished reading body
                soup = BeautifulSoup("\n".join(body), "lxml")
                headline = soup.find("headline")
                text = soup.find("text")
                docs[doc_id] = {
                    "title": headline.text if headline is not None else "",  # use an empty string if no <HEADLINE> found
                    "content": text.text if text is not None else ""  # everything inside <TEXT> is indexed as content
                }
                # get ready for next document
                doc_id = None
                is_body = False
            elif is_body:  # accumulate body content
                body.append(line)

        # bulk index the collected documents
        print("Bulk indexing", len(docs), "documents")
        add_docs_bulk(es, docs)

if __name__ == "__main__":
    es = Elasticsearch()

    #es.indices.delete(index=INDEX_NAME)  # delete old index
    
    if not es.indices.exists(INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body={"settings": {"index": ELASTIC_SETTINGS}})

    index(es, "data/aquaint/nyt/2000/20000101_NYT.gz")