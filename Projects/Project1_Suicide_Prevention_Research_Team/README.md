Suicide Prevention Research Team Census Geocoder Interaction Program

Project Overview:

This project interacts with censusgeocoder as an API. I created this project for the Sucide Prevention Research Team at Lousiana state University in order to automate a task that would have taken weeks, and turned it into an overnight process that the computer could handle unsupervised. This project takes a csv file which includes data from the Texas Children's Hospital. The csv has columns 


Dataset Information:

The dataset contains transactional records from food orders placed through an aggregator app. Key columns include:

- Order ID – Unique identifier for each order
- Restaurant Name – Name of the restaurant fulfilling the order
- Cuisine Type – Type of cuisine offered
- Ratings – Customer ratings for each order
- Delivery Time – Time taken for the order to be delivered
- Order Cost – Total amount paid for the order
- Additional Features – Other relevant details about the orders


Files in the Repository:

- PROJECT1-4.ipynb – Jupyter Notebook containing all analyses, visualizations, and insights
- project1-2.py - Python script exported from Google Collab
- foodhub_order.csv – The dataset used for this analysis
- requirements.txt – List of required Python libraries


Analysis & Findings:

Through detailed EDA, I identified trends and insights related to customer behavior, restaurant efficiency, and pricing strategies. Some key observations include:

- Restaurant ratings did not significantly vary based on food preparation or delivery time.
- Higher-rated restaurants were not always the most frequently ordered from, suggesting factors beyond ratings influence customer choices.
- Delivery time distribution revealed outliers, indicating occasional inefficiencies in the fulfillment process.
- Order cost analysis showed that certain cuisine types had consistently higher average order values.
- Rather than a single major finding, this project uncovered multiple small yet meaningful insights that help understand user behavior and service performance.

Key Insights & Recommendations

- Since ratings are not strongly influenced by delivery speed, restaurants could introduce premium pricing for faster delivery options without negatively impacting customer satisfaction.
- Frequent order trends suggest that offering personalized promotions on high-demand cuisine types could increase sales.
- Outliers in delivery time indicate potential bottlenecks in fulfillment. Addressing these inconsistencies could improve customer experience and optimize restaurant operations.


Installation & Setup:

To run the analysis, follow these steps:

Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project2_EDA
- Install dependencies:
- pip install -r requirements.txt
- Open and run the Jupyter Notebook (PROJECT1-4.ipynb).


Conclusion:

This EDA provided valuable insights into customer ordering behavior, restaurant performance, and potential areas for improvement. The findings can help businesses refine their pricing, promotions, and logistics strategies for better efficiency and customer satisfaction.
