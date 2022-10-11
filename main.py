import streamlit as st
from training_data import defaultPrompt
import openai

## openai.api_key='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'
openai.api_key = st.secrets["SECRET_KEY"]
class Code:
    def __init__(self):
        print("Model Initialization--->")

    def query(self, prompt, myKwargs={}):
        kwargs = {
            #"model":"text-davinci-002",
            "temperature":0.9,
             "max_tokens":150,
              "top_p":1,
              "frequency_penalty":0,
               "presence_penalty":0.6,
            "stop": ["Person:"]
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.Completion.create(prompt=prompt, **kwargs, engine="text-davinci-002")["choices"][0]["text"].strip()
        return r

    def model_prediction(self, input):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        ##set_openai_key(api_key)
        output = self.query(defaultPrompt.format(input))
        return output

