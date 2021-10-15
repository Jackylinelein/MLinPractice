#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Train or evaluate a single classifier with its given set of hyperparameters.

Created on Wed Sep 29 14:23:48 2021

@author: lbechberger
"""

import argparse, pickle
from sklearn.dummy import DummyClassifier

from sklearn.metrics import accuracy_score, precision_score, cohen_kappa_score, recall_score, f1_score

from sklearn.metrics import accuracy_score, cohen_kappa_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline


# setting up CLI
parser = argparse.ArgumentParser(description = "Classifier")
parser.add_argument("input_file", help = "path to the input pickle file")
parser.add_argument("-s", '--seed', type = int, help = "seed for the random number generator", default = None)
parser.add_argument("-e", "--export_file", help = "export the trained classifier to the given location", default = None)
parser.add_argument("-i", "--import_file", help = "import a trained classifier from the given location", default = None)
parser.add_argument("-m", "--majority", action = "store_true", help = "majority class classifier")
parser.add_argument("-f", "--frequency", action = "store_true", help = "label frequency classifier")
parser.add_argument("--knn", type = int, help = "k nearest neighbor classifier with the specified value of k", default = None)
parser.add_argument("-gnb", "--gaussian_naive_bayes", type = float, help = "gaussian naive bayes classifier with specified value of var_smoothing", default = None)
parser.add_argument("-bnb", "--bernoulli_naive_bayes", type = float, help = "bernoulli naive bayes classifier with specified value of alpha", default = None)
parser.add_argument("-dt", "--decision_tree", type = int, help = "decision tree classifier with specifiled value of max_depth", default = None)
parser.add_argument("-a", "--accuracy", action = "store_true", help = "evaluate using accuracy")
parser.add_argument("-p", "--precision", action = "store_true", help = "evaluate using precision")
parser.add_argument("-k", "--kappa", action = "store_true", help = "evaluate using Cohen's kappa")
parser.add_argument("-r", "--recall", action = "store_true", help = "evaluate using recall")
parser.add_argument("-f1", "--f_measure", action = "store_true", help = "evaluate F1 score, also known as F-measure")
args = parser.parse_args()

# load data
with open(args.input_file, 'rb') as f_in:
    data = pickle.load(f_in)

if args.import_file is not None:
    # import a pre-trained classifier
    with open(args.import_file, 'rb') as f_in:
        classifier = pickle.load(f_in)

else:   # manually set up a classifier

    if args.majority:
        # majority vote classifier
        print("    majority vote classifier")
        classifier = DummyClassifier(strategy = "most_frequent", random_state = args.seed)

    elif args.frequency:
        # label frequency classifier
        print("    label frequency classifier")
        classifier = DummyClassifier(strategy = "stratified", random_state = args.seed)
        
    elif args.knn is not None:
        print("    {0} nearest neighbor classifier".format(args.knn))
        standardizer = StandardScaler()
        knn_classifier = KNeighborsClassifier(args.knn)
        classifier = make_pipeline(standardizer, knn_classifier)
    
    elif args.gaussian_naive_bayes is not None:
        print("    gaussian naive bayes classifier")
        standardizer = StandardScaler()
        gnb_classifier = GaussianNB(var_smoothing = args.gaussian_naive_bayes)
        classifier = make_pipeline(standardizer, gnb_classifier)
    
    elif args.bernoulli_naive_bayes is not None:
        print("    bernoulli naive bayes classifier")
        standardizer = StandardScaler()
        bnb_classifier = BernoulliNB(alpha = args.bernoulli_naive_bayes)
        classifier = make_pipeline(standardizer, bnb_classifier) 
    
    elif args.decision_tree is not None:
        print("    decision tree classifier")
        standardizer = StandardScaler()
        dt_classifier = DecisionTreeClassifier(max_depth = args.decision_tree)
        classifier = make_pipeline(standardizer, dt_classifier) 
    
    classifier.fit(data["features"], data["labels"].ravel())

# now classify the given data
prediction = classifier.predict(data["features"])

# collect all evaluation metrics
evaluation_metrics = []
if args.accuracy:
    evaluation_metrics.append(("accuracy", accuracy_score))

if args.precision:
    evaluation_metrics.append(("precision", precision_score))

if args.kappa:
    evaluation_metrics.append(("kappa", cohen_kappa_score))

if args.recall:
    evaluation_metrics.append(("recall", recall_score))

if args.f_measure:
    evaluation_metrics.append(("f_measure", f1_score))
# compute and print them
for metric_name, metric in evaluation_metrics:
    print("        {0}: {1}".format(metric_name, metric(data["labels"], prediction)))

# export the trained classifier if the user wants us to do so
if args.export_file is not None:
    with open(args.export_file, 'wb') as f_out:
        pickle.dump(classifier, f_out)
