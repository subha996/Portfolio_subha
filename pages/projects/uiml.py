import os
import streamlit as st
from streamlit_player import st_player

def run_uiml():
    st.markdown("<h3 style='text-align: center; color: red;'>🤖 UI-ML 🤖™</h3>", unsafe_allow_html=True)

    st.write("<h5 style='text-align: center;'>🎈Create Machine Learning Model by just <b>Clicking</b>🎈</h5>", unsafe_allow_html=True)

    summary = """
                Quickly load your tabular data, perform Exploratory Data Analysis, \
                choose problem type, select algorithm, tune hyperparameter, check validation metrics, \
                and download your model with out writing single line of code.
    """
    st.write(summary)
    col1, col2, col3  = st.columns(3)
    col2.image(os.path.join("images", "uiml.png"), caption="UI ML", width=600)
    st.write("[Web Link](http://uiml.herokuapp.com/)" + "\n" + "Please wait until the below page is loading")
    uiml_src = "http://uiml.herokuapp.com/"
    st.components.v1.iframe(uiml_src, width=1300, height=800, scrolling=True)

    # http://uiml.herokuapp.com/ # deployment link
    st.write("[Demo Video](https://youtu.be/6wd-zUU0UMQ?list=PLPL68eAk13ftZWE40_teT3NCWW5ChFqWs)")
    with st.spinner("Please wait until the player is loading"):
        st_player("https://youtu.be/6wd-zUU0UMQ?list=PLPL68eAk13ftZWE40_teT3NCWW5ChFqWs")
