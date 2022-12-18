import streamlit as st

from app.input_form import user_info
from app.eval_type import eval_type
from app.recommender_system import recommender_system
from app.show_ouput import show_ouput

if __name__ == "__main__":
    st.title("Mealpick")
    st.header("당신의 한 끼를 책임질 mealpick")
    
    information = user_info()
    selected_type = eval_type()

    # 유저 정보와 추천 방식으로 추천 알고리즘 진행
    result = recommender_system(information, selected_type)

    # output 보여주기
    show_ouput(result)
    
