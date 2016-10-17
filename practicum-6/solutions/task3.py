
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

# In[2]:

gtruth = {
    "q1": [1, 3],
    "q2": [2, 4, 5, 6],
    "q3": [7]
}


# ## Computing evaluation metrics

# In[3]:

sum_p5, sum_p10, sum_ap, sum_rr = 0, 0, 0, 0

for qid, ranking in sorted(rankings.items()):
    gt = gtruth[qid]    
    print("Evaluating", qid, "\n\tranking:", ranking, "\n\tground truth:", gt)
    
    p5, p10, ap, rr, num_rel = 0, 0, 0, 0, 0
    
    for i, doc_id in enumerate(ranking):
        if doc_id in gt:  # doc is relevant
            num_rel += 1  
            pi = num_rel / (i + 1)  # P@i
            ap += pi  # AP
            
            if i < 5:  # P@5
                p5 += 1
            if i < 10:  # P@10
                p10 += 1
            if rr == 0:  # Reciprocal rank
                rr = 1 / (i + 1)
    
    p5 /= 5
    p10 /= 10
    ap /= len(gt)  # divide by the number of relevant documents
    print("\tP@5:", round(p5, 3), "\n\tP@10:", round(p10, 3), "\n\tAP:", round(ap, 3), "\n\tRR:", round(rr, 3))
    
    
    sum_p5 += p5
    sum_p10 += p10
    sum_ap += ap
    sum_rr += rr

print("Average")
print("\tP@5:", round(sum_p5 / len(rankings), 3), "\n\tP@10:", round(sum_p10 / len(rankings), 3), 
      "\n\tMAP:", round(sum_ap / len(rankings), 3), "\n\tMRR:", round(sum_rr / len(rankings), 3))

