from create_html_file import create_html
import os

# importing flask module in the project is mandatory
# an object of Flask class is our WSGI application 
# (WSGI is a specification for a universal interface between web server and web applications )
from flask import Flask

# Flask constructor takes the name of current module(__name__) as argument
app = Flask(__name__)

create_html()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.
@app.route('/')
def hello_world():
    return open('demo_html.html','r')

# main driver function
if __name__ == '__main__':
    app.run()





