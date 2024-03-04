import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def preprocessing(file_path_csv: str):
    raw_df = pd.read_csv(file_path_csv)
    raw_df['dteday'] = pd.to_datetime(raw_df['dteday'])

    """
    Membuat dictionary untuk memudahkan membaca data
    """
    seasons = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
    year = {0: 2011, 1: 2012}
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    weather_condition = {1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'}

    """ 
    Mengubah beberapa variabel untuk memudahkan membaca data
    """
    raw_df.rename(columns={
        'instant': 'rec_id',
        'dteday': 'datetime',
        'yr': 'year',
        'mnth': 'month',
        'holiday': 'is_holiday',
        'workingday': 'is_workingday',
        'weathersit': 'weather_condition',
        'hum': 'humidity',
        'cnt': 'total_count',
    }, inplace=True)

    df = raw_df.copy()
    df['season'] = df['season'].map(seasons)
    df['year'] = df['year'].map(year)
    df['month'] = df['month'].map(months)
    df['weekday'] = df['weekday'].map(days)
    df['weather_condition'] = df['weather_condition'].map(weather_condition)
    
    return raw_df, df

if __name__ == "__main__":
    logdayraw_df, logday_df = preprocessing('./data/day.csv')
    loghourraw_df, loghour_df = preprocessing('./data/hour.csv')

    """
    tampilan
    """
    st.title("Proyek Analisis Data Dicoding")

