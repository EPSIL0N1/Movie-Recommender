import streamlit as st
import pickle
import pandas as pd
import requests

# Movies Dataset
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Similarity Dataset
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Fecth Poster

def fetch_poster(movie_id):
    
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3Yjk4YjYwYTBkYjFlYjQ4ZTU4ZmRiNGE1YjJmNmEzMiIsInN1YiI6IjY2MDVhOWEzZmNlYzJlMDE4NmM1NDM2NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.IyGwdeiaQQlClEBLoPNLR1otE0DgTFyfAlNM1BG5YBs"
    }

    response = requests.get(url, headers=headers)
    # print(response.text)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    
    
    

# Movie Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1:6]
    
    r_list = []
    r_list_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        r_list.append(movies.iloc[i[0]].title)
        r_list_poster.append(fetch_poster(movie_id))
        
    return r_list, r_list_poster


# Frontend
st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Enter Movie Name for Recommendation', movies['title'].values)

if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)
    for i in range(5):
        # st.write(i)
        st.write(names[i])
        st.image(poster[i])

