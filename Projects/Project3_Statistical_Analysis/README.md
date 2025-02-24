Business Statistics - E-news Express Project

Project Overview:

This project used statistical analysis, a/b testing, and visualization to decide whether the new landing page of an online news portal (E-news Express) is effective enough to gather new subscribers or not. The simulated dataset has certain important metrics such as converted status and time spent on the page that will help to conclude the effectiveness of the new landing page. Apart from that, the dependence of conversion on the preferred language will also be analyzed in this project.

Dataset Information:

The dataset contains records of each user that interacted with either the new or old website. Key columns include:

landing_page - either the new or old page, time_spent_on_the_page - how long each user was on the page, converted - whether or not the user converted from their given website to the other website, language_preferred - the language the website was in

Files in the Repository:

EDA_food_aggregator.ipynb – Jupyter Notebook containing all analyses, visualizations, and insights foodhub_order.csv – The dataset used for this analysis requirements.txt – List of required Python libraries

Analysis & Findings:

Through detailed EDA, I identified trends and insights related to customer behavior, restaurant efficiency, and pricing strategies. Some key observations include:

Restaurant ratings did not significantly vary based on food preparation or delivery time.
Higher-rated restaurants were not always the most frequently ordered from, suggesting factors beyond ratings influence customer choices.
Delivery time distribution revealed outliers, indicating occasional inefficiencies in the fulfillment process.
Order cost analysis showed that certain cuisine types had consistently higher average order values.
Rather than a single major finding, this project uncovered multiple small yet meaningful insights that help understand user behavior and service performance.
Key Insights & Recommendations

Since ratings are not strongly influenced by delivery speed, restaurants could introduce premium pricing for faster delivery options without negatively impacting customer satisfaction.
Frequent order trends suggest that offering personalized promotions on high-demand cuisine types could increase sales.
Outliers in delivery time indicate potential bottlenecks in fulfillment. Addressing these inconsistencies could improve customer experience and optimize restaurant operations.
Installation & Setup:

To run the analysis, follow these steps:

Clone the repository: git clone https://github.com/ameliatodd2002/DS-Portfolio.git cd Project2_EDA Install dependencies: pip install -r requirements.txt Open and run the Jupyter Notebook (PROJECT1-4.ipynb).

Conclusion:

This EDA provided valuable insights into customer ordering behavior, restaurant performance, and potential areas for improvement. The findings can help businesses refine their pricing, promotions, and logistics strategies for better efficiency and customer satisfaction.
