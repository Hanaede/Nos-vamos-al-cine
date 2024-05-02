"""
Author: Enrique Mariño Jiménez
"""
from v185.menu import Menu
from v185.tmbd_class import Tmdbclient


def main():
    tmdb_client = Tmdbclient()
    menu = Menu(tmdb_client)
    menu.show_menu()


if __name__ == '__main__':
    main()
