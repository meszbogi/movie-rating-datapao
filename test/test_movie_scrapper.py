from schema import Schema, And, Use
from movie_scrapper import get_top_20_movie_info

def test_srapped_structure():
    schema = Schema([{
        "movieID": str,
        "title": str,
        "votes": int,
        "oscars": int
    }])
    top = get_top_20_movie_info()

    assert schema.is_valid(top) == True

def test_number_of_movies():
    top = get_top_20_movie_info()

    assert len(top) == 20
