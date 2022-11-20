import streamlit as st 

st.header("Web app made with streamlit :)")
st.subheader("File uploader")
fileup = st.file_uploader(label="Upload files here", type=['png', 'jpg', 'webp', 'jpeg'], accept_multiple_files=True)
for i in fileup:
    st.write('filename:', i.name)


st.subheader("Input text")
title = st.text_input(label="Enter your name: ", value="")
if title != '':
    st.write('Hello!', title)
else:
    st.write('Hello')