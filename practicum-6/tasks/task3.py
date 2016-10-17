
# coding: utf-8

# # Retrieval evaluation, binary relevance
# 
#   - Compute retrieval evaluation metrics using binary relevance: P@5, P@10, Average Precision, and Reciprocal Rank
#   - Compute the metrics for each query individually, as well as the averages over the entire query set

# #### Rankings produced for each query
# 
# The key is the queryID, the value is a list of docIDs 

# In[1]:

rankings = {
    "q1": [1, 2, 4, 5, 3, 6, 9, 8, 10, 7],
    "q2": [1, 2, 4, 5, 3, 9, 8, 6, 10, 7],
    "q3": [1, 7, 4, 5, 3, 6, 9, 8, 10, 2]
}


# #### Ground truth
# 
# The key is the queryID, the value is a list of documents that are relevant for that query;  documents not listed here are irrelevant.

# In[3]:

gtruth = {
    "q1": [1, 3],
    "q2": [2, 4, 5, 6],
    "q3": [7]
}


# ## Computing evaluation metrics

# In[6]:

for qid, ranking in sorted(rankings.items()):
    gt = gtruth[qid]    
    print("Evaluating", qid, "ranking:", ranking, "ground truth:", gt)
    
    # TODO
    # - Average precision
    # - Precision@5
    # - Precision@10
    #  -Reciprocal rank


# In[ ]:



