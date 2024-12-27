from abc import ABC, abstractmethod
import requests

# Movie Class
class Movie:
    def __init__(self, title, genre, rating, description):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.description = description

    def display_info(self):
        return f"**Title:** {self.title}\n**Genre:** {self.genre}\n**Rating:** {self.rating}\n**Description:** {self.description}\n"

# Abstract Recommendation Engine Class
class RecommendationEngine(ABC):
    @abstractmethod
    def recommend(self, movies, criterion):
        pass

# Genre Recommendation Engine Class
class GenreRecommendationEngine(RecommendationEngine):
    def recommend(self, movies, genre):
        return [movie for movie in movies if movie.genre.lower() == genre.lower()]

# Mood Recommendation Engine Class
class MoodRecommendationEngine(RecommendationEngine):
    def recommend(self, movies, mood):
        mood_map = {
            "happy": ["Comedy", "Adventure"],
            "sad": ["Drama", "Romance"],
            "excited": ["Action", "Thriller"],
            "thoughtful": ["Sci-Fi", "Documentary"],
            "scared": ["Horror"],
            "curious": ["Mystery"],
            "inspired": ["Biography"]
        }
        genres = mood_map.get(mood.lower(), [])
        return [movie for movie in movies if movie.genre in genres]

# Main App Class
class NetflixApp:
    def __init__(self, name):
        self.name = name
        self.movies = []
        self.genre_map = self.fetch_genre_map()

    def fetch_genre_map(self):
        url = "https://api.themoviedb.org/3/genre/movie/list?api_key=5a6c420f1b7a72698ed6fe37cf856d0f&language=en-US"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {genre['id']: genre['name'] for genre in data['genres']}
        else:
            print("Failed to fetch genre map from API")
            return {}

    def browse_movies(self):
        return self.movies

    def recommend_movies(self, genre=None, mood=None):
        if genre:
            engine = GenreRecommendationEngine()
            return engine.recommend(self.movies, genre)
        elif mood:
            engine = MoodRecommendationEngine()
            return engine.recommend(self.movies, mood)
        else:
            return []

    def fetch_movies_from_api(self, api_key):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                genre_name = self.genre_map.get(item['genre_ids'][0], "Unknown")  # Simplified for example purposes
                movie = Movie(
                    title=item['title'],
                    genre=genre_name,
                    rating=item['vote_average'],
                    description=item['overview']
                )
                self.movies.append(movie)
        else:
            print("Failed to fetch movies from API")

# Initialize App
app = NetflixApp("NetflixApp")

# Fetch movies from API (replace 'your_api_key' with an actual API key)
app.fetch_movies_from_api('5a6c420f1b7a72698ed6fe37cf856d0f')

# Menu system for user input
while True:
    print("\nMenu:")
    print("1. Browse all movies")
    print("2. Recommend movies by genre")
    print("3. Recommend movies by mood")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nAll Movies:")
        for movie in app.browse_movies():
            print(movie.display_info())
    elif choice == '2':
        user_genre = input("Enter a genre: ")
        print("\nRecommended Movies by Genre:")
        for movie in app.recommend_movies(genre=user_genre):
            print(movie.display_info())
    elif choice == '3':
        user_mood = input("Enter a mood: ")
        print("\nRecommended Movies by Mood:")
        for movie in app.recommend_movies(mood=user_mood):
            print(movie.display_info())
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")