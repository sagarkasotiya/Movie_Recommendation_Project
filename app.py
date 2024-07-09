import streamlit as st
import pickle
import pandas as pd
import requests

#cosine distance
from sklearn.metrics.pairwise import cosine_similarity
vectors=pickle.load(open('vectors.pkl','rb'))
similarity=cosine_similarity(vectors)

movies_with_id=pickle.load(open('movies_with_id.pkl','rb'))
movies=pd.DataFrame(movies_with_id)

def recommend(movie):
    movie_index=int(movies[movies['title']==movie].index[0])
    l=sorted(list(enumerate([float(dist) for dist in list(similarity[movie_index])])),reverse=True,key=lambda x:x[1])
    movie_indices=[]
    for touple in l[0:5]:
        movie_indices.append(touple[0])
    movies_id=[]
    for index in movie_indices:
        movies_id.append(movies['movie_id'][index])
    
    id=[int(id) for id in movies_id]
    return id


    

api_key = 'd2d4b32b05152dc8aaa36f986035a606' 
def get_movie_poster(movie_id, api_key):
    base_url = "https://api.themoviedb.org/3/movie/"
    response = requests.get(f"{base_url}{movie_id}?api_key={api_key}")
    data = response.json()
    
    if 'poster_path' in data:
        poster_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
        return poster_url
    else:
        return None


st.title("Movie Recommendation System")
input_movie=st.selectbox("Select a movie name to discover similar films:",movies['title'].values)


def fetch_movie_name(movie_id):
     return movies[movies['movie_id']==movie_id]['title'].values[0]
        
if st.button('Recommend'):
    recommendation = recommend(input_movie)
    if recommendation:
        st.subheader("Recommended Movies:")
        cols = st.columns(len(recommendation))
        for col, movie_id in zip(cols, recommendation):
            movie_name=fetch_movie_name(movie_id)
            poster_url = get_movie_poster(movie_id, api_key)
            if poster_url:
                col.image(poster_url, caption=f"{movie_name}", width=150)
            else:
                col.write(f"Poster not found for movie ID: {movie_id}")
    else:
        st.write("No recommendations found.")



st.markdown("""
    <div class="footer">
        <p>Created by Sagar Kasotiya</p>
    </div>
    """, unsafe_allow_html=True)











   
    
    