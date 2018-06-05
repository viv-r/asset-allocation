import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import backend.user_input as ui
import pandas as pd
import frontend.portfolios_tab as pt
from frontend.state import options
import plotly.graph_objs as go


def get_params(x, y, text):
    return {
        'data': [go.Scatter({
            'x': x,
            'y': y,
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
    id = 'measure-return'
    component = html.Div(children=[
        "Measure of return",
        html.Span(id=id + 'out', children=''),
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i}
                for i in ui.return_type_dict
            ],
            value=options['Measure of return'],
            id=id
        )
    ])

    return component


def measure_of_return_callback(app):
    id = 'measure-return'

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        options['Measure of return'] = value
        return ''


def measure_of_risk_component():
    id = 'measure-risk'
    component = html.Div(children=[
        "Measure of risk",
        html.Span(id=id + 'out', children=''),
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i}
                for i in ui.risk_type_dict
            ],
            value=options['Measure of risk'],
            id=id
        )
    ])

    return component


def measure_of_risk_callback(app):
    id = 'measure-risk'

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        options['Measure of risk'] = value
        return ''


def return_period_component():
    id = 'return-period'
    component = html.Span(children=[
        "Period of return (days) to use for risk measure",
        html.Span(id=id + 'out', children=''),
        dcc.Input(
            type='number',
            id=id,
            value=options['Period of return (days) to use for risk measure']
        ),
        html.Div(),
    ])

    return component


def return_period_callback(app):
    id = 'return-period'

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        options['Period of return (days) to use for risk measure'] = value
        return ''


def threshold_component():
    id = 'threshold-rate-of-return'
    component = html.Span(children=[
        "Threshold rate of return",
        html.Span(id=id + 'out', children=''),
        dcc.Input(
            type='number',
            id=id,
            value=options['Threshold rate of return']
        ),
        html.Div(),
    ])

    return component


def threshold_callback(app):
    id = 'threshold-rate-of-return'

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        options['Threshold rate of return'] = value
        return ''


def frequency_component():
    id = 'period-of-return'
    component = html.Span(children=[
        "Frequency to measure return",
        html.Span(id=id + 'out', children=''),
        dcc.Input(
            type='number',
            id=id,
            value=options['Frequency to measure return']
        )
    ])

    return component


def frequency_callback(app):
    id = 'period-of-return'

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        options['Frequency to measure return'] = value
        return ''


def annualized_component():
    id = 'annualized_checkbox'
    component = html.Div(children=[
        "Use annualized return",
        html.Span(id=id + 'out', children=''),
        dcc.Checklist(
            options=[
                {'label': 'Return', 'value': 'return'},
                {'label': 'Risk', 'value': 'risk'},
            ],
            id=id,
            values=(['return'] if options['Display annualized return'] else []) +
            (['risk'] if options['Use annualized return for risk measure'] else [])
        )
    ])

    return component


def annualized_callback(app):
    id = 'annualized_checkbox'

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        options['Display annualized return'] = 'return' in value
        options['Use annualized return for risk measure'] = 'risk' in value
        return ''


def render_component():
    id = 'render'
    component = html.Div(children=[
        html.Button("Re-render graph", id=id, style={
            'width': '80px',
            'height': '30px',
            'background-color': '#333',
            'color': 'white'})
    ])

    return component


def render_callback(app):
    id = 'render'

    @app.callback(
        Output('riskreturn_graph', 'figure'),
        [Input(id, 'n_clicks')])
    def callback(value):
        s = ui.export_user_portfolios(
            [s['input'] for s in pt.state],
            [s['name'] for s in pt.state], options)

        x, y, text = s['Risk'].values, s['Return'].values, s['Label'].values
        return get_params(x, y, text)


def get_component():
    s = ui.export_user_portfolios(
        [s['input'] for s in pt.state],
        [s['name'] for s in pt.state], options)

    x, y, text = s['Risk'].values, s['Return'].values, s['Label'].values

    return html.Div(children=[
        measure_of_return_component(),
        measure_of_risk_component(),
        return_period_component(),
        threshold_component(),
        frequency_component(),
        annualized_component(),
        render_component(),
        dcc.Graph(id='riskreturn_graph', figure=get_params(x, y, text)),
    ])


def attach_callbacks(app):
    measure_of_return_callback(app)
    measure_of_risk_callback(app)
    return_period_callback(app)
    threshold_callback(app)
    frequency_callback(app)
    annualized_callback(app)
    render_callback(app)
