# Bike Sharing Data Analysis
Data Science Institute - Cohort 5 - Team Project
# Overview
As part of our Final Team Project for the Data Science Software Foundations certificate, we have selected the [Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) from the given datasets. This dataset contains the hourly and daily count of rental bikes between years 2011 and 2012 in Capital bikeshare system with the corresponding weather and seasonal information, making it ideal for exploring trends, patterns, and predictive modeling.

![bike rentals](https://github.com/user-attachments/assets/20dd50eb-0e58-4003-9690-868e25c6d80b)
The scatterplot with the regression lines for both years demonstrates once again the difference between the correlation for 2011 and 2012 years. The slope of the regression lines shows that the influence of the temperature for 2011 is more significant than for 2012.
![blob](https://github.com/user-attachments/assets/91e822da-d5de-49c5-96a1-68049eed32aa)


# Business Case
Our target audience are bike sharing companies looking to expand into other cities with a similar population size and seasonal trends as Washington D.C. Referring to the bike sharing usage patterns in Washington D.C. will help make an informed decision about bike demand in other cities. Our goal is to build a predictive model to forecast bike demand based on factors such as weather, seasons, holidays etc. 

# Team Members:
* [Rachel Fernandes](https://github.com/rachfern)
* [Jingkenh Loh](https://github.com/jkenloh)
* [Daniel Troniak](https://github.com/troniak)
* [Saleha Ejaz Qureshi](https://github.com/saleha-12)
* [Efren Tumialan Tenorio](https://github.com/efrenltt24)

# Project Overview
* Requirements 
   - Incl. libraries used in Python
* Exploratory Data Analysis
* Understanding the Raw Data
* Data Cleaning and Handling Missing Values
* Data Analysis using Python -- Linear Regression
* Data Visualization on Tableau (TBD – contingent on progress and time available)
* Risks/Unknown 
* Conclusion
* Team Videos

# Exploratory Data Analysis
In this Exploratory Data Analysis (EDA), we cleaned and prepared bike-sharing datasets by removing irrelevant columns and handling missing values. Duplicate rows were dropped, and outliers in the rental count (cnt) were filtered using the Interquartile Range (IQR) method. We combined the cleaned hourly and daily data into a single DataFrame for further analysis. The final dataset was saved into a new CSV file for future use. This process ensured that the data was ready for accurate and reliable analysis.

# Data Cleaning and Handling Missing Values
There do not seem to be any missing values, and the data do not seem to require extensive cleaning. Our team will be conducting a more thorough exploration of the data within the next day or so and update this section.

# Creating a Regression Model
categorical features (such as season, weather type, and weekday) are identified, while the numerical features (like temperature, humidity, and wind speed) are also noted. Outlier detection is performed using the Interquartile Range (IQR) method to identify values that are unusually high or low compared to the typical range in the data. If a value falls outside the range of [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR], it's considered an outlier. The categorical features are then one-hot encoded to transform them into a numerical format, creating binary columns for each category, while numerical features are scaled to ensure all values have the same scale (mean = 0, standard deviation = 1), enhancing the model's performance. Finally, the model's performance is evaluated using Mean Squared Error (MSE), which calculates the average squared difference between actual and predicted values (with lower values indicating better performance), and the R² score, which measures how well the model's predictions align with the actual data, with a score closer to 1 indicating stronger predictions.

# Model Optimization through Hyperparameter Tuning
After creating the initial Random Forest model, we implemented hyperparameter tuning using GridSearchCV with 5-fold cross-validation to optimize the model's performance. The grid search explored different combinations of:

* Number of trees (n_estimators): [100, 200, 300]
* Maximum tree depth (max_depth): [10, 20, 30, None]
* Minimum samples for split (min_samples_split): [2, 5, 10]
* Minimum samples per leaf (min_samples_leaf): [1, 2, 4]

The best performing model configuration was found to be:
* max_depth: None
* min_samples_leaf: 1
* min_samples_split: 5
* n_estimators: 300

This optimized model achieved improved performance metrics on the test set:
* Mean Squared Error (MSE): 2491.49
* Mean Absolute Error (MAE): 30.13
* R² Score: 0.884

The feature importance analysis revealed which factors had the strongest influence on bike rental predictions, helping to identify the key drivers of bike sharing demand. This information is valuable for bike sharing companies looking to expand into new markets, as it highlights which environmental and temporal factors most strongly affect ridership.
