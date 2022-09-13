from app.oscar_rewarder import calculate_oscar_score, oscar_score
import pandas as pd
from decimal import Decimal

def test_scores():
    assert oscar_score(1) == Decimal('0.3')
    assert oscar_score(-1) == Decimal('0.0')
    assert oscar_score(11) == Decimal('1.5')

def test_oscar_scores():
    movies = [{'movieID': '0',
               'title': 'movie_0',
               'oscars': 1},
               {'movieID': '1',
               'title': 'movie_1',
               'oscars': 3},
               {'movieID': '2',
               'title': 'movie_2',
               'oscars': 6},
               {'movieID': '3',
               'title': 'movie_3',
               'oscars': 11}]
    result = calculate_oscar_score(movies)
    print(result)
    assert result.equals(pd.DataFrame([
              {'movieID': '0',
               'title': 'movie_0',
               'oscars': 1,
               'oscar_score': Decimal('0.3')},
              {'movieID': '1',
               'title': 'movie_1',
               'oscars': 3,
               'oscar_score': Decimal('0.5')},
              {'movieID': '2',
               'title': 'movie_2',
               'oscars': 6,
               'oscar_score': Decimal('1.0')},
              {'movieID': '3',
               'title': 'movie_3',
               'oscars': 11,
               'oscar_score': Decimal('1.5')}]))