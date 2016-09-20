
# coding: utf-8

# # Plotting Gaussian distributions for the Iris dataset
# 
# Create a plot for each of the four attributes in the Iris dataset and display the Gaussian distribution for each of the three classes (i.e., three lines).

# In[2]:

#get_ipython().magic('matplotlib inline')


# In[3]:

import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

ATTRS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


# Loading data 

# In[4]:

def load_data(filename):
    instances = []
    labels = []
    with open(filename, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 5:
                instance = {ATTRS[i]: float(row[i]) for i in range(4)}  # first four values are attributes
                label = row[4]  # 5th value is the class label
                instances.append(instance)
                labels.append(label)
                    
    return instances, labels


# ## Main

# Load data

# In[5]:

instances, labels = load_data("../data/iris.data")


# Create a separate plot each attribute.
# On each plot there should be three lines, corresponding to the three classes.
# Add a legend so that it is clear which color corresponds to which class. 

# In[10]:

# Plot between -10 and 10 with .001 steps
x_axis = np.arange(-10, 10, 0.001)

for a in ATTRS:
    plt.title(a)
    # Statistics for the given attribute for each of the classes
    for l, _ in Counter(labels).items():
        vals = np.array([instances[i][a] for i in range(len(instances)) if labels[i] == l])
        mean = np.mean(vals)
        std = np.std(vals)
        plt.plot(x_axis, norm.pdf(x_axis, mean, std), label=l)
    plt.legend(loc="upper left")
    plt.show()


# In[ ]:



