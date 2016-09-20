
# coding: utf-8

# # Comparing different classifiers on the Iris dataset
# 
# Train different classifiers and compare their performance by filling out the following table.
# 
# | Method                   | Accuracy | Error rate |
# | ------------------------ | -------- | ---------- |
# | Decision tree            |   0.94   |    0.06    |
# | Nearest Neighbors (k=3)  |   0.98   |    0.02    |
# | Naive Bayes (Gaussian)   |   0.94   |    0.06    |
# | SVM (linear kernel)      |   0.98   |    0.02    |
# | SVM (polyn. kernel)      |   0.98   |    0.02    |
# | SVM (RBF kernel)         |   0.96   |    0.04    |
# | Random Forest            |   0.94   |    0.06    |
# 

# In[1]:

import csv
from collections import Counter
import numpy as np
import pprint
import math


# In[2]:

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


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
                instance = [float(row[i]) for i in range(4)]  # first four values are attributes
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


# ### Load data
# 
# Note that we need the data in a different format. Each instance is a list of values (not a dict, as before).

# In[5]:

train_x, train_y, test_x, test_y = load_data("../data/iris.data")


# ## Comparing different classifiers

# ### Decision tree

# In[6]:

print("Decision tree")
clf = DecisionTreeClassifier()
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)


# ### Nearest Neighbors

# In[7]:

print("Nearest Neighbors")
k = 3
clf = KNeighborsClassifier(k)
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)


# ### Naive Bayes (Gaussian)

# In[8]:

print("Naive Bayes (Gaussian)")
clf = GaussianNB()
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)


# ### SVM (linear kernel)

# In[9]:

print("SVM (linear kernel)")
clf = SVC(kernel='linear')
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)


# ### SVM (polynomial kernel)

# In[10]:

print("SVM (polynomial kernel)")
clf = SVC(kernel='poly')
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)


# ### SVM (RBF kernel)

# In[11]:

print("SVM (RBF kernel)")
clf = SVC(kernel='rbf')
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)


# ### Random Forest

# In[12]:

trees = 10  # number of trees in the forest
max_features = 2  # maximum number of features in each tree
clf = RandomForestClassifier(n_estimators=trees, max_features=max_features)
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)

