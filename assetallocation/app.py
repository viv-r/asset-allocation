"""
The entry point for the application, creates a dash web server.
"""
from frontend.page import init

if __name__ == '__main__':
    APP = init()
    APP.run_server(debug=True)
