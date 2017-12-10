from app import app

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
"""Here we import the app instance. We then check if the
 script is run directly and then use the app.run() method
  to launch our server. We pass in the debug = True argument
   to allow us to run on debug mode so that we can easily
    track errors in our application.

    We now remove the debug = True argument from our app.run()
     because the debug mode has been enabled in the configuration file.
    """



