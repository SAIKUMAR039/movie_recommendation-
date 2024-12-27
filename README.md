# Movie Recommendation App

This is a simple movie recommendation application that fetches movie data from the TMDB API and recommends movies based on genre or mood.

## Features

- Fetches popular movies from the TMDB API.
- Recommends movies based on genre.
- Recommends movies based on mood.
- Displays movie information including title, genre, rating, and description.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/movie_recommendation.git
    cd movie_recommendation
    ```

2. Install the required dependencies:
    ```sh
    pip install requests
    ```

## Usage

1. Replace `'your_api_key'` in [app.py](http://_vscodecontentref_/1) with your actual TMDB API key.

2. Run the application:
    ```sh
    python app.py
    ```

3. Follow the menu prompts to browse movies or get recommendations based on genre or mood.

## Code Overview

### [Movie](http://_vscodecontentref_/2) Class

Represents a movie with attributes like title, genre, rating, and description. It also has a method to display movie information.

### [RecommendationEngine](http://_vscodecontentref_/3) Class

An abstract base class for recommendation engines. It defines an abstract method [recommend](http://_vscodecontentref_/4) that must be implemented by subclasses.

### [GenreRecommendationEngine](http://_vscodecontentref_/5) Class

A subclass of [RecommendationEngine](http://_vscodecontentref_/6) that recommends movies based on genre.

### [MoodRecommendationEngine](http://_vscodecontentref_/7) Class

A subclass of [RecommendationEngine](http://_vscodecontentref_/8) that recommends movies based on mood. It uses a predefined mood-to-genre mapping.

### [NetflixApp](http://_vscodecontentref_/9) Class

The main application class that:
- Initializes the app with a name and an empty movie list.
- Fetches a genre map from the TMDB API.
- Fetches popular movies from the TMDB API and populates the movie list.
- Provides methods to browse all movies and recommend movies based on genre or mood.

## Example

```sh
Menu:
1. Browse all movies
2. Recommend movies by genre
3. Recommend movies by mood
4. Exit
Enter your choice: 1

All Movies:
**Title:** Inception
**Genre:** Sci-Fi
**Rating:** 8.8
**Description:** A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.

...