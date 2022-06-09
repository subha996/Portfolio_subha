import streamlit as st
import os
from streamlit_player import st_player

def run_od_yolo():
    st.markdown("<h3 style='text-align: center; color: red;'>🤖 Object Detection with YoloV5 🤖</h3>", unsafe_allow_html=True)

    st.write("Used state-of-the-art object detection model YoloV5 trained on [COCO 80 classes](https://github.com/ultralytics/yolov5/blob/master/data/coco.yaml), default weights are used. \
    Used [streamlit](https://streamlit.io/) for the webpage")

    col1, col2, col3 = st.columns(3)
    col2.image(os.path.join("images", "diagram_yolo.png"))
    st.markdown("<h4 style='text-align: left; color: red;'>To run the program on the local machine, follow below steps.</h4>", unsafe_allow_html=True)

    drsc1 = """
    1. Clone the repository

    2. Create an virtual env (python>=3.8)

    3. pip install -r requirements.txt

    4. streamlit run st.py

    Application should open on your default browser
    """
    st.write(drsc1)
    drsc2 = """You can upload an image or video file, the app will understand and \
    will show you a message about your file type and inference will proceed as 
    per your file type. Click on the infer button to start the inference. 
    The inference will take time as per your file size and system configuration. 
    one sample image and video are provided contained in the samples_inputs folder,
    although it can perform detection from any video or image that is uploaded. 
    After the completion of the inference output will appear along with a download link for the file.
    [GIthub](https://github.com/subha996/OD-yolov5_1)
    """
    st.write(drsc2)   
    st.write("[Demo Video](https://www.youtube.com/watch?v=lLWXCNhjrUA&ab_channel=SubhabrataNath)") # video link
    with st.spinner("Please wait until the player is loading"):
        st_player("https://youtu.be/lLWXCNhjrUA") # yotube link

    
