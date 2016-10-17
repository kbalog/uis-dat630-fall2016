
# coding: utf-8

# # Term-at-a-time scoring
# 
#   - Implement term-at-a-time scoring using vector space retrieval with TFIDF term weighting
#   - Use normalized frequencies for TF weight, i.e., $tf_{t,d}=\frac{f_{t,d}}{|d|}$, where $f_{t,d}$ is the number of occurrences of term $t$ in document $d$ and $|d|$ is the document length (=total number of terms).
#   - Compute IDF values using the following formula: $idf_{t}=\log \frac{N}{n_t}$, where $N$ is the total number of document and $n_t$ is the number of documents that contain term $t$.  (Use base 10 for the logarithm to get the same values as for the paper-based exercise.)
#   - Compare the results against the scores from the previous practicum (P5 / Task 1)

# In[59]:

from pprint import pprint
import math


# #### Term-document matrix

# In[60]:

td_matrix = {
    "beijing": [0, 1, 0, 0, 1],
    "dish": [0, 1, 0, 0, 1],
    "duck": [3, 2, 2, 0, 1],
    "rabbit": [0, 0, 1, 1, 0],
    "recipe": [0, 0, 1, 1, 1],
    "roast": [0, 0, 0, 0, 0]
}


# The number of documents is set manually for simplicity

# In[61]:

NUM_DOCS = 5


# #### Creating the corresponding inverted index
# 
# The postings hold (docID, freq) pairs. docID indices start from 0
# 
# doclen stores the document length

# In[62]:

inv_idx = {}
doclen = {}
for term, vec in td_matrix.items():
    inv_idx[term] = []
    for doc_id, freq in enumerate(vec):
        if freq > 0:
            inv_idx[term].append((doc_id, freq))
            doclen[doc_id] = doclen.get(doc_id, 0) + freq

pprint(inv_idx)


# #### This class provides access to the inverted index

# In[63]:

class InvIndex(object):
    def __init__(self, idx_contents):
        self.idx = idx_contents
    
    def terms(self):
        return self.idx.keys()
    
    def postings(self, term):
        return self.idx.get(term, [])


# #### Create index object

# In[64]:

idx = InvIndex(inv_idx)


# ### Term-at-a-time scoring
# 
# $Score(q,d) = \sum_{t \in q} w_{t,q} \cdot w_{t,d}$
# 
# where $w_{t,d}=\frac{tfidf_{t,d}}{\sqrt{\sum_{t} tfidf_{t,d}^2}}$ and $w_{t,q}=\frac{tfidf_{t,q}}{\sqrt{\sum_{t} tfidf_{t,q}^2}}$

# #### IDF calculation
# 
# $IDF(t) = \log \frac{N}{n_t}$
# 
# where $N$ is the total number of documents and $n_t$ is the number of documents that contain term t.
# Note that $n_t$ is the length of the posting list of the term in the inverted index.

# In[65]:

def idf(term):
    return math.log(NUM_DOCS / len(idx.postings(term))) if len(idx.postings(term)) > 0 else 0


# #### Pre-computing document normalizers
# 
# $\sqrt{\sum_{t} tfidf_{t,d}^2}$

# In[66]:

docnorm = {}
# summation part
for term in idx.terms():
    for (doc_id, freq) in idx.postings(term): 
        tf = freq / doclen[doc_id]
        tfidf = tf * idf(term)
        docnorm[doc_id] = docnorm.get(doc_id, 0) + tfidf**2

# sqrt part
for doc_id in docnorm.keys():
    docnorm[doc_id] = math.sqrt(docnorm[doc_id])


# #### Scoring

# In[67]:

def score_tt(query):
    scores = {}  # score accumulator
    
    # computing query normalizer
    # note that this could also be ignored as it does not affect the ranking
    qnorm = 0
    for term in set(query):
        tf = query.count(term) / len(query)
        tfidf = tf * idf(term)
        qnorm += tfidf**2
    qnorm = math.sqrt(qnorm)
    
    # term-at-a-time scoring
    for term in query:
        for (doc_id, freq) in idx.postings(term): 
            tf_td = freq / doclen[doc_id]
            tfidf_td = tf_td * idf(term)  # doc tfidf score
            tf_tq = 1 / len(query)
            tfidf_tq = tf_tq * idf(term)  # query tfidf score
            score_term = tfidf_tq * tfidf_td / (qnorm * docnorm[doc_id])
            scores[doc_id] = scores.get(doc_id, 0) + score_term
    return scores


# In[68]:

query = ["beijing", "duck", "recipe"]
scores = score_tt(query)


# In[69]:

for doc_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print("D #" + str(doc_id + 1), round(score, 3))

