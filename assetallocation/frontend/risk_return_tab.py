"""
UI component loaded on the 'Risk-return' tab.

Functions:
    get_component():
        returns a component containing the graph specific
        input components and the plotly Graph component
    attach_callbacks():
        attaches the callbacks for the input components.
Classes:
    None
"""
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import backend.user_input as ui
from backend.demo_portfolios import TEST_USER_PARAM_A as options
import frontend.portfolios_tab as pt


def get_params(x_cords, y_cords, text):
    """
    Constructs the plotly specific graph parameters. This configuration
    object can be passed to a Graph dash component.

    Args:
        x = the vector containing the x-coordinates of all the points
        y = the vector containing the y-coordinates of all the points
        text = the vector containing the labels of the points.

    Returns:
        Plotly graph configuration object
    """
    return {
        'data': [go.Scatter({
            'x': x_cords,
            'y': y_cords,
            'text': text,
            'textfont': dict(
                family='sans serif',
                size=18,
                color='#1f77b4'
            ),
            # 'type': 'scatter',
            'mode': 'markers',
            'marker': dict(
                color='black',
                size=7
            )
        })],
        'layout': {
            'title': 'Risk-Return Chart',
            'xaxis': {
                'title': 'Risk'
            },
            'yaxis': {
                'title': 'Return'
            }
        }
    }


def measure_of_return_component():
    """
    The dash input component that renders
    a dropdown for selecting a measure of return.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'measure-return'
    component = html.Div(children=[
        "Measure of return",
        html.Span(id=component_id + 'out', children=''),
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i}
                for i in ui.RETURN_TYPE_DICT
            ],
            value=options['Measure of return'],
            id=component_id
        )
    ])

    return component


def measure_of_return_callback(app):
    """
    Attaches the callback function for the component
    rendered in the measure_of_return function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'measure-return'

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        options['Measure of return'] = value
        return ''


def measure_of_risk_component():
    """
    The dash input component that renders
    a dropdown for selecting a measure of risk.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'measure-risk'
    component = html.Div(children=[
        "Measure of risk",
        html.Span(id=component_id + 'out', children=''),
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in ui.RISK_TYPE_DICT],
            value=options['Measure of risk'],
            id=component_id
        )
    ])

    return component


def measure_of_risk_callback(app):
    """
    Attaches the callback function for the component
    rendered in the measure_of_risk function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'measure-risk'

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        options['Measure of risk'] = value
        return ''


def return_period_component():
    """
    Returns the dash input component that renders
    a numeric input for specifying the period of
    return to use for the risk measure.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'return-period'
    component = html.Span(children=[
        "Period of return (days) to use for risk measure",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(
            type='number',
            id=component_id,
            value=options['Period of return (days) to use for risk measure']
        ),
        html.Div(),
    ])

    return component


def return_period_callback(app):
    """
    Attaches the callback function for the input
    rendered in the return_period_component function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'return-period'

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        options['Period of return (days) to use for risk measure'] = value
        return ''


def threshold_component():
    """
    Returns the dash input component that renders
    a numeric input for the rate of return threshold.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'threshold-rate-of-return'
    component = html.Span(children=[
        "Threshold rate of return",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(
            type='number',
            step=0.005,
            id=component_id,
            value=options['Threshold rate of return']
        ),
        html.Div(),
    ])

    return component


def threshold_callback(app):
    """
    Attaches the callback function for the input
    rendered in the threshold_component function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'threshold-rate-of-return'

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        options['Threshold rate of return'] = value
        return ''


def frequency_component():
    """
    Returns the dash input component that renders
    a numeric input for return measure frequency.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'period-of-return'
    component = html.Span(children=[
        "Frequency to measure return",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(
            type='number',
            id=component_id,
            value=options['Frequency to measure return']
        )
    ])

    return component


def frequency_callback(app):
    """
    Attaches the callback function for the input
    rendered in the frequency_component function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'period-of-return'

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        options['Frequency to measure return'] = value
        return ''


def annualized_component():
    """
    Renders two checkboxes, specifying if risk and
    return should be calculated using annualized returns.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'annualized_checkbox'
    component = html.Div(children=[
        "Use annualized risk/return measures",
        html.Span(id=component_id + 'out', children=''),
        dcc.Checklist(
            options=[
                {'label': 'Return', 'value': 'return'},
                {'label': 'Risk', 'value': 'risk'},
            ],
            id=component_id,
            values=(['return'] if options['Display annualized return'] else []) +
            (['risk'] if options['Use annualized return for risk measure'] else [])
        )
    ])

    return component


def annualized_callback(app):
    """
    Attaches the callback function for the checkboxes
    rendered in the annualized_component function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'annualized_checkbox'

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'values')])
    def _callback(value):
        if value is None:
            value = []

        options['Display annualized return'] = 'return' in value
        options['Use annualized return for risk measure'] = 'risk' in value
        return ''


def render_component():
    """
    Renders a button which the user has to press after
    any modifications to the inputs inorder to
    trigger a re-render of the graph component.

    Args:
        None

    Returns:
        dcc.Div object containing the input
    """
    component_id = 'render'
    component = html.Div(children=[
        html.Button("Re-render graph", id=component_id, style={
            'width': '80px',
            'height': '30px',
            'background-color': '#333',
            'color': 'white'})
    ])

    return component


def render_callback(app):
    """
    Attaches the callback function for the button
    rendered in render_component function

    Args:
        app = the dash app
    Returns:
        None
    """
    component_id = 'render'

    @app.callback(
        Output('riskreturn_graph', 'figure'),
        [Input(component_id, 'n_clicks')])
    def _callback(_value):
        graph_df = ui.export_user_portfolios(
            [s['input'] for s in pt.state],
            [s['name'] for s in pt.state], options)

        x_cords = graph_df['Risk'].values
        y_cords = graph_df['Return'].values
        text = graph_df['Label'].values

        return get_params(x_cords, y_cords, text)


def get_component():
    """
    Returns a wrapper div contains all the input components in this file
    and also the risk-return-graph component.

    Args:
        None

    Returns:
        the div containing all the components on this tab
    """
    graph_df = ui.export_user_portfolios(
        [s['input'] for s in pt.state],
        [s['name'] for s in pt.state], options)

    x_cords = graph_df['Risk'].values
    y_cords = graph_df['Return'].values
    text = graph_df['Label'].values

    return html.Div(children=[
        measure_of_return_component(),
        measure_of_risk_component(),
        return_period_component(),
        threshold_component(),
        frequency_component(),
        annualized_component(),
        render_component(),
        dcc.Graph(id='riskreturn_graph', figure=get_params(x_cords, y_cords, text)),
    ])


def attach_callbacks(app):
    """
    Calls the attach_callback functions for each
    of the inputs components in this tab

    Args:
        app = the dash app
    Returns:
        None
    """
    measure_of_return_callback(app)
    measure_of_risk_callback(app)
    return_period_callback(app)
    threshold_callback(app)
    frequency_callback(app)
    annualized_callback(app)
    render_callback(app)
