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
	"train.csv" file will be used to make the tree model.
	"test.csv" file will be used to test the tree model.

	The output of the program is the accuracy percentage of the
	tree modelwith the test data to whether it has resulted
	in the same label as the test data.

Dataset used:
	Dataset 2: Red Wine Quality
		Classification

Usage:
	The tree will accept 
	
Library used:
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

