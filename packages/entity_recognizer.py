import streamlit as st
import spacy
from spacy import displacy

NLP = spacy.load("en_core_web_sm")

def visualize_entities(text):
    if text:
        doc = NLP(text)
        entity_labels = {ent.label_ for ent in doc.ents}
        ner_words = [ent.text for ent in doc.ents]
        entity_types = st.multiselect("Select Entity Type", ("ALL",)+ tuple(entity_labels), ("ALL"))
        output: str = '' 
        if not entity_types or entity_types == ["ALL"]:
            output = displacy.render([doc], style="ent")
            st.write(output, unsafe_allow_html=True)
        else:
            output = displacy.render([doc], style="ent", options={"ents": entity_types})
            st.write(output, unsafe_allow_html=True)