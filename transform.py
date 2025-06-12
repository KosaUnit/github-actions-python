import pandas as pd

def load_weather_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def clean_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    df_cleaned = df.dropna()
    df_cleaned['city'] = df_cleaned['city'].str.lower()
    return df_cleaned

def save_cleaned_data(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index=False)

def main():
    input_file = 'weather.csv'
    output_file = 'cleaned_weather.csv'

    df = load_weather_data(input_file)
    df_cleaned = clean_weather_data(df)
    save_cleaned_data(df_cleaned, output_file)

    print("Cleaned data has been saved to cleaned_weather.csv")

if __name__ == "__main__":
    main()
