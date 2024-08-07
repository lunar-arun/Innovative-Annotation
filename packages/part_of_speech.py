import streamlit as st
import spacy
from IPython.core.display import HTML



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


def pos_tagging(text):
    if text:
        doc = NLP(text)
        tag = {word.pos_ for word in doc}
        pos_types = {word.pos_ for word in doc}
        pos_tags = st.multiselect("Select Part of Speech Tags", ("ALL",) + tuple(pos_types),("ALL"))
        for pos, color in POS_COLORS.items():
            if pos in tag:
                st.sidebar.markdown(f'<div style="display:flex; align-items: center;"><div style="background-color:{color}; width:20px; height:20px; margin-right:10px; border-radius: 5px;"></div><div>{pos}</div></div>', unsafe_allow_html=True)            
        if len(pos_tags) == 0 or pos_tags[0] == "ALL":
            # Generate HTML markup to highlight each word with its POS tag using colors
            html = "<div>"
            for token in doc:
                # Get the color for the POS tag, default to white if not found
                color = POS_COLORS.get(token.pos_, "#FFFFFF")
                html += f"<a href='https://www.google.com/search?q={token.text}' style='text-decoration: none;'><span style='background-color: {color}; color: white; padding: 2px; margin: 3px; border-radius: 0.3em;'>{token.text} </span></a>"
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
        st.write(HTML(html), unsafe_allow_html=True)    
       
              