
# coding: utf-8

# # Plotting Gaussian distributions for the Iris dataset
# 
# Create a plot for each of the four attributes in the Iris dataset and display the Gaussian distribution for each of the three classes (i.e., three lines).

# In[1]:

get_ipython().magic('matplotlib inline')


# In[2]:

import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

ATTRS = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


# Loading data 

# In[3]:

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

# In[4]:

instances, labels = load_data("../data/iris.data")


# This is just an example of how to plot two distributions.
# You may reuse part of this code inside the loop below.

# In[5]:

# Plot between -10 and 10 with .001 steps
x_axis = np.arange(-10, 10, 0.001)
# mean and std dev. for the 1st distr
mean1 = 0  
std1 = 2
plt.plot(x_axis, norm.pdf(x_axis, mean1, std1))
# mean and std dev. for the 2nd distr
mean2 = 2  
std2 = 3
plt.plot(x_axis, norm.pdf(x_axis, mean2, std2))
plt.title("Give it a title")
plt.show()


# Create a separate plot each attribute.
# On each plot there should be three lines, corresponding to the three classes.
# Add a legend so that it is clear which color corresponds to which class. 

# In[6]:

for a in ATTRS:
    print(a)
    # Statistics for the given attribute for each of the classes
    for l, _ in Counter(labels).items():
        vals = [instances[i][a] for i in range(len(instances)) if labels[i] == l]
        print(l, vals)


# In[ ]:



