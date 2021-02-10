# import Flask
from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager

# importing resources from their respective .py files
# from resources.persons import persons

# importing models.py
# import models

# Initialize an instance of flask
app = Flask(__name__)

app.config.from_pyfile('config.py') # creates the session secret

# login_manager = LoginManager() # JS equivalent to ''const loginManager = new LoginManager()''
# login_manager.init_app(app) # take LoginManager instance (login_manager) and initialize in an app (init_app()), which we called 'app'

# # @<name of function> is called a "decorator", which is native to flask. Adds additional functionality to the functions you declare under it.

# @login_manager.user_loader
# def load_person(person_id):
#   try:
#     return models.Person.get_by_id(person_id)
#   except models.DoesNotExist:
#     return None

# @app.before_request
# def before_request():
#   '''Connect to the database before each request.'''
#   g.db = models.DATABASE #ALL CAPS INDICATE TO OTHER READERS OF THE CODE THAT A VARIABLE NAME SHOULD NOT BE CHANGED
#   g.db.connect()

# @app.after_request
# def after_request(response):
#     '''Close the database connection after each request.'''
#     g.db = models.DATABASE
#     g.db.close()
#     return response

# # '\' allows you to break a line in your code and have Python ignore the line break
# CORS(app,\
#      origins=['http://localhost:3000'],\
#      supports_credentials=True)

# # equivalent to app.use(persons, '/api/v1/persons') in express
# app.register_blueprint(persons, url_prefix='/api/v1/persons')





# assumes a GET route if not specified, e.g. @app.route('/', methods=['PUT'])
# home route equivalent
@app.route('/')
def index():
  return 'hi, there HEY!!!!' 
  
# Return is used for response. Equivalent to res.whatever. Cannot return ints or lists.
# Use jsonify to pass all data types within a json object.
# @app.route('/sayhello/<name>')
# def say_hello(name):
#   # how to get query string from the browser
#   band = request.args.get('bandname')

#   return jsonify(
#     msg='Hello, {}!'.format(name),
#     bandname=band, 
#     status=200, 
#     list=['Bob', 'Rick', 'Jennifer'])

@app.route('/sayhi/<username>') # When someone goes here...
def hello(username): # Do this.
    return "Hello {}".format(username)




# Listener route
if __name__ == '__main__':
  # models.initialize()
  app.run(port=8000, debug=True)