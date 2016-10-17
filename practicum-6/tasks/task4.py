
# coding: utf-8

# # Retrieval evaluation, graded relevance
# 
#   - Compute retrieval evaluation metrics using graded relevance: NDCG@5 and NDCG@10
#   - Compute the metrics for each query individually, as well as the averages over the entire query set

# #### Rankings produced for each query
# 
# The key is the queryID, the value is a list of docIDs 

# In[2]:

rankings = {
    "q1": [2, 1, 3, 4, 5, 6, 10, 7, 9, 8],
    "q2": [1, 2, 9, 4, 5, 6, 7, 8, 3, 10],
    "q3": [1, 7, 4, 5, 3, 6, 9, 8, 10, 2]
}


# #### Ground truth
# 
# The key is the queryID, the value is a dictionary with (docID, level) pairs. Relevance level is on a 3-point scale: non-relevant (0), poor (1), good (2), excellent (3). Documents not listed here are non-relevant (level=0).

# In[3]:

gtruth = {
    "q1": {4: 3, 1: 2, 2: 1},
    "q2": {3: 3, 4: 3, 1: 2, 2: 1, 8: 1},
    "q3": {1: 3, 4: 3, 7: 2, 5: 2, 6: 1, 8: 1}
}


# ## Computing evaluation metrics
# 
# Discounted cumulative gain at rank p:
# $DCG_p = rel_1 + \sum_{i=2}^p\frac{rel_i}{\log_2 i}$
# 
# Normalized discounted cumulative gain at rank p:
# $NDCG_p = \frac{DCG_p}{IDCG}$
# 
# where IDCG is the DCG_p score of an idealized (perfect) ranking.

# #### Function that computes DCG_p
# 
# It takes a list of relevance levels (corresponding to the documents) and the rank cutoff p as input

# In[5]:

def dcg(rel, p):
    return 0


# In[12]:

for qid, ranking in sorted(rankings.items()):
    gt = gtruth[qid]    
    print("Evaluating", qid)
    
    gains = [] # holds corresponding relevance levels for the ranked docs
    for doc_id in ranking: 
        gain = gt.get(doc_id, 0)
        gains.append(gain)
    print(gains)
    
    # relevance levels of the idealized ranking
    gain_ideal = sorted([v for _, v in gt.items()], reverse=True)
    print(gain_ideal)
    
    # TODO
    # - compute NDCG@5
    # - compute NDCG@10


# In[ ]:



