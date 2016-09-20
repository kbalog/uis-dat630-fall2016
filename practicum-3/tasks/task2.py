
# coding: utf-8

# # Comparing different classifiers on the Iris dataset
# 
# Train different classifiers and compare their performance by filling out the following table.
# 
# | Method               | Accuracy | Error rate |
# | -------------------- | -------- | ---------- |
# | Decision tree        |          |            |
# | Nearest Neighbors    |          |            |
# | Naive Bayes          |          |            |
# | SVM (linear kernel)  |          |            |
# | SVM (polyn. kernel)  |          |            |
# | SVM (RBF kernel)     |          |            |
# | Random Forest        |          |            |
# 

# In[23]:

import csv
from collections import Counter
import numpy as np
import pprint
import math


# In[24]:

from sklearn.tree import DecisionTreeClassifier


# ### Loading data 

# In[25]:

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

# In[26]:

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
# 
# Note that we need the data in a different format. Each instance is a list of values (not a dict, as before).

# In[27]:

train_x, train_y, test_x, test_y = load_data("../data/iris.data")


# ### Train model

# In[28]:

clf = DecisionTreeClassifier()
clf.fit(train_x, train_y)


# ### Apply model

# In[29]:

predictions = clf.predict(test_x)


# ### Evaluate predictions

# In[30]:

evaluate(predictions, test_y)

