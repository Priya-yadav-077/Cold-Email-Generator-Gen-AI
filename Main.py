import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from Chain import Chain
from portofolio import Portfolio
from utils import clean_text

def create_streamlit(llm,portfolio,clean_text):
    st.title("Cold Email Generator")
    input=st.text_input("enter the url:",value="https://atliq.keka.com/careers/jobdetails/53247")
    button=st.button("Generate Email")
    if button:
        try:
            loader=WebBaseLoader([input])
            data=clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs=llm.extract_job(data)
            for job in jobs:
                skill=job.get('skill',[])
                Links=portfolio.get_query(skill)
                email=llm.write_mail(job,Links)
                st.code(email,language='markdown')
        except Exception as e:
            st.error(f"An error occured:{e}")

if __name__=="__main__":
    llm=Chain()
    portfolio=Portfolio()
    st.set_page_config(layout="centered",page_title="Cold Email Generator",page_icon="📧")
    create_streamlit(llm,portfolio,clean_text)



