import streamlit as st
from transformers import pipeline

# Load the English NER model
@st.cache_resource
def load_ner_model():
    return pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

ner_pipeline = load_ner_model()

st.set_page_config(page_title="AI Entity Detector", page_icon="🏷️")
st.title("🏷️ English Named Entity Recognition")
st.write("### NLP Project 3: Entity Intelligence")

# User Input
default_text = "Elon Musk founded SpaceX in California back in 2002."
user_input = st.text_area("Enter English Text:", default_text)

if st.button("Extract Entities"):
    entities = ner_pipeline(user_input)
    
    st.markdown("---")
    if entities:
        st.subheader("Results:")
        for ent in entities:
            tag_map = {"PER": "👤 PERSON", "LOC": "📍 LOCATION", "ORG": "🏢 ORGANIZATION", "MISC": "✨ MISC"}
            label = tag_map.get(ent['entity_group'], ent['entity_group'])
            st.success(f"**{ent['word']}** is a **{label}**")
    else:
        st.warning("No entities found.")

st.caption("21-Project Portfolio - NLP Final")