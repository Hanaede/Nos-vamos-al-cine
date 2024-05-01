"""
Author: Enrique Mariño Jiménez
"""
from v181c.menu import Menu
from v181c.tmbd_class import TMDBClient


def main():
    tmdb_client = TMDBClient()
    menu = Menu(tmdb_client)
    menu.show_menu()


if __name__ == '__main__':
    main()
