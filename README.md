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
* **Attribute** Information:
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
   - Python libraries used for data manipulation, analysis, and visualization:
     * pandas
     * numpy
     * matplotlib.pyplot
     * seaborn
   - Python libraries used for machine leraning and model development:
     * sklearn.model_selection
       * train_test_split
       * GridSearchCV
     * sklearn.preprocessing
       * OneHotEncoder
       * StandardScaler
     * sklearn.linear_model
       * LinearRegression
     * sklearn.tree
       * DecisionTreeRegressor
     * sklearn.ensemble
       * RandomForestRegressor
     * sklearn.metrics
       * mean_squared_error, mean_absolute_error, r2_score
       * make_scorer
* Data Cleaning and Handling Missing Values
* Exploratory Data Analysis (EDA)
* Creating a Regression Model
* Model Building
  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor
* Model Evaluation
  * Mean Squared Error (MSE)
  * Mean Absolute Error (MAE)
  * R² Score
* Model Optimization
* Risks and Limitations
* Revisions and Adjustments
* Conclusion
* Team Videos
  
## 1. Data Cleaning and Handling Missing Values
* We first removed columns in the datasset that were not relevant to the analysis. 
* We checked the dataset for missing values and removed them.
* We then used the Interquartile Range (IQR) method to remove data points outside of the acceptable range to avoid extreme values skewing the analysis.
* We also checked the dataset for duplicate entries to ensure that no duplicates existed.
* Finally, we exported the cleaned dataset for further analysis and modeling.

## 2. Exploratory Data Analysis
The first step in our EDA was to load the uploaded dataset from GitHub and inspect the first few rows to ensure that the dataset reflected the changes made from the data cleaning process.

Next, we checked the shape of the dataset to confirm the number of rows and columns. We also examined the column data types to ensure they were correctly formatted for analysis. We found that the "date" column was stored as a string, which would need to be converted to a datetime format if any calculations using dates were needed. The "temperature", "humidity", and "windspeed" columns were correctly set as floats, while the remaining columns were integers, which aligned with our expectations.

To gain an initial understanding of the dataset, we used the .describe() method to generate summary statistics. Key observations included:

* The "weekday" column contained integers ranging from 0 to 6, indicating that the week starts at integer '0'.
* The "weathersit" column had no occurrences of '4', meaning there were no instances of heavy rain throughout the recorded time period.
* The "count" column (total rental bikes) ranged from a minimum of 22 to a maximum of 8,714, suggesting significant fluctuations in bike rentals.

We then examined the distribution of each feature using histograms. One key insight was that the most common weather type in the "weathersit" column was '1', followed by '2', which had roughly half the count of '1'. There were very few occurrences of '3' and none of '4'.

To detect potential outliers and assess data validity, we utilized boxplots. Finally, we analyzed feature correlations using a heatmap, which revealed several strong correlations with the "count" column, particularly with season, year, weathersit, temperature, and windspeed. These findings indicate that these variables do have influence on the number of bike rentals.

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

## Revisions and Adjustments to the Original Project Plan

Initially, our predictive model only considered temperature as a numerical feature. However, we later decided to include humidity and wind speed as additional numerical variables. This change was essential because weather conditions significantly impact bike rental demand. While temperature is a crucial factor, it does not fully capture the overall comfort level for cyclists. High humidity can make riding uncomfortable, potentially reducing demand, while strong winds can create physical barriers that discourage bike usage. By incorporating these variables, our model better reflects real-world conditions that influence biking behavior.
This adjustment aligns with our business case, as our goal is to provide bike-sharing companies with accurate demand forecasts in cities with similar seasonal trends as Washington, D.C. Understanding how multiple weather factors impact bike rentals allows companies to optimize fleet distribution, plan for fluctuations in demand, and make informed decisions about expansion. By including humidity and wind speed, we enhance the model’s predictive accuracy, ensuring that bike-sharing providers have a more comprehensive view of the factors affecting their business.

## Working as a Team
Our team's approach to working collaboratively involved a clear division of responsibilities while maintaining open communication and shared decision-making. By leveraging GitHub Project and Slack, we maintained efficient communication, timely updates, and seamless task coordination. We began by jointly determining the business case to ensure a mutual understanding of our objectives. 
Each team member then took ownership of specific tasks as mentioned in the table below. Finally, we collaborated as a team to compile the ReadMe file, ensuring that our project was documented comprehensively and clearly for future reference.
This structured yet flexible approach allowed us to leverage each member's strengths while promoting a supportive and inclusive working environment.

| Name | GitHub Account | Roles/Responsibilities | Reflection Video |
| :---: | :---: | :---: | :---: |
| Rachel Fernandes | [rachfern](https://github.com/rachfern) |Data Cleaning and Handling Missing Values |video here|
| Jingkenh Loh | [jkenloh](https://github.com/jkenloh) |Exploratory Data Analysis |video here|
| Daniel Troniak | [troniak](https://github.com/troniak) |Creating a Regression Model|video here|
| Saleha Ejaz Qureshi | [saleha-12](https://github.com/saleha-12) |Model Buidling and Evaluation|video here|
| Efren Tumialan Tenorio | [efrenltt24](https://github.com/efrenltt24) |Model Optimization through Hyperparameter Tuning|video here|

## Conclusion

Our analysis of the Capital Bikeshare dataset has yielded valuable insights for bike-sharing companies looking to expand into new markets. Through rigorous data cleaning, exploratory analysis, and model development, we've created a robust predictive framework that can forecast bike rental demand with high accuracy.

Our analysis revealed that bike rental demand is influenced by multiple weather factors beyond just temperature. By incorporating humidity and wind speed into our model, we captured a more comprehensive picture of how environmental conditions affect ridership. The feature importance analysis highlighted significant temporal patterns in bike usage, with hour of the day, season, and month being strong predictors. This information allows companies to optimize fleet distribution throughout the day and across seasons.

The Random Forest model achieved an impressive R² score of 0.884, explaining nearly 90% of the variance in bike rentals. The hyperparameter-tuned version further reduced prediction errors, with a Mean Absolute Error of just 30.13 bikes. These results demonstrate the effectiveness of our approach in creating a reliable predictive model.

The insights from our model provide actionable intelligence for bike-sharing companies, enabling them to anticipate demand fluctuations based on weather forecasts, plan maintenance during predicted low-demand periods, optimize bike distribution across stations, and make data-driven decisions about fleet size when expanding to new locations.

By combining rigorous data science methodology with business-focused analysis, our project delivers not just a predictive model, but a valuable decision-making tool for the bike-sharing industry.

