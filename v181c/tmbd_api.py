"""
Author: Enrique Mariño Jiménez.
"""
from v181c.menu import Menu
from v181c.tmbd_class import Tmdbclient


def main():
    tmdb_client = Tmdbclient()
    menu = Menu(tmdb_client)
    menu.show_menu()


if __name__ == '__main__':
    main()
