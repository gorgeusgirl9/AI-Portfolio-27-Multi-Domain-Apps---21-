import streamlit as st
from transformers import pipeline
from PIL import Image

st.set_page_config(page_title="AI Image Classifier", page_icon="📸")

# Modeli önbelleğe alarak yükleyelim
@st.cache_resource
def load_classifier():
    # En güvenli model: Google ViT
    return pipeline("image-classification", model="google/vit-base-patch16-224")

st.title("📸 AI Image Classifier")
st.write("### Computer Vision Serisi: Proje 1/3")

try:
    classifier = load_classifier()
    
    uploaded_file = st.file_uploader("Bir resim seçin (JPG, PNG)...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Yüklenen Resim', use_container_width=True)
        
        if st.button("Resmi Analiz Et"):
            with st.spinner('Yapay zeka inceliyor...'):
                results = classifier(image)
                st.markdown("---")
                st.subheader("Tahminler:")
                for res in results:
                    st.write(f"🔍 **{res['label'].capitalize()}**: %{res['score']*100:.2f}")
                    st.progress(res['score'])
except Exception as e:
    st.error(f"Bir hata oluştu: {e}")

st.caption("21-Project Portfolio - Computer Vision")