# Eğitim süreci benzer projelerle (Computer Vision & Derin Öğrenme) paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# AI-Face-Analyzer
## Ödev Türü: Bilgisayarlı Görü (Computer Vision)
# Project Title: AI-Face-Analyzer
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-Face-Analyzer
# Assignment: Computer Vision - Facial Analysis

# Görüntü üzerindeki insan yüzlerini tespit eden ve temel yüz hatlarını analiz eden bir derin öğrenme uygulamasıdır.

import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np
import os

# Sayfa Ayarları
st.set_page_config(page_title="AI Face Analyzer", page_icon="👤")

st.title("👤 AI Face Analyzer")
st.write("### Computer Vision Serisi: Final Projesi")

# Modellerin yükleneceği dizini belirle (Hugging Face için kritik)
os.environ['DEEPFACE_HOME'] = '/home/user/app'

uploaded_file = st.file_uploader("Bir portre fotoğrafı yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)
    st.image(image, caption='Yüklenen Resim', use_column_width=True)
    
    if st.button("Yüzü Analiz Et"):
        with st.spinner('Yapay zeka analiz ediyor (İlk çalıştırma biraz uzun sürebilir)...'):
            try:
                # Analiz Motoru
                results = DeepFace.analyze(
                    img_path = img_array, 
                    actions = ['emotion', 'age', 'gender'],
                    enforce_detection = False,
                    detector_backend = 'opencv'
                )
                
                res = results[0]
                
                st.success("Analiz Başarılı!")
                st.markdown("---")
                
                # Sonuç Paneli
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Baskın Duygu", res['dominant_emotion'].capitalize())
                with col2:
                    st.metric("Tahmini Yaş", res['age'])
                with col3:
                    st.metric("Cinsiyet", res['dominant_gender'])
                
                # Duygu Grafiği
                st.subheader("📊 Duygu Analizi Detayları")
                for emotion, score in res['emotion'].items():
                    st.write(f"{emotion.capitalize()}: %{score:.2f}")
                    st.progress(min(score / 100, 1.0))
                    
            except Exception as e:
                st.error(f"Hata: {str(e)}")
                st.info("İpucu: Yüzün net göründüğü, çok büyük olmayan bir fotoğraf deneyin.")

st.caption("21-Project Portfolio - Computer Vision Final")

# Yüz tanıma ve özellik çıkarımı algoritmaları kullanılarak, görsel veriden biyometrik bilgi tespiti gerçekleştirilir.
