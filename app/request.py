from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie
'''
This is where we will write code to make requests to our API.
'''
# Getting api key
api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

'''We import the flask application instance. We then import
 the Python urllib.request module that will help us create a
  connection to our API URL and send a request and json modules
   that will format the JSON response to a Python dictionary.
   '''


def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results
    '''We create a get_movies() function that takes in
             a movie category as an argument.We use the .format()
            method on the base_url and pass in the movie category
            and the api_key. this will replace the {} curly brace
            placeholders in the base_url with the category and api_key
            respectively.This creates get_movies_url as the final URL
             for our API request.We then use with as our context manager
            to send a request using the urllib.request.urlopen() function
            that take in the get_movies_url as an argument and sends a request
            as urlWe use the read() function to read the response and store it
            in a get_movies_data variable.We then convert the JSON response to
             a Python dictionary using json.loads function and pass in the
            get_movies_data variable.We then check if the response contains
            any results. If it does we call a process_results() function that
            take in the list of dictionary objects and returns a
             list of movie objects.
            '''


def process_results(movie_list):
    '''
    Function  that processes the movie result and transform
     them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)
    return movie_results
    '''We create a function process_results() that takes in a list
     of dictionaries. We create an empty list movie_results this is
    where we will store our newly created movie objects.We then loop
    through the list of dictionaries using the get() method and pass
    in the keys so that we can access the values.Some movie_item 's
    might not have a poster. This will give an error when we are
    trying to create an object. So we check if the movie_item has
    a poster then we create the movie object. We use the values we
     get to create a new movie object then we append it to our empty list.
     We then return the list with movie objects.
     '''
