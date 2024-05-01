"""
Author: Enrique Mariño Jiménez
"""


class Menu:
    def __init__(self, tmdb_client):
        self.tmdb_client = tmdb_client

    def show_menu(self):
        while True:
            print("\n¿Qué quieres hacer?:")
            print("1. Buscar el ID de una película por su nombre")
            print("2. Obtener información de una película proporcionando su código")
            print("3. Obtener películas similares a una proporcionada")
            print("4. Películas trending semanales")
            print("5. Películas trending del día")
            print("6. Mostrar todos los géneros disponibles")
            print("7. Salir")
            print("\n")

            choice = input("Selecciona la opción que quieras: ")

            if choice == '1':
                movie_name = input("Ingrese el nombre de la película: ")
                self.tmdb_client.get_id_by_movie_name(movie_name)
            elif choice == '2':
                movie_id = input("Ingrese el código de la película: ")
                self.tmdb_client.get_movie_info_by_id(movie_id)
            elif choice == '3':
                movie_name = input("Ingrese el nombre de la película: ")
                self.tmdb_client.get_similar_movies(movie_name)
            elif choice == '4':
                print("Películas trending semanales: ")
                self.tmdb_client.get_trending_movies_week()
            elif choice == '5':
                print("Películas trending del día: ")
                self.tmdb_client.get_trending_movies_day()
            elif choice == '6':
                self.tmdb_client.get_all_genres()
            elif choice == '7':
                print("¡Hasta luego! :)")
                break
            else:
                print("¡No has seleccionado bien! Por favor, seleccione una opción válida. :D")
