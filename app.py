import streamlit as st
from streamlit_option_menu import option_menu

from packages import option

def main():
    st.set_page_config(page_title="Innovative AI Playground", page_icon=":books:", layout="wide")
    st.title("Innovative AI Playground")
    
    
    with st.sidebar:
        Options: list = ["Introduction" ,"Search", "Image to Text"]
        selected: str = option_menu("Main Menu", Options, 
            icons=['clipboard', 'search', 'image'], menu_icon="cast", default_index=0)
        
    if selected == "Introduction":
        option.introduction()
    elif selected == "Search":
        option.search()
    elif selected == "Image to Text":
        option.image_to_text()

if __name__ == "__main__":
    main()