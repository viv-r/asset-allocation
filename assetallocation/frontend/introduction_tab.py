"""
UI component loaded on the 'Introduction' tab.

Functions:
    get_component():
        returns a component containing the tab content.
    attach_callbacks():
        attaches the callbacks specific to the tab content.
"""
import requests
import dash_core_components as dcc

README_PATH = ('https://raw.githubusercontent.com/viv-r/'
               'asset-allocation/master/doc/Design.md')


def attach_callbacks(_app):
    """
    This component does not require any callbacks as there
    is no user interaction on the page.

    INPUTS:
        _app: Dash application (unused)
    OUTPUTS:
        None
    """
    pass


def get_component():
    """
    The UI component is a markdown web page that is pulled directly
    from the github repository spcified in 'README_PATH'

    INPUTS:
        None
    OUTPUTS:
        dcc.Markdown component
    """
    text = requests.get(README_PATH).text
    return dcc.Markdown(text)
