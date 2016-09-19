
# coding: utf-8

# # Task 1A) Implement a Naive Bayes classifier
# 
#   - We use categorical attributes by discretizing each attribute into three equally-sized bins: low, medium, high.
#   - We need to apply smoothing to avoid zero probabilities.
#   - Additionally, we compute probabilities in the log space.

# In[1]:

import csv
from collections import Counter
import numpy as np
import pprint
import math

ATTRS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


# ## Naive Bayes classifier using categorical attributes

# In[2]:

class NB(object):
    def __init__(self):
        self.model = None
    
    def train(self, attributes, labels):
        self.model = {}
        ccounter = Counter(labels)
        numclasses = len(ccounter)
        for l, freq in ccounter.items():
            # class prior probabilities P(Y)
            self.model[l] = {'P(Y)': freq / len(labels)}
            # conditional probabilities P(X=x|Y=y)
            for a in ATTRS:
                for v in ["low", "medium", "high"]:
                    # count how many times attribute `a` has value `v` when the target class is `l`
                    cnt = sum(attributes[i][a] == v and labels[i] == l for i in range(len(attributes)))
                    # store is as key "a=v"
                    key = a + "=" + v
                    # apply Laplace smoothing
                    self.model[l][key] = (cnt + 1) / (freq + numclasses)
                                
        # pprint.pprint(self.model)
    
    def apply(self, attributes):
        if not self.model:
            raise Exception("Model has not been trained")
        # P(Y|X) \propto P(Y) * P(X_1|Y) * ... * P(X_n|Y)
        # in log space: 
        # log P(Y|X) \propto log P(Y) + log P(X_1|Y) + ... + log P(X_n|Y)
        maxp = float("-inf") 
        maxl = None
        for l, p in self.model.items():
            prob = math.log(p['P(Y)'])  # log P(Y)
            expl = "P(" + l + ")=" + str(prob)  # explanation string (only for debugging)
            for a in ATTRS:
                key = a + '=' + attributes[a]
                prob += math.log(p[key])  # + log P(X_i|Y)
                expl += " * P(" + key + "|" + l +")=" + str(prob)
            #print(expl)  # debug
            if prob > maxp:
                maxp = prob
                maxl = l
         
        return maxl


# ### Loading data 

# In[3]:

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
                instance = {ATTRS[i]: float(row[i]) for i in range(4)}  # first four values are attributes
                label = row[4]  # 5th value is the class label
                if i % 3 == 0:  # test instance
                    test_x.append(instance)
                    test_y.append(label)
                else:  # train instance
                    train_x.append(instance)
                    train_y.append(label)
                    
    return train_x, train_y, test_x, test_y


# ### Evaluating predictions

# In[4]:

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


# ### Discretization
# 
# We need to replace numerical values with labels 'low', 'medium', 'high' such that 1/3 of the values are assigned 'low', 1/3 of the values are assigned 'medium', and 1/3 of the values are assigned 'high'. 

# In[5]:

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

# ### Load data

# In[6]:

train_x, train_y, test_x, test_y = load_data("../data/iris.data")


# ### Discretize attribute values
# Importantly, we do it on the entire data set (training and testing), to ensure that values are assigned to the same bins in the train and in the test part. We then split back the data into train and test.

# In[7]:

x2 = discretize(train_x + test_x)
train_x2 = x2[:len(train_x)]
test_x2 = x2[-len(test_x):]


# ### Train model

# In[8]:

nb = NB()
nb.train(train_x2, train_y)


# ### Apply model

# In[9]:

predictions = []
for instance in test_x2:
    label = nb.apply(instance)
    predictions.append(label)


# ### Evaluate predictions

# In[10]:

evaluate(predictions, test_y)

