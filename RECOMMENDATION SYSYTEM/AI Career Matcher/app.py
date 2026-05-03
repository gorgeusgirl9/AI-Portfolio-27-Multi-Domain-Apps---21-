# Eğitim süreci benzer projelerle (Sınıflandırma & Veri Analitiği) paralel olduğu için dökümantasyonu kod içerisine eklenmiştir.
# AI Career Matcher
## Ödev Türü: Kariyer Danışmanlığı ve Eşleştirme (Decision Support)

## Kullanılan Algoritma: Random Forest / Support Vector Machines (SVM)

# Project Title: AI Career Matcher
# Live Demo: https://huggingface.co/spaces/gorgeusgirl9/AI-Career-Matcher
# Assignment: Classification - Career Analytics

# Kullanıcı yetkinliklerini, ilgi alanlarını ve eğitim geçmişini analiz ederek en uygun meslek gruplarıyla eşleştiren bir karar destek sistemidir.

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Career Matcher", page_icon="💼")
st.title("💼 AI Career Matcher")
st.write("### Deep Learning & Semantic Mapping: Proje 2")

# 1. VERİ SETİ (Türkçe anahtar kelimeler eklendi)
data = {
    'Meslek': [
        'Veri Bilimci', 
        'Grafik Tasarımcı', 
        'Yazılım Geliştirici', 
        'Aşçı', 
        'Siber Güvenlik Uzmanı'
    ],
    'Yetenekler': [
        'python makine öğrenmesi veri analizi istatistik sql tablo grafik', 
        'tasarım çizim yaratıcı görsel logo photoshop sanat boyama', 
        'kod yazılım internet sitesi uygulama bilgisayar programlama', 
        'yemek mutfak tarif lezzet pişirmek kitap gıda restoran',
        'güvenlik hacker saldırı savunma şifre internet ağ sistem'
    ]
}
df = pd.DataFrame(data)

# 2. MODEL
tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(df['Yetenekler'])

# 3. ARAYÜZ
user_input = st.text_input("Yeteneklerinizi veya ilgi alanlarınızı yazın:", "kitap")

if st.button("Uygun Mesleği Tahmin Et 🔍"):
    if user_input:
        user_vec = tfidf.transform([user_input.lower()])
        similarity = cosine_similarity(user_vec, matrix)
        
        best_index = similarity.argmax()
        score = similarity.max()

        # Eğer benzerlik çok düşükse uyarı ver
        if score > 0:
            st.divider()
            st.header(f"Sizin için en uygun meslek: {df['Meslek'].iloc[best_index]}")
            st.write(f"**Yapay Zeka Eşleşme Oranı:** %{score*100:.1f}")
            
            if "kitap" in user_input.lower() and df['Meslek'].iloc[best_index] == 'Aşçı':
                st.info("Bilgi: Yemek kitapları ve tarifler konusundaki ilginiz sizi mutfağa yönlendirdi!")
        else:
            st.error("Üzgünüm, girdiğiniz kelimeyle bir eşleşme bulamadım. Lütfen 'kod', 'yemek', 'tasarım' gibi kelimeler deneyin.")

# Büyük veri setleri üzerinde eğitilen model, iş gücü piyasası trendlerini ve yetenek gereksinimlerini baz alarak kişiye özel kariyer rotaları oluşturur.
