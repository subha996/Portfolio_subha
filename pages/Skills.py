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

st.write("I passionate about Data Science and Machine Learning. I have a background in Python, SQL, I am also familiar with C++, and C")

st.markdown("<h3 style='text-align: center; color: red;'>Programming Language</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.write("* Python")
col3.write("* C++")


st.markdown("<h3 style='text-align: center; color: red;'>Skills</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.write("* Python")
col2.write("* SQL")
col3.write("* Pandas")
col1.write("* Numpy")
col2.write("* Scikit-Learn")
col3.write("* Matplotlib")
col1.write("* Tensorflow")
col2.write("* Keras")
col3.write("* Pytorch")
col1.write("* OpenCV")
col2.write("* Flask")
col3.write("* Streamlit")

