from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
groq_api_key = os.getenv('GROQ_API_KEY')

st.title('Story Writer ChatBot')

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Craft a story based on the user's provided topic and story type and language.please try to answer in user provided language."),
        ("user",["Topic:{topic}","Story_type:{story_type}","Language:{language}"])
    ]
)


# Get user input
topic = st.text_input('Provide a topic for the story:')
story_type = st.text_input('Specify the type of story (e.g., mystery, romance, sci-fi, etc.):')
language = st.text_input('Provide Language which you want to write in story?')

llm = ChatGroq(groq_api_key=groq_api_key, model='llama3-70b-8192')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser



if st.button("Generate"):
    if topic != '' and story_type != '':
        st.write(chain.invoke({'topic':topic,'story_type':story_type,'language':language}))
    else:
        st.write("Please provide both a topic and a story type to generate a story.")

