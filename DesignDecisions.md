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

#### Data Analysis
The `data_analysis.py` can plot extracted features in order to have an impression if the feature has some valid information on how a viral tweet can be classified. For instance, for
the number of hashtags in a tweet it seems to be better if the tweet has more than 5 hashtags. Three different graphs can be plotted and saved. 
1. The percentage of viral tweets within a certain feature. So how many tweets are viral if there are 5 hashtags in it.
2. The percentage or relative frequency of tweets posted within a certain feature. So here you can see the percentage of how many tweets were viral (/not viral/overall) w.r.t. all feature values. So for instance, 0.1 of all tweets have 5 hashtags
3. The absolute number of tweets posted within a certain feature. Look at 2). For example 30.000 tweets have 5 hashtags, 20.000 tweets have 6 hashtags and so on.

### Feature Extraction

All features which where extracted additionally to the original project are described in the following.
#### Class TweetTotalCount
The `tweet_total_count.py` (inherits from the class `feature_extractor.py`) extracts the feature total counts of tweets made by a useer in the given data set.
The data is read from the given pandas data frame and written into a numpy array. 
There is no further processing of the data from the input list itself, but it is required to transform the data into a numpy array 
for further processing in the feature collector and the following steps behind. 
For reasons of time, it was decided not to write a unit test for this application, 
since the class TweetTotalCount is purely about the transformation of the data into a numpy array and no further processing of the data takes place.

#### Class #hashtags 
The first feature is the number of hashtags for each tweet. The idea is that maybe there is a golden number of hashtags which makes the tweet more likeable/viral. For instance, if there is 
no hashtag, it might just not reach a lot of people and hence it will probably not be viral. Therefore, in `hashtags.py` the number of hashtags are counted and stored.
Since the hashtags are stored as a single string like '"["These", "are", hashtags"]"' we needed some workaround to count the number of hashtags. We decided to
just count the "," in the whole string and look if the length of the string is > 2, because then it does not only contain "[]" but some hashtag in it.
For instance:
"[]" - length is not greater than 2 -> 0 hashtags
"["coolhashtag"]" - length is greater than 2 -> +1 hashtag
"["cool", "hashtag"]" -> length is greater than 2-> +1 hashtag; one time "," -> 2 hashtags in total

#### date
This feature looks when a tweet was posted w.r.t. the year, month, day and which weekday (monday-sunday). Here we just read out the overall date which is provided as year-month-day in the format "2012-05-21"
Extracting this feature is quite easy as you only slice the format into year, month or day and for weekdays we use some package where you can read out the day by providing the whole date.

#### Class WantedStr
The `wanted_str.py` (inherits from the class `feature_extractor.py`) extracts wether the given string is included inside the tweet. 
It was decided not to make a distinction between upper and lower case, as the statement whether a tweet goes viral is probably not very meaningful. 
It is more important whether the transferred word is actually present or not. When calling the function there is the possibility to give the wanted string, 
otherwise an empty string will be taken as default (default = ""). This will result in an all false array.

### Dimensionality Reduction

### Classification
The implementation of the classifier is done directly in `run_classifier.py`. 
For this purpose, new parser arguments are added and some newly learned classifiers are implemented with the help of the `sklearn` libraries.
#### Naive Bayes
It was decided to implement two different types of Naive Bayes Classifier (`sklearn.naive_bayes`). 
On the one hand the simplest type, the Gaussian Naive Bayes Classifier (`GaussianNB`) and on the other hand the Bernoulli Naive Bayes Classifier (`BernoulliNB`).
The Gaussian Naive Bayes classifier can be specified with the given value of var_smoothing (portion of the largest variance, default: None). 
For classification it uses the simple gaussian algorithm, thats why it assumed that the likelihood of the features is gaussian.  
Moreover, the Bernoulli Naive Bayes classifier can be specified with a given value of alpha (additive smoothing parameter, default: None). 
This kind of classifier distributes the labels according to the multivariate Bernoulli distribution. 
It was decided to implement these two Naive Bayes classifier, because the Bernoulli and Gaussian distribution are one of the most known and used distributions.
#### Decision Tree
It was decided to implement a simple decision tree classifier. 
For this, the class `sklearn.tree.DecisionTreeClassifier` from the `sklearn` library was used for. 
Classification of a decision tree is based on simple decision rules. 
The parameter for the maximum depth of the decision tree (max_depth, default = None) can be specified via a parser argument.
#### Support Vector Machine
It was decided to implement a support vetor machine using the libary `sklearn.svm`. 
A Linear Support Vecotr Classifier (`LinearSVC`) was choosen, because it's a faster implementation of the original Support Vector Machine. 
Especially for large datasets including a big amomunt of samples the `LinearSVC` is the best choice. 
The parameter for the maximum number of iterations (max_iter, default = None) can be specified via a parser argument.
#### Random Forest
In addition to the decision tree, it was decided to include a random forest classifier. 
This is integrated with the class `sklear.ensemble.RandomForestClassifier`. 
Furthermore, the number of decision trees in the random forest can be defined via the parser argument (`n_estimators`, default: None).
#### Multi Layer Perceptron
It was decided to implement a multi layer perceptron classifier. 
For this, the class `sklearn.neural_network.MLPClassifier` from the `sklearn` library was used for. 
For classification a simple multi layer perceptron is used. 
The parameter for the maximum number of iterations (max_iter, default = None) can be specified via a parser argument.
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
Inside the folder `test` a new folder `preprocessing` was created to collect all unit tests for the newly created preprocessors.
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

### Feature Extraction
Inside the folder `test` a new folder `feature_extraction` was created to collect all unit tests for the newly created feature extractors.
These ones are described in the following.

#### WantedStr Test
The unit test `wanted_str_test.py` checks the functionality of the feature extractor `wanted_str.py`.
This is needed to check for different use cases. It was produced as a simple unittest as well as a test driven unittest. 
A set up function and several test cases are defined:
- `def setUp(self)`: New instance of `WantedStr` are defined with different `wanted_str`, as well as the `INPUT_COLUMN` and a test input data frame.
- `def test_input_columns(self)`: Checks wether the input column given to the instance matches the input column of the instance.
- `def test_feature_name(self)`: Checks wether the feature name matches the one produced by the instance. 
- `def test_list_of_wanted_str_true(self)`: Checks whether a wanted string which is included in the test tweet gets the feature true. 
- `def test_list_of_wanted_str_false(self)`: Checks whether a wanted string which is not included in the test tweet gets the feature false. 
- `def test_list_of_wanted_str_capital(self)`: Checks whether a wanted string with capital letters which is included as lower case in the test tweet gets the feature true. 
- `def test_list_of_wanted_str_lower(self)`: Checks whether a wanted string with lower case which is included using capital letters in the test tweet gets the feature true. 
- `def test_list_of_wanted_str_empty(self)`: Checks whether an empty string (default) gets the feature false.





