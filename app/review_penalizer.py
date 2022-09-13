import pandas as pd
from decimal import Decimal

def calculate_review_penalty(movies):
    movie_df = pd.DataFrame(movies)

    max_votes = movie_df['votes'].max()
    movie_df['review_penalty'] = movie_df['votes'].apply(lambda v: Decimal(str(round(((v - max_votes)/100000)*0.1, 1))))
    return movie_df