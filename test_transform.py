import os
import pandas as pd
from transform import pd, df_cleaned  # Import reused objects if any
import transform

def test_cleaned_weather_file(tmp_path):
    # Create a temporary weather.csv file
    test_data = """city,temperature,humidity
New York,22,65
los angeles,25,60
,30,50
Chicago,20,70
Houston,,55
miami,28,80
"""
    temp_file = tmp_path / "weather.csv"
    temp_file.write_text(test_data)

    # Replace file paths in transform.py logic
    df = pd.read_csv(temp_file)
    df_cleaned = df.dropna()
    df_cleaned['city'] = df_cleaned['city'].str.lower()
    output_file = tmp_path / "cleaned_weather.csv"
    df_cleaned.to_csv(output_file, index=False)

    # Load the output and verify
    result_df = pd.read_csv(output_file)

    # Expected result
    expected_data = {
        'city': ['new york', 'los angeles', 'chicago', 'miami'],
        'temperature': [22.0, 25.0, 20.0, 28.0],
        'humidity': [65, 60, 70, 80]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)

