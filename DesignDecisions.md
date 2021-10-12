# Design Decisions
The project is based on the original github repo [MLinPractice](https://github.com/lbechberger/MLinPractice) by Lucas Bechberger. As part of the ML in Practice module in winter term 2021/2022 of the course of studies Cognitive Science/Cognitive Computing at University of Osnabrueck, the project is expaned in various parts by [Hendrik Timm](https://github.com/sweedp) and [Jacqueline Naether](https://github.com/jackylinelein). In the following, the design decisions of the adjustments inside the project are presented and briefly explained to ensure the traceability of the decisions.

## Functionalities
In the following, all newly implemented classes and functions are described with all their functionalities. 
In addition to the explanation of the functionality, the design decisions and backgrounds are also discussed.

### Preprocessing
All design decisions and functionalities of the newly implemented classes and functions of the preprocessing step will be explained in the following.
#### Class Counter
The `counter.py` (inherits from the class `preprocesser.py`) was integrated as an extension in the preprocessing steps. 
This decision evolved from the idea that a possible feature could represent the total number of tweets a user made in the given period of time (data set limit).
After various attempts to implement it, a new generalized preprocessor class was implemented. 
Now the `counter.py` class can also be used more easily in the future for the other columns of the table. 
It counts the total number of occurrences of each element within the given input list. Therefore the function `list.count` is used. 
For columns in which the individual elements are again lists including different elements, it was decided that differently sorted list elements are regarded as identical. 
This results from the thought that, for example tweets are found in the same way via a hashtag, regardless of whether the hashtag was mentioned first or last. 
To ensure this, a new function `_sort_list_elements` was implemented. First it's checked whether the input list consists of further list elements. 
If this is the case, the function `_sort_list_elements` is called and all list elements within the input list are sorted, 
so that the count function treats each list element including the same elements as equal. 
The original pandas data frame and so the original input column is not changed. 
The total number of occurences is then written in a new column called `<input_columnname>_count` (default: `username_count`). 
For example, in addition to the default username, the number of occurrences of the same locations can also be counted.

### Feature Extraction
All features which where extracted additionally to the original project are described in the following.
#### Class TweetTotalCount
The `tweet_total_count.py` (inherits from the class `feature_extractor.py`) extracts the feature total counts of tweets made by a useer in the given data set.
The data is read from the given pandas data frame and written into a numpy array. 
There is no further processing of the data from the input list itself, but it is required to transform the data into a numpy array 
for further processing in the feature collector and the following steps behind. 
For reasons of time, it was decided not to write a unit test for this application, 
since the class TweetTotalCount is purely about the transformation of the data into a numpy array and no further processing of the data takes place.

### Dimensionality Reduction

### Classification

#### Classifier
- A new kind of classifier was implemented, using the dummy classifier class. It predicts on lable frequency in the training data.

#### Evaluation Metrics
Different evaluation metrics newly learned in the lecture were integrated into the project as an extra. These are:
- precision
- cohen's kappa
- recall
- f1 measure

## Unit Tests
In addition to the reason that the unit tests were taught in the lecture, unit tests are implemented in this project in order to ensure the functionality of the newly added classes and functions.
A new folder structure was set up for this. 
It was decided to collect the tests in a new folder `test` on the same level as the folders `code` and `data`.
Since many different classes and functions are already in the folder `code` and the associated subfolders, we are hereby creating a better overview.
In addition, the functionality can be strictly separated from the tests.
In the following, the implemented unit tests are described in a structured manner in the individual pipeline steps.

### Preprocessing
Inside the folder `code` a new folder `preprocessing` was created to collect all unit tests for the newly created preprocessors.
These ones are described in the following.

#### Counter Test
The unit test `counter_test.py` checks the functionality of the preprocessor `counter.py`.
This is helpful because with large data sets, such as the one used, a manual check for correctness of the function is no longer easily possible.
A set up function and four test cases are defined:
- `def setUp(self)`: A new instance of `Counter` is defined, as well as the `INPUT_COLUMN` and `OUTPUT_COLUMN`.
- `def test_input_columns(self)`: Checks wether the input column given to the instance matches the input column of the instance.
- `def test_output_columns(self)`: Checks wether the output column given to the instance matches the output column of the instance.
- `def test_counting_elements(self)`: Checks whether the counted total number of a single string element within the column was counted correctly.
- `def test_counting_list_elements(self)`: Checks whether the counted number of a list of string elements within the column was counted correctly.