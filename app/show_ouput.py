import streamlit as st

def show_ouput(result):
    st.subheader('당신의 추천 음식점입니다.')
    st.write(result)

    