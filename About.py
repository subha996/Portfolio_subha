import streamlit as st
import os
from datetime import datetime
from PIL import Image

# making the page wider
st.set_page_config(layout="wide")

# Resizing the sidebar width.
st.markdown(
     """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 150px;
       }
       [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
           width: 1000px;
           margin-left: -1000px;
        }
        </style>
        """,
        unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: red;'>About Myself</h3>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: left; color: red;'>Summary</h5>", unsafe_allow_html=True)

col1, col2  = st.columns(2)
summary = """
Having working experience working on AI Product  involved developing models and finding the best solution for getting 
efficient result. Currently working as Jr Data Analyst focused on developing computer vision model and creating APIs, building chatbotwith Rasa integration on varios \
platforms. 
Continuously learning and looking forward to growing and utilizing my analytical skills, programming knowledge, 
along Engineering techniques.
"""
col1.write(summary)
# image path
img = os.path.join("images", "subha2.jpg")
img = Image.open(img).rotate(270)
col2.image(img)


col1.markdown("<h5 style='text-align: left; color: red;'>Contact</h5>", unsafe_allow_html=True)
col1.write("Email: subhabratanath98@gmail.com")
col1.write("Address: Mumbai, India")
st.write("[Github](https://github.com/subha996)")
# creating resume path
resume = os.path.join("resume", "Resume.pdf")
with open(resume, "rb") as f: # opening the resume file as bytes
  pdf = f.read()
  
# getting the current date and time
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
file_name = "Subhabrata_Nath_Resume_" + date + ".pdf"
col1.download_button(label="Download Resume", data=pdf, file_name=file_name)
