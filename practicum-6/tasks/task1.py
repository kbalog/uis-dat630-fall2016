
# coding: utf-8

# # Term-at-a-time scoring
# 
#   - Implement term-at-a-time scoring using vector space retrieval with TFIDF term weighting
#   - Use normalized frequencies for TF weight, i.e., $tf_{t,d}=\frac{f_{t,d}}{|d|}$, where $f_{t,d}$ is the number of occurrences of term $t$ in document $d$ and $|d|$ is the document length (=total number of terms).
#   - Compute IDF values using the following formula: $idf_{t}=\log \frac{N}{n_t}$, where $N$ is the total number of document and $n_t$ is the number of documents that contain term $t$.  (Use base 10 for the logarithm to get the same values as for the paper-based exercise.)
#   - Compare the results against the scores from the previous practicum (P5 / Task 1)

# In[1]:

from pprint import pprint


# #### Term-document matrix

# In[2]:

td_matrix = {
    "beijing": [0, 1, 0, 0, 1],
    "dish": [0, 1, 0, 0, 1],
    "duck": [3, 2, 2, 0, 1],
    "rabbit": [0, 0, 1, 1, 0],
    "recipe": [0, 0, 1, 1, 1],
    "roast": [0, 0, 0, 0, 0]
}


# The number of documents is set manually for simplicity

# In[3]:

NUM_DOCS = 5


# #### Creating the corresponding inverted index
# 
# The postings hold (docID, freq) pairs. docID indices start from 0

# In[4]:

inv_idx = {}
for term, vec in td_matrix.items():
    inv_idx[term] = []
    for doc_id, freq in enumerate(vec):
        if freq > 0:
            inv_idx[term].append((doc_id, freq))

pprint(inv_idx)


# #### This class provides access to the inverted index

# In[5]:

class InvIndex(object):
    def __init__(self, idx_contents):
        self.idx = idx_contents
    
    def postings(self, term):
        return self.idx.get(term, [])


# ### Term-at-a-time scoring

# In[6]:

def score_tt(query, index):
    scores = {}  # score accumulator
    for term in query:
        for (doc_id, freq) in index.postings(term): 
            score_term = 0  # TODO
            scores[doc_id] = scores.get(doc_id, 0) + score_term
    return scores


# In[7]:

idx = InvIndex(inv_idx)
query = ["beijing", "duck", "recipe"]
scores = score_tt(query, idx)


# In[8]:

for doc_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print("D #" + str(doc_id), score)

