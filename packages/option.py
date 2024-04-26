import streamlit as st
import wikipedia
from PIL import Image
import pytesseract
import textwrap

from packages import entity_recognizer, part_of_speech

INTRO = """
Innovative AI Playground is an application for children from third to sixth class to enhance their learning journey through interactive learning using artificial intelligence. It helps students to understand concepts or terms in their study materials using entity recognition. Parts of speech
Integration for vocabulary and grammar.

Using natural language processing, based on search terms like a word or term,retrieves relevant search results with highlighted key entities and color coded parts of speech to understand the meaning and context. In the Image to Text category, the student can upload an image of a .png file format, and the highlight entity and parts of speech category can be used for understanding the study material uploaded in the app.

By Leveraging Open AI, the Speech to Text category with an audio recorder where the students can read or speak by clicking on the mic in the interface, further displaying the entities and parts of speech in the text captured through audio."""


def introduction():
    st.markdown(INTRO, unsafe_allow_html=True)
    
def option_menu(text: str):
    option = st.radio("Select Visualization", ("Entity Recognizer", "Part of Speech Tagging"),horizontal=True)
    if option == "Entity Recognizer":
        entity_recognizer.visualize_entities(text)
    elif option == "Part of Speech Tagging":
        part_of_speech.pos_tagging(text)
    
def search():
    input_text = st.text_input("Search", "")
    if input_text:
        option_menu(wikipedia.summary(input_text))
        
def image_to_text():
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    with st.container(border = True):
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)
            option_menu(textwrap.fill(text, 100))
            #st.markdown(textwrap.fill(text, 100))


def speech_to_text():
    pass
    