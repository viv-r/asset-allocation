import requests
import dash_core_components as dcc

README_PATH = 'https://raw.githubusercontent.com/viv-r/asset-allocation/master/doc/Design.md'


def attach_callbacks(app):
    return None


def get_component():
    text = requests.get(README_PATH).text
    return dcc.Markdown(''' *_Note: This file is pulled directly from github.
     Once README.md is updated, change this location to point to it._*\n\n''' + text)
