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

- PROJECT3-2.ipynb – Jupyter Notebook with analysis, regression model, and insights.
- project3.py - Python script exported from Google Collab
- used_device_data.csv – Dataset used for analysis and testing.
- requirements.txt – List of required Python libraries.


Analysis and Findings:

Key Insights/Business Recommendations:

- Based on this model, we are able to predict the price of a used device through this equation: normalized used price = -0.41727730370151694 + 0.0196548933373735 * ( main_camera_mp ) + 0.013283854744645426 * ( selfie_camera_mp ) + 0.023546993773401727 * ( ram ) + 0.0015971302387318648 * ( weight ) + 1.2082111403732825 * ( normalized_new_price ) + -0.03858244293186329 * ( years_out ) + -0.04183447812024251 * ( brand_name_LG ) + -0.036832609866963295 * ( brand_name_Others ) + -0.04721591042782653 * ( brand_name_Samsung ) + -0.06273438914126221 * ( brand_name_Sony ) + 0.07454635421813148 * ( brand_name_Xiaomi ) + -0.07154813472250998 * ( normalized_new_price_sq )
- We can explain about 84.4% of the variance in the price of used devices through these variables: main camera resolution, selfie camera resolution, ram, weight, normalized new price, the number of years the device has been out, whether it is an LG device, a device that does not fall into one of the main brand categories, a Samsung device, a Sony device, or a Xiaomi device.
- Based on these observations, I would advice the startup ReCell to use this equation to figure out which combinations of variables produce th highest resell price, and aim towards selling those devices on their site, as I assume they get a percentage of the profits. So, by using this model they can determine which kinds of devices would produce the highest profits for their company.
- Also, even if ReCell decides to sell all deices, regardless of the predicted price, being able to use this model to accurately predict the price that a customer is willing to buy it would be extremely beneficial to the company. It would bring customers in because they would be compelled by the prices on the site since they would be pricing it based soley on the components and data of what customers are willing to buy each device for.
- I would also reccommend that ReCell does not focus too much on individual characteristics of the device alone, as we see in the data that the price can vary drastically for each device depending on the combination of each type of component, not just one component alone. For example, we see that just because a device is heavy does not mean the price or value of the device decreases because this could indicate that the battery size is actually much larger, which is an attractive feature in the device, and could make the price increase significantly. This is why paying attention to the relationships between each variable, and accounting for collinearity in the data is so important.


Installation and Setup:

To run the analysis:

- Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project4_Supervised_Learning
- Install dependencies:
- pip install -r requirements.txt
- Run the Jupyter Notebook:
- jupyter notebook PROJECT3-2.ipynb


Conclusion:

The final model effectively predicts used smartphone prices with high accuracy, making it useful for pricing strategies in the refurbished device market. Further improvements could include testing non-linear models or adding more market-driven features.
