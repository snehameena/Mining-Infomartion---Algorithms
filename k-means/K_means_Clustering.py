# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:10:04 2020

@author: vinuk
url --> https://www.kaggle.com/andyxie/k-means-clustering-implementation-in-python?select=Iris.csv

https://github.com/andrewxiechina/DataScience/blob/master/K-Means/cs229-notes7a%202.pdf
"""

# Import necessary libraries
from copy import deepcopy
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

def plot(data,centers,marker = '*',c = 'black'):
    # Plot the data and the centers generated as random
    plt.scatter(data[:,0], data[:,1], s=7, c='blue')
    plt.scatter(centers[:,0], centers[:,1], marker= marker, c= c, s=150)
    plt.show()
    
    
    
def read_dataset(data_path, x_label, y_label):
    #Read  Dataset from CSV file & select appropriate data & feature from Labels
    df = pd.read_csv(data_path, usecols = [x_label, y_label]) #load the dataset
    print(df)
    data = df.values[:, 0:2]
    return data

csv_file_path = 'Dataset_BankDetails.csv'
data_source_from_csv = True
k = 3 # Number of clusters
if data_source_from_csv:
    data = read_dataset(csv_file_path, 'ApplicantIncome', 'LoanAmount')
else:
    #Generate Random Data based on Cluster Size
    data, y = make_blobs(n_samples=1000, centers=k, cluster_std=0.5, random_state=1)
n = data.shape[0] # Length of training data
c = data.shape[1] # Length of features in the data
print('Cluster Size :'+str(k))
print('Training Data Size :'+str(n))
print('Feature Size :'+str(n))
# Generate random centers, here we use sigma and mean to ensure it represent the whole data
mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
centers = np.random.randn(k,c)*std + mean
#Plot Data with Random Centers
plot(data, centers, marker ='*')

centers_old = np.zeros(centers.shape) # Placeholder to store old centers
centers_new = deepcopy(centers) # Placeholder to store new centers
itr = 0
clusters = np.zeros(n)
distances = np.zeros((n,k)) #Placeholer to store euclidean distance from each poin to each cluster center
error = np.linalg.norm(centers_new - centers_old)
c = ['black']

# When, after an update, the estimate of that center stays the same, exit loop
while error !=0 and error > 0.05:
    itr+=1
    print(itr)
    centers_old = deepcopy(centers_new)
    
    # Measure the distance to every center
    for i in range(k):
        distances[:,i] = np.linalg.norm(data - centers_new[i], axis=1)
    # Assign all training data to closest center
    clusters = np.argmin(distances, axis = 1)
    
    # Calculate mean for every cluster and update the center
    for i in range(k):
        centers_new[i] = np.mean(data[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)
    print(error)
    if error != 0:
        # Plot the data and the new centers calculated
        plot(data, centers_new, c=c[itr%len(c)])

    


'''center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

# Generate random data and center it to the three centers
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3
print(data_3)

data = np.concatenate((data_1, data_2, data_3), axis = 0)

# Plot the data and the centers generated as random
plt.scatter(data[:,0], data[:,1], s=7, c='cyan')
plt.scatter(centers[:,0], centers[:,1], marker='*', c='r', s=150)
plt.show()'''


'''df = pd.read_csv("Iris.csv") #load the dataset
df.drop('Id',axis=1,inplace=True) # Se elimina la columna no requerida

# Change categorical data to number 0-2
df["Species"] = pd.Categorical(df["Species"])
df["Species"] = df["Species"].cat.codes
# Change dataframe to numpy matrix
data = df.values[:, 0:4]
category = df.values[:, 4]

# Number of clusters
k = 3
# Number of training data
n = data.shape[0]
# Number of features in the data
c = data.shape[1]

# Generate random centers, here we use sigma and mean to ensure it represent the whole data
mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
centers = np.random.randn(k,c)*std + mean

# Plot the data and the centers generated as random
colors=['orange', 'blue', 'green']
for i in range(n):
    plt.scatter(data[i, 0], data[i,1], s=7, color = colors[int(category[i])])
plt.scatter(centers[:,0], centers[:,1], marker='*', c='g', s=150)

centers_old = np.zeros(centers.shape) # to store old centers
centers_new = deepcopy(centers) # Store new centers

data.shape
clusters = np.zeros(n)
distances = np.zeros((n,k))

error = np.linalg.norm(centers_new - centers_old)

# When, after an update, the estimate of that center stays the same, exit loop
while error != 0:
    # Measure the distance to every center
    for i in range(k):
        distances[:,i] = np.linalg.norm(data - centers[i], axis=1)
    # Assign all training data to closest center
    clusters = np.argmin(distances, axis = 1)
    
    centers_old = deepcopy(centers_new)
    # Calculate mean for every cluster and update the center
    for i in range(k):
        centers_new[i] = np.mean(data[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)
centers_new    

# Plot the data and the centers generated as random
colors=['orange', 'blue', 'green']
for i in range(n):
    plt.scatter(data[i, 0], data[i,1], s=7, color = colors[int(category[i])])
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)'''