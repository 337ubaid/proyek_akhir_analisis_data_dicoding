import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

def load_data(file_path_csv: str):
    raw_df = pd.read_csv(file_path_csv)
    raw_df['dteday'] = pd.to_datetime(raw_df['dteday'])

    seasons = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
    year = {0: 2011, 1: 2012}
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    weather_condition = {1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'}


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

def show_monthly():
    monthly_progress_2011 = logdayraw_df[logdayraw_df['year'] == 0].groupby('month')['total_count'].sum()
    monthly_progress_2012 = logdayraw_df[logdayraw_df['year'] == 1].groupby('month')['total_count'].sum()
    monthly_progress_2011.plot(kind='line', label='2011')
    monthly_progress_2012.plot(kind='line', label='2012')

    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    plt.title('Monthly Progress')
    plt.xticks(monthly_progress_2011.index, monthly_progress_2011.index.map(months), rotation=90)
    plt.xlabel('Month')
    plt.ylabel('Total Count')

    plt.legend()
    st.pyplot(plt)

def show_corr(corr_total_count):
    st.pyplot(plt.imshow(corr_total_count.values.reshape(1, -1), cmap='coolwarm', aspect='auto'))
    st.pyplot(plt.colorbar())
    st.pyplot(plt.title('Correlation Rental Amount Heatmap'))
    st.pyplot(plt.xticks(range(len(corr_total_count.index)), corr_total_count.index, rotation=90))
    st.pyplot(plt.show())

if __name__ == "__main__":
    logdayraw_df, logday_df = load_data('./data/day.csv')
    loghourraw_df, loghour_df = load_data('./data/hour.csv')

    st.header("Proyek Analisis Data Dicoding")
    st.markdown("""
    - **Nama:** Muhammad Ubaidillah
    - **Email:** devvevan@student.ub.ac.id
    - **ID Dicoding:** beyubey
    """)

    corr_total_count = logdayraw_df.corr()['total_count']
    corr_total_count.to_frame()
    # show_corr(corr_total_count)
    show_monthly() 