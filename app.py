import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended


st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    rec = recommend(selected_movie)
    for movie in rec:
        st.write(movie)
