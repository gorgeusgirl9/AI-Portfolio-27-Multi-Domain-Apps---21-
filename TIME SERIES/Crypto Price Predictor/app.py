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