"""
UI component loaded on the 'Datasets' tab.

Functions:
    get_component():
        returns a component containing the input dropdown
        and a graph plot for each dataset we have.
    attach_callbacks():
        attaches the callback for the dropdown.

Classes:
    None
"""
import dash_core_components as dcc
import dash_html_components as html
import dash
import backend.user_input as user_input


def get_params(x_cords, y_cords):
    """
    Constructs the plotly specific graph parameters. This configuration
    object can be passed to a Graph dash component.

    Args:
        x_cords = the vector containing the x-coordinates of all the points
        y_cords = the vector containing the y-coordinates of all the points

    Returns:
        Plotly graph configuration object
    """
    return {
        'data': [{
            'x': x_cords,
            'y': y_cords,
            'text': x_cords,
            'textfont': dict(
                family='sans serif',
                size=19,
                color='#1f77b4'
            ),
            'type': 'line'
        }],
        'layout': {
            'title': 'Index time-series',
            'xaxis': {
                'title': 'Date'
            },
            'yaxis': {
                'title': 'Price'
            }
        }
    }


def get_component():
    """
    Returns a div containing the dropdown and
    the graph of the dataset selected.

    Args:
        None
    Returns:
        div containing the component in this tab.
    """
    return html.Div(children=[
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i} for i in user_input.INVESTMENT_CLASS_DICT
            ],
            value=list(user_input.INVESTMENT_CLASS_DICT)[0],
            id='datasets-dropdown'
        ),
        html.Div(id='datasets-container')
    ])


def attach_callbacks(app):
    """
    Attaches the callback to the dropdown component in this tab.
    Re-renders the graph when a new value is selected in the dropdown

    Args:
        app: the dash app
    Returns:
        None
    """
    @app.callback(
        dash.dependencies.Output('datasets-container', 'children'),
        [dash.dependencies.Input('datasets-dropdown', 'value')])
    def _update_output(value):
        if value is None:
            return ""
        dataset = user_input.INVESTMENT_CLASS_DICT[value]
        return dcc.Graph(
            id='datasets-graph',
            figure=get_params(dataset.index, dataset.values[:, 0]))
