import requests
from frontend.page import init

if __name__ == '__main__':
    app = init()
    app.run_server(debug=True)
