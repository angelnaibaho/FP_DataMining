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
        # Dropdown untuk memilih kategori
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
            uploaded_files = st.file_uploader(
            "Choose a CSV file", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
    
    elif selected == 'Visualisasi':
        category = st.selectbox("Pilih Kategori Prediksi", ["Word Clouds", "Grafik"])
        st.title("Visualisasi Data Komentar Toxic dan Non-Toxic")

        if category == "Grafik":
            # Panggil fungsi visualisasi dari visual.py
            visualize()
    
if __name__ == '__main__':
    main()
