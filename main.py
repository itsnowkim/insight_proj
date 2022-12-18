import streamlit as st

from app.input_form import user_info, user_mbti
from app.eval_type import eval_type
from app.recommender_system import recommender_system
from app.show_ouput import show_ouput

if __name__ == "__main__":
    st.title("Mealpick")
    st.header("당신의 한 끼를 책임질 mealpick")
    

    expander1 = st.expander("Start stage 1")
    with expander1:
        information = user_info()
    
    expander2 = st.expander("Start stage 2")
    with expander2:
        information["mbti"] = user_mbti()
    
    expander3 = st.expander("Start stage 2")
    with expander3:
        # 추천을 진행할 알고리즘 선택
        selected_type = eval_type()

        # 유저 정보와 추천 방식으로 추천 알고리즘 진행
        if st.button('추천받기!'):
            print(information, selected_type)
            result = recommender_system(information, selected_type)
            
            # output 보여주기
            if result != '':
                show_ouput(result)

