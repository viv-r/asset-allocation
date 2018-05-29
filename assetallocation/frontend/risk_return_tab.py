import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import user_input as ui
import pandas as pd
import frontend.portfolios_tab as pt


def get_params(x, y, text):
    return {
        'data': [{
            'x': x,
            'y': y,
            'text': text,
            'textfont': dict(
                family='sans serif',
                size=18,
                color='#1f77b4'
            ),
            'type': 'line'
        }],
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


options = {
    'Measure of return': 'Change in log of portfolio value',
    'Measure of risk': 'Probability of return below a threshold',
    'Period of return (days) to use for risk measure': 365,
    'Threshold rate of return': 0.0,
    'Frequency to measure return': 10,
    'Start of period to display': pd.Timestamp('2013-01-01 00:00:00'),
    'End of period to display': pd.Timestamp('2018-01-01 00:00:00'),
    'Display annualized return': False,
    'Use annualized return for risk measure': False
}


def get_component():
    s = ui.export_user_portfolios(
        [s['input'] for s in pt.state],
        [s['name'] for s in pt.state], options).values
    x, y, text = s[:, 0], s[:, 1], s[:, 2]
    return html.Div(children=[
        html.Div(children=[
            "Measure of return",
            dcc.Dropdown(
                options=[
                    {'label': i, 'value': i}
                    for i in ui.return_type_dict
                ],
                value=options['Measure of return'],
                id='measure-of-return'
            )
        ]),
        html.Div(children=[
            "Measure of risk",
            dcc.Dropdown(
                options=[
                    {'label': i, 'value': i}
                    for i in ui.risk_type_dict
                ],
                value=options['Measure of risk'],
                id='measure-of-risk'
            )
        ]),
        html.Div(),
        html.Span(children=[
            "Period of return (days) to use for risk measure",
            dcc.Input(
                placeholder='Enter a value...',
                type='number',
                id='period-of-return',
                value=options['Period of return (days) to use for risk measure']
            )
        ]),
        html.Div(),
        html.Span(children=[
            "Period of return (days) to use for risk measure",
            dcc.Input(
                placeholder='Enter a value...',
                type='number',
                id='period-of-return',
                value=options['Period of return (days) to use for risk measure']
            )
        ]),
        html.Div(children=[
            "Use annualized return",
            dcc.Checklist(
                options=[
                    {'label': 'Return', 'value': 'return'},
                    {'label': 'Risk', 'value': 'risk'},
                ],
                values=[]
            )
        ]),

        dcc.Graph(
            id='riskreturn_graph',
            figure=get_params(x, y, text)),
    ])


def attach_callbacks(app):
    return None
