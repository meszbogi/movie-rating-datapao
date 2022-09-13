from imdb import Cinemagoer, IMDbError
from decimal import Decimal

def get_top_n_movie_info(n=20):
    movie_info = []
    try:
        ia = Cinemagoer()
        top = ia.get_top250_movies()
        for mv in top[:n]:
            info = ia.get_movie(mv.movieID, info=['awards'])
            oscars = len([oscar for oscar in info['awards'] if oscar['award'] == 'Oscar'])
            movie = {"movieID": mv.movieID,
                    "title": mv['title'],
                    "rating": Decimal(str(mv['rating'])),
                    "votes": mv['votes'],
                    "oscars": oscars
            }
            movie_info.append(movie)
    except IMDbError as e:
        print(e)
    return movie_info
