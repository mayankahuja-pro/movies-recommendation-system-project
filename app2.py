import streamlit as st
import pickle 
import pandas as pd
import requests

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name= st.selectbox(
    "Select a movie you like:",
    movies['title'].values,
)

def fetch_poster(movie_title):
    api_key = "YOUR_OMDB_API_KEY"  # Get free key from http://www.omdbapi.com/apikey.aspx
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey=3ac16529"
    response = requests.get(url)
    data = response.json()
    return data.get('Poster', 'https://via.placeholder.com/300x450?text=No+Poster')

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_title = movies.iloc[i[0]].title
        recommended_movie_names.append(movie_title)
        recommended_movie_posters.append(fetch_poster(movie_title))
    return recommended_movie_names, recommended_movie_posters

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])