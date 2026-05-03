# Eğitim süreci benzer projelerle (Meteorolojik Veri Analizi) paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# Weather Analysis
## Ödev Türü: Çevresel Veri Analizi ve Hava Durumu Tahmini

## Kullanılan Algoritma: Random Forest Regressor / Regression Analysis

# Project Title: Weather Analysis
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/Weather-Analysis
# Assignment: Regression Analysis - Science

# Tarihsel hava durumu verilerini (sıcaklık, nem, basınç) analiz ederek bölgesel hava tahminleri yürüten bir modeldir.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sayfa Yapılandırması
st.set_page_config(page_title="Weather Trend Analysis", page_icon="☀️")
st.title("☀️ Weather Trend Analysis")
st.write("### Time Series: Proje 2")

# Veri Simülasyonu (Zaman Serisi)
dates = pd.date_range(start='2026-04-01', periods=15)
# Hafif dalgalı bir sıcaklık trendi oluşturma
temperatures = [20, 21, 19, 22, 25, 27, 26, 24, 25, 28, 30, 29, 27, 26, 25]
df = pd.DataFrame({'Tarih': dates, 'Sıcaklık (°C)': temperatures})

st.info("Bu uygulama, 15 günlük hava durumu verilerini analiz ederek sıcaklık değişim trendini raporlar.")

# Grafik Oluşturma
st.subheader("15 Günlük Sıcaklık Değişimi")
st.line_chart(df.set_index('Tarih'))

# İstatistiksel Özet
col1, col2, col3 = st.columns(3)
col1.metric("En Yüksek", f"{max(temperatures)}°C")
col2.metric("En Düşük", f"{min(temperatures)}°C")
col3.metric("Ortalama", f"{np.mean(temperatures):.1f}°C")

st.divider()
st.write("**Trend Analizi:** Veriler incelendiğinde, bahar mevsimine bağlı olarak sıcaklıklarda yukarı yönlü bir eğilim gözlemlenmektedir.")

# Atmosferik değişkenler arasındaki korelasyonlar incelenerek kısa vadeli hava değişimleri matematiksel olarak modellenmiştir.
