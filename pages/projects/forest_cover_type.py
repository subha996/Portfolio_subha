import streamlit as st
import os


def run_forest_cover_type():
    st.markdown("<h3 style='text-align: center; color: red;'>Forest Cover Type Prediction</h3>", unsafe_allow_html=True)


    st.markdown("<h3 style='text-align: left; color: red;'>Problem Statement</h3>", unsafe_allow_html=True)
    ps = """
    The government is used to employ officers for inspection of the various region to find the Forest cover type are present in 
    a specific region. This process needs a huge amount of manpower, time along money. They have to visit the forest regions
    manually and have to inspect them to Label the Forest type for that region.
    They have collected various geographical information like Elevation, Aspect, 
    and it was observed that the forest type is dependent on these information. 
    It was found that there is some strong relation between collected information and the Forest Cover labels. 
    It was our Problem statement to build a classification methodology to build a system that will be able 
    to predict Forest Cover type based on geographical information.
    """
    st.write(ps)
    # Methodology
    st.markdown("<h3 style='text-align: center; color: red;'>Architecture</h3>", unsafe_allow_html=True)
    archi_img = os.path.join("images", "forest_cover.png")
    col1, col2, col3 = st.columns(3)
    col2.image(archi_img, use_column_width=True)
    st.markdown("<h3 style='text-align: left; color: red;'>Used Tools</h3>", unsafe_allow_html=True)
    st.write("* Python")
    st.write("* Pandas")
    st.write("* Numpy")
    st.write("* Matplotlib")
    st.write("* Seaborn")
    st.write("* Scikit-learn")
    st.write("* Streamlit")
    st.write("Link: [Code can be found here](https://github.com/subha996/Forest-Cover-Type)")

    

