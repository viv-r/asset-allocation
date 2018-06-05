"""
This module initializes a dash webpage. The page mainly consists
of a tab component with the content each tab specified in the modules
mapping in the TAB_COMPONENT_MAP contant.

Contants:
    TAB_COMPONENT_MAP: A map containing the names of each tab and
        the module to be loaded when that tab is clicked.

Functions:
    init():
        inits a dash application, attaches callbacks and css.

Classes:
    None
"""
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from frontend import datasets_tab
from frontend import portfolios_tab
from frontend import introduction_tab
from frontend import risk_return_tab


TAB_COMPONENT_MAP = [
    {'label': 'Introduction', 'component': introduction_tab},
    {'label': 'Portfolios', 'component': portfolios_tab},
    {'label': 'Risk return graph', 'component': risk_return_tab},
    {'label': 'Datasets', 'component': datasets_tab}
]


def init():
    """
    This init function for the dash application.
    Defines the tabs component, attaches callbacks,
    and external CSS files

    Args:
        None
    Returns:
        dash app
    """
    app = dash.Dash()
    app.config['suppress_callback_exceptions'] = True
    app.title = 'Asset Allocation'
    app.css.append_css({'external_url': 'https://codepen.io/accsgs/pen/pVMmQM.css'})

    app.layout = html.Div(children=[
        html.Div(id='state'),
        html.H1(children='Asset allocation',
                style={'margin': '0',
                       'padding': '10px',
                       'padding-left': '5px',
                       'background-color': '#354545',
                       'color': '#e5e5e5'}),
        html.Div(dcc.Tabs(tabs=[{'label': component['label'],
                                 'value': i} for i, component in enumerate(TAB_COMPONENT_MAP)],
                          value=1,
                          id='tabs',
                          vertical=True,
                          style={'height': '100vh',
                                 'padding': '10px',
                                 'borderRight': 'thin lightgrey solid',
                                 'textAlign': 'left'}),
                 style={'width': '20%', 'float': 'left'}),
        html.Div(id='tab-output', style={
            'width': '80%-50px',
            'padding': '25px',
            'margin-left': '20%'
        })
    ])

    for i in TAB_COMPONENT_MAP:
        i['component'].attach_callbacks(app)

    @app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
    def _tabs_callback(value):
        return TAB_COMPONENT_MAP[value]['component'].get_component()

    return app
