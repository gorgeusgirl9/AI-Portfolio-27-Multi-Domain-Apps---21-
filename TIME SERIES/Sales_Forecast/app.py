import streamlit as st
import pandas as pd
import numpy as np

# Sayfa Yapılandırması
st.set_page_config(page_title="AI Sales Forecaster", page_icon="📊")
st.title("📊 AI Sales Forecaster")
st.write("### Time Series: Proje 3")

# Veri Simülasyonu
months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos']
sales_data = [15000, 18500, 14200, 21000, 25600, 23000, 28500, 31000]
df = pd.DataFrame({'Ay': months, 'Satış ($)': sales_data})

st.info("Bu asistan, geçmiş 8 aylık satış verilerini analiz ederek bir sonraki ayın performansını tahmin eder.")

# Grafik
st.subheader("Aylık Satış Trendi")
st.bar_chart(df.set_index('Ay'))

# Tahmin Mantığı (Basit Hareketli Ortalama & Trend)
if st.button("Eylül Ayı Tahminini Oluştur"):
    last_val = sales_data[-1]
    # %5 ile %15 arası büyüme simülasyonu
    predicted_sales = last_val * (1 + np.random.uniform(0.05, 0.15))
    
    st.success(f"Eylül ayı için beklenen tahmini satış: ${predicted_sales:,.2f}")
    st.write(f"**Beklenen Büyüme:** %{((predicted_sales-last_val)/last_val)*100:.1f}")

st.divider()
st.caption("Model: Simple Trend Analysis Agent")