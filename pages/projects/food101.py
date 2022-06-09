import streamlit as st
import os
from streamlit_player import st_player

# 
def run_food101():
    st.markdown("<h3 style='text-align: center; color: red;'>Food 101 Classifier™</h3>", unsafe_allow_html=True)
    st.write("A image classifier based on the Food 101 dataset")

    note = """ 
    \n
    This project based on the [Food101](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/) Paper which used Convolutional network trained for 2 to 3 days to achieve 77.4% top-1 accuracy.
    The project is made by download the food101 dataset from the [TensorFlow dataset](https://www.tensorflow.org/datasets/catalog/food101)(size: 4.6GB) which consists of 750 images x 101 training classes = 75750 training images.
    I used the [EfficientNetB0](https://www.tensorflow.org/api_docs/python/tf/keras/applications/EfficientNetB0) model with fine-tune unfreeze all layers of the model. \n
    Although this WebApp model accuracy is around 80% to 82%. I am also sharing the [notebook](https://colab.research.google.com/drive/15sJJhrZBo12CA3flnrX-NC4WwrP84z0D?usp=sharing) for this project.
    [Github](https://github.com/subha996/food-101_updated)
    """
    st.write(note)
    co1, col2, col3 = st.columns(3)
    col2.image(os.path.join("images","food101.png"))
    deploy_link = "[WebApp](https://share.streamlit.io/subha996/food-101_updated/main/food101.py)"
    st.write(deploy_link + "\n" + "Please wait until the below page is loading") 
    src = "https://share.streamlit.io/subha996/food-101_updated/main/food101.py"
    st.components.v1.iframe(src, width=1300, height=700, scrolling=True)
    # video
    st.write("[Video Link](https://youtu.be/tP1Zj2f6TQU)")
    st_player("https://youtu.be/tP1Zj2f6TQU")
    
