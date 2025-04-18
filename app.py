import streamlit as st
import dask.dataframe as dd
from dask.distributed import Client
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from collections import Counter
 
client = Client("tcp://192.168.137.162:8786")
 
load = pd.read_csv('movies.csv')
df = dd.from_pandas(load)
 
df = df.compute()
word_could_dict = Counter(df['genres'].tolist())
judul_movie = df['title'].tolist()
genre_movie = df['genres'].tolist()
 
data_pandas = pd.DataFrame({
    'judul': judul_movie,
    'genre': genre_movie
})
 
data = dd.from_pandas(data_pandas, npartitions=4)
 
genre_counts = data['genre'].value_counts()
 
value_genre = genre_counts.compute().reset_index()
value_genre.columns = ['genre', 'count']
 
judul = data['judul'].compute().tolist()
genre = data['genre'].compute().tolist()
 
tf = CountVectorizer()
tf.fit(genre) 
tfidf_matrix = tf.fit_transform(genre) 
tfidf_matrix.todense()
cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['judul'], columns=genre)
 
cosine_sim = cosine_similarity(tfidf_matrix)
 
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['judul'], columns=data['judul'])
indices = pd.Series(data.index, index=data['judul']).drop_duplicates()
 
def movie_recommendations(judul, cosine_sim, items=data[['judul', 'genre']]):
    idx = indices.loc[judul] 
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:20] 
    movie_indices = [i[0] for i in sim_scores]
    result = items.loc[movie_indices].compute()
    return result[['judul', 'genre']].values.tolist()
    # return data.loc[movie_indices, 'judul'].compute().tolist()
 
recomendation = movie_recommendations('Johnny English Reborn (2011)', cosine_sim)

st.title("Sistem Rekomendasi Film")
selected_movie = st.selectbox('Pilih Film', judul_movie)
 
if selected_movie:
    recomendation = movie_recommendations(selected_movie, cosine_sim)
    selected_genre = data[data['judul'] == selected_movie]['genre'].compute().values[0]
    st.write(f"Rekomendasi untuk film **{selected_movie}**: {selected_genre}")
    for r in recomendation:
        st.write(f"- **{r[0]}** (Genre: {r[1]})")
    # for r in recomendation:
    #     st.write(r)
 
# Menutup client Dask setelah selesai (tidak diperlukan dalam aplikasi ini)
# client.close()