Supervised Learning - Classification - INN Hotels Project

Project Overview:

This project analyzes booking data from INN Hotels to identify key factors influencing cancellations, build a predictive model to anticipate cancellations, and formulate profitable cancellation and refund policies.

Dataset Information:

The data contains the different attributes of customers' booking details. The detailed data dictionary is given below.

- Booking_ID: Unique identifier of each booking
- no_of_adults: Number of adults
- no_of_children: Number of children
- no_of_weekend_nights: Number of weekend nights (Saturday or Sunday) booked
- no_of_week_nights: Number of weekday nights (Monday–Friday) booked
- type_of_meal_plan: Type of meal plan booked by the customer:
  - Not Selected – No meal plan selected
  - Meal Plan 1 – Breakfast
  - Meal Plan 2 – Half board (breakfast and one other meal)
  - Meal Plan 3 – Full board (breakfast, lunch, and dinner)
- required_car_parking_space: Whether a parking space was requested (0 - No, 1 - Yes)
- room_type_reserved: Encoded room type designation
- lead_time: Days between booking and arrival
- arrival_year: Year of arrival date
- arrival_month: Month of arrival date
- arrival_date: Date of the month
- market_segment_type: Market segment classification
- repeated_guest: Whether the guest is a repeat customer (0 - No, 1 - Yes)
- no_of_previous_cancellations: Previous cancellations by the customer
- no_of_previous_bookings_not_canceled: Previous bookings not canceled
- avg_price_per_room: Average daily room price in euros
- no_of_special_requests: Number of special requests (e.g., high floor, view)
- booking_status: Whether the booking was canceled (Target Variable)


Files included in repository:

- PROJECT4_fullcode2-2.ipynb – Jupyter Notebook with analysis, logistic regression model, decision tree models, and insights.
- project4_fullcode2.py - Python script exported from Google Collab
- INNHotelsGroup.csv – Dataset used for analysis and testing.
- requirements.txt – List of required Python libraries.


Models Tested & Performance:

This project evaluated multiple supervised learning models for predicting cancellations.

1. Logistic Regression Analysis:
- Tested a Logistic Regression Model to predict cancellations.
- Results: Moderate accuracy but weaker than decision tree models, as it struggled to capture nonlinear patterns.
2. Decision Tree Model (Baseline):
- Basic decision tree classifier tested.
- Strengths: Captured complex interactions in the data.
- Weaknesses: Overfitted the training data, reducing generalization ability.
3. Pre-Pruned Decision Tree:
- Applied pre-pruning (max depth, min samples split, min samples leaf) to prevent overfitting.
- Results: Improved generalization but still slightly over-complex.
4. Post-Pruned Decision Tree (Final Model Chosen):
- Used cost-complexity pruning (CCP) to remove unnecessary branches.
- Final Performance:
  - Accuracy: 86.9%
  - Recall: 85.6%
  - Precision: 76.6%
  - F1 Score: 0.808
  - Balanced generalization & accuracy.

Why Decision Tree (Post-Pruned) Was Selected:
- Higher interpretability than logistic regression.
- Better performance than the pre-pruned model.
- More generalizable than the unpruned decision tree.


Analysis and Findings:

Actionable Insights and Recommendations for INN Hotels:

- The final post-pruned decision tree model achieved an F1 score of 0.808, making it the most reliable and generalizable predictive model.
- The model correctly identifies 85.6% of canceled bookings.
- Top predictors of cancellation:
  - Longer lead time
  - Market segment type (Online bookings more likely to cancel)
  - Higher average room price
- Patterns Observed from the Decision Tree:
  - A booking is more likely to be canceled if:
  - Lead time ≤ 16.5 days
  - No special requests
  - Not from the online market segment
  - Weekend nights ≤ 0.5
  - Average price per room ≤ 68.5
  - Not from the offline market segment
  - Arrival date is the 30th or later

  
Business Recommendations:

- Implement an automated flagging system where each booking is analyzed using the decision tree model. High-risk bookings can trigger alerts for hotel managers.
- Adjust cancellation and refund policies based on predicted likelihood of cancellation. For example, rooms at high risk of cancellation could be double-booked using a flexible reservation system.
- Continue collecting and analyzing booking data to keep the model updated and improve predictive accuracy over time.


Installation and Setup:

To run the analysis:

- Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project5_Supervised_Learning-Classification
- Install dependencies:
- pip install -r requirements.txt
- Run the Jupyter Notebook:
- jupyter notebook PROJECT4_fullcode2-2.ipynb


Conclusion:

This analysis identified key predictors of hotel booking cancellations, with lead time, market segment type, and average room price playing the most significant roles. The final post-pruned decision tree model, with an F1 score of 0.808, offers a reliable way to predict cancellations. By implementing an automated system to flag high-risk bookings and adopting dynamic rebooking strategies, INN Hotels can proactively minimize financial losses and optimize occupancy management.
