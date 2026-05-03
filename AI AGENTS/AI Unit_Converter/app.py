# Eğitim süreci benzer projelerle (Utility AI & Fonksiyonel Modelleme) paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# AI Unit Converter
## Ödev Türü: Fonksiyonel Yapay Zeka Uygulamaları (Utility AI)
# Project Title: AI Unit Converter
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-Unit-Converter
# Assignment: Utility AI Applications

# Farklı ölçü birimleri arasında akıllı dönüşüm sağlayan, kullanıcı girdisine göre en uygun formülü uygulayan bir araçtır.


import streamlit as st

st.set_page_config(page_title="AI Unit Converter", page_icon="⚖️")
st.title("⚖️ AI Unit Converter Agent")
st.write("### AI Agents: Proje 3")

# Agent Mantığı: Birim Dönüşüm Sözlüğü
conversions = {
    "Kilometre -> Mil": 0.621371,
    "Mil -> Kilometre": 1.60934,
    "Kilogram -> Pound": 2.20462,
    "Pound -> Kilogram": 0.453592,
    "Celsius -> Fahrenheit": "C*9/5+32",
}

st.info("Benim görevim, teknik ölçümleri birbirine hızlıca dönüştürmektir.")

option = st.selectbox("Dönüştürmek istediğiniz birimi seçin:", list(conversions.keys()))
value = st.number_input("Değeri girin:", value=1.0)

if st.button("Dönüştür ✨"):
    if option == "Celsius -> Fahrenheit":
        result = (value * 9/5) + 32
    else:
        result = value * conversions[option]
    
    st.success(f"İşlem Tamamlandı: {value} birim = {result:.2f} hedef birim.")
    st.balloons()

st.divider()
st.caption("Agent Capability: Mathematical Reasoning & Unit Transformation")

# Karmaşık birim sistemlerini tanıma ve matematiksel modelleme prensipleri üzerine inşa edilmiştir.
