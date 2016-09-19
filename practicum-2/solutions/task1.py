
# coding: utf-8

# # Implement a Naive Bayes classifier
# 
#   - a) Use categorical attributes by discretize each attribute into three equally-sized bins: low, medium, high.
#   - b) Use continuous attributes and assume a Gaussian (normal) distribution. Estimate the parameters of the distribution (mean and variance) from the training data (you'll have different parameters for each attribute)!

# In[176]:

import csv
from collections import Counter
import numpy as np
import pprint
import math

ATTRS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


# Complete the parts marked with #TODO

# In[177]:

class NB(object):
    def __init__(self):
        self.model = None
    
    def train(self, attributes, labels):
        self.model = {}
        numclasses = 3  # TODO this should be computed from the data
        for l, freq in Counter(labels).items():
            # class prior probabilities
            self.model[l] = {'P(y)': freq / len(labels)}
            # conditional probabilities P(X=x|Y=y)
            for a in ATTRS:
                for v in ["low", "medium", "high"]:
                    cnt = 0
                    for i in range(len(attributes)):
                        if attributes[i][a] == v and labels[i] == l:
                            cnt += 1
                    key = a + "=" + v
                    self.model[l][key] = (1 + cnt) / (numclasses + freq)
                                
        # pprint.pprint(self.model)
    
    def apply(self, attributes):
        if not self.model:
            raise Exception("Model has not been trained")
        # P(Y|X) \propto P(Y) * P(X_1|Y) * ... * P(X_n|Y)
        # in log space: 
        # log P(Y|X) \propto log P(Y) + log P(X_1|Y) + ... + log P(X_n|Y)
        maxp = -1000 
        maxl = None
        for l, p in self.model.items():
            prob = math.log(p['P(y)'])
            #s = "P(" + l + ")=" + str(prob)
            for a in ATTRS:
                key = a + '=' + attributes[a]
                prob += math.log(p[key])
                #s += " * P(" + key + "|" + l +")=" + str(prob)
            #print(s)  # debug
            if prob > maxp:
                maxp = prob
                maxl = l
        
        #print(maxl, maxp)
        
        return maxl


# Loading data 

# In[178]:

def load_data(filename):
    train_x = []
    train_y = []
    test_x = []
    test_y = []
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in csvreader:
            if len(row) == 5:
                i += 1
                instance = {
                    "sepal_length": float(row[0]),
                    "sepal_width": float(row[1]),
                    "petal_length": float(row[2]),
                    "petal_width": float(row[3]),
                }
                label = row[4]
                if i % 3 == 0:  # test instance
                    test_x.append(instance)
                    test_y.append(label)
                else:  # train instance
                    train_x.append(instance)
                    train_y.append(label)
                    
    return train_x, train_y, test_x, test_y


# Evaluating predictions

# In[179]:

def evaluate(predictions, true_labels):
    correct = 0
    incorrect = 0
    for i in range(len(predictions)):
        if predictions[i] == true_labels[i]:
            correct += 1
        else:
            incorrect += 1

    print("Accuracy:   ", correct / len(predictions))
    print("Error rate: ", incorrect / len(predictions))
    
    return 0


# **Discretization**
# 
# We need to replace numerical values with labels 'low', 'medium', 'high' such that 1/3 of the values are assigned 'low', 1/3 of the values are assigned 'medium', and 1/3 of the values are assigned 'high'. 

# In[180]:

def discretize(attributes):
    attrs2 = [{} for _ in range(len(attributes))]  # initialize list of empty dicts
    for a in ATTRS:
        # find thresholds
        values = np.array([x[a] for x in attributes])
        t1 = np.percentile(values, 100/3)  # 33.3th percentile
        t2 = np.percentile(values, 2*100/3)  # 66.6th percentile
        for i in range(len(attributes)):
            val = attributes[i][a]
            if val <= t1:
                val2 = "low" 
            elif val > t2:
                val2 = "high"
            else:
                val2 = "medium"
            attrs2[i][a] = val2
     
    return attrs2


# ## Main logic

# Load data

# In[181]:

train_x, train_y, test_x, test_y = load_data("../data/iris.data")


# In[182]:

### Using discretization


# In[183]:

nb = NB()


# Discretizatize attribute values

# In[184]:

x2 = discretize(train_x + test_x)
train_x2 = x2[:len(train_x)]
test_x2 = x2[-len(test_x):]


# Train model

# In[185]:

nb.train(train_x2, train_y)


# Apply model

# In[186]:

predictions = []
for instance in test_x2:
    label = nb.apply(instance)
    predictions.append(label)


# Evaluate predictions

# In[187]:

evaluate(predictions, test_y)

