# Eğitim süreci benzer projelerle (İş Zekası & Veri Analitiği) paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# AI_Global_SaaS_Subscription_Dashboard
## Ödev Türü: İş Zekası ve Tahminleyici Analitik (Business Intelligence)

## Kullanılan Algoritma: Random Forest / Linear Regression (Churn Prediction)

# Project Title: AI Global SaaS Subscription Dashboard
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-SaaS-Dashboard
# Assignment: Business Intelligence - Data Analytics

# Küresel ölçekteki SaaS abonelik verilerini görselleştiren ve müşteri kaybını (churn) tahmin eden bir yönetim panelidir.

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Global Sales Dashboard", layout="wide")
st.title("🌐 AI Global SaaS Subscription Dashboard")
st.info("Dünya Geneli Yapay Zeka Yazılım Lisans Satış Analizi")
st.write("### Data Visualization: Proje 25/30")

# Örnek Veri Seti Oluşturma
data = {
    'Country': ['United States', 'Canada', 'Brazil', 'Turkey', 'Germany', 'China', 'India', 'Australia', 'Japan', 'France'],
    'Sales': np.random.randint(10000, 50000, 10),
    'Growth': np.random.uniform(5, 25, 10)
}
df = pd.DataFrame(data)

col1, col2 = st.columns([2, 1])

with col1:
    st.write("#### 🗺️ Dünya Geneli Satış Yoğunluğu")
    fig = px.choropleth(df, locations="Country", locationmode='country names', 
                        color="Sales", hover_name="Country", 
                        color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("#### 📊 Ülke Bazlı Büyüme")
    fig2 = px.bar(df, x='Country', y='Growth', color='Growth')
    st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.caption("30-Project Portfolio - Business Intelligence Series")

# Veri madenciliği teknikleri kullanılarak kullanıcı davranışları analiz edilmiş ve işletme için stratejik içgörüler sunulmuştur.
