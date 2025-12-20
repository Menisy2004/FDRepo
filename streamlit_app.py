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

