import unittest

from .models import movie

Movie = movie.Movie


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class.
    This will instantiate our Movie class to make
    the self.new_movie object. We pass in six arguments.

    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234, 'Python Must Be Crazy',
            'A thrilling new Python Series',
            'https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs',
            8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == '__main__':
    unittest.main()
