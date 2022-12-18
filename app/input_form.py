import streamlit as st

from .constants import menus, tastes, questions
from .utils import construct_styled_component

def user_mbti():
    st.markdown("<hr/>", unsafe_allow_html=True)
    html = construct_styled_component("h4",0,"사용자 특성을 받는","입력 form ","입니다. <br>더 정확한 추천을 위해 입력해 주세요. 😎")
    st.markdown(html, unsafe_allow_html=True)
    
    # 저장할 유저 정보
    score = [1,2,3,4,5]
    answer = []
    
    with st.container():
        st.markdown("#### 0 ~ 5 점까지 선택해 주세요")
        for question, val in questions.items():
            point = st.select_slider(
                question,
                options=[val[0],1,2,3,4,val[1]]
            )
            if point == val[0]:
                point = 0
            elif point == val[1]:
                point = 1
            assert isinstance(point, int), 'Argument of wrong type!'
            
            answer.append(point)
    
    if len(answer) == 13:
        return answer

def user_info():
    st.markdown("<hr/>", unsafe_allow_html=True)
    html = construct_styled_component("h3",0,"사용자 정보를 받는","입력 form ","입니다. <br>추천을 위해 입력해 주세요. 😎")
    st.markdown(html, unsafe_allow_html=True)
    
    # 저장할 유저 정보
    user = {}
    score = [1,2,3,4,5]
    
    with st.container():
        st.markdown("#### 이름을 입력해 주세요")
        name = st.text_input(
            "이름을 입력해 주세요 👇",
            placeholder="당신의 이름은?"
        )
        if name != '':
            user["name"] = name
            st.write(f"{name}님, 반갑습니다.")

            st.markdown("#### 성별을 입력해 주세요")
            gender = st.radio(
                "성별을 입력해 주세요",
                ('남성', '여성'))
            user["gender"] = gender
            
            if user["gender"]:
                st.markdown('#### 맛에 대한 선호도를 나타내 주세요')
                taste = []
                for idx, t in enumerate(tastes):
                    taste.append(st.radio(
                        t,
                        score,
                        horizontal=True,
                        key = idx
                        ))
                user["taste"] = taste
                if user["taste"] :
                    user["preference_category"] = st.multiselect(
                        '선호하는 음식 분류를 선택하세요 (복수 선택 가능)',
                        ['한식','양식','일식','중식','아시안','분식','패스트푸드']
                    )
                    
                    st.markdown('#### 음식 메뉴에 따른 선호도')
                    st.write("1점 : 싫어함  \n  2점 : 찾아서 먹진 않지만 먹긴 함  \n  3점 : 종종 먹음 (상관없음)  \n  4점 : 상당히 좋아하는 편  \n  5점 : 제일 좋아하는 메뉴 중 하나 ")
                    menu_preference = []
                    for idx, menu in enumerate(menus):
                        menu_preference.append(st.radio(
                            menu,
                            score,
                            horizontal=True,
                            key = idx+143
                        ))
                    user["menu_preference"] = menu_preference
    return user