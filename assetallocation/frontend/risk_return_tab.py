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


def get_component():
    s = ui.export_user_portfolios(
        [s['input'] for s in pt.state],
        [s['name'] for s in pt.state], {
            'Measure of return': 'Change in log of portfolio value',
            'Measure of risk': 'Probability of return below a threshold',
            'Period of return to measure': 'Annual',
            'Threshold rate of return': 0.0,
            'Frequency to measure return': 10,
            'Start of period to display': pd.Timestamp('2014-01-01 00:00:00'),
            'End of period to display': pd.Timestamp('2018-01-01 00:00:00')
        }).values
    print(s)
    x, y, text = s[:, 0], s[:, 1], s[:, 2]
    return html.Div(children=[
        dcc.Graph(
            id='riskreturn_graph',
            figure=get_params(x, y, text)),
    ])


def attach_callbacks(app):
    pass
