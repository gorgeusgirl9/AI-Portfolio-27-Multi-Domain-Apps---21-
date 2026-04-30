import streamlit as st
import joblib
import numpy as np

# Modeli Yükle
model = joblib.load('space_object_model.pkl')

st.set_page_config(page_title="Deep Space Clustering", page_icon="🌌")
st.title("🌌 Deep Space Object Clustering")
st.write("### Clustering Project 2: Astronomical Analysis")

st.info("Teleskop verilerini girerek cismin hangi kozmik küme içinde olduğunu keşfedin.")

# Kullanıcı Giriş Alanları
col1, col2 = st.columns(2)

with col1:
    b = st.slider("Cisim Parlaklığı (Magnitude)", 0.0, 100.0, 45.0)
    r = st.slider("Radyasyon Yayılımı (THz)", 0.1, 15.0, 3.5)
with col2:
    d = st.number_input("Dünyaya Uzaklık (Işık Yılı)", 100, 100000, 15000)

if st.button("Cismi Analiz Et ve Kümele"):
    # Giriş verisini hazırla
    input_data = np.array([[b, d, r]])
    cluster = model.predict(input_data)[0]
    
    st.markdown("---")
    
    # Grupların mantıksal açıklamaları
    objects = {
        0: "⭐ **Cüce Yıldız Kümesi:** Düşük radyasyon ve stabil parlaklık değerlerine sahip yerel cisimler.",
        1: "🌟 **Dev Yıldızlar / Pulsarlar:** Yüksek enerji ve yoğun radyasyon yayan çok parlak cisimler.",
        2: "🌀 **Uzak Galaksiler / Bulutsular:** Çok büyük mesafelerde bulunan, yaygın ışık yapısına sahip yapılar."
    }
    
    st.subheader(f"Kümeleme Sonucu: **Grup {cluster}**")
    st.success(objects[cluster])

st.caption("21-Project Portfolio - Space Science Series 2/3")