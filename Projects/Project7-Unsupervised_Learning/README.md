Unsupervised Learning - Model Tuning - Trade&Ahead Project

Project Overview:

"ReneWind" is a company focused on enhancing wind energy production by leveraging machine learning. This project aimed to develop and fine-tune classification models to predict generator failures in wind turbines using sensor data. By identifying failures early, the company can reduce maintenance costs and optimize resource allocation.

Skills:

- Exploratory Data Analysis
- Data Preprocessing
- Class Imbalance Handling (Upsampling & Downsampling)
- Regularization & Hyperparameter Tuning
- Model Evaluation & Performance Optimization
  

Dataset Information:

The dataset consists of sensor readings collected from wind turbine generators. The data has been preprocessed for analysis.

Train.csv - To be used for training and tuning of models.
Test.csv - To be used only for testing the performance of the final best model.
Both the datasets consist of 40 predictor variables and 1 target variable


Files included in repository:

- Todd_Project_6_FullCode-2.ipynb – Jupyter Notebook with full analysis, model training, and tuning.
- todd_project6_fullcode.py – Python script exported from Google Colab.
- Train.csv – Training dataset.
- Test.csv – Testing dataset.
- requirements.txt – List of required Python libraries.


Models Tested & Performance:

This project tested multiple supervised learning models for predicting failures:

1. Bagging Classifier
2. Random Forest Classifier
3. Gradient Boosting Classifier
4. AdaBoost Classifier
5. XGBoost Classifier
6. Decision Tree Classifier


Model Performance & Findings:

- Primary metric: Recall Score (Identifying failed machines is the priority).
- Best Model: Tuned XGBoost with Oversampled Data – Achieved 99% accuracy, 85% recall, 96% precision, and 90% F1-score.
- Key Observations:
  - Random Forest and Bagging Classifier performed well with balanced recall scores and minimal overfitting.
  - Gradient Boosting (GBM) had slightly lower recall but good generalizability.
  - AdaBoost underperformed in recall.
  - Decision Tree was prone to overfitting and had lower agreement between training and validation sets.
  - XGBoost outperformed all models even before tuning and was further improved through hyperparameter tuning and oversampling.
 
- After regularization, I decided the XGBoost model with oversampled data was the best model, and the one we would proceed with. I picked this model because all the models suffer from overfitting, but the tuned XGBoost model with oversampled data has the highest score.
  

Analysis and Findings:

Actionable Insights/Business Recommendations:

- The XGBoost model provides a highly accurate failure prediction system using the company's sensor data. This model uses the 40 predictors provided by the company, and is able to identify when there will be a machine failure with about 99% accuracy, 85% recall, 96% precision, and 90% F1.
- Implementation Strategy:
  - Integrate the model into ReneWind's maintenance pipeline.
  - Continuously feed real-time sensor data into the model.
  - Flag high-risk turbines for proactive maintenance.
- Cost Savings:
  - Avoid unnecessary preventive maintenance on turbines unlikely to fail.
  - Reduce downtime and extend the lifespan of turbines.
  - Optimize resource allocation for repairs.


Installation and Setup:

To run the analysis:

- Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project6_Unsupervised_Learning-Model_Tuning
- Install dependencies:
- pip install -r requirements.txt
- Run the Jupyter Notebook:
- jupyter notebook Todd_Project_6_FullCode-2.ipynb


Conclusion:

This project successfully developed and tuned a classification model for predictive maintenance in wind energy. The XGBoost model with oversampling demonstrated the highest performance, making it a valuable tool for ReneWind to minimize costs and improve operational efficiency.
