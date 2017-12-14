from flask import render_template
from app import app

# Views


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data.
    We want to pass in a title to our templates instead of defining
    them inside the html structure. We create a variable title
    and pass it into our templates.
    '''
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title, popular=popular_movies,
     upcoming = upcoming_movie, now_showing = now_showing_movie )
    '''
    We create a variable popular_movies where we call our get_movies()
     function and pass in "popular" as an argument. we then pass the
      result from that function call to our template
      We use our get_movies() function to get two more movie categories
       upcoming movies and now showing movies and then we pass them
        into our template.
    '''


@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id=movie_id)

    '''We add a new route that have a movie() view function.
     The part in the angle brackets <> is dynamic. And any route
      mapped to this will be passed. This returns a response of
       a movie.html file.By default, dynamic parts are rendered as
        strings but they can be transformed to be of any type
    '''




