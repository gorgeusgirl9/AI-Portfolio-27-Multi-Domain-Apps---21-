import streamlit as st
import joblib
import numpy as np

# Modeli Yükle
model = joblib.load('traffic_cluster_model.pkl')

st.title("🚦 Traffic Zone Clustering")
st.write("### Clustering Project 1: Smart City Analysis")

st.info("Sensör verilerini girerek bölgenin trafik karakteristiğini belirleyin.")

# Kullanıcı Girişleri
v_count = st.slider("Saatlik Araç Sayısı", 50, 2500, 500)
speed = st.slider("Ortalama Hız (km/h)", 5, 130, 60)

if st.button("Bölgeyi Analiz Et"):
    prediction = model.predict([[v_count, speed]])
    cluster = prediction[0]
    
    st.markdown("---")
    
    # Grupları isimlendirelim
    zones = {
        0: "🟢 **Akıcı Bölge:** Düşük araç yoğunluğu, yüksek hız. (Otoyollar)",
        1: "🟡 **Yoğun Bölge:** Yüksek araç sayısı, orta hız. (Ana arterler)",
        2: "🔴 **Kritik Bölge (Kilit):** Orta-Yüksek araç, çok düşük hız. (Şehir içi kavşaklar)"
    }
    
    st.subheader(f"Küme Sonucu: Zone {cluster}")
    st.write(zones[cluster])

st.caption("21-Project Portfolio - Smart City Solutions 1/3")