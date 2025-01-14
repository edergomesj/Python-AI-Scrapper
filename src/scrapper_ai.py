import streamlit as st
#import langchain
#import langchain_ollama
#import selenium
#import beautifulsoup4
#import lxml
#import html5lib
#import python_dotenv

st.title("AI Web Scrapper")
url = st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    st.write("Scraping Website...")