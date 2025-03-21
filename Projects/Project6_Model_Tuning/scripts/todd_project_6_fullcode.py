# -*- coding: utf-8 -*-
"""Todd_Project_6_FullCode.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MoGCHK1_74W_7-qWznDmRnQkjwU7hmDC

## Problem Statement

### Business Context

Renewable energy sources play an increasingly important role in the global energy mix, as the effort to reduce the environmental impact of energy production increases.

Out of all the renewable energy alternatives, wind energy is one of the most developed technologies worldwide. The U.S Department of Energy has put together a guide to achieving operational efficiency using predictive maintenance practices.

Predictive maintenance uses sensor information and analysis methods to measure and predict degradation and future component capability. The idea behind predictive maintenance is that failure patterns are predictable and if component failure can be predicted accurately and the component is replaced before it fails, the costs of operation and maintenance will be much lower.

The sensors fitted across different machines involved in the process of energy generation collect data related to various environmental factors (temperature, humidity, wind speed, etc.) and additional features related to various parts of the wind turbine (gearbox, tower, blades, break, etc.).



## Objective
“ReneWind” is a company working on improving the machinery/processes involved in the production of wind energy using machine learning and has collected data of generator failure of wind turbines using sensors. They have shared a ciphered version of the data, as the data collected through sensors is confidential (the type of data collected varies with companies). Data has 40 predictors, 20000 observations in the training set and 5000 in the test set.

The objective is to build various classification models, tune them, and find the best one that will help identify failures so that the generators could be repaired before failing/breaking to reduce the overall maintenance cost.
The nature of predictions made by the classification model will translate as follows:

- True positives (TP) are failures correctly predicted by the model. These will result in repairing costs.
- False negatives (FN) are real failures where there is no detection by the model. These will result in replacement costs.
- False positives (FP) are detections where there is no failure. These will result in inspection costs.

It is given that the cost of repairing a generator is much less than the cost of replacing it, and the cost of inspection is less than the cost of repair.

“1” in the target variables should be considered as “failure” and “0” represents “No failure”.

## Data Description
- The data provided is a transformed version of original data which was collected using sensors.
- Train.csv - To be used for training and tuning of models.
- Test.csv - To be used only for testing the performance of the final best model.
- Both the datasets consist of 40 predictor variables and 1 target variable

## Importing necessary libraries
"""

# Libraries to help with reading and manipulating data
import pandas as pd
import numpy as np

# Libaries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# To tune model, get different metric scores, and split data
from sklearn.metrics import (
    f1_score,
    accuracy_score,
    recall_score,
    precision_score,
    confusion_matrix,
    roc_auc_score,
    ConfusionMatrixDisplay,
)
from sklearn import metrics

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score

# To be used for data scaling and one hot encoding
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder

# To impute missing values
from sklearn.impute import SimpleImputer

# To oversample and undersample data
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# To do hyperparameter tuning
from sklearn.model_selection import RandomizedSearchCV

# To be used for creating pipelines and personalizing them
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# To define maximum number of columns to be displayed in a dataframe
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# To supress scientific notations for a dataframe
pd.set_option("display.float_format", lambda x: "%.3f" % x)

# To help with model building
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
    BaggingClassifier,
)
from xgboost import XGBClassifier

# To suppress scientific notations
pd.set_option("display.float_format", lambda x: "%.3f" % x)

# To suppress warnings
import warnings

warnings.filterwarnings("ignore")

# This will help in making the Python code more structured automatically (good coding practice)
#%load_ext nb_black

"""## Loading the dataset"""

#load dataset
df = pd.read_csv('Train.csv')
df_test = pd.read_csv('Test.csv')

# creating a copy of each dataset
data = df.copy()
data_test = df_test.copy()

"""## Data Overview

- Observations
- Sanity checks
"""

# check first 5 rows of dataset
data.head()

# check first 5 rows of test dataset
data_test.head()

# last 5 rows of dataset
data.tail()

# last 5 rows of test dataset
data_test.tail()

"""1 = failure; 0 = no failure"""

# check rows and columns
data.shape

"""41 cols (40 independent variables; 1 target/dependent variable); 20,000 rows"""

# check rows and columns of test dataset
data_test.shape

"""41 cols (40 independent variables; 1 target/dependent variable); 5,000 rows"""

# check var datatypes
data.info()

"""- first 2 variables are missing 18 datapoints
- all other variables are not missing data
- all independent vars are floats
- independent/target var is int
"""

# check test var datatypes
data_test.info()

"""All the same as train data; but, first var is missing 5 datapoints, second var is missing 6 (similar ratio of missing datapoints)."""

# check data stats
data.describe()

# check test data stats
data_test.describe()

"""Same median and mean."""

#check for duplicates
data.duplicated().sum()

#check for duplicates in test data
data_test.duplicated().sum()

"""No duplicates"""

# investigate missing vals
data.isna().sum()

# investigate missing vals in test
data_test.isna().sum()

"""We will investigate these missing values more after the initial exploratory data analysis, during data presprocessing.

## Exploratory Data Analysis (EDA)

### Plotting histograms and boxplots for all the variables
"""

def histogram_boxplot(data, feature, figsize=(12, 7), kde=False, bins=None):
    """
    Boxplot and histogram combined

    data: dataframe
    feature: dataframe column
    figsize: size of figure (default (12,7))
    kde: whether to show density curve (default False)
    bins: number of bins for histogram (default None)
    """
    f2, (ax_box2, ax_hist2) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid= 2
        sharex=True,  # x-axis will be shared among all subplots
        gridspec_kw={"height_ratios": (0.25, 0.75)},
        figsize=figsize,
    )  # creating the 2 subplots
    f2.suptitle(feature, fontsize=16)  # Add the title to the figure
    sns.boxplot(
        data=data, x=feature, ax=ax_box2, showmeans=True, color="violet"
    )  # boxplot will be created and a star will indicate the mean value of the column
    if bins:
        sns.histplot(data=data, x=feature, kde=kde, ax=ax_hist2, bins=bins)
    else:
        sns.histplot(data=data, x=feature, kde=kde, ax=ax_hist2)

    ax_hist2.axvline(
        data[feature].mean(), color="green", linestyle="--"
    )  # Add mean to the histogram
    ax_hist2.axvline(
        data[feature].median(), color="black", linestyle="-"
    )  # Add median to the histogram

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for title
    plt.show()

"""### Plotting all the features at one go"""

# Loop through each feature in the DataFrame
for feature in df.columns:
    histogram_boxplot(df, feature, figsize=(12, 7), kde=False, bins=None)

"""- All independent variable histograms show a normal distribution.
- None of the boxplots particularly stand out to me. All are pretty similar with the median being very close to the mean, and about an even amount of outliers on each side.
- The dependent (target) variable shows most of the data falls into the 0 (no failure) category, and very few datapoints fall into the 1 (failure) category (1 represnts failure, 0 represents no failure). This tells me there is a major class imbalance, which will affect the measure of my model. Accuracy will not be as important to me in this context because even if we label everything as no failure, we will still have a high accuracy; but, in this context, that would not be helpful. So, the statistic that matters most to me will be is Recall, because I care most about reducing false negatives.
"""

# understand the class imbalance a bit better
data['Target'].value_counts(normalize=True)

"""Not even 1% of the data is failures. This is a major class imbalance. We will need to regularize each model in some way to have a better understanding of model performance."""

# understand the class imbalance in test data a bit better
data_test['Target'].value_counts(normalize=True)

"""Same proportion of failures to non-failures in test data - good.

No feature engineering necessary bc we don't know what each variable is, and they are all integers, so we do not need to reorganize in any way.

## Data Pre-processing

### Data Preparation for Modeling
"""

data.head()

# Dividing train data into X and y
X = data.drop(["Target"], axis=1)
# don't need to get dummies bc all ints

y = data["Target"]

# Splitting train dataset into training and validation set

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)

print(X_train.shape, X_val.shape)

# Dividing test data into X_test and y_test

X_test = data_test.drop(["Target"], axis=1)

y_test = data_test["Target"]

# Checking the number of rows and columns in the X_test data
X_test.shape

"""testing data is the same shape as validation data - good.

### Missing value imputation
"""

# investigate missing values more
data[data.isna().any(axis=1)]

"""This data all looks normal, and all are non-failures, which statistically makes sense due to the class imbalance. I assume the missing values were due to data entry issues or lack of infomation, but the data is still good. So, we will use a simple imputer to get rid of the missing values and use this data."""

# using simple imputer to quickly impute all nan values with the median

imputer = SimpleImputer(strategy="median")

# Fit and transform the train data
X_train = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)
# by only using fit_transform on training data, I am ensuring the median is only being fit to training data (only using median for training data)
# then, I use the median fitted to training data for val and test data, to avoid data leakage
# (using median for val or train data and accidentally using that median in training data would allow my model to learn from this median, and get info that would not normally be providing)
# (thus, creating a model that predicts very well, but is less generalizable on real data)

# Transform the validation data
X_val = pd.DataFrame(imputer.transform(X_val), columns=X_train.columns)
# not using fit_transform to avoid data leakage

# Transform the test data
X_test = pd.DataFrame(imputer.transform(X_test), columns=X_train.columns)

# Checking that no column has missing values in train or test sets

print(X_train.isna().sum())
print("-" * 30)
print(X_val.isna().sum())
print("-" * 30)
print(X_test.isna().sum())

"""No more missing data in training, validation, or test sets!

## Model Building

### Model evaluation criterion

The nature of predictions made by the classification model will translate as follows:

- True positives (TP) are failures correctly predicted by the model.
- False negatives (FN) are real failures in a generator where there is no detection by model.
- False positives (FP) are failure detections in a generator where there is no failure.

**Which metric to optimize?**

* We need to choose the metric which will ensure that the maximum number of generator failures are predicted correctly by the model.
* We would want Recall to be maximized as greater the Recall, the higher the chances of minimizing false negatives.
* We want to minimize false negatives because if a model predicts that a machine will have no failure when there will be a failure, it will increase the maintenance cost.

**Let's define a function to output different metrics (including recall) on the train and test set and a function to show confusion matrix so that we do not have to use the same code repetitively while evaluating models.**
"""

# defining a function to compute different metrics to check performance of a classification model built using sklearn
def model_performance_classification_sklearn(model, predictors, target):
    """
    Function to compute different metrics to check classification model performance

    model: classifier
    predictors: independent variables
    target: dependent variable
    """

    # predicting using the independent variables
    pred = model.predict(predictors)

    acc = accuracy_score(target, pred)  # to compute Accuracy
    recall = recall_score(target, pred)  # to compute Recall
    precision = precision_score(target, pred)  # to compute Precision
    f1 = f1_score(target, pred)  # to compute F1-score

    # creating a dataframe of metrics
    df_perf = pd.DataFrame(
        {
            "Accuracy": acc,
            "Recall": recall,
            "Precision": precision,
            "F1": f1

        },
        index=[0],
    )

    return df_perf

"""### Defining scorer to be used for cross-validation and hyperparameter tuning

- We want to reduce false negatives and will try to maximize "Recall".
- To maximize Recall, we can use Recall as a **scorer** in cross-validation and hyperparameter tuning.
"""

# Type of scoring used to compare parameter combinations
scorer = metrics.make_scorer(metrics.recall_score)

"""### Model Building with original data

Sample Decision Tree model building with original data
"""

models = []  # Empty list to store all the models

# Appending models into the list
models.append(("Bagging", BaggingClassifier(random_state=1)))
models.append(("Random forest", RandomForestClassifier(random_state=1)))
models.append(("GBM", GradientBoostingClassifier(random_state=1)))
models.append(("Adaboost", AdaBoostClassifier(random_state=1)))
models.append(("Xgboost", XGBClassifier(random_state=1, eval_metric="logloss")))
models.append(("dtree", DecisionTreeClassifier(random_state=1)))

results1 = []  # Empty list to store all model's CV scores
names = []  # Empty list to store name of the models


# loop through all models to get the mean cross validated score
print("\n" "Cross-Validation performance on training dataset:" "\n")

for name, model in models:
    kfold = StratifiedKFold(
        n_splits=5, shuffle=True, random_state=1
    )  # Setting number of splits equal to 5
    cv_result = cross_val_score(
        estimator=model, X=X_train, y=y_train, scoring=scorer, cv=kfold
    )
    results1.append(cv_result)
    names.append(name)
    print("{}: {}".format(name, cv_result.mean()))

print("\n" "Validation Performance:" "\n")

for name, model in models:
    model.fit(X_train, y_train)
    scores = recall_score(y_val, model.predict(X_val))
    print("{}: {}".format(name, scores))

"""We are testing for recall score because we care most about identifying the failed machines correctly.

It looks like the bagging model and random forrest model performed pretty similarly, with relatively high recall scores, and good agreeability between training and validation data. Both seem to be pretty good models before any regularizing or hyperparameter tuning.

The GBM model has pretty good recall scores, and good agreeability; maybe slight underfitting in this model, but not too bad.

The Adaboost model has lower scores, but good agreeability.

XGBoodt is the best model so far. The recall score is pretty high for the training data, and the validation data matches it pretty well.

The dtree has a lower score with less agreeability.

Ideally, all these scores would be a bit higher, but nothing is too bad. We will see if we can increase these scores with regularizing the model either through undersampling or oversampling, or with hyperparameter tuning. However, the XGBoost model is already very good.
"""

# Plotting boxplots for CV scores of all models defined above
fig = plt.figure(figsize=(10, 7))

fig.suptitle("Algorithm Comparison")
ax = fig.add_subplot(111)

plt.boxplot(results1)
ax.set_xticklabels(names)

plt.show()

"""Visualization of models. XGBoost model is perfomring very well.

### Model Building with Oversampled data

We have to check model performance with regularized data because of the class imbalance. The first method we will use is oversampling the data using SMOTE (using synthetic data in the minority class to treat class imbalance).
"""

# Synthetic Minority Over Sampling Technique
sm = SMOTE(sampling_strategy=1, k_neighbors=5, random_state=1)
X_train_over, y_train_over = sm.fit_resample(X_train, y_train)

# print number of datapoints in each class before and after oversampling

print("Before Oversampling, counts of label 'Failure': {}".format(sum(y_train == 1)))
print("Before Oversampling, counts of label 'No Failure': {} \n".format(sum(y_train == 0)))


print("After Oversampling, counts of label 'Failure': {}".format(sum(y_train_over == 1)))
print("After Oversampling, counts of label 'No Failure': {} \n".format(sum(y_train_over == 0)))


print("After Oversampling, the shape of train_X: {}".format(X_train_over.shape))
print("After Oversampling, the shape of train_y: {} \n".format(y_train_over.shape))

"""Before oversampling, we see the data has a major class imbalance, with a large majority falling into 'No Failure'. After oversampling, we created synthetic data to include in the minority class, so now both classes have the same number datapoints that, previously, only the majority class had."""

# check cross-validation scores and training and testing set for oversamples data

results_over = []  # Empty list to store all model's CV scores


# loop through all models to get the mean cross validated score
print("\n" "Cross-Validation performance on training dataset:" "\n")

for name, model in models:
    kfold = StratifiedKFold(
        n_splits=5, shuffle=True, random_state=1
    )  # Setting number of splits equal to 5
    cv_result_over = cross_val_score(
        estimator=model, X=X_train_over, y=y_train_over, scoring=scorer, cv=kfold
    )
    results_over.append(cv_result_over)
    print("{}: {}".format(name, cv_result_over.mean()))

print("\n" "Validation Performance:" "\n")

for name, model in models:
    model.fit(X_train_over, y_train_over)
    scores = recall_score(y_val, model.predict(X_val))
    print("{}: {}".format(name, scores))

"""All scores for each model in training set increased quite a bit after oversampling.

Validation set scores increased, but not as drastically, meaning these models could lead to more overfitting and less generalizability after the model is regularized.

GBM and Adaboost are the models with the most agreeability between training and validation sets. However, XGBoost still has the highest scores.
"""

# Plotting boxplots for CV scores of all models defined above with oversampled data

fig = plt.figure(figsize=(10, 7))

fig.suptitle("Algorithm Comparison")
ax = fig.add_subplot(111)

plt.boxplot(results_over)
ax.set_xticklabels(names)

plt.show()

"""### Model Building with Undersampled data

We have to check model performance with regularized data because of the class imbalance. The first method we will use is oversampling the data using random undersampler (randomly reducing the number of samples in the majority class to treat class imbalanace).
"""

# Random undersampler for under sampling the data
rus = RandomUnderSampler(random_state=1, sampling_strategy=1)
X_train_un, y_train_un = rus.fit_resample(X_train, y_train)

# print number of datapoints in each class before and after undersampling

print("Before Undersampling, counts of label 'Failure': {}".format(sum(y_train == 1)))
print("Before Undersampling, counts of label 'No Failure': {} \n".format(sum(y_train == 0)))


print("After Undersampling, counts of label 'Failure': {}".format(sum(y_train_un == 1)))
print("After Undersampling, counts of label 'No Failure': {} \n".format(sum(y_train_un == 0)))


print("After Undersampling, the shape of train_X: {}".format(X_train_un.shape))
print("After Undersampling, the shape of train_y: {} \n".format(y_train_un.shape))

"""Before undersampling, we see the same major class imbalance. After undersampling through randomly chosing datapoints to include in the 'No Failure' class, we see the size of the majority class has been reduced to match the minority class, eliminating the class imabalance."""

# check cross-validation scores and training and testing set for oversamples data

results_un = []  # Empty list to store all model's CV scores


# loop through all models to get the mean cross validated score
print("\n" "Cross-Validation performance on training dataset:" "\n")

for name, model in models:
    kfold = StratifiedKFold(
        n_splits=5, shuffle=True, random_state=1
    )  # Setting number of splits equal to 5
    cv_result_un = cross_val_score(
        estimator=model, X=X_train_un, y=y_train_un, scoring=scorer, cv=kfold
    )
    results_un.append(cv_result_un)
    print("{}: {}".format(name, cv_result_un.mean()))

print("\n" "Validation Performance:" "\n")

for name, model in models:
    model.fit(X_train_un, y_train_un)
    scores = recall_score(y_val, model.predict(X_val))
    print("{}: {}".format(name, scores))

"""After undersampling, we notice an increase in scores from the original data for all models. And, the scores between training and validation sets are still higly similar.

So, undersampling seems to be the best way to deal with the class imbalance.

I still think XGBoost is the best option, since the scores are so high with very similar scores between training and teting sets, but the random forrest model is very good as well.
"""

# Plotting boxplots for CV scores of all models defined above with undersampled data

fig = plt.figure(figsize=(10, 7))

fig.suptitle("Algorithm Comparison")
ax = fig.add_subplot(111)

plt.boxplot(results_un)
ax.set_xticklabels(names)

plt.show()

"""### Model Selection

XGBoost performed the best, so I will proceed with hypertuning this model.
"""

#define XGBoost Classifier
xgb_classifier = XGBClassifier(random_state=1, eval_metric="logloss")
#fit
xgb_classifier.fit(X_train, y_train)

#check performance on train data
xgb_classifier_model_train_perf = model_performance_classification_sklearn(xgb_classifier, X_train, y_train)
xgb_classifier_model_train_perf

#check performance for validation data
xgb_classifier_model_val_perf = model_performance_classification_sklearn(xgb_classifier, X_val, y_val)
xgb_classifier_model_val_perf

"""## HyperparameterTuning

### Sample Parameter Grids

**Hyperparameter tuning can take a long time to run, so to avoid that time complexity - you can use the following grids, wherever required.**

- For Gradient Boosting:

param_grid = {
    "n_estimators": np.arange(100,150,25),
    "learning_rate": [0.2, 0.05, 1],
    "subsample":[0.5,0.7],
    "max_features":[0.5,0.7]
}

- For Adaboost:

param_grid = {
    "n_estimators": [100, 150, 200],
    "learning_rate": [0.2, 0.05],
    "base_estimator": [DecisionTreeClassifier(max_depth=1, random_state=1), DecisionTreeClassifier(max_depth=2, random_state=1), DecisionTreeClassifier(max_depth=3, random_state=1),
    ]
}

- For Bagging Classifier:

param_grid = {
    'max_samples': [0.8,0.9,1],
    'max_features': [0.7,0.8,0.9],
    'n_estimators' : [30,50,70],
}

- For Random Forest:

param_grid = {
    "n_estimators": [200,250,300],
    "min_samples_leaf": np.arange(1, 4),
    "max_features": [np.arange(0.3, 0.6, 0.1),'sqrt'],
    "max_samples": np.arange(0.4, 0.7, 0.1)
}

- For Decision Trees:

param_grid = {
    'max_depth': np.arange(2,6),
    'min_samples_leaf': [1, 4, 7],
    'max_leaf_nodes' : [10, 15],
    'min_impurity_decrease': [0.0001,0.001]
}

- For Logistic Regression:

param_grid = {'C': np.arange(0.1,1.1,0.1)}

- For XGBoost:

param_grid={
    'n_estimators': [150, 200, 250],
    'scale_pos_weight': [5,10],
    'learning_rate': [0.1,0.2],
    'gamma': [0,3,5],
    'subsample': [0.8,0.9]
}

### Sample tuning method for Decision tree with original data
"""

# defining model
Model = DecisionTreeClassifier(random_state=1)

# Parameter grid to pass in RandomSearchCV
param_grid = {'max_depth': np.arange(2,6),
              'min_samples_leaf': [1, 4, 7],
              'max_leaf_nodes' : [10,15],
              'min_impurity_decrease': [0.0001,0.001] }

#Calling RandomizedSearchCV
randomized_cv = RandomizedSearchCV(estimator=Model, param_distributions=param_grid, n_iter=10, n_jobs = -1, scoring=scorer, cv=5, random_state=1)

#Fitting parameters in RandomizedSearchCV
randomized_cv.fit(X_train,y_train)

print("Best parameters are {} with CV score={}:" .format(randomized_cv.best_params_,randomized_cv.best_score_))

"""### Sample tuning method for Decision tree with oversampled data"""

# defining model
Model = DecisionTreeClassifier(random_state=1)

# Parameter grid to pass in RandomSearchCV
param_grid = {'max_depth': np.arange(2,6),
              'min_samples_leaf': [1, 4, 7],
              'max_leaf_nodes' : [10,15],
              'min_impurity_decrease': [0.0001,0.001] }

#Calling RandomizedSearchCV
randomized_cv = RandomizedSearchCV(estimator=Model, param_distributions=param_grid, n_iter=10, n_jobs = -1, scoring=scorer, cv=5, random_state=1)

#Fitting parameters in RandomizedSearchCV
randomized_cv.fit(X_train_over,y_train_over)

print("Best parameters are {} with CV score={}:" .format(randomized_cv.best_params_,randomized_cv.best_score_))

"""### Sample tuning method for Decision tree with undersampled data"""

# defining model
Model = DecisionTreeClassifier(random_state=1)

# Parameter grid to pass in RandomSearchCV
param_grid = {'max_depth': np.arange(2,20),
              'min_samples_leaf': [1, 2, 5, 7],
              'max_leaf_nodes' : [5, 10,15],
              'min_impurity_decrease': [0.0001,0.001] }

#Calling RandomizedSearchCV
randomized_cv = RandomizedSearchCV(estimator=Model, param_distributions=param_grid, n_iter=10, n_jobs = -1, scoring=scorer, cv=5, random_state=1)

#Fitting parameters in RandomizedSearchCV
randomized_cv.fit(X_train_un,y_train_un)

print("Best parameters are {} with CV score={}:" .format(randomized_cv.best_params_,randomized_cv.best_score_))

"""### Hyperparameter tuning with XGBoost (original data)"""

# XGBoost Hyperparameter Tuning

# defining model
Model = XGBClassifier(random_state=1, eval_metric="logloss")

# Parameter grid to pass in RandomSearchCV
param_grid = {
    "n_estimators": np.arange(150, 300, 50),
    "scale_pos_weight": [5, 10],
    "learning_rate": [0.1, 0.2],
    "gamma": [0, 3, 5],
    "subsample": [0.8, 0.9],
}

#Calling RandomizedSearchCV
randomized_cv = RandomizedSearchCV(estimator=Model, param_distributions=param_grid, n_iter=10, n_jobs = -1, scoring=scorer, cv=5, random_state=1)

#Fitting parameters in RandomizedSearchCV
randomized_cv.fit(X_train,y_train)

print("Best parameters are {} with CV score={}:" .format(randomized_cv.best_params_,randomized_cv.best_score_))

# building model with best parameters
xgb_tuned = XGBClassifier(
    n_estimators=200,
    scale_pos_weight=10,
    learning_rate=0.1,
    gamma=0,
    subsample=0.8,
    random_state=1,
    base_estimator=DecisionTreeClassifier(max_depth=2, random_state=1),
)

# Fit the model on training data
xgb_tuned.fit(X_train, y_train)

# Calculating different metrics on train set
xgb_random_train = model_performance_classification_sklearn(
    xgb_tuned, X_train, y_train
)
print("Training performance:")
xgb_random_train

# Calculating different metrics on validation set
xgb_random_val = model_performance_classification_sklearn(xgb_tuned, X_val, y_val)
print("Validation performance:")
xgb_random_val

"""After hyperparameter tuning on the XGBoost model with original data, the model suffers from overfitting.

### Hyperparameter tuning with XGBoost (oversampled data)
"""

# XGBoost Hyperparameter Tuning

# defining model
Model = XGBClassifier(random_state=1, eval_metric="logloss")

# Parameter grid to pass in RandomSearchCV
param_grid = {
    "n_estimators": np.arange(150, 300, 50),
    "scale_pos_weight": [5, 10],
    "learning_rate": [0.1, 0.2],
    "gamma": [0, 3, 5],
    "subsample": [0.8, 0.9],
}

#Calling RandomizedSearchCV
randomized_cv = RandomizedSearchCV(estimator=Model, param_distributions=param_grid, n_iter=10, n_jobs = -1, scoring=scorer, cv=5, random_state=1)

#Fitting parameters in RandomizedSearchCV
randomized_cv.fit(X_train_over,y_train_over)

print("Best parameters are {} with CV score={}:" .format(randomized_cv.best_params_,randomized_cv.best_score_))

# building model with best parameters
xgb_tuned_over = XGBClassifier(
    n_estimators=200,
    scale_pos_weight=10,
    learning_rate=0.2,
    gamma=0,
    subsample=0.9,
    random_state=1,
    base_estimator=DecisionTreeClassifier(max_depth=2, random_state=1),
)

# Fit the model on training data
xgb_tuned_over.fit(X_train, y_train)

# Calculating different metrics on train set
xgb_random_train_over = model_performance_classification_sklearn(
    xgb_tuned_over, X_train, y_train
)
print("Training performance:")
xgb_random_train_over

# Calculating different metrics on validation set
xgb_random_val_over = model_performance_classification_sklearn(xgb_tuned_over, X_val, y_val)
print("Validation performance:")
xgb_random_val_over

"""After hyperparameter tuning on the XGBoost model with oversampled data, the model suffers from overfitting.

### Hyperparameter tuning with XGBoost (undersampled data)
"""

# XGBoost Hyperparameter Tuning

# defining model
Model = XGBClassifier(random_state=1, eval_metric="logloss")

# Parameter grid to pass in RandomSearchCV
param_grid = {
    "n_estimators": np.arange(150, 300, 50),
    "scale_pos_weight": [5, 10],
    "learning_rate": [0.1, 0.2],
    "gamma": [0, 3, 5],
    "subsample": [0.8, 0.9],
}

#Calling RandomizedSearchCV
randomized_cv = RandomizedSearchCV(estimator=Model, param_distributions=param_grid, n_iter=10, n_jobs = -1, scoring=scorer, cv=5, random_state=1)

#Fitting parameters in RandomizedSearchCV
randomized_cv.fit(X_train_un,y_train_un)

print("Best parameters are {} with CV score={}:" .format(randomized_cv.best_params_,randomized_cv.best_score_))

# building model with best parameters
xgb_tuned_un = XGBClassifier(
    n_estimators=200,
    scale_pos_weight=10,
    learning_rate=0.1,
    gamma=0,
    subsample=0.8,
    random_state=1,
    base_estimator=DecisionTreeClassifier(max_depth=2, random_state=1),
)

# Fit the model on training data
xgb_tuned_un.fit(X_train, y_train)

# Calculating different metrics on train set
xgb_random_train_un = model_performance_classification_sklearn(
    xgb_tuned_un, X_train, y_train
)
print("Training performance:")
xgb_random_train_un

# Calculating different metrics on validation set
xgb_random_val_un = model_performance_classification_sklearn(xgb_tuned_un, X_val, y_val)
print("Validation performance:")
xgb_random_val_un

"""After hyperparameter tuning on the XGBoost model with original data, the model suffers from overfitting.

## Model performance comparison and choosing the final model
"""

# training performance comparison

models_train_comp_df = pd.concat(
    [
        xgb_classifier_model_train_perf.T,
        xgb_random_train.T,
        xgb_random_train_over.T,
        xgb_random_train_un.T,
    ],
    axis=1,
)
models_train_comp_df.columns = [
    "XGBoost",
    "XGBoost Tuned",
    "XGBoost Tuned with oversampled data,",
    "XGBoost Tuned with undersampled data",
]
print("Training performance comparison:")
models_train_comp_df

# validation performance comparison

models_train_comp_df = pd.concat(
    [
        xgb_classifier_model_val_perf.T,
        xgb_random_val.T,
        xgb_random_val_over.T,
        xgb_random_val_un.T,
    ],
    axis=1,
)
models_train_comp_df.columns = [
    "XGBoost",
    "XGBoost Tuned",
    "XGBoost Tuned with oversampled data,",
    "XGBoost Tuned with undersampled data",

]
print("Validation performance comparison:")
models_train_comp_df

"""In conclusion, all the models suffer from overfitting, but the tuned XGBoost model with oversampled data has the highest score, so we will pick this as our best model.

### Test set final performance
"""

# Calculating different metrics on the test set
xgb_test = model_performance_classification_sklearn(xgb_tuned_over, X_test, y_test)
print("Test performance:")
xgb_test

"""## Pipelines to build the final model

"""

# no need to separate data into num and cat columns bc all cols are the same

# no need for imputation process bc no missing vals

# Separating target variable and other variables
X = data.drop(columns="Target")
Y = data["Target"]

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.20, random_state=1, stratify=Y
)
print(X_train.shape, X_test.shape)

# Creating new pipeline with best parameters
model = Pipeline(steps=[
    ("XGB", XGBClassifier(
        n_estimators=200,
        scale_pos_weight=10,
        learning_rate=0.2,
        gamma=0,
        subsample=0.9,
        random_state=1
    ))
])

# Fit the model on training data
model.fit(X_train, y_train)

# Let's check the performance on test set
Model_test = model_performance_classification_sklearn(model, X_test, y_test)
Model_test

"""These are good scores. Overall, this is a good model.

# Business Insights and Conclusions

- The XGBoost model uses the 40 predictors provided by the company, and is able to identify when there will be a machine failure with about 99% accuracy, 85% recall, 96% precision, and 90% F1.
- I would advise “ReneWind” to use this algorithm by entering the data from the different sensors of each machine, and when one machine is about to fail, this model will likley be able to predict this failure ahead of time, so this company should use their reasources more wisely by allocating the time, energy, and supplies used to prevent these failures only into the machines that are predicted to soon fail by the model. By doing this, no reasources will be wasted on doing preventative maintence on machines that were unlikley to fail in the first place.
- This will result in less time, energy, and reasource waste, and reduce maintence cost.

***
"""

!jupyter nbconvert Todd_Project_6_FullCode.ipynb --to html

