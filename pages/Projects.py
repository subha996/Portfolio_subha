import streamlit as st
from pages.projects import forest_cover_type, od_yolo, uiml, food101, car_price

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


st.markdown("<h3 style='text-align: center; color: red;'>Projects are here.</h3>", unsafe_allow_html=True)


# creating select box for projects
project = st.selectbox(label="Please select project from below drop down.",
                      options=[
                          "UI ML - Create Machine Learning Model Without Code.",
                          "Food Vision Big™",
                          "Object Detection with Yolo",
                          "Used Car Price Prediction™",
                          "Forest Cover Type Prediction",  
                      ])


if project == "UI ML - Create Machine Learning Model Without Code.":
    uiml.run_uiml()
elif project == "Object Detection with Yolo":
    od_yolo.run_od_yolo()
elif project == "Forest Cover Type Prediction":
    forest_cover_type.run_forest_cover_type()
elif project == "Food Vision Big™":
    food101.run_food101()
elif project == "Used Car Price Prediction™":
    car_price.run_car_price()