class Config:
    '''
    General configuration parent class
    '''
    pass


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