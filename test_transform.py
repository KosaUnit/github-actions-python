import pandas as pd
from transform import load_weather_data, clean_weather_data, save_cleaned_data


def test_cleaned_weather_file(tmp_path):
    test_data = """city,temperature,humidity
New York,22,65
los angeles,25,60
,30,50
Chicago,20,70
Houston,,55
miami,28,80
"""
    input_file = tmp_path / "weather.csv"
    output_file = tmp_path / "cleaned_weather.csv"
    input_file.write_text(test_data)

    # Use the transformation pipeline
    df = load_weather_data(input_file)
    df_cleaned = clean_weather_data(df)
    save_cleaned_data(df_cleaned, output_file)

    # Verify output
    result_df = pd.read_csv(output_file)

    expected_data = {
        'city': ['new york', 'los angeles', 'chicago', 'miami'],
        'temperature': [22.0, 25.0, 20.0, 28.0],
        'humidity': [65, 60, 70, 80]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(
        result_df.reset_index(drop=True),
        expected_df
        )
