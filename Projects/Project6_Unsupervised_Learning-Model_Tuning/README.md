Unsupervised Learning - Model Tuning - ReneWind Project

Project Overview:

"ReneWind" is a company working on improving the machinery/processes involved in the production of wind energy using machine learning and has collected data of generator failure of wind turbines using sensors. The objective was to build various classification models, tune them and find the best one that will help identify failures so that the generator could be repaired before failing/breaking and the overall maintenance cost of the generators can be brought down.

Skills:

- Exploratory Data Analysis
- Data Preprocessing
- Up and Downsampling
- Regularization
- Hyperparameter Tuning
  

Dataset Information:

The data provided is a transformed version of original data which was collected using sensors.
Train.csv - To be used for training and tuning of models.
Test.csv - To be used only for testing the performance of the final best model.
Both the datasets consist of 40 predictor variables and 1 target variable


Files included in repository:

- Todd_Project_6_FullCode-2.ipynb – Jupyter Notebook with analysis, logistic regression model, decision tree models, and insights.
- todd_project6_fullcode.py - Python script exported from Google Collab
- Train.csv - Dataset used for analysis and testing on training data
- Test.csv – Dataset used for analysis and testing on testing data
- requirements.txt – List of required Python libraries.


Models Tested & Performance:

This project evaluated multiple supervised learning models for predicting cancellations.

1. Decision Tree Model (Baseline):
- Basic decision tree classifier tested.
- Strengths: Captured complex interactions in the data.
- Weaknesses: Overfitted the training data, reducing generalization ability.
3. Tuned Decision Tree:
- Applied hyperparameter tuning (class_weight, max_depth=10, max_leaf_nodes, min_impurity_decrease, min_samples_leaf) to prevent overfitting.
- Results: Improved generalization, and imporved agreeability between training and testing data for all scores - accuracy, recall, precision, and f1 scores. 
4. Bagging Classifier
- A lot of overfitting
5. Tuned Bagging Classifier
- A lot of overfitting
6. Random Forest
- A lot of overfitting
7. Tuned Random Forest
8. Adaboost Classifier
9. Tuned Adaboost Classifier
10. Gradient Boost Classifier
11. Tuned Gradient Boost Classifier
12. XGBoost Classifier
13. XGBoost Classifier Tuned (chosen model)
14. Stacking Classifier

Why XGBoost Classifier Tuned Was Selected:
- Minimized Overfitting: Unlike bagging models (Random Forest, Bagging Classifier), XGBoost showed strong generalization.
- Best Balance of Precision & Recall: Achieved an F1 score of 0.833, making it the most reliable model for visa decision prediction.
- Business Context: Since both false approvals and false denials carry consequences, the F1 score (balancing precision & recall) was prioritized.


Analysis and Findings:

Actionable Insights/Business Recommendations:

- Use the Tuned XGBoost Model: It has strong generalization and a high F1 score, making it ideal for predicting visa outcomes.
- Prioritize Applicants with Higher Education: The model indicates that those without post-secondary education are much more likely to be denied.
- Prioritize Job Experience: Applicants without prior experience have a significantly lower chance of approval.
- Consider Wage Thresholds: Higher prevailing wages correlate with approvals. This suggests that lower-wage jobs may not require out-of-country expertise, leading to more denials.

Installation and Setup:

To run the analysis:

- Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project6_Ensemble_Methods
- Install dependencies:
- pip install -r requirements.txt
- Run the Jupyter Notebook:
- jupyter notebook PROJECT5_fullcode2-2.ipynb


Conclusion:

This project successfully identified key predictors of visa approvals and denials, with education, job experience, and prevailing wage playing critical roles. The Tuned XGBoost Classifier was selected as the best model due to its high generalizability and optimal F1 score. Implementing this model can help streamline visa application reviews and improve decision-making accuracy.
