from imdb import Cinemagoer, IMDbError

def get_top_20_movie_info():
    movie_info = []
    try:
        ia = Cinemagoer()
        top = ia.get_top250_movies()
        for mv in top[:20]:
            info = ia.get_movie(mv.movieID, info=['awards'])
            oscars = len([oscar for oscar in info['awards'] if oscar['award'] == 'Oscar'])
            movie = {"movieID": mv.movieID,
                    "title": mv['title'],
                    "votes": mv['votes'],
                    "oscars": oscars
            }
            movie_info.append(movie)
    except IMDbError as e:
        print(e)
    return movie_info
