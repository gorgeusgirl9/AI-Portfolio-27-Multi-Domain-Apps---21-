import streamlit as st
import joblib
import numpy as np

# Modeli yükle
model = joblib.load('health_model.pkl')

st.set_page_config(page_title="Sigorta Tahmin", page_icon="🏥")

st.title("🏥 Sağlık Sigortası Ücret Tahmini")
st.write("Hocanın ödevi için hazırlanan regresyon projesidir.")

# Giriş alanları
age = st.slider("Yaşınız", 18, 100, 30)
bmi = st.number_input("Vücut Kitle İndeksi (BMI)", 10.0, 60.0, 25.0)
smoker = st.radio("Sigara İçiyor musunuz?", ["Evet", "Hayır"])

if st.button("Tahmini Ücreti Hesapla"):
    smoker_val = 1 if smoker == "Evet" else 0
    # Modeli eğitirken kullandığımız 6 sütun (age, sex, bmi, children, smoker, region)
    # Diğerlerini (sex, children, region) 0 olarak varsayıyoruz
    input_features = np.array([[age, 0, bmi, 0, smoker_val, 0]])
    
    prediction = model.predict(input_features)
    st.success(f"Tahmini Yıllık Sigorta Ücreti: ${prediction[0]:,.2f}")