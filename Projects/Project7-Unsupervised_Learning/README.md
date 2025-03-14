Unsupervised Learning - Trade&Ahead Project

Project Overview:

This project analyzes stock data, groups stocks based on financial attributes, and provides insights into the characteristics of each group using unsupervised learning techniques.

Skills:

- Exploratory Data Analysis
- K-Means Clustering
- Hierarchical Clustering
- Cluster Profiling
  

Dataset Information:

The dataset includes stock prices and financial indicators for companies listed on the New York Stock Exchange (NYSE).

Data Dictionary:
- Ticker Symbol: An abbreviation used to uniquely identify publicly traded shares of a particular stock on a particular stock market
- Company: Name of the company
- GICS Sector: The specific economic sector assigned to a company by the Global Industry Classification Standard (GICS) that best defines its business operations
- GICS Sub Industry: The specific sub-industry group assigned to a company by the Global Industry Classification Standard (GICS) that best defines its business operations
- Current Price: Current stock price in dollars
- Price Change: Percentage change in the stock price in 13 weeks
- Volatility: Standard deviation of the stock price over the past 13 weeks
- ROE: A measure of financial performance calculated by dividing net income by shareholders' equity (shareholders' equity is equal to a company's assets minus its debt)
- Cash Ratio: The ratio of a company's total reserves of cash and cash equivalents to its total current liabilities
- Net Cash Flow: The difference between a company's cash inflows and outflows (in dollars)
- Net Income: Revenues minus expenses, interest, and taxes (in dollars)
- Earnings Per Share: Company's net profit divided by the number of common shares it has outstanding (in dollars)
- Estimated Shares Outstanding: Company's stock currently held by all its shareholders
- P/E Ratio: Ratio of the company's current stock price to the earnings per share
- P/B Ratio: Ratio of the company's stock price per share by its book value per share (book value of a company is the net difference between that company's total assets and total liabilities)


Files included in repository:

- PROJECT_stock_Todd-3.ipynb – Jupyter Notebook with full analysis, model fitting, and insights.
- project_stock_todd.py – Python script exported from Google Colab.
- stock_data.csv - CSV file including all data from Trade&Ahead
- requirements.txt – List of required Python libraries.


Models Tested & Performance:

This project created and compared two clustering techniques:

1. K-Means Clustering
2. Hierarchical Clustering Model


Comparing Model Performance & Findings:

- Execution Time:
  - K-Means (3 clusters) – 0.0503 seconds
  - Hierarchical Clustering (4 clusters) – 0.0170 seconds (Faster)
- Cluster Quality (Silhouette Score):
  - K-Means – 0.8070
  - Hierarchical – 0.8042 (K-Means produced slightly more distinct clusters)
- Cluster Comparison:
  - K-Means grouped stocks into 3 clusters, while Hierarchical Clustering used 4 clusters.
  - The two models produced different groupings, making direct comparison difficult.
  

Analysis and Findings:

Actionable Insights/Business Recommendations:

- K-Means Clustering (3 clusters) provides a streamlined way for Trade&Ahead to categorize stocks and offer investment recommendations.
- Hierarchical Clustering (4 clusters) provides a more granular approach to segmenting stocks.
- The choice of clustering method depends on the level of separation required. Providing both models allows Trade&Ahead to use them separately or together for deeper insights.

Installation and Setup:

To run the analysis:

- Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project7-Unsupervised_Learning
- Install dependencies:
- pip install -r requirements.txt
- Run the Jupyter Notebook:
- jupyter notebook PROJECT_stock_Todd-3.ipynb


Conclusion:

This project successfully applied unsupervised learning to group stocks based on financial attributes. The results can help Trade&Ahead provide better stock recommendations by leveraging different clustering approaches.
