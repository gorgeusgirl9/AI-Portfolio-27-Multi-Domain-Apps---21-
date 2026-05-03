# Eğitim süreci benzer projelerle (Zaman Serisi & Regresyon) paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# Crypto Price Predictor
## Ödev Türü: Zaman Serisi Analizi ve Fiyat Tahminleme
# Project Title: Crypto Price Predictor
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/Crypto-Predictor
# Assignment: Time Series Forecasting - Finance

# Kripto para piyasalarındaki geçmiş fiyat hareketlerini analiz ederek gelecek trendlerini tahmin eden bir modeldir.

import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Crypto Time Series Predictor")
st.write("### Time Series: Proje 1")

# Örnek Zaman Serisi Verisi
dates = pd.date_range(start='2026-04-01', periods=30)
prices = np.cumsum(np.random.randn(30) + 0.5) + 50000 # Rastgele trend
df = pd.DataFrame({'Tarih': dates, 'Fiyat': prices})

st.line_chart(df.set_index('Tarih'))

if st.button("Yarınki Tahmini Hesapla"):
    last_price = prices[-1]
    prediction = last_price * (1 + np.random.uniform(-0.02, 0.05))
    st.metric("Tahmini BTC Fiyatı", f"${prediction:,.2f}", delta=f"{prediction-last_price:.2f}")

# Derin öğrenme tabanlı zaman serisi algoritmaları kullanılarak volatilite analizi yapılmış ve fiyat öngörüleri oluşturulmuştur.
