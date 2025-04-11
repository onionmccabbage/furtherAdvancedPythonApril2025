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
    app.run() # start the server


if __name__ == '__main__':
    main()