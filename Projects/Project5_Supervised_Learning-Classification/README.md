Supervised Learning - Classification - INN Hotels Project

Project Overview:

This project analyzes the data of INN Hotels to find which factors have a high influence on booking cancellations, builds a predictive model that can predict which booking is going to be canceled in advance, and helps in formulating profitable policies for cancellations and refunds.

Dataset Information:

The data contains the different attributes of customers' booking details. The detailed data dictionary is given below.

- Booking_ID: unique identifier of each booking
- no_of_adults: Number of adults
- no_of_children: Number of Children
- no_of_weekend_nights: Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
- no_of_week_nights: Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
- type_of_meal_plan: Type of meal plan booked by the customer:
  - Not Selected – No meal plan selected
  - Meal Plan 1 – Breakfast
  - Meal Plan 2 – Half board (breakfast and one other meal)
  - Meal Plan 3 – Full board (breakfast, lunch, and dinner)
- required_car_parking_space: Does the customer require a car parking space? (0 - No, 1- Yes)
- room_type_reserved: Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.
- lead_time: Number of days between the date of booking and the arrival date
- arrival_year: Year of arrival date
- arrival_month: Month of arrival date
- arrival_date: Date of the month
- market_segment_type: Market segment designation.
- repeated_guest: Is the customer a repeated guest? (0 - No, 1- Yes)
- no_of_previous_cancellations: Number of previous bookings that were canceled by the customer prior to the current booking
- no_of_previous_bookings_not_canceled: Number of previous bookings not canceled by the customer prior to the current booking
- avg_price_per_room: Average price per day of the reservation; prices of the rooms are dynamic. (in euros)
- no_of_special_requests: Total number of special requests made by the customer (e.g. high floor, view from the room, etc)
- booking_status: Flag indicating if the booking was canceled or not.


Files included in repository:

- PROJECT4_fullcode2-2.ipynb – Jupyter Notebook with analysis, logistic regression model, decision tree models, and insights.
- project4_fullcode2.py - Python script exported from Google Collab
- INNHotelsGroup.csv – Dataset used for analysis and testing.
- requirements.txt – List of required Python libraries.


Analysis and Findings:

Actionable Insights and Recommendations for INN Hotels:

- The final predictive model can correctly identify 85.6% of canceled bookings.
- Key predictors of cancellation:
  - Longer lead time
  - Online market segment type
  - Higher average price per room
- Patterns observed from the decision tree:
  - A booking is more likely to be canceled if:
    - Lead time ≤ 16.5 days
    - No special requests
    - Not from the online market segment
    - Weekend nights ≤ 0.5
    - Average price per room ≤ 68.5
    - Not from the offline market segment
    - Arrival date is the 30th or later


Business recommendations:

- Implement an automated system where new bookings are run through the post-pruned decision tree model. If a booking is predicted to be canceled, hotel managers should be alerted to make contingency plans.
- Consider adjusting cancellation and refund policies based on the probability of cancellation. For example, rooms predicted to be canceled could be double-booked with a flexible reservation system.
- Continue collecting data and retrain the model periodically to ensure accuracy in predicting cancellations over time.


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

This analysis identified key predictors of hotel booking cancellations, with lead time, market segment type, and average room price playing the most significant roles. The final post-pruned decision tree model, achieving an F1 score of 0.808, provides a reliable and generalizable method for predicting cancellations. By implementing an automated system to flag high-risk bookings and adopting dynamic rebooking strategies, INN Hotels can proactively minimize financial losses and optimize occupancy management.
