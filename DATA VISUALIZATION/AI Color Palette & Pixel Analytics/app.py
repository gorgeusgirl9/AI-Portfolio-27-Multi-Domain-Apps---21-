# Eğitim süreci benzer projelerle paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# AI Color Palette & Pixel Analytics
## Ödev Türü: Görüntü İşleme ve Renk Analitiği

## Kullanılan Algoritma: K-Means Clustering 

# Project Title: AI Color Palette & Pixel Analytics
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-Color-Palette
# Assignment: Computer Vision - Analytics

# Yüklenen görsellerdeki baskın renkleri tespit eden ve piksel bazlı renk dağılımı analizi yapan bir araçtır.

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go

# Sayfa Ayarları
st.set_page_config(page_title="AI Pixel Analytics", layout="wide")
st.title("🎨 AI Color Palette & Pixel Analytics")
st.write("### Data Visualization: Proje 26/30 (Görsel Veri Analizi)")

# Dosya Yükleme
uploaded_file = st.file_uploader("Bir fotoğraf yükle ve renk şifrelerini çöz:", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(img, caption="Orijinal Görsel", use_container_width=True)
    
    # Görüntüyü analiz için küçültelim (Performans için 100x100)
    img_small = img.convert("RGB").resize((100, 100))
    img_array = np.array(img_small).reshape(-1, 3)
    
    with st.spinner('Piksel verileri analiz ediliyor...'):
        # En baskın 5 rengi bulmak için K-Means
        n_colors = 5
        kmeans = KMeans(n_clusters=n_colors, n_init=10, random_state=42)
        kmeans.fit(img_array)
        colors = kmeans.cluster_centers_.astype(int)
        
        # Renklerin oranlarını hesapla
        labels = kmeans.labels_
        counts = pd.Series(labels).value_counts().sort_index()
        
    with col2:
        st.write("#### 📊 Baskın Renk Dağılımı")
        # Hex kodlarını oluştur
        hex_colors = [f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}' for c in colors]
        
        # Pasta Grafiği (Hata düzeltilmiş hali)
        fig_pie = px.pie(
            values=counts.values, 
            names=hex_colors, 
            hole=0.4,
            title="Renk Paylaşım Oranları"
        )
        
        # Renkleri grafiğe manuel enjekte et (Identity hatasını çözer)
        fig_pie.update_traces(
            marker=dict(colors=hex_colors),
            textinfo='percent+label'
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()
    
    # 3D Renk Uzayı Görselleştirmesi
    st.write("#### 🧊 3D Renk Uzayı (RGB Dağılım Analizi)")
    st.info("Piksellerin RGB evrenindeki konumları:")
    
    # Görselleştirme için örneklem al (1000 piksel)
    indices = np.random.choice(img_array.shape[0], 1000, replace=False)
    sample_pixels = img_array[indices]
    sample_colors = [f'rgb({p[0]},{p[1]},{p[2]})' for p in sample_pixels]
    
    fig_3d = go.Figure(data=[go.Scatter3d(
        x=sample_pixels[:, 0], y=sample_pixels[:, 1], z=sample_pixels[:, 2],
        mode='markers',
        marker=dict(size=4, color=sample_colors, opacity=0.8)
    )])
    
    fig_3d.update_layout(
        scene=dict(
            xaxis_title='Kırmızı (R)', 
            yaxis_title='Yeşil (G)', 
            zaxis_title='Mavi (B)'
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    st.plotly_chart(fig_3d, use_container_width=True)

else:
    st.info("Lütfen analiz için bir görsel yükleyin.")

st.divider()
st.caption("30-Project Portfolio | Data Visualization & Image Analytics | 2026")

# K-Means algoritması kullanılarak renkler kümelenmiş ve tasarımcılar için uyumlu renk paletleri otomatik olarak oluşturulmuştur.
