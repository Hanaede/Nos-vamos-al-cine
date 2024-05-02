"""
Author: Enrique Mariño Jiménez
"""
import os
import requests
import json
import socket


class Tmdbclient:
    def __init__(self):
        self.__API_KEY = os.environ.get('TMDB_API_KEY')
        self.__BASE_URL = 'https://api.themoviedb.org/3'

    @property
    def is_internet_available(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False

    def internet_check(self):
        if not self.is_internet_available:
            raise Exception("No hay conexión a internet")

    # Opción 1
    def get_id_by_movie_name(self, movie_name):
        try:
            self.internet_check()
            movie_data = self.collect_info_movie(movie_name)

            results_movie_list = movie_data['results']
            if results_movie_list:
                first_movie_id = results_movie_list[0]['id']
                print(f"Código de la película '{movie_name}': {first_movie_id}")
            else:
                print("No se encontraron películas con ese nombre.")
        except (requests.exceptions.HTTPError, Exception) as err:
            self.print_error_message(err)

    def collect_info_movie(self, movie_name):
        url = f"{self.__BASE_URL}/search/movie"
        params = {'api_key': self.__API_KEY, 'query': movie_name}
        return self.get_response_api(params, url)

    def get_response_api(self, params, url):  # Utilizado también por collect_genres_film
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_json_file = response.json()
        self.save_to_json(response_json_file)
        return response_json_file

    # Opción 2
    def get_movie_info_by_id(self, movie_id):
        try:
            self.internet_check()
            self.collect_info_move_id(movie_id)

        except (requests.exceptions.HTTPError, Exception) as err:
            self.print_error_message(err)

    def collect_info_move_id(self, movie_id):
        url = f"{self.__BASE_URL}/movie/{movie_id}"
        params = {'api_key': self.__API_KEY}
        response = requests.get(url, params=params)
        response.raise_for_status()
        movie_info_json = response.json()
        self.save_to_json(movie_info_json)
        self.print_movie_info(movie_info_json)

    @staticmethod
    def print_movie_info(movie_info_json):
        print("Título:", movie_info_json['title'])
        print("Géneros", end=": ")
        for genre in movie_info_json['genres']:
            print(genre['name'], end=", ")
        print("\b\b")
        print("Argumento:", movie_info_json['overview'])
        print("Duración:", f"{movie_info_json['runtime']} minutos")
        print("Enlace a IMDb:", f"https://www.imdb.com/title/{movie_info_json['imdb_id']}")
        # Se pueden añadir los datos que quiera buscando en la key en el diccionario

    # Opción 3
    def get_similar_movies(self, movie_name):
        try:
            self.internet_check()
            movie_data = self.collect_info_movie(movie_name)  # Mismo método que en la opción 1
            self.search_similar_films(movie_data)

        except (requests.exceptions.HTTPError, Exception) as err:
            self.print_error_message(err)

    def search_similar_films(self, movie_data):
        results_movie_list = movie_data['results']
        if results_movie_list:
            movie_id = results_movie_list[0]['id']  # id guardado de la película introducida

            similar_movies = self.get_info_similar_movies(movie_id)  # Películas similares con el id anterior

            if similar_movies['results']:
                similar_movies = [movie['title'] for movie in similar_movies['results'][:5]]
                print("Películas similares:")
                for movie_title in similar_movies:
                    print(movie_title)
            else:
                print("No se encontraron películas similares.")
        else:
            print("No se encontraron películas con ese nombre.")

    def get_info_similar_movies(self, movie_id):
        url = f"{self.__BASE_URL}/movie/{movie_id}/similar"
        params = {'api_key': self.__API_KEY}
        response = requests.get(url, params=params)
        response.raise_for_status()
        similar_info_json = response.json()
        return similar_info_json

    # Opción 4
    def get_trending_movies_week(self):
        try:
            self.internet_check()
            week_trending_info = self.get_info_trending_week()

            if week_trending_info['results']:
                trending_movies = []
                for movie in week_trending_info['results'][:5]:
                    trending_movies.append(movie['title'])
                self.save_to_json({"Trending semanal": trending_movies})
                self.print_movies(trending_movies)
            else:
                print("No se encontraron películas trending.")

        except (requests.exceptions.HTTPError, Exception) as err:
            self.print_error_message(err)

    def get_info_trending_week(self):
        url = f"{self.__BASE_URL}/trending/movie/week"
        params = {'api_key': self.__API_KEY}
        response = requests.get(url, params=params)
        response.raise_for_status()
        trending_info_week = response.json()
        return trending_info_week

    # Opción 5
    def get_trending_movies_day(self):
        try:
            self.internet_check()
            day_trending_info = self.get_info_trending_day()

            if day_trending_info['results']:
                trending_movies = []
                for movie in day_trending_info['results'][:5]:
                    trending_movies.append(movie['title'])
                self.save_to_json({"Trending diario": trending_movies})
                self.print_movies(trending_movies)
            else:
                print("No se encontraron películas trending.")

        except (requests.exceptions.HTTPError, Exception) as err:
            self.print_error_message(err)

    def get_info_trending_day(self):
        url = f"{self.__BASE_URL}/trending/movie/day"
        params = {'api_key': self.__API_KEY}
        response = requests.get(url, params=params)
        response.raise_for_status()
        trending_info_day = response.json()
        return trending_info_day

    # Opción 6
    def get_all_genres(self):
        try:
            self.internet_check()
            movie_genres_info = self.collect_genres_films()

            if movie_genres_info['genres']:
                genres_list = []
                for genre in movie_genres_info['genres']:
                    genres_list.append(genre['name'])
                    genres_list.append(genre['id'])
                self.save_to_json({"Géneros disponibles": genres_list})
                self.print_movies(genres_list)
            else:
                print("No se encontraron géneros disponibles.")

        except (requests.exceptions.HTTPError, Exception) as err:
            self.print_error_message(err)

    def collect_genres_films(self):
        url = f"{self.__BASE_URL}/genre/movie/list"
        params = {'api_key': self.__API_KEY}
        return self.get_response_api(params, url)

    @staticmethod
    def print_movies(movies_info):
        for info in movies_info:
            print(info)

    @staticmethod
    def save_to_json(data):
        with open("tmdb_response.json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def print_error_message(error):
        print(f"Error: {error}")
