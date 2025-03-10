Ensemble Techiques - EasyVisa Project

Project Overview:

This project analyzes the data of Visa applicants, build a predictive model to facilitate the process of visa approvals, and based on important factors that significantly influence the Visa status recommend a suitable profile for the applicants for whom the visa should be certified or denied.

Skills:

- Exploratory Data Analysis
- Data Preprocessing
- Customer Profiling
- Bagging Classifiers (Bagging and Random Forest)
- Boosting Classifier (AdaBoost
- Gradient Boosting
- XGBoost
- Stacking Classifier
- Hyperparameter Tuning using GridSearchCV
  

Dataset Information:

The data contains the different attributes of the employee and the employer. The detailed data dictionary is given below.

- case_id: ID of each visa application
- continent: Information of continent the employee
- education_of_employee: Information of education of the employee
- has_job_experience: Does the employee has any job experience? Y= Yes; N = No
- requires_job_training: Does the employee require any job training? Y = Yes; N = No
- no_of_employees: Number of employees in the employer's company
- yr_of_estab: Year in which the employer's company was established
- region_of_employment: Information of foreign worker's intended region of employment in the US.
- prevailing_wage: Average wage paid to similarly employed workers in a specific occupation in the area of intended employment. The purpose of the prevailing wage is to ensure that the foreign worker is not underpaid compared to other workers offering the same or similar service in the same area of employment.
- unit_of_wage: Unit of prevailing wage. Values include Hourly, Weekly, Monthly, and Yearly.
- full_time_position: Is the position of work full-time? Y = Full Time Position; N = Part Time Position
- case_status: Flag indicating if the Visa was certified or denied


Files included in repository:

- PROJECT5_fullcode2-2.ipynb – Jupyter Notebook with analysis, logistic regression model, decision tree models, and insights.
- project5_fullcode2.py - Python script exported from Google Collab
- EasyVisa.csv – Dataset used for analysis and testing.
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
