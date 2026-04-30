import streamlit as st
import joblib
import numpy as np

# Modeli Yükle
model = joblib.load('market_model.pkl')

st.set_page_config(page_title="Global Market Predictor", page_icon="📈")
st.title("📈 Global Market Predictor")
st.write("### Regression Project 3: Multi-Variable Analysis")

st.info("Altın, Gümüş ve Petrol fiyatlarının borsa endeksi üzerindeki etkisini tahmin edin.")

# Giriş Alanları
col1, col2, col3 = st.columns(3)

with col1:
    gold_price = st.number_input("Gold (Ons/$) ", 1500, 3000, 2100)
with col2:
    silver_price = st.number_input("Silver (Ons/$) ", 15, 50, 25)
with col3:
    oil_price = st.number_input("Oil (Brent/$) ", 40, 150, 85)

# Tahmin Butonu
if st.button("Piyasa Endeksini Tahmin Et"):
    input_data = np.array([[gold_price, silver_price, oil_price]])
    prediction = model.predict(input_data)
    
    st.markdown("---")
    st.subheader(f"Tahmini Piyasa Skoru: **{prediction[0]:,.2f}**")
    
    # Görsel bir metrik gösterimi
    st.metric(label="Tahmin Edilen Endeks", value=f"{prediction[0]:,.0f} Puan", delta="Piyasa Analizi Tamamlandı")

st.caption("21-Project Portfolio - Regression Series 3/3")