Supervised Learning - Foundations - ReCell Project

Project Overview:

This project analyzes the used devices dataset, builds a model which will help develop a dynamic pricing strategy for used and refurbished devices, and identifies factors that significantly influence the price.

Skills:

EDA
Linear Regression
Linear Regression assumptions
Business insights and recommendations


Dataset Information:

The data contains the different attributes of used/refurbished phones and tablets. The data was collected in the year 2021. The detailed data dictionary is given below:


- brand_name: Name of manufacturing brand
- os: OS on which the device runs
- screen_size: Size of the screen in cm
- 4g: Whether 4G is available or not
- 5g: Whether 5G is available or not
- main_camera_mp: Resolution of the rear camera in megapixels
- selfie_camera_mp: Resolution of the front camera in megapixels
- int_memory: Amount of internal memory (ROM) in GB
- ram: Amount of RAM in GB
- battery: Energy capacity of the device battery in mAh
- weight: Weight of the device in grams
- release_year: Year when the device model was released
- days_used: Number of days the used/refurbished device has been used
- normalized_new_price: Normalized price of a new device of the same model in euros
- normalized_used_price: Normalized price of the used/refurbished device in euros


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

