import streamlit as st
from main import Code
import openai
from streamlit_chat import message as st_message
##openai.api_key='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'
openai.api_key = st.secrets["SECRET_KEY"]
def app():
        
    # Creating an object of prediction service
    pred = Code()

    #api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

    # Using the streamlit cache 
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input)
     
        # Setting up the Title
    if "history" not in st.session_state:
        st.session_state.history = []

    st.title("🕹️ GPT-3 Chatbot")

    st.write(f"""
        ## Made with ❤️ for 🤖 by The Achievers
        """)
        
    st.write("---")

    st.image("chefbot_image.png", use_column_width=True)

    input = st.text_input('Input:')

    if st.button('Submit'):
        #st.write('**Output**')
        ## st.write(f"""---""")
        with st.spinner(text='In progress'):
            report_text = process_prompt(input)
            #st.markdown(report_text)

        st.session_state.history.append({"message": input, "is_user": True})
        st.session_state.history.append({"message": report_text, "is_user": False})

    for chat in st.session_state.history:
        st_message(**chat)


    ## video
    vid=open('chatbot_vid.mp4', 'rb').read()
    st.video(vid)




