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


st.markdown("<h3 style='text-align: center; color: red;'>Professional Experiece</h3>", unsafe_allow_html=True)

st.write("Having working experience on Data Science project involved developing models and finding the best solution for \
getting efficient result. Currently working as Jr Data Analyst focused on developing computer vision model and creating APIs. \
Continuously learning and looking forward to growing and utilizing my analytical skills, programming knowledge, \
 along Engineering techniques")

st.markdown("<h4 style='text-align: left; color: red;'>Finacus Solutions Private Limited.</h4>", unsafe_allow_html=True)
st.write("A product and service-based firm for banking and finance sectors making and providing services for digital banking solutions")
st.write("* Jr Data Analyst (Machine Learning Engineer)")
st.write("* Dec 2021 to Present")
st.write("* Mumbai, India")

st.markdown("<h5 style='text-align: center; color: red;'>Key Qualification and Responsibilities</h5>", unsafe_allow_html=True)
st.write("* Understanding and applying the requirements of digital products and services ")
st.write("* Creating and understanding product architecture and planning with team members.")
st.write("* Data Collecting and writing modular code for data preprocessing to make the data accessible for model development.")
st.write("* Developing Deep Learning (for computer vision) models for the development of products as needed.")
st.write("* Developed chatbot for assisting customers' needs.")


st.markdown("<h3 style='text-align: center; color: red;'>Intership Experiece</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left; color: red;'>iNeuron Pvt Ltd</h4>", unsafe_allow_html=True)
st.write("AI Tech product-driven organization and educational sector carrying domestic international clients and providing quality education for Data Science")
st.write("* Sep 2021 to Dec 2021")
st.write("* Bengalore, India")

st.markdown("<h5 style='text-align: center; color: red;'>Key Qualification and Responsibilities</h5>", unsafe_allow_html=True)
st.write("* Design, build and evaluate machine learning models for predictive learning.")
st.write("* Use of statistical techniques, machine learning, data mining to build a scalable and innovative solution ")
st.write("* Develop modular code for large-scale data analysis, data validation, data encoding, model validation. ")
st.write("* Writing High-Level Documents, Low-Level Documents, and Designing Architecture.")
