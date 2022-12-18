import streamlit as st

from .utils import construct_styled_component

def eval_type():
    html = construct_styled_component("h3",0,"추천받을 방식을 고르는","알고리즘"," 입니다. <br>추천을 위해 선택해 주세요. 😎")
    st.markdown(html, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    available_type = ["type1", "type2", "type3"]

    with col1:
        selected_eval_type = st.radio(
            "추천받을 타입을 골라주세요 👇",
            available_type,
            horizontal=False,
        )

    with col2:

        selected_element = construct_styled_component("span",available_type.index(selected_eval_type),"선택한 추천 방식은",selected_eval_type, "입니다.")

        if selected_eval_type == "type1":
            st.markdown(selected_element, unsafe_allow_html=True)
            st.text("type 1 추천 방식에 대한 설명")
        elif selected_eval_type == "type2":
            st.markdown(selected_element, unsafe_allow_html=True)
            st.text("type 2 추천 방식에 대한 설명")
        else:
            st.markdown(selected_element, unsafe_allow_html=True)
            st.text("type 3 추천 방식에 대한 설명")

    return selected_eval_type