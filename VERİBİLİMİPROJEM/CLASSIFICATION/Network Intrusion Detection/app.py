import streamlit as st
import joblib
import numpy as np

# Modeli Yükle
model = joblib.load('network_security_model.pkl')

st.set_page_config(page_title="Network Intrusion Detector", page_icon="🛡️")
st.title("🛡️ Cyber Security: Network Traffic Clustering")
st.write("### Clustering Project 3: Cyber Intelligence")

st.info("Ağ paket verilerini girerek trafiğin güvenliğini analiz edin.")

# Kullanıcı Girişleri
size = st.number_input("Paket Boyutu (KB)", 1, 5000, 500)
interval = st.slider("Paket Gönderim Aralığı (ms)", 0.1, 200.0, 50.0)

if st.button("Trafiği Analiz Et"):
    prediction = model.predict([[size, interval]])
    cluster = prediction[0]
    
    st.markdown("---")
    
    # Siber güvenlik yorumları
    security_zones = {
        0: "🟢 **Normal Trafik:** Standart kullanıcı davranışı tespit edildi.",
        1: "🟡 **Şüpheli Hareket:** Olağandışı paket boyutları; sistem takibe alınmalı.",
        2: "🔴 **Potansiyel Saldırı (Intrusion):** Çok hızlı ve yoğun veri akışı! DDoS veya sızma girişimi olabilir."
    }
    
    st.subheader(f"Analiz Sonucu: Cluster {cluster}")
    if cluster == 2:
        st.error(security_zones[cluster])
    elif cluster == 1:
        st.warning(security_zones[cluster])
    else:
        st.success(security_zones[cluster])

st.caption("21-Project Portfolio - Cybersecurity Series 3/3")