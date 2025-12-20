import streamlit as st

st.set_page_config(page_title='Face Detection Project', layout='wide')
st.title('😄 Face detection Model')

st.info('This app builds a machine learning model!')

section = st.sidebar.radio(
    "Go to",
    [
        "Introduction",
        "Dataset",
        "Model Architecture",
        "Training",
        "Results",
        "Live Demo",
        "Conclusion"
    ]
)

if section == "Introduction":
    st.header("Introduction")
    st.write("""
    Face detection is a computer vision task that identifies human faces in images or videos.
    This project implements a deep learning-based face detection model capable of detecting
    faces under different lighting and pose conditions.
    """)


