# Design Decisions
The project is based on the original github repo [MLinPractice](https://github.com/lbechberger/MLinPractice) by Lucas Bechberger. As part of the ML in Practice module in winter term 2021/2022 of the course of studies Cognitive Science/Cognitive Computing at University of Osnabrueck, the project is expaned in various parts by [Hendrik Timm](https://github.com/sweedp) and [Jacqueline Naether](https://github.com/jackylinelein). In the following, the design decisions of the adjustments inside the project are presented and briefly explained to ensure the traceability of the decisions.

## Preprocessing
The `counter.py` (inherits from the class `preprocesser.py`) was integrated as an extension in the preprocessing steps. This decision evolved from the idea that a possible feature could represent the total number of tweets a user made in the given period of time (data set limit).
After various attempts to implement it, a new generalized preprocessor class was implemented. Now the `Counter.py` class can also be used more easily in the future for the other columns of the table. 
It counts the total number of occurrences of each element within the given input list. It uses the function `list.count` to count the occurences. The total number of occurences is then written in a new column called `<input_columnname>_count` (default: `username_count`). For example, in addition to the default username, the number of occurrences of the same locations can also be counted.

## Feature Extraction

## Dimensionality Reduction

## Classification

### Classifier
- A new kind of classifier was implemented, using the dummy classifier class. It predicts on lable frequency in the training data.

### Evaluation Metrics
Different evaluation metrics newly learned in the lecture were integrated into the project as an extra. These are:
- precision
- cohen's kappa
- recall
- f1 measure

## Unit Tests


