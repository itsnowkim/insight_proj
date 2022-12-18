import os
import streamlit as st
import numpy as np

def eval_type():
    st.subheader('_추천받을 방식_을 고르는 :blue[checkbox]입니다. 추천을 위해 선택해 주세요. :sunglasses:')

    col1, col2 = st.columns(2)

    with col1:
        selected_eval_type = st.radio(
            "추천받을 타입을 골라주세요 👇",
            ["type1", "type2", "type3"],
            key="visibility",
            horizontal=False,
        )
        

    with col2:
        if selected_eval_type == "type1":
            st.text("type1")
            st.text("type 1 추천 방식에 대한 설명")
        elif selected_eval_type == "type2":
            st.text("type2")
            st.text("type 2 추천 방식에 대한 설명")
        else:
            st.text("type3")
            st.text("type 3 추천 방식에 대한 설명")

    # 선택한 type에 맞게 추천 실행
    