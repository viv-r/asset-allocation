import dash_core_components as dcc
import dash_html_components as html
import dash
import os
import pandas as pd
import backend.user_input


def get_params(x, y):
    return {
        'data': [{
            'x': x,
            'y': y,
            'text': x,
            'textfont': dict(
                family='sans serif',
                size=18,
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
    return html.Div(children=[
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i} for i in user_input.investment_class_dict
            ],
            value=list(user_input.investment_class_dict)[0],
            id='datasets-dropdown'
        ),
        html.Div(id='datasets-container')
    ])


def attach_callbacks(app):
    @app.callback(
        dash.dependencies.Output('datasets-container', 'children'),
        [dash.dependencies.Input('datasets-dropdown', 'value')])
    def update_output(value):
        if value is None:
            return ""
        df = user_input.investment_class_dict[value]
        return dcc.Graph(
            id='datasets-graph',
            figure=get_params(df.index, df.values[:, 0]))
