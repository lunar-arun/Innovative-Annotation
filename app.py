import spacy
from spacy import displacy

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

import pytesseract
import textwrap

import wikipedia


NLP = spacy.load("en_core_web_sm")

POS_COLORS = {
        "ADJ": "#FF5733",  # Adjective
        "ADP": "#FFD700",  # Adposition
        "ADV": "#00FFFF",  # Adverb
        "AUX": "#FF6347",  # Auxiliary verb
        "CONJ": "#FF00FF",  # Coordinating conjunction
        "CCONJ": "#FF00FF",  # Coordinating conjunction (alternative)
        "DET": "#32CD32",  # Determiner
        "INTJ": "#00FF7F",  # Interjection
        "NOUN": "#1E90FF",  # Noun
        "NUM": "#FF8C00",  # Numeral
        "PART": "#FFA500",  # Particle
        "PRON": "#9370DB",  # Pronoun
        "PROPN": "#FF1493",  # Proper noun
        "PUNCT": "#696969",  # Punctuation
        "SCONJ": "#000080",  # Subordinating conjunction
        "SYM": "#8B008B",  # Symbol
        "VERB": "#800080",  # Verb
        "X": "#708090"  # Other
    }

def visualize_entities(text):
    if text:
        doc = NLP(text)
        entity_labels = {ent.label_ for ent in doc.ents}
        entity_types = st.multiselect("Select Entity Type", ("ALL",) + tuple(entity_labels), ("ALL"))
        if not entity_types or entity_types == ["ALL"]:
            output = displacy.render([doc], style="ent")
            st.write(output, unsafe_allow_html=True)
        else:
            output = displacy.render([doc], style="ent", options={"ents": entity_types})
            st.write(output, unsafe_allow_html=True)

def pos_tagging(text):
    # Load the English language model    
    # Process the text with SpaCy
    if text:
        doc = NLP(text)
        tag = {word.pos_ for word in doc}
        pos_types = {word.pos_ for word in doc}
        pos_tags = st.multiselect("Select Part of Speech Tags", ("ALL",) + tuple(pos_types),("ALL"))
        for pos, color in POS_COLORS.items():
            if pos in tag:
                st.sidebar.markdown(f'<div style="display:flex; align-items: center;"><div style="background-color:{color}; width:20px; height:20px; margin-right:10px; border-radius: 5px;"></div><div>{pos}</div></div>', unsafe_allow_html=True)
                
        if pos_tags[0] == "ALL" or len(pos_tags) == 0:
            # Generate HTML markup to highlight each word with its POS tag using colors
            html = "<div>"
            for token in doc:
                # Get the color for the POS tag, default to white if not found
                color = POS_COLORS.get(token.pos_, "#FFFFFF")
                html += f"<a href='https://www.google.com/search?q={token.text}' style='text-decoration: none;'><span style='background-color: {color}; text-decoration: none; color: white; padding: 2px; margin: 3px; border-radius: 0.3em;'>{token.text} </span></a>"
            html += "</div>"
        else:
            # Generate HTML markup to highlight each word with its POS tag using colors
            html = "<div>"
            for token in doc:
                if token.pos_ in pos_tags:
                # Get the color for the POS tag, default to white if not found
                    color = POS_COLORS.get(token.pos_, "#FFFFFF")
                    html += f"<a href='https://www.google.com/search?q={token.text}' style='text-decoration: none;'><span style='background-color: {color};  color: white; padding: 2px; margin: 3px; border-radius: 0.3em;'>{token.text} </span></a>"
                else:
                    html += f"<span>{token.text} </span>"
            html += "</div>"

        st.write(html, unsafe_allow_html=True)

def extract_text_from_image(uploaded_file):

    # Display uploaded image
    image = Image.open(uploaded_file)
    #st.image(image, caption='Uploaded Image', use_column_width=True)
    text = pytesseract.image_to_string(image)
    return textwrap.fill(text, 100)

def search(search_text):
    try:
        if search_text:
            results = wikipedia.summary(search_text, sentences = 4)
            doc = NLP(results) 
            return doc
    except wikipedia.exceptions.DisambiguationError:
        return None        

def main():
    st.title("Innovative Annotation Application")
    selected = option_menu(None, ["Entity Recognition", "Part Of Speech", "Image To Text"], 
        icons=["house", "book", "camera"], menu_icon="cast", default_index=0, orientation="horizontal")
    if selected == "Entity Recognition":
        results = search(st.text_input("Enter text:"))
        visualize_entities(results)
    elif selected == "Part Of Speech":
        results = search(st.text_input("Enter text:"))
        pos_tagging(results)
    elif selected == "Image To Text":
        
        uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
        if uploaded_file is not None: 
            results = extract_text_from_image(uploaded_file)
            option = st.radio("Select Visualization", ("Entity Recognizer", "Part of Speech Tagging"),horizontal=True)
            if option == "Entity Recognizer":
                visualize_entities(results)
            elif option == "Part of Speech Tagging":
                pos_tagging(results)


if __name__ == '__main__':
    main()        