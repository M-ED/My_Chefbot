import app2
import streamlit as st
from streamlit_chat import message as st_message
import openai
import main
##openai.api_key='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'
openai.api_key = st.secrets["SECRET_KEY"]

#st.set_page_config(
 #  page_title="GPT-3 Chatbot",
  # page_icon="🐾",
  # layout="centered")

# Pages as key-value pairs
PAGES = {
    "Dashboard": app2
}

st.sidebar.title('Go to:')

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
