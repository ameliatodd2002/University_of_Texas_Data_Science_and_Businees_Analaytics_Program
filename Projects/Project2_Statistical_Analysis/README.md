Business Statistics - E-news Express Project

Project Overview:

This project applies statistical analysis, A/B testing, and data visualization to evaluate whether the new landing page of an online news portal (E-news Express) is more effective in acquiring new subscribers. Key metrics analyzed include time spent on the page, conversion rate, and language preference.


Skills:
- Hypothesis Testing
- A/B testing
- Data Visualization
- Statistical Inference


Dataset Information:

The dataset contains user interaction records with either the new or old landing page. Key columns:

- landing_page: Indicates whether the user visited the new or old page.
- time_spent_on_the_page: Duration spent on the page (in seconds).
- converted: Whether the user subscribed (1) or not (0).
- language_preferred: The language version of the page.


Files in the Repository:

- PROJECT2-2.ipynb – Jupyter Notebook with analysis, visualizations, and insights.
- project2.py - Python script exported from Google Collab
- abtest.csv – Dataset used for analysis.
- requirements.txt – List of required Python libraries.


Analysis and Findings:

Key Insights:
- Users spent significantly more time on the new page than the old page.
- Users who converted spent more time on either page than those who did not.
- A one-tailed t-test confirmed that users spend significantly more time on the new page than the old page (μ1 > μ2).
- A two-proportions z-test showed that the conversion rate for the new page is significantly higher than the old page.
- A Chi-Square test revealed that language preference is independent of conversion rate.
- An ANOVA test indicated that time spent on the new page does not vary significantly by language.

Business Recommendations:

- Encourage users to stay longer on the website, as higher engagement correlates with a higher conversion rate.
- Switch to the new website entirely, as it leads to higher engagement and a significantly higher conversion rate.
- Avoid targeting users based on language preference, as conversion rates do not significantly differ by language.


Installation and Setup:

To run the analysis:

- Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git  
- cd Project3_Statistical_Analysis  
- Install dependencies:
- pip install -r requirements.txt  
- Run the Jupyter Notebook:
- jupyter notebook PROJECT2-2.ipynb  


Conclusion:

This statistical analysis provided valuable insights into user behavior, website engagement, and conversion optimization. The findings help businesses understand what drives user subscriptions, validate the effectiveness of a new website design, and make data-driven decisions for improved subscriber growth.
