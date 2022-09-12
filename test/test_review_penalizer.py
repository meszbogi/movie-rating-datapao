from app.review_penalizer import calculate_review_penalty
import pandas as pd
from decimal import Decimal

def test_penalty_calculation():
    movies = [{'movieID': '0',
               'title': 'title_0',
               'votes': 1200000},
               {'movieID': '1',
               'title': 'title_1',
               'votes': 1000000}
            ]
    result = calculate_review_penalty(movies)
    assert result.equals(pd.DataFrame([
                       {'movieID': '0',
                        'title': 'title_0',
                        'votes': 1200000,
                        'review_penalty': Decimal('0')},
                       {'movieID': '1',
                        'title': 'title_1',
                        'votes': 1000000,
                        'review_penalty': Decimal('-0.2')}]))