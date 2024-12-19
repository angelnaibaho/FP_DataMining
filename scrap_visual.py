import streamlit as st
import pandas as pd
import plotly.express as px

def visualize():
    df = pd.read_csv('Youtube Scrapping.csv')
    
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    
    # Memfilter komentar Toxic dan Non-Toxic
    toxic_comments = df[df['Type'] == 'Toxic']
    non_toxic_comments = df[df['Type'] == 'Non-Toxic']

    # Menghitung jumlah komentar per tanggal
    toxic_per_day = toxic_comments.groupby(toxic_comments['publishedAt'].dt.floor('D')).size().reset_index(name='Toxic')
    non_toxic_per_day = non_toxic_comments.groupby(non_toxic_comments['publishedAt'].dt.floor('D')).size().reset_index(name='Non-Toxic')

    # Membuat grafik garis interaktif untuk jumlah komentar Toxic dan Non-Toxic per tanggal
    fig_line = px.line(
        toxic_per_day, 
        x='publishedAt', 
        y='Toxic', 
        title='Jumlah Komentar Toxic per Tanggal', 
        labels={'publishedAt': 'Tanggal', 'Toxic': 'Jumlah Komentar Toxic'}
    )
    fig_line.add_scatter(
        x=non_toxic_per_day['publishedAt'], 
        y=non_toxic_per_day['Non-Toxic'], 
        mode='lines', 
        name='Non-Toxic'
    )

    # Menampilkan grafik garis interaktif di Streamlit
    st.plotly_chart(fig_line)

    # Hitung nilai untuk setiap kategori
    rating_counts = df['Type'].value_counts().reset_index()
    rating_counts.columns = ['Type', 'Count']  # Rename kolom untuk Plotly

    # Membuat grafik batang interaktif
    fig_bar = px.bar(
        rating_counts, 
        x='Type', 
        y='Count', 
        color='Type', 
        title='Jumlah Pembagian Toxic dan Non-Toxic', 
        labels={'Type': 'Kategori', 'Count': 'Jumlah'},
        text='Count',  # Menampilkan nilai di atas batang
        color_discrete_map={'Toxic': '#BB8082', 'Non-Toxic': '#82BB80'}  # Warna khusus
    )

    # Menampilkan grafik batang interaktif di Streamlit
    st.plotly_chart(fig_bar)

# Panggil fungsi untuk visualisasi
visualize()
