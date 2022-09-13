from decimal import Decimal
from schema import Schema
from app.movie_scraper import get_top_n_movie_info

def test_scrapped_structure():
    schema = Schema([{
        "movieID": str,
        "title": str,
        "rating": Decimal,
        "votes": int,
        "oscars": int
    }])
    top = get_top_n_movie_info(1)

    assert schema.is_valid(top) == True

def test_number_of_movies():
    top_default = get_top_n_movie_info()
    top_5 = get_top_n_movie_info(5)
    
    assert len(top_default) == 20
    assert len(top_5) == 5
