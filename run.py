from movie_scrapper import get_top_20_movie_info

def run():
    for mv in get_top_20_movie_info():
        print(mv)

if __name__ == '__main__':
    run()