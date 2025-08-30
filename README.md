# 🎬 Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit that suggests similar movies based on user preferences.

## ✨ Features

- 🔍 **Smart Recommendations**: Get 5 similar movies based on your selection
- 🎭 **Visual Interface**: Movie posters fetched from OMDb API
- ⚡ **Fast Performance**: Optimized with caching for quick responses
- 📱 **Responsive Design**: Works on desktop and mobile devices

 

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **ML**: Cosine Similarity
- **API**: OMDb API for movie posters
- **Deployment**: Streamlit Community Cloud

## 📊 How It Works

1. **Data Processing**: Movie features are vectorized using TF-IDF
2. **Similarity Calculation**: Cosine similarity between movie vectors
3. **Recommendation Engine**: Returns top 5 most similar movies
4. **Visual Display**: Fetches and displays movie posters

## 🏃‍♂️ Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
