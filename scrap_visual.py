import streamlit as st
import pandas as pd
import plotly.express as px

def visualize():
    # Membaca file CSV
    df = pd.read_csv('Youtube Scrapping.csv')

    # Memastikan kolom 'publishedAt' adalah datetime
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])

    # Memfilter komentar Toxic dan Non-Toxic
    toxic_comments = df[df['Type'] == 'Toxic']
    non_toxic_comments = df[df['Type'] == 'Non-Toxic']

    # Menghitung jumlah komentar per tanggal
    toxic_per_day = toxic_comments.groupby(toxic_comments['publishedAt'].dt.floor('D')).size().reset_index(name='Toxic')
    non_toxic_per_day = non_toxic_comments.groupby(non_toxic_comments['publishedAt'].dt.floor('D')).size().reset_index(name='Non-Toxic')

    # Membuat grafik interaktif menggunakan Plotly
    fig = px.line(toxic_per_day, x='publishedAt', y='Toxic', title='Jumlah Komentar Toxic per Tanggal', labels={'publishedAt': 'Tanggal', 'Toxic': 'Jumlah Komentar Toxic'})
    fig.add_scatter(x=non_toxic_per_day['publishedAt'], y=non_toxic_per_day['Non-Toxic'], mode='lines', name='Non-Toxic')

    # Menampilkan grafik interaktif di Streamlit
    st.plotly_chart(fig)

# Panggil fungsi untuk visualisasi
visualize()
