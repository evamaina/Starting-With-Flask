class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=ed92bde7262096770c0c40c9443d203e'
    '''
    We use the {} to represent sections in the URL that will be
     replaced with actual values
    '''


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with
        General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with
         General configuration settings
    '''

    DEBUG = True

    '''
    Here we created three classes. The parent Config
    class contains configurations that are used in
    both production and development stages. The
    ProdConfig subclasscontains configurations that
    are used in production stages of our applicationand
    inherits from the parent Config class. The DevConfig
    subclass containsconfigurations that are used in
    development stages of our application and inherits
     from the parent Config class.
    Inside DevConfig subclass we add DEBUG = True
    this enables debug mode in our application.
    '''