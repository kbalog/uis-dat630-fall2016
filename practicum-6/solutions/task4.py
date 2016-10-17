
# coding: utf-8

# # Retrieval evaluation, graded relevance
# 
#   - Compute retrieval evaluation metrics using graded relevance: NDCG@5 and NDCG@10
#   - Compute the metrics for each query individually, as well as the averages over the entire query set

# In[1]:

import math


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
# It takes a list of relevance levels (corresponding to the documents) and rank position p

# In[4]:

def dcg(rel, p):
    dcg = rel[0]
    for i in range(1, min(p, len(rel))): 
        dcg += rel[i] / math.log(i + 1, 2)  # rank position is indexed from 1..
    return dcg


# #### Evaluating all queries

# In[5]:

sum_ndcg5 = 0
sum_ndcg10 = 0

for qid, ranking in sorted(rankings.items()):
    gt = gtruth[qid]    
    print("Query", qid)
    
    gains = [] # holds corresponding relevance levels for the ranked docs
    for doc_id in ranking: 
        gain = gt.get(doc_id, 0)
        gains.append(gain)
    print("\tGains:", gains)
    
    # relevance levels of the idealized ranking
    gain_ideal = sorted([v for _, v in gt.items()], reverse=True)
    print("\tIdeal gains:", gain_ideal)
    
    ndcg5 = dcg(gains, 5) / dcg(gain_ideal, 5)
    ndcg10 = dcg(gains, 10) / dcg(gain_ideal, 10)
    sum_ndcg5 += ndcg5
    sum_ndcg10 += ndcg10
    
    print("\tNDCG@5:", round(ndcg5, 3), "\n\tNDCG@10:", round(ndcg10, 3))

print("Average")
print("\tNDCG@5:", round(sum_ndcg5 / len(rankings), 3), "\n\tNDCG@10:", round(sum_ndcg10 / len(rankings), 3))    

