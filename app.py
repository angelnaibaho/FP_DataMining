import pickle
import streamlit as st
from streamlit_option_menu import option_menu
 
# Load model dan vectorizer
with open(r'multinominalNB_model.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

with open(r'vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf = pickle.load(vectorizer_file)

with st.sidebar:
    selected = option_menu("Kelompok 12", ["Prediksi", "Visualisasi"], 
        icons=['house', 'gear'], menu_icon="cast")
    selected

# Fungsi prediksi
def prediction(kalimat):
    # Transformasi input teks menjadi vektor numerik
    kalimat_vectorized = tfidf.transform([kalimat])
    # Lakukan prediksi
    prediction = classifier.predict(kalimat_vectorized)
    return prediction[0]

# Fungsi utama aplikasi Streamlit
def main():
    if selected == 'Prediksi':
        category = st.selectbox("Pilih Kategori Prediksi", ["Kalimat", "Input Data"])
        
        if category == "Kalimat":
            # Judul aplikasi
            st.title('Prediksi Kalimat Toxic')

            # Input teks dari pengguna
            kalimat = st.text_input("Masukkan komentar yang ingin diprediksi", "")

            result = ""
            if st.button("Prediksi"):
                result = prediction(kalimat)
                st.success('Hasil Prediksi: {}'.format(result))
                if result == 'Toxic':  # Jika prediksi toxic
                    st.warning("-- Toxicity doesn't build, it destroys. Let's be kind!🙌🏻 ---")
                elif result == 'Non-Toxic':  # Jika prediksi non-toxic
                    st.success("--- Let’s lift each other up, not tear each other down!🫶🏻 ---")
        
        elif category == "Input Data":
            st.title("Input Data")
            uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])
            
            if uploaded_file is not None:
                # Membaca file CSV ke dalam DataFrame pandas
                data = pd.read_csv(uploaded_file)
                st.write("Data yang diunggah:")
                st.dataframe(data)
                
                # Asumsi kolom dengan komentar bernama 'comment'
                if 'comment' in data.columns:
                    # Terapkan fungsi prediksi pada setiap komentar di kolom 'comment'
                    predictions = data['comment'].apply(prediction)
                    data['Prediction'] = predictions

                    # Menampilkan DataFrame dengan hasil prediksi
                    st.write("Hasil Prediksi:")
                    st.dataframe(data[['comment', 'Prediction']])

                    # Menampilkan jumlah komentar toxic dan non-toxic
                    toxic_count = (data['Prediction'] == 'Toxic').sum()
                    non_toxic_count = (data['Prediction'] == 'Non-Toxic').sum()

                    st.write(f"Komentar Toxic: {toxic_count}")
                    st.write(f"Komentar Non-Toxic: {non_toxic_count}")
                else:
                    st.error("Kolom 'comment' tidak ditemukan dalam file CSV.")

        
    elif selected == 'Visualisasi':
        category = st.selectbox("Pilih Kategori Prediksi", ["Word Clouds", "Grafik"])
        st.title("Visualisasi Data Komentar Toxic dan Non-Toxic")

        if category == "Grafik":
            # Panggil fungsi visualisasi dari visual.py
            visualize()
    
if __name__ == '__main__':
    main()
