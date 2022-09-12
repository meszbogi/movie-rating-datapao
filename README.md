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

The main functionalty is in **/app/run.py**. To run the application start this scrip from the project structrure:
`python .\app\run.py`

For testing I used the **pytest** library. Run unit tests from the **app** folder with the following command: `python -m pytest ..\test\`. More details about pytest [here](https://docs.pytest.org/en/latest/how-to/usage.html)

*This setup is required while the python -m command adds the current folder to syspath, which required for have the necessery imports for testing.*
