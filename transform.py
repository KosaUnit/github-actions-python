import pandas as pd

# Read the raw CSV file
df = pd.read_csv('weather.csv')

# Drop rows with any missing values
df_cleaned = df.dropna()

# Convert all city names to lowercase
df_cleaned['city'] = df_cleaned['city'].str.lower()

# Write the cleaned data to a new CSV
df_cleaned.to_csv('cleaned_weather.csv', index=False)

print("Cleaned data has been saved to cleaned_weather.csv")
