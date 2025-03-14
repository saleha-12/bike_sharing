import pandas as pd

# Load the datasets
hour_df = pd.read_csv('/Users/frach/Downloads/Final Team Project/bike_sharing/bike+sharing+dataset/hour.csv')
day_df = pd.read_csv('/Users/frach/Downloads/Final Team Project/bike_sharing/bike+sharing+dataset/day.csv')

# List of irrelevant columns for analysis
columns_to_exclude_from_analysis = ['holiday', 'workingday', 'atemp', 'hum', 'windspeed', 'casual', 'registered']

# Keep all columns in the DataFrame but exclude the ones from analysis
hour_df_cleaned = hour_df.drop(columns=columns_to_exclude_from_analysis)
day_df_cleaned = day_df.drop(columns=columns_to_exclude_from_analysis)

# Check for missing values
print(hour_df_cleaned.isnull().sum())
print(day_df_cleaned.isnull().sum())

# Drop rows with missing values (if any)
hour_df_cleaned.dropna(inplace=True)
day_df_cleaned.dropna(inplace=True)

# Check for duplicates and drop them
hour_df_cleaned.drop_duplicates(inplace=True)
day_df_cleaned.drop_duplicates(inplace=True)

# IQR for hourly data (only for 'cnt' column)
Q1_hour = hour_df_cleaned['cnt'].quantile(0.25)
Q3_hour = hour_df_cleaned['cnt'].quantile(0.75)
IQR_hour = Q3_hour - Q1_hour
hour_df_cleaned = hour_df_cleaned[(hour_df_cleaned['cnt'] >= (Q1_hour - 1.5 * IQR_hour)) & (hour_df_cleaned['cnt'] <= (Q3_hour + 1.5 * IQR_hour))]

# IQR for daily data (only for 'cnt' column)
Q1_day = day_df_cleaned['cnt'].quantile(0.25)
Q3_day = day_df_cleaned['cnt'].quantile(0.75)
IQR_day = Q3_day - Q1_day
day_df_cleaned = day_df_cleaned[(day_df_cleaned['cnt'] >= (Q1_day - 1.5 * IQR_day)) & (day_df_cleaned['cnt'] <= (Q3_day + 1.5 * IQR_day))]

# Concatenate both dataframes into one (keeping all columns)
combined_df = pd.concat([hour_df, day_df], axis=0, ignore_index=True)

# Save the combined cleaned data to a new CSV file with all columns included
combined_df.to_csv('/Users/frach/Downloads/Final Team Project/bike_sharing/bike+sharing+dataset/cleaned_bike.csv', index=False)