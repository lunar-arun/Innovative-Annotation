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

SUMMER = """Summer is the hottest and brightest of the four temperate seasons, occurring after spring and before autumn. At or centred on the summer solstice, daylight hours are the longest and darkness hours are the shortest, with day length decreasing as the season progresses after the solstice. The earliest sunrises and latest sunsets also occur near the date of the solstice. The date of the beginning of summer varies according to climate, tradition, and culture. When it is summer in the Northern Hemisphere, it is winter in the Southern Hemisphere, and vice versa."""
WINTER ="""Winter is the coldest and darkest season of the year in polar and temperate climates. It occurs after autumn and before spring. The tilt of Earth's axis causes seasons; winter occurs when a hemisphere is oriented away from the Sun. Different cultures define different dates as the start of winter, and some use a definition based on weather. When it is winter in the Northern Hemisphere, it is summer in the Southern Hemisphere, and vice versa. Winter typically brings precipitation that, depending on a region's climate, is mainly rain or snow. The moment of winter solstice is when the Sun's elevation with respect to the North or South Pole is at its most negative value; that is, the Sun is at its farthest below the horizon as measured from the pole. The day on which this occurs has the shortest day and the longest night, with day length increasing and night length decreasing as the season progresses after the solstice."""
MONSOON = """A monsoon is traditionally a seasonal reversing wind accompanied by corresponding changes in precipitation but is now used to describe seasonal changes in atmospheric circulation and precipitation associated with annual latitudinal oscillation of the Intertropical Convergence Zone (ITCZ) between its limits to the north and south of the equator. Usually, the term monsoon is used to refer to the rainy phase of a seasonally changing pattern, although technically there is also a dry phase. The term is also sometimes used to describe locally heavy but short-term rains."""
def introduction():
    st.markdown(INTRO, unsafe_allow_html=True)
    
def option_menu(text: str):
    option = st.radio("Select Visualization", ("Entity Recognizer", "Part of Speech Tagging"),horizontal=True)
    if option == "Entity Recognizer":
        entity_recognizer.visualize_entities(text)
    elif option == "Part of Speech Tagging":
        part_of_speech.pos_tagging(text)
    
def search():
    option = st.selectbox(
        "Select Option",
        ("Default Option", "User Input", "Search(Beta Testing)"),
        index=None,
        )
    if option == "Default Option":
        option_menu(SUMMER)
    elif option == "User Input":
        input_text: str = st.text_input("Input Example Text!", "")
        if input_text:
            option_menu((input_text))
    elif option == "Search(Beta Testing)":  
        input_text: str = st.text_input("Search", "")
        if input_text:
            option_menu(wikipedia.summary(input_text,sentences = 10))
        
def image_to_text():
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    with st.container(border = True):
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            text = pytesseract.image_to_string(image)
            option_menu(textwrap.fill(text, 100))
