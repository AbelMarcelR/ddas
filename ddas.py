import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

day_df = pd.read_csv("day.csv")
day_df['mnth'] = day_df['mnth'].map({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'})

def main():
    st.title("Dashboard Analisis Pengguna Sepeda")

    option = st.sidebar.selectbox(
        "Pilih Analisis:",
        ("Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca",
         "Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu",
         "Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun")
    )

    if option == "Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca":
        plot_weather_condition()

    elif option == "Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu":
        plot_working_holiday_weekday()

    elif option == "Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun":
        plot_monthly_counts()


def plot_weather_condition():
    plt.figure(figsize=(9, 5))
    correlation_matrix = day_df.corr()
    correlation_matrix['cnt'].plot(kind='bar')
    plt.title("Correlation with count ")
    plt.xlabel("Features")
    plt.ylabel("Correlation")
    plt.xticks(rotation=45)
    plt.show()


def plot_working_holiday_weekday():
    plt.figure(figsize=(9, 5))
    sns.lineplot(
        x='weathersit',
        y='cnt',
        data=day_df
    )
    plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Pengguna Sepeda')
    plt.show()


def plot_monthly_counts():
    pivot_table = day_df.pivot_table(index='weekday', columns='workingday', values='cnt', aggfunc='sum')
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt=".0f")
    plt.title('Jumlah Pengguna Sepeda berdasarkan Hari dalam Seminggu dan Hari Kerja')
    plt.xlabel('Hari Kerja')
    plt.ylabel('Hari dalam Seminggu')
    plt.show()


if __name__ == "__main__":
    main()
