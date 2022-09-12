import pandas as pd

def calculate_review_penalty(movies):
    movie_df = pd.DataFrame(movies)

    max_votes = movie_df['votes'].max()
    movie_df['review_penalty'] = movie_df['votes'].apply(lambda v: round((v - max_votes)/100000)*0.1, 1)
    return movies