#!/bin/bash

# create directory if not yet existing
mkdir -p data/classification/

# run feature extraction on training set (may need to fit extractors)
echo "  training set"

# Classifier Majority
python -m code.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --majority -s 42 --accuracy --kappa --recall --f_measure 
# Classifier Frequency
python -m code.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --frequency -s 42 --accuracy --kappa --recall --f_measure 
# Classifier KNN
python -m code.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 5 -s 42 --accuracy --kappa --recall --f_measure 
# Classifier Gaussian Naive Bayes
python -m code.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --gaussian_naive_bayes 0.000000008 -s 42 --accuracy --kappa --recall --f_measure 
# Classifier Bernoulli Naive Bayes
python -m code.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --bernoulli_naive_bayes 1.0 -s 42 --accuracy --kappa --recall --f_measure 
# Classifier Decion Tree
python -m code.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --decision_tree 5 -s 42 --accuracy --kappa --recall --f_measure 

# run feature extraction on validation set (with pre-fit extractors)
echo "  validation set"
python -m code.classification.run_classifier data/dimensionality_reduction/validation.pickle -i data/classification/classifier.pickle --accuracy --kappa

# don't touch the test set, yet, because that would ruin the final generalization experiment!
