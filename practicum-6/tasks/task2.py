
# coding: utf-8

# # Document-at-a-time scoring
# 
#   - Implement document-at-a-time scoring using vector space retrieval with TFIDF term weighting
#   - Use the TF-IDF weighting schemes from the previous task

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


# ### Document-at-a-time scoring

# In[22]:

def score_dt(query, index):
    # get a list of documents that need to be scored
    # content[docID] = [freq_1, freq_2, ..., freq_n], 
    # where freq_i is the frequency of the ith query term
    content = {i: [] for i in range(NUM_DOCS)}
    for i, term in enumerate(query):
        # get freq from index for documents that contain the term
        for (doc_id, freq) in index.postings(term): 
            content[doc_id].append(freq)
        # add 0 freq for documents that don't contain the term
        for doc_id in range(NUM_DOCS):
            if len(content[doc_id]) < i + 1:
                content[doc_id].append(0)
    
    pprint(content)
    
    # score each document
    scores = {}  # score accumulator
    for doc_id, tvec in content.items():
        scores[doc_id] = 0
        for i in range(len(query)): 
            f_q = query[i]  # term frequency in query
            f_d = tvec[i]  # term frequency in the document
            scores[doc_id] += 0  # TODO  
    return scores


# In[23]:

idx = InvIndex(inv_idx)
query = ["beijing", "duck", "recipe"]
scores = score_dt(query, idx)


# In[ ]:

for doc_id, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print("D #" + str(doc_id), score)

