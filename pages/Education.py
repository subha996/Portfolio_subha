import streamlit as st

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


st.markdown("<h3 style='text-align: center; color: red;'>Education</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# graduation
col1.markdown("<h3 style='text-align: left; color: red;'>Graduation</h3>", unsafe_allow_html=True)
col1.write("I have completed my Bachelors in from the West Bengal University of Technology (Kolkata).")
col1.write("* West Bengal University of Technology")
col1.write("* August, 2015 to Jun 2019")


col2.markdown("<h3 style='text-align: left; color: red;'>Schooling</h3>", unsafe_allow_html=True)
col2.write("I have done my 12th grade from West Bengal Council of Higher Secondary Education (Kolata)")
col2.write("* West Bengal Council of Higher Secondary Education")
col2.write("* Jan 2013 to Aug 2015")


