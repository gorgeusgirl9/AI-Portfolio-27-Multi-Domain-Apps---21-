import streamlit as st
import joblib

# Modelleri Yükle
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("😊 Duygu Analizi (Sentiment Analysis)")
st.write("### NLP Project 1")

user_input = st.text_area("Analiz edilecek metni girin:", "Bu proje gerçekten çok başarılı.")

if st.button("Duyguyu Analiz Et"):
    # Metni vektöre çevir ve tahmin et
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)
    
    st.markdown("---")
    if prediction[0] == 1:
        st.success(f"Sonuç: **POZİTİF** 😍")
    else:
        st.error(f"Sonuç: **NEGATİF** 😡")

st.caption("21-Project Portfolio - NLP Series 1/3")