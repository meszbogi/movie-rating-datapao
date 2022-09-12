from app.review_penalizer import calculate_review_penalty
import pandas as pd

def test_penalty_calculation():
    movies = [{'movieID': '0',
               'title': 'title_0',
               'rating': 7.6,
               'votes': 1200000},
               {'movieID': '1',
               'title': 'title_1',
               'rating': 7.6,
               'votes': 1000000}
            ]
    result = calculate_review_penalty(movies)
    assert result.equals(pd.DataFrame([
                       {'movieID': '0',
                        'title': 'title_0',
                        'rating': 7.6,
                        'votes': 1200000,
                        'review_penalty': 0},
                       {'movieID': '1',
                        'title': 'title_1',
                        'rating': 7.6,
                        'votes': 1000000,
                        'review_penalty': -0.2}]))