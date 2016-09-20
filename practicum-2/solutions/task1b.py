
# coding: utf-8

# # Task 1B) Implement a Naive Bayes classifier
# 
#   - We use continuous attributes and assume a Gaussian (normal) distribution.

# In[1]:

import csv
from collections import Counter
import numpy as np
import pprint
import math


# We use the scipy package (and specifically the [stats.norm module](http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.norm.html)) for computing the probability density function.

# In[2]:

from scipy.stats import norm


# In[3]:

ATTRS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


# ## Naive Bayes classifier using continuous attributes

# In[4]:

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
            # estimate mean and variance for each attribute and for each class
            for a in ATTRS:
                # collect values of attribute `a` when the target class is `l`
                # and make it a numpy array
                vals = np.array([attributes[i][a] for i in range(len(attributes)) if labels[i] == l])                                   
                self.model[l][a] = {'mean': np.mean(vals), 'var': np.var(vals)}
                                
        #pprint.pprint(self.model)  # print model
    
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
                pxy = normpdf(attributes[a], p[a]['mean'], p[a]['var'])
                prob += math.log(pxy)  # + log P(X_i|Y)
                expl += " * P(" + a + '=' + str(attributes[a]) + "|" + l +")=" + str(prob)
            #print(expl)  # debug
            if prob > maxp:
                maxp = prob
                maxl = l
         
        return maxl


# Calculating probability density function for Gaussian distribution with a given mean and variance

# In[5]:

def normpdf(x, mean, var):
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


# ### Loading data 

# In[6]:

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

# In[7]:

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


# ## Main logic

# ### Load data

# In[8]:

train_x, train_y, test_x, test_y = load_data("../data/iris.data")


# ### Train model

# In[9]:

nb = NB()
nb.train(train_x, train_y)


# ### Apply model

# In[10]:

predictions = []
for instance in test_x:
    label = nb.apply(instance)
    predictions.append(label)


# ### Evaluate predictions

# In[11]:

evaluate(predictions, test_y)

