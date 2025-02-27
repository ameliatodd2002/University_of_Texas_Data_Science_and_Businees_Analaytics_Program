Automated Census Geocoding for Suicide Prevention Research

Project Overview:

This project automates the interaction with the Census Geocoder API to process participant address data efficiently. It was developed for the Suicide Prevention Research Team at Louisiana State University to replace a manual process that would have taken weeks with an overnight, unsupervised script.

The program takes a CSV file containing 249,975 participant records from Texas Children's Hospital, including ID, address, city, state, and zip code. Since the Census Geocoder can only process batches of 9,999 at a time, this script automatically splits the data into batches, submits them sequentially, and handles errors to prevent data loss and unnecessary restarts.

The output file includes the address, census tract, state code, county code, and block number. The program processes the data in a structured manner, ensuring accuracy and efficiency while mitigating API crashes.


Dataset Information:

- Original dataset (input):
- ID
- Address
- City
- State
- Zip Code

Processed dataset (output):
- Address
- Census Tract Code
- State Code
- County Code
- Block Number


Files in the Repository:

- SPR.py – Python script for processing data
- data.txt – Description of the dataset
- requirements.txt – List of required Python libraries


Context & Additional Data Integration:

- Beyond this program, further data integration and translation were performed to include:
  - Houston Police Records
  - Houston State of Health Data
  - Suicide Ideation Rates (independent variable)
- With this expanded dataset, I conducted an in-depth statistical analysis in SPSS to identify the strongest predictors of high suicide ideation rates at the census-tract level.

Statistical Findings:
- Using only census tracts with at least 25 surveys (309 tracts total), the data followed a normal distribution:
  - Range: 3% to 48% (45%)
  - Mean: 21.36
  - SD: 8.56
  - Skew: 0.56
  - Kurtosis: 0.25
- A stricter analysis using minimum 50 surveys per tract (63 tracts total) also showed a normal distribution:
  - Range: 10% to 33% (23%)
  - Mean: 20.39
  - SD: 5.26
  - Skew: 0.58
  - Kurtosis: -0.11


Installation & Setup:

To run the program, follow these steps:

Clone the repository:
- git clone https://github.com/ameliatodd2002/DS-Portfolio.git
- cd Project1_Suicide_Prevention_Research
- Install dependencies:
- pip install -r requirements.txt
- Open and run the script (SPR.py).


Conclusion:

- The normal distribution of suicidal behavior across Houston's census tracts enables statistical modeling at a social-ecological level, helping identify high-risk areas.
- This enables us to pinpoint census tracts with higher or lower rates of suicidal behavior.
- Understanding the suicidal behavior distribution can inform the development and targeting of intervention strategies, and it provides a basis for public health planning and resource allocation.
