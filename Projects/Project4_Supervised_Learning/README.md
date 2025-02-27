Supervised Learning - Foundations - ReCell Project

Project Overview:

This project analyzes the used devices dataset, builds a model which will help develop a dynamic pricing strategy for used and refurbished devices, and identifies factors that significantly influence the price.

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

PROJECT2-2.ipynb – Jupyter Notebook with analysis, visualizations, and insights.
project2.py - Python script exported from Google Collab
abtest.csv – Dataset used for analysis.
requirements.txt – List of required Python libraries.
Analysis and Findings:

Key Insights:

Users spent significantly more time on the new page than the old page.
Users who converted spent more time on either page than those who did not.
A one-tailed t-test confirmed that users spend significantly more time on the new page than the old page (μ1 > μ2).
A two-proportions z-test showed that the conversion rate for the new page is significantly higher than the old page.
A Chi-Square test revealed that language preference is independent of conversion rate.
An ANOVA test indicated that time spent on the new page does not vary significantly by language.
Business Recommendations:

Encourage users to stay longer on the website, as higher engagement correlates with a higher conversion rate.
Switch to the new website entirely, as it leads to higher engagement and a significantly higher conversion rate.
Avoid targeting users based on language preference, as conversion rates do not significantly differ by language.
Installation and Setup:

To run the analysis:

Clone the repository:
git clone https://github.com/ameliatodd2002/DS-Portfolio.git
cd Project3_Statistical_Analysis
Install dependencies:
pip install -r requirements.txt
Run the Jupyter Notebook:
jupyter notebook PROJECT2-2.ipynb
Conclusion:

This statistical analysis provided valuable insights into user behavior, website engagement, and conversion optimization. The findings help businesses understand what drives user subscriptions, validate the effectiveness of a new website design, and make data-driven decisions for improved subscriber growth.
