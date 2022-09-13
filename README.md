# movie-rating-datapao

This is a solution for the home assignment **The Big IMDB quest** from **Datapao** by *Boglarka Mesz*

## Setup
The application is written in Python (version 3). 
I used *pipenv* virtual environment manager to handle third-party libraries.

1. Install python 3 (if it is not already done so) and pip
2. Install pipenv (if it is not already done so)
    * `pip install pipenv`
3. Start pipenv shell
    * `pipenv shell`
4. Install third-party libriaries required for the app through pipenv
    * `pipenv install`

## Usage

The main functionalty is in **/app/run.py**. To run the application start this scrip from the project root directory:
`python .\app\run.py`
This will run the script with default configuration values. See configuration possibilites with:
`python .\app\run.py --help`
```
Usage: run.py [OPTIONS]

Options:
  -n, --number-of-movies INTEGER  The number of movies to adjust the score of.
                                  (It will get the top n movie)  [default: 20]
  -f, --filename TEXT             The filename where the results should be
                                  saved.  [default:
                                  movies_with_recalculated_scores]
  -e, --extension [json|csv|parquet]
                                  The file format which in the result will be
                                  saved.  [default: json]
  --help                          Show this message and exit.
```

For testing I used the **pytest** library. Run unit tests from the **app** folder with the following command: `python -m pytest ..\test\`. More details about pytest [here](https://docs.pytest.org/en/latest/how-to/usage.html)

*This setup is required while the python -m command adds the current folder to syspath, which required for have the necessery imports for testing.*
