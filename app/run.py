from app.movie_scrapper import get_top_20_movie_info
from app.review_penalizer import calculate_review_penalty
from app.oscar_rewarder import calculate_oscar_score

def run():
    movies = get_top_20_movie_info()
    recalculated = recalculate_imdb_scores(movies)
    recalculated.to_json("movies_with_racalculated_scores.json")

def recalculate_imdb_scores(movies):
    with_review_penalty = calculate_review_penalty(movies)
    with_oscar_score = calculate_oscar_score(with_review_penalty)

    with_oscar_score['adjusted'] = with_oscar_score['rating'] + \
                                   with_oscar_score['review_penalty'] + \
                                   with_oscar_score['oscar_score']
    return with_oscar_score[['movieID', 'title', 'votes', 'oscars', 'rating', 'adjusted']]

if __name__ == '__main__':
    run()