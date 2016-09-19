
# coding: utf-8

# # Implement a Naive Bayes classifier

# In[14]:

import csv


# Complete the parts marked with #TODO

# In[15]:

class NB(object):
    def __init__(self):
        self.trained = False
    
    def train(self, attributes, labels):
        # TODO
        self.trained = True
    
    def apply(self, attributes):
        if not self.trained:
            raise Exception("Model has not been trained")
        label = "TODO"
        # TODO
        return label


# Loading data 

# In[16]:

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

# In[17]:

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


# ## Main logic

# Load data

# In[18]:

train_x, train_y, test_x, test_y = load_data("../data/iris.data")

