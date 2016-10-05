
# coding: utf-8

# # Term weighting and vector space retrieval
# 
# Score a toy-sized document collection against a query using the vector space model (i.e., TFIDF term weighting and cosine similarity).
# 
# This is exactly the same task that was given as a paper-based exercise earlier this week.

# In[1]:

import math
import operator


# Term-document matrix
# 
# | term | D1 | D2 | D3 | D4 | D5 |
# | -- |:--:|:--:|:--:|:--:|:--:|
# | beijing | | 1 | | | 1 |
# | dish | | 1 | | | 1 |
# | duck | 3 | 2 | 2 | | 1 |
# | rabbit | | | 1 | 1 | |
# | recipe | | | 1 | 1 | 1 |
# | roast | | | | | |

# In[2]:

td_matrix = {
    "beijing": [0, 1, 0, 0, 1],
    "dish": [0, 1, 0, 0, 1],
    "duck": [3, 2, 2, 0, 1],
    "rabbit": [0, 0, 1, 1, 0],
    "recipe": [0, 0, 1, 1, 1],
    "roast": [0, 0, 0, 0, 0]
}


# The vocabulary is a list of terms. We sort them here, but that's not necessary.
# 
# Use this list every time iterating through terms. 

# In[3]:

voc = list(td_matrix.keys())
voc.sort()


# The number of documents is set manually for simplicity

# In[4]:

NUM_DOCS = 5


# The query is given as a sequence of terms

# In[5]:

query = ["beijing", "duck", "recipe"]


# ## TFIDF term weighting
# 
# Use normalized frequencies for TF weight, i.e., $tf_{t,d}=\frac{f_{t,d}}{|d|}$, where $f_{t,d}$ is the number of occurrences of term $t$ in document $d$ and $|d|$ is the document length (=total number of terms).
# 
# Compute IDF values using the following formula: $idf_{t}=\log \frac{N}{n_t}$, where $N$ is the total number of document and $n_t$ is the number of documents that contain term $t$.  (Use base 10 for the logarithm to get the same values as for the paper-based exercise.)

# In[6]:

idf = []  # idf[i] holds the IDF weight for term voc[i]
for t in voc:    
    nt = sum([1 for x in td_matrix[t] if x >0]) # number of documents that contain t
    idf.append(math.log(NUM_DOCS / nt, 10) if nt > 0 else 0)


# In[7]:

idf


# ### Term weighting for documents
# 
# Takes term-document matrix as an argument.

# In[8]:

def tfidf_docs(tdm):
    tdm_tfidf = {}
    
    dlen = []  # dlen[i] stores the length of the i-th document
    for d in range(NUM_DOCS):
        l = 0
        for t in voc:
            l += td_matrix[t][d]
        #sum([x for t in voc for x in td_matrix[t][d]])
        dlen.append(l)
    
    # iterate through terms
    for i, t in enumerate(voc):
        td = tdm[t]  # vector of docs for the given term
        tdm_tfidf[t] = []
        for d, f in enumerate(td):
            # f is the frequency of term t for doc d
            # Compute TFIDF score for term t in doc d
            tf = f / dlen[d]
            tfidf = tf * idf[i]
            tdm_tfidf[t].append(round(tfidf, 3))  # round to 3 digits
    
    return tdm_tfidf


# Perform TFIDF-weighting for documents

# In[9]:

tdm_tfidf = tfidf_docs(td_matrix)


# In[10]:

tdm_tfidf


# ## TFIDF term weighting for the query
# 
# Takes query term vector as an argument

# In[11]:

def tfidf_q(tqv):
    tqv_tfidf = []
    for i, t in enumerate(voc):
        # tqv[i] holds the raw frequency for term t
        tf = tqv[i] / len(query)
        tfidf = tf * idf[i]
        tqv_tfidf.append(round(tfidf, 3))  # round to 3 digits
    return tqv_tfidf


# Create a term vector for the query and perform TFIDF weighting

# In[12]:

tqv = []
for t in voc:
    tqv.append(query.count(t) if t in query else 0)


# In[13]:

tqv_tfidf = tfidf_q(tqv)


# Print original and TFIDF-weighted query vectors

# In[14]:

print(tqv, "=>", tqv_tfidf)


# ## Scoring documents

# ### Cosine similarity between a document and a query vector
# 
# $cosine(\mathbf{d}, \mathbf{q})= \frac{\mathbf{d} \cdot \mathbf{q}}{||\mathbf{d}||~||\mathbf{q}||} =\frac{\sum_{t} w_{t,d}\cdot w_{t,q}}{\sqrt{\sum_{t} w_{t,d}^2 \sum_{t} w_{t,q}^2}}$

# In[15]:

def cosine(dv, qv):
    sumdq, sumd, sumq = 0, 0, 0
    # Iterate two lists parallel    
    for wtd, wtq in zip(dv, qv):
        sumdq += wtd * wtq
        sumd += wtd**2
        sumq += wtq**2
    return sumdq / math.sqrt(sumd * sumq)


# ### Scoring

# In[16]:

scores = {}

for d in range(NUM_DOCS):
    dtv = []
    for t in voc:
        dtv.append(tdm_tfidf[t][d])
    score = round(cosine(dtv, tqv_tfidf), 3)  # round to 3 digits
    scores[d] = score
    print("scoring D" + str(d), dtv, "vs. ", tqv_tfidf, score)    


# #### Output documents sorted by relevance score

# In[17]:

for d, score in sorted(scores.items(), key=operator.itemgetter(1), reverse=True):
    print("D" + str(d+1) + ": " + str(score))

