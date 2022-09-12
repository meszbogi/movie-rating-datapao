from app.run import recalculate_imdb_scores
import pandas as pd
from decimal import Decimal

def test_rating_recalculation():
    movies = [{'movieID': '0',
            'title': 'title_0',
            'rating': Decimal('7.6'),
            'votes': 1200000,
            'oscars': 3},
            {'movieID': '1',
            'title': 'title_1',
            'rating': Decimal('7.6'),
            'votes': 1000000,
            'oscars': 1}
        ]
    result = recalculate_imdb_scores(movies)
    assert result.equals(pd.DataFrame([
                            {'movieID': '0',
                            'title': 'title_0',
                            'votes': 1200000,
                            'oscars': 3,
                            'rating': Decimal('7.6'),
                            'adjusted': Decimal('8.1')}, #7.6-0.0+0.5
                            {'movieID': '1',
                            'title': 'title_1',
                            'votes': 1000000,
                            'oscars': 1,
                            'rating': Decimal('7.6'),
                            'adjusted': Decimal('7.7')}])) #7.6-0.2+0.3