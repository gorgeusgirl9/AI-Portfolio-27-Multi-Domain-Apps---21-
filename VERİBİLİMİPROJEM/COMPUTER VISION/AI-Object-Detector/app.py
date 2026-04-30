import streamlit as st
from transformers import pipeline
from PIL import Image, ImageDraw

st.set_page_config(page_title="AI Object Detector", page_icon="🎯")

@st.cache_resource
def load_detector():
    # Nesne tespiti için Facebook'un DETR modelini kullanıyoruz
    return pipeline("object-detection", model="facebook/detr-resnet-50")

st.title("🎯 AI Object Detector")
st.write("### Computer Vision Serisi: Proje 2/3")

detector = load_detector()

uploaded_file = st.file_uploader("Bir fotoğraf yükle (Sokak, oda, manzara...)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    with st.spinner('Nesneler tespit ediliyor...'):
        results = detector(image)
        
        # Kutuları çizmek için resmi kopyala
        draw = ImageDraw.Draw(image)
        
        for res in results:
            box = res['box']
            label = res['label']
            score = res['score']
            
            # Sadece %80 ve üzeri güvenli sonuçları göster
            if score > 0.8:
                # Koordinatları al ve kutuyu çiz
                draw.rectangle([(box['xmin'], box['ymin']), (box['xmax'], box['ymax'])], outline="red", width=4)
                draw.text((box['xmin'], box['ymin']), f"{label} {int(score*100)}%", fill="red")
        
        # Az önceki hatayı almamak için doğru komutu kullanıyoruz
        st.image(image, caption='Tespit Edilen Nesneler', use_column_width=True)
        
        st.subheader("Bulunan Nesnelerin Listesi:")
        for res in results:
            if res['score'] > 0.8:
                st.write(f"- ✅ **{res['label'].capitalize()}** (Güven: %{res['score']*100:.1f})")

st.caption("21-Project Portfolio - Computer Vision Project 14")