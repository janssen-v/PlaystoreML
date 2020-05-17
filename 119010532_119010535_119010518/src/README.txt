! ! ! README ! ! !

How to use Team Project CSC 1001 program.


Name: 
	main.py

Description: 
	The project is a machine learning program to handle 
	csv file with a certain number of features and a label.

	The program will take two inputs from user. 
	The two inputs are: 
		Train data ("train.csv")
		Test data("test.csv")
	"train.csv" file will be used to build the tree model.
	"test.csv" file will be used to test the tree model.

	The output of the program is the accuracy percentage of the
	tree modelwith the test data to whether it has resulted
	in the same label as the test data.

Dataset used:
	Dataset 2: Red Wine Quality
		Classification

Datasets available;
	train.csv
	train25.csv
	train50.csv
	test.csv

Usage:
	The tree will accept csv files with the label on the 
	furthest right of the table. And the element in this case
	are all numeric. 

How to use:
	To use the program, user just need to run the python 
	program in their terminal.
	It will take a while to build the tree model.
	Once the tree model is built, the test data will be inputed
	to measure the accuracy of the model. 

Libraries used:
	csv
	os
	Path

Function defined: 
	class_counts
	is_numeric
	partition
	gini
	info_gain
	build_tree
	classify

Class defined:
	Question
	Node
	Leaf

