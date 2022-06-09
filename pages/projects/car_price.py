import os
import streamlit as st
from streamlit_player import st_player


def run_car_price():
    st.markdown("<h3 style='text-align: center; color: red;'>Used Car Price Prediction™</h3>", unsafe_allow_html=True)
    note = """
    Regression problem predict used car price by analyzing features. 
    Here you can predict used car 🚙 price by giving some information like car brand, 
    model of the car, how much the car has been driven and so on. 
    User have to give some information about car, like how much the car has driven, model, brand e.t.c 
    and based on these feature the car price will be predicted.
    """
    st.write(note)
    col1, col2,col3 = st.columns(3)
    col2.image(os.path.join("images", "car_price_pred.png"))
    car_price_src = "https://share.streamlit.io/subha996/used-car-price-prediction/main/main.py"
    st.write("[Web Link](https://share.streamlit.io/subha996/used-car-price-prediction/main/main.py)" + "\n" + "Please wait until the below page is loading") 
    st.components.v1.iframe(car_price_src, width=1300, height=800, scrolling=True)

    st_player("https://www.youtube.com/watch?v=ia6E3C4aIzQ&list=PLPL68eAk13fsESpD9_-2fl6zb-PFknvd8&index=7")
    st.write("[Full Playlist](https://www.youtube.com/playlist?list=PLPL68eAk13fsESpD9_-2fl6zb-PFknvd8)")
    st.write("[Detailed Report can be found here.](https://github.com/subha996/Used-Car-Price-Prediction/blob/main/sales%20car%20price%20predictions.pptx)")