# we may need to pip install flask
from flask import Flask

# Caution: Flask is a development server with no security features
# For secure services, combine Flask with a WSGI server (Tomcat, Apache...)

def main():
    '''a simple Flask implementation'''
    app = Flask(__name__)
    # we then declare routing for this web server
    @app.route('/') #this is the top level of our server
    def root():
        return 'welcome'
    @app.route('/hello')
    def hello():
        return '<h3>Hello</h3>'
    # multiple routes to the same content
    @app.route('/info')
    @app.route('/about')
    @app.route('/stuff')
    def generic():
        '''any of the three routes will end up here'''
        return '<p>Information about stuff</p>'

    # using URL parameters
    @app.route('/greet/<person>') # <> mean there will be a parameter
    def greet(person='Friend'):
        if person:
            return f'<h3>Welcome {person}</h3>'
        else:
            return 'Welcome to Flask Server'

    # using HTML templates

    app.run(debug=True) # start the server as a listening server (restart on change)


if __name__ == '__main__':
    main()