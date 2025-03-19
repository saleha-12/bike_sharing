# Bike Sharing Data Analysis
Data Science Institute - Cohort 5 - Team Project
# Overview
As part of our Final Team Project for the Data Science Software Foundations certificate, we have selected the [Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) from the given datasets. This dataset contains the hourly and daily count of rental bikes system between years 2011 and 2012 in Capital bikeshare system with the corresponding weather and seasonal information, making it ideal for exploring trends, patterns, and predictive modeling.

<img src="https://github.com/user-attachments/assets/20dd50eb-0e58-4003-9690-868e25c6d80b" alt="bike rentals" width="1000"/>
<p align="center">The scatterplot with the regression lines for both years demonstrates the difference between the correlation for 2011 and 2012 years. The slope of the regression lines shows that the influence of the temperature for 2011 is more significant than for 2012.</p>
<p align="center">
  <a href="https://rstudio-pubs-static.s3.amazonaws.com/158595_1f520fd8d8e34a5ab3a127376f2f6169.html">Image Source</a>
</p>

* **Dataset Size**: 17389 samples
* **Features**: 13 numerical features
* #### Attribute Information:
* `instant`: record index
* `dteday` : date
* `season` : season (1:springer, 2:summer, 3:fall, 4:winter)
* `yr` : year (0: 2011, 1:2012)
* `mnth` : month ( 1 to 12)
* `hr` : hour (0 to 23)
* `holiday` : weather day is holiday or not (extracted from [Web Link])
* `weekday` : day of the week
* `workingday` : if day is neither weekend nor holiday is 1, otherwise is 0.
* `weathersit` :
   * 1: Clear, Few clouds, Partly cloudy, Partly cloudy
   * 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
   * 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
   * 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
* `temp` : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
* `atemp`: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
* `hum` : Normalized humidity. The values are divided to 100 (max)
* `windspeed` : Normalized wind speed. The values are divided to 67 (max)
* `casual` : count of casual users
* `registered` : count of registered users
* `cnt` : count of total rental bikes including both casual and registered
  
# Business Case
Our target audience are bike sharing companies looking to expand into other cities with a similar population size and seasonal trends as Washington D.C. Referring to the bike sharing usage patterns in Washington D.C. will help make an informed decision about bike demand in other cities. Our goal is to build a predictive model to forecast bike demand based on factors such as weather, seasons, holidays etc. 

# Project Workflow
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
## 1. Data Cleaning and Handling Missing Values
* We first removed columns in the datasset that were not relevant to the analysis. 
* We checked the dataset for missing values and removed them.
* We then used the Interquartile Range (IQR) method to remove data points outside of the acceptable range to avoid extreme values skewing the analysis.
* We also checked the dataset for duplicate entries to ensure that no duplicates existed.
* Finally, we exported the cleaned dataset for further analysis and modeling.

## 2. Exploratory Data Analysis
* The first step in our EDA was to load the the uploaded dataset from GitHub and check the first few rows to make sure the dataset reflected the changes from the data cleaning.
* We then checked the shape of our dataset to confirm the number of rows and columns.
* We checked the column data types to make sure each column was the data type we needed to prepare it for the analysis. What we found here was that the "date" column was a string, which would need to be converted to datetime if we needed to do any calculations using dates. Columns for "temperature", "humidity", and "windspeed" were data type float, and the rest of the columns were integers, which were the data types we needed.
* We then checked the summary stats using .describe() method. Some observations here: column "weekday" has integers between 0-6, so the week starts at integer '0'. Column "weathersit" has no rows that are '4', which means there was no heavy rain throughout the entire time period of this dataset. Column "count" had a minimum of 22 and maximum of 8714, meaning there was significant fluctuation in total rental bikes throughout the time period.
* We then checked the distribution of each feature using histograms. An observation here is that the most common weather type in the "weathersit" column was '1', followed by '2' with roughly half of the count, with very few '3' and no '4'.
* We used a boxplot to confirm if there were any outliers and to make sure all the datapoints made sense.
* Finally, we checked the feature correlations using a heatmap, where we could see that there were a number of correlated features with "count", especially with season, year, weathersit, temperature, adn windspeed, which meant these affected the number of rentals.
  
* Cleaned and prepared bike-sharing datasets by removing irrelevant columns and handling missing values
* Duplicate rows were dropped, and outliers in the rental count (cnt) were filtered using the Interquartile Range (IQR) method.
* Combined the cleaned hourly and daily data into a single DataFrame for further analysis. The final dataset was saved into a new CSV file for future use. This process ensured that the data was ready for accurate and reliable analysis.

## 3. Creating a Regression Model
* Categorical features (such as season, weather type, and weekday) are identified, while the numerical features (like temperature, humidity, and wind speed) are also noted.
* Outlier detection is performed using the Interquartile Range (IQR) method to identify values that are unusually high or low compared to the typical range in the data. If a value falls outside the range of [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR], it's considered an outlier.
* The categorical features are then one-hot encoded to transform them into a numerical format, creating binary columns for each category, while numerical features are scaled to ensure all values have the same scale (mean = 0, standard deviation = 1), enhancing the model's performance.
* Finally, the model's performance is evaluated using Mean Squared Error (MSE), which calculates the average squared difference between actual and predicted values (with lower values indicating better performance), and the R² score, which measures how well the model's predictions align with the actual data, with a score closer to 1 indicating stronger predictions.

## 4. Model Building
#### Regression Models:
* Linear Regression: A baseline model to establish a performance benchmark.
* Decision Tree Regressor: A non-linear model to capture complex relationships.
* Random Forest Regressor: An ensemble model to improve accuracy and reduce overfitting.
#### Evaluation Metrics:
* Mean Squared Error (MSE): Measures the average squared difference between predicted and actual values.
* Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual values.
* R² Score: Measures the proportion of variance in the target variable explained by the model.
## 5. Model Evaluation
#### Linear Regression:
* Mean Squared Error (MSE): 7595.54
* Mean Absolute Error (MAE): 65.31
* R² Score: 0.67
#### Interpretation: 
The model explains 67% of the variance in bike rentals but has relatively high errors, indicating it may not capture non-linear relationships well.
#### Decision Tree Regressor:
* Mean Squared Error (MSE):  5170.95
* Mean Absolute Error (MAE):  43,37
* R² Score: 0.78
#### Interpretation:
The model performs better than Linear Regression, capturing more complex patterns, but may still overfit.
##3 Random Forest Regressor:
* Mean Squared Error (MSE):  2664.21
* Mean Absolute Error (MAE):  32.66
* R² Score: 0.88
* Interpretation: The best-performing model, explaining 88% of the variance with the lowest errors. It generalizes well to unseen data.

#### Overall Comparison
![Comparing our 3 models](https://github.com/user-attachments/assets/f5557539-3360-4c70-97fa-20bf9332dbb7)
<p align="center">visual comparison of the performance of the Linear Regression, Decision Tree Regressor, and Random Forest Regressor models.</p>

In our analysis, we tested three different regression models to predict bike rentals: Linear Regression, Decision Tree Regressor, and Random Forest Regressor. Each model was evaluated based on its accuracy and error rates.

Linear Regression assumes a simple, straight-line relationship between the input features and bike rentals. However, this approach struggles to capture complex patterns in the data. The model had a Mean Squared Error (MSE) of 7595.54 and a Mean Absolute Error (MAE) of 65.31. MAE indicates that, on average, the model’s predictions were off by 62.64 rental bikes. A smaller MAE signifies better accuracy. The R² score was 0.67, meaning the model could explain only 67% of the variation in bike rentals. While this is a decent result, it shows that linear regression lacks the flexibility to accurately model the data.

Next, we used a Decision Tree Regressor, which can better capture non-linear relationships in the dataset. This model significantly improved accuracy, reducing the MSE to 5170.95 and MAE to 43.37. MAE means that, on average, the model’s predictions were off by 43.37 rental bikes, an improvement over linear regression. The R² score increased to 0.780, meaning it explained 78% of the variation in bike rentals. However, decision trees have a tendency to overfit, meaning they might perform well on training data but may not generalize well to new data.

Finally, we used a Random Forest Regressor, which combines multiple decision trees to improve stability and accuracy. This model performed the best, with an MSE of 2664.21 and an MAE of 32.66. This MAE shows that, on average, the model’s predictions were off by 32.66 rental bikes, making it the most accurate among the three models. The R² score was 0.884, meaning it could explain 88.4% of the variation in bike rentals. Because Random Forest averages multiple trees, it reduces overfitting and provides more reliable predictions.

Random Forest Regression:
* Uses multiple decision trees and averages their predictions.
* Each tree works by splitting the data at different points to create regions with similar target values.
* The final prediction is the average output of all trees.
* Captures non-linear relationships (bike rentals are influenced by many non-linear factors).
* Less sensitive to outliers since multiple trees reduce their impact.

#### Conclusion:
Random Forest is the best-performing model, with the lowest MSE, lowest MAE, and highest R² score. It’s ensemble nature (combining multiple decision trees) allows it to reduce overfitting and capture complex, non-linear relationships in the data.
Decision Tree performs better than Linear Regression, likely because it can model non-linear relationships, but is still outperformed by Random Forest. It is likely overfitting to some extent or not capturing all the complexity in the data.
Linear Regression is underperforming, likely because the relationship between the features and the target variable is not purely linear. It may not be capturing complex patterns in the data.

## Limitations and Considerations
While the Random Forest model performs exceptionally well, there are a few considerations:
#### Interpretability:
Random Forest models are less interpretable than Linear Regression or single Decision Trees. While you can extract feature importance, understanding the exact decision-making process is challenging due to the ensemble nature of the model.
#### Computational Cost:
Training a Random Forest can be computationally expensive, especially with a large number of trees (n_estimators) or deep trees (max_depth). However, this is often a worthwhile trade-off for the improved accuracy.
#### Overfitting:
While Random Forest is generally robust to overfitting, it can still overfit if not properly tuned (e.g., with too many trees or insufficient min_samples_split). Regular hyperparameter tuning is recommended.

## 6. Model Optimization through Hyperparameter Tuning
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

## Risks and Limitations

Our analysis, while comprehensive, faces several important limitations. The dataset exhibits a notable data collection gap, with approximately 140 hours missing from the hourly dataset (17,380 records versus the expected 17,520 hours over two years). This missing data could potentially introduce bias if these gaps correspond to specific events or conditions that affected bike rentals. Additionally, the dataset is limited to Washington D.C.'s specific urban environment and climate patterns, which may not generalize well to cities with significantly different characteristics. The model's predictions might also be less reliable for extreme weather conditions that are underrepresented in the training data. Furthermore, the analysis doesn't account for long-term changes in urban infrastructure, population demographics, or competing transportation options that could influence bike-sharing demand. While our Random Forest model shows strong performance, its "black box" nature makes it difficult to explain specific predictions to stakeholders, which could affect its adoption in decision-making processes where transparency is crucial. These predictions should be considered alongside all these limitations when making business decisions about expanding into new markets.

# Team Members:
* [Rachel Fernandes](https://github.com/rachfern)
* [Jingkenh Loh](https://github.com/jkenloh)
* [Daniel Troniak](https://github.com/troniak)
* [Saleha Ejaz Qureshi](https://github.com/saleha-12)
* [Efren Tumialan Tenorio](https://github.com/efrenltt24)
