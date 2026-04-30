import streamlit as st
import joblib
import numpy as np

# 1. Modeli yükle (Dosya adının snow_model.pkl olduğundan emin ol)
try:
    model = joblib.load('snow_model.pkl')
except:
    st.error("Model dosyası (snow_model.pkl) bulunamadı. Lütfen dosyayı yükleyin.")

# Sayfa Ayarları
st.set_page_config(page_title="Kar Tahmin Projesi", page_icon="❄️")
st.title("❄️ Kar Yağışı Predictor")
st.write("### Proje 4: Sınıflandırma (Classification) Analizi")

st.info("Sıcaklık ve nem gibi verileri girerek kar yağma ihtimalini görün.")

# 2. Kullanıcı Giriş Alanları
col1, col2 = st.columns(2)

with col1:
    temp = st.slider("Hava Sıcaklığı (°C)", -20, 20, 0)
    hum = st.slider("Nem Oranı (%)", 0, 100, 70)

with col2:
    wind = st.slider("Rüzgar Hızı (km/h)", 0, 100, 20)
    press = st.number_input("Basınç (hPa)", 950, 1050, 1013)

# 3. Tahmin Butonu ve Mantığı
if st.button("Kar Yağacak Mı?"):
    # Girdileri modele uygun diziye çevir
    input_data = np.array([[temp, hum, wind, press]])
    prediction = model.predict(input_data)
    
    st.markdown("---")
    
    if prediction[0] == 1:
        st.snow() # Ekranda kar taneleri uçuşur ❄️
        st.error("### ❄️ Tahmin: Kar Yağışı Bekleniyor!")
        st.write("Sıcaklık ve nem değerleri kar oluşumu için uygun görünüyor.")
    else:
        st.success("### ☀️ Tahmin: Kar Beklenmiyor.")
        st.write("Hava şartları kar yağışı için yeterli soğuklukta veya nemde değil.")

# Alt Bilgi
st.markdown("---")
st.caption("Veri Bilimi Portfolyosu - Proje No: 4 (Snowfall Classification)")