# import requests
from frontend.page import init

if __name__ == '__main__':
    APP = init()
    APP.run_server(debug=True)