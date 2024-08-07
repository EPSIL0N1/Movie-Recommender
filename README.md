# Movie Recommender System

Welcome to the Movie Recommender System! This is a Streamlit-based web application that recommends movies based on a user's input.

## Features

- **Movie Recommendations**: Input a movie name and get recommendations for similar movies.
- **Movie Posters**: View movie posters for the recommended movies.

## Installation

To get started, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EPSIL0N1/EPIC_Final_Project.git
   cd EPIC_Final_Project
   ```

2. **Install dependencies**:
   Ensure you have Python 3.7+ installed. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:
   ```
   streamlit
   pandas
   requests
   ```

3. **Prepare datasets**:
   - Ensure `movies_dict.pkl` and `similarity.pkl` are in the root directory. These are pickled files containing the movie data and similarity matrix, respectively.

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

   The application will start, and you can access it via the provided local URL.

## Code Overview

### Dependencies

```python
import streamlit as st
import pickle
import pandas as pd
import requests
```

### Loading Data

- **Movies Dataset**: Loaded from `movies_dict.pkl` and converted to a DataFrame.
- **Similarity Dataset**: Loaded from `similarity.pkl`.

### Functions

- **`fetch_poster(movie_id)`**: Fetches the movie poster URL using The Movie Database (TMDb) API.

- **`recommend(movie)`**: Recommends similar movies based on the input movie name. Returns a list of recommended movie names and their corresponding posters.

### Streamlit Frontend

- **Title**: "Movie Recommender System"
- **Movie Selector**: Dropdown menu for selecting a movie.
- **Recommendation Button**: Fetches and displays recommendations and posters when clicked.

## API Key

The app uses The Movie Database (TMDb) API for fetching movie posters. Ensure you have a valid API key and replace the existing placeholder key in the `fetch_poster` function with your own.

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [The Movie Database (TMDb)](https://www.themoviedb.org/)
