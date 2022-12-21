import streamlit as st
import pandas as pd
import numpy as np
from .utils import construct_horizontal_star

from sklearn.metrics.pairwise import cosine_similarity

def content_based_rec(user_id:str, user_input=dict):
    df = pd.read_csv('csv/data_v1.csv')
    df_user = df.iloc[:, [1, 5, 26, 27, 28, 29, 30, 31, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]].copy()
    df_user.columns = np.arange(len(df_user.columns))
    df_user.set_index(0, inplace=True)
    df_user.dropna(inplace=True)
    df_user.loc[df_user[1]=='남성', 1] = 0
    df_user.loc[df_user[1]=='여성', 1] = 1
    df_user[1] = df_user[1].astype('int')
    
    # input 처리
    input_index = user_input['name']
    input_value = list()
    input_value.append(0 if user_input['gender']=='남성' else 0)
    input_value.extend(user_input['taste'])
    for category in ['한식', '양식', '일식', '중식', '아시안', '분식', '패스트푸드']:
        if category in user_input['preference_category']:
            input_value.append(1)
        else:
            input_value.append(0)
    input_value.extend(user_input['menu_preference'])
    input_value.extend(user_input['mbti'])
    
    df_user.loc[input_index] = input_value

    
    cosine_sim = cosine_similarity(df_user)
    df_sim = pd.DataFrame(data=cosine_sim, index=df_user.index, columns=df_user.index)
    sim_users = df_sim[user_id].sort_values(ascending=False).iloc[1:11].index
    
    pred = df.loc[df['Respondent ID'].isin(sim_users)].iloc[:, 133:151].mean().sort_values(ascending=False)
    print(pred)
    
    return [(pred.index[i], pred[i]) for i in range(5)]

def matrix_factorization_rec_(user=None, dataframe=None, predicted_ratings=None, user_input=dict):
    dataframe = pd.read_csv('csv/data_v1.csv')
    predicted_ratings = pd.read_csv('csv/prediced_ratings_mf.csv', index_col=0)
    df_mf_sg = dataframe.iloc[:, [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]].copy()
    df_mf_sg.fillna(0, inplace=True)
    
    df_input = pd.DataFrame(data= user_input['rate'], columns=[user_input['name']], index=predicted_ratings.columns)
    
    rate_exist = df_input.loc[df_input[user_input['name']] != 0]
    rate_nan = df_input.loc[df_input[user_input['name']] == 0]
    
    predicted_ratings['similarity'] = cosine_similarity(predicted_ratings[rate_exist.index], df_input.loc[df_input[user_input['name']] != 0].values.reshape(1, -1))

    pred = predicted_ratings.loc[predicted_ratings['similarity'].nlargest(3).index].mean()[rate_nan.index].sort_values(ascending=False)
    
    print(pred)
    
    return [(pred.index[i], pred[i]) for i in range(5)]

def implicit_feedback_rec_(user=None, dataframe=None, predicted_ratings=None, user_input=dict):
    dataframe = pd.read_csv('csv/data_v1.csv')
    predicted_ratings = pd.read_csv('csv/prediced_ratings_im.csv', index_col=0)
    df_mf_sg = dataframe.iloc[:, [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]].copy()
    df_mf_sg.fillna(0, inplace=True)
    
    df_input = pd.DataFrame(data= user_input['rate'], columns=[user_input['name']], index=predicted_ratings.columns)
    
    rate_exist = df_input.loc[df_input[user_input['name']] != 0]
    rate_nan = df_input.loc[df_input[user_input['name']] == 0]
    
    predicted_ratings['similarity'] = cosine_similarity(predicted_ratings[rate_exist.index], df_input.loc[df_input[user_input['name']] != 0].values.reshape(1, -1))

    pred = predicted_ratings.loc[predicted_ratings['similarity'].nlargest(3).index].mean()[rate_nan.index].sort_values(ascending=False)
    
    print(pred)
    
    return [(pred.index[i], pred[i]) for i in range(5)]

def star(num:float):
    # star_full='★'
    # star_empty='☆'
    path_full = './img/full.png'
    path_half = './img/half.png'
    path_emp = './img/empty.png'
    rnum = round(num, 1)

    # for i in range(int(rnum)):
    #     st.image(path_full, width=20)

    full_star = construct_horizontal_star(rnum)
    st.markdown(full_star, unsafe_allow_html=True)

    # if (rnum-int(rnum)>=0.5 and rnum-int(rnum)<1):
    #     st.image(path_half, width=20)
    st.write(rnum)



def recommender_system(information, selected_type):
    st.subheader(f'{selected_type}에 의한 추천시스템 알고리즘 시작')
    
    #content_based_rec
    if selected_type == 'type1':
        rec_cb = content_based_rec(information['name'], information)
        print(rec_cb)
        for i in rec_cb:
            st.write(i[0])
            star(i[1])

    # [TODO] streamlit- Star Rate 받는부분 구현 이후 info['rate'] 지우기 
    #                   rate length = 28개
    if selected_type == 'type2':
        information['rate'] = [0, 3, 2, 1, 4, 5, 0, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 3, 2, 0, 1, 5, 0, 0, 2, 4, 4]
        rec_cb = matrix_factorization_rec_(user_input=information)
        
        for i in rec_cb:
            st.write(i[0])
            star(i[1])

    if selected_type == 'type3':
        information['rate'] = [0, 3, 2, 1, 4, 5, 0, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 3, 2, 0, 1, 5, 0, 0, 2, 4, 4]
        rec_cb = implicit_feedback_rec_(user_input=information)
        for i in rec_cb:
            st.write(f'"{i[0]}"에 대한 예상 선호도 :{(i[1]*100)}')
    
    
    return rec_cb[0]
