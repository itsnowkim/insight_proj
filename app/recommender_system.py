import streamlit as st
import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

def content_based_rec(user_id:str, user_input=dict):
    df = pd.read_csv('./data_v1.csv')
    df_user = df.iloc[:, [1, 5, 26, 27, 28, 29, 30, 31, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]].copy()
    df_user.columns = np.arange(len(df_user.columns))
    df_user.set_index(0, inplace=True)
    df_user.dropna(inplace=True)
    df_user.loc[df_user[1]=='남성', 1] = 0
    df_user.loc[df_user[1]=='여성', 1] = 1
    df_user[1] = df_user[1].astype('int')
    
    # input 처리
    input_index = input['name']
    input_value = list()
    input_value.append(0 if input['gender']=='남성' else 0)
    input_value.extend(input['taste'])
    for category in ['한식', '양식', '일식', '중식', '아시안', '분식', '패스트푸드']:
        if category in input['preference_category']:
            input_value.append(1)
        else:
            input_value.append(0)
    input_value.extend(input['menu_preference'])
    input_value.extend(input['mbti'])
    
    df_user.loc[input_index] = input_value

    
    cosine_sim = cosine_similarity(df_user)
    df_sim = pd.DataFrame(data=cosine_sim, index=df_user.index, columns=df_user.index)
    sim_users = df_sim[user_id].sort_values(ascending=False).iloc[1:11].index
    
    pred = df.loc[df['Respondent ID'].isin(sim_users)].iloc[:, 133:151].mean().sort_values(ascending=False)
    print(pred)
    
    return [(pred.index[i], pred[i]) for i in range(5)]

def recommender_system(information, selected_type):
    st.subheader(f'{selected_type}에 의한 추천시스템 알고리즘 시작')

    if selected_type == content_based_rec:
        st.write(selected_type)
    return ''
    

    