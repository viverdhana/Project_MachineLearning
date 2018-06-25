#!/usr/bin/python3
import numpy
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris=load_iris()

#list to store different sizes
l1=[]

#list to store accuracy score for knn algo
l2=[]

choice=1
while choice==1:
	s=float(input("Enter the test size"))
	#splitting
	train_iris, test_iris, train_target, test_target=train_test_split(iris.data,iris.target,test_size=s)
	l1.append(s)
	#calling knn classifier
	knclf=KNeighborsClassifier(n_neighbors=3)
	#data training
	trained_knclf=knclf.fit(train_iris,train_target)
	#predicting output
	output_knclf
