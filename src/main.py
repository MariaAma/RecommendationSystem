import streamlit as st
import appFile

st.set_page_config(page_title="anime_recommendations", page_icon="🚀")

st.header(':blue[**Welcome to this project!**]')
st.subheader(":violet[*You don't know, what anime to watch?*]")
st.subheader(":violet[DON'T WORRY, I got you!]")

title = st.text_input(":blue[Tell me your favorite Anime.]")

if st.button(":blue[Sumbit]"):
    appFile.app(title)
    

