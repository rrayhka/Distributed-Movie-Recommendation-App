# 🎬 Distributed Movie Recommendation System

This project is a **Content-Based Movie Recommendation System** built with Python. It uses **Streamlit** for the interactive web interface and **Dask** to enable distributed data processing. The system analyzes movie genres to compute similarities and recommends films that are most similar to a selected title.

---

## 📽️ Demo Video

📽️ A tutorial video demonstrating how the system works is available [here](https://drive.google.com/file/d/1hm_4OhGE4cLMDNK88SOSX1sZVLgq5bXM/view?usp=sharing). Please watch it to understand how to use the app.

---

## 🧠 Key Features

- ⚡ **Distributed Processing with Dask** – Efficient parallel processing of movie data.
- 🧾 **Content-Based Filtering** – Recommends movies based on genre similarity.
- 📊 **Cosine Similarity + CountVectorizer** – Uses basic NLP techniques to calculate similarity scores.
- 🖥️ **Interactive Interface** – Built with Streamlit for a clean and simple user experience.

---

## 🧰 Technologies Used

- Python 3
- [Dask](https://www.dask.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- Pandas

---

## ⚠️ Notes

- The `movies.csv` file must contain at least the `title` and `genres` columns.
- Genres should be pipe-separated (e.g., `Action|Adventure|Fantasy`) and will be transformed into feature vectors.
- This is a content-based recommendation system; it does **not** rely on user behavior or ratings (i.e., not collaborative filtering).

---

## 📫 Contact

Developed by **Akhyar** and Team.
