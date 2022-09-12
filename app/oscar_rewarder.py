import pandas as pd
from decimal import Decimal

def calculate_oscar_score(movies):
    movie_df = pd.DataFrame(movies)
    movie_df['oscar_score'] = movie_df['oscars'].apply(lambda o: oscar_score(o))
    return movie_df

def oscar_score(num_oscars):
    match num_oscars:
                case o if o in range(1,3):
                    score = Decimal('0.3')
                case o if o in range(3,6):
                    score = Decimal('0.5')
                case o if o in range(6,10):
                    score = Decimal('1.0')
                case o if o >= 10:
                    score = Decimal('1.5')
                case _:
                    score = 0
    return score