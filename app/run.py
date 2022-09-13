from email.policy import default
from pydoc import cli
from movie_scraper import get_top_n_movie_info
from review_penalizer import calculate_review_penalty
from oscar_rewarder import calculate_oscar_score
import click

@click.command()
@click.option('-n', '--number-of-movies', default=20, help='The number of movies to adjust the score of. (It will get the top n movie)', show_default=True)
@click.option('-f', '--filename', default='movies_with_recalculated_scores', help='The filename where the results should be saved.', show_default=True)
@click.option('-e', '--extension', type=click.Choice(['json', 'csv', 'parquet'], case_sensitive=False), default='json', help='The file format which in the result will be saved.', show_default=True)
def run(number_of_movies, filename, extension):
    movies = get_top_n_movie_info(number_of_movies)
    recalculated = recalculate_imdb_scores(movies)
    name = '{}.{}'.format(filename, extension)
    match extension:
        case 'json':
            recalculated.to_json(name)
        case 'csv':
            recalculated.to_csv(name, header=True, index=False)
        case 'parquet':
            recalculated.to_parquet(name)
        case _:
            print('Invalid file extension. Use either json, csv or parquet.')

def recalculate_imdb_scores(movies):
    with_review_penalty = calculate_review_penalty(movies)
    with_oscar_score = calculate_oscar_score(with_review_penalty)

    with_oscar_score['adjusted'] = with_oscar_score['rating'] + \
                                   with_oscar_score['review_penalty'] + \
                                   with_oscar_score['oscar_score']
    return with_oscar_score[['movieID', 'title', 'votes', 'oscars', 'rating', 'adjusted']]

if __name__ == '__main__':
    run()