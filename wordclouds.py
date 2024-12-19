import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def wordClouds():
    # Misalnya df sudah ada
    df = pd.read_csv('D:\Data Mining\Youtube Stemming.csv')

    # Filter komentar Toxic dan Non-Toxic
    toxic = df[df['Type'] == 'Toxic']
    non_toxic = df[df['Type'] == 'Non-Toxic']

    # Gabungkan hasil stemming untuk komentar Toxic dan Non-Toxic
    toxic_text = ' '.join([' '.join(text) for text in toxic['textDisplay_stemming']])
    non_toxic_text = ' '.join([' '.join(text) for text in non_toxic['textDisplay_stemming']])

    # Membuat word cloud untuk komentar Toxic dan Non-Toxic
    wordcloud_toxic = WordCloud(width=800, height=500, background_color='white').generate(toxic_text)
    wordcloud_non_toxic = WordCloud(width=800, height=500, background_color='white').generate(non_toxic_text)

    # Membuat tata letak kolom
    col1, col2 = st.columns(2)

    # Menampilkan word cloud di kolom pertama (Toxic)
    with col1:
        st.markdown("<h3 style='text-align: center;'>Word Cloud for Toxic Comments</h3>", unsafe_allow_html=True)
        fig_toxic, ax_toxic = plt.subplots(figsize=(5, 5))
        ax_toxic.imshow(wordcloud_toxic, interpolation='bilinear')
        ax_toxic.axis('off')
        st.pyplot(fig_toxic)

    # Menampilkan word cloud di kolom kedua (Non-Toxic)
    with col2:
        st.markdown("<h3 style='text-align: center;'>Word Cloud for Non-Toxic Comments</h3>", unsafe_allow_html=True)
        fig_non_toxic, ax_non_toxic = plt.subplots(figsize=(5, 5))
        ax_non_toxic.imshow(wordcloud_non_toxic, interpolation='bilinear')
        ax_non_toxic.axis('off')
        st.pyplot(fig_non_toxic)
