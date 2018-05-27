import dash_core_components as dcc
import dash_html_components as html
import os
import pandas as pd


def read_dataset(value):
    df = pd.read_csv('../Data/' + value + '.csv').values
    return df[:, 0], df[:, 1]


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


def update_graph(value):
    if value is None:
        return "Nothing here"

    return dcc.Graph(
        id='datasets-graph',
        figure=get_params(*read_dataset(value))
    )


def get_data_filenames():
    files = os.listdir('../Data')
    return [f.split('.')[0] for f in files if f.endswith('.csv')]


def get_component():
    files = get_data_filenames()
    return html.Div(children=[
        dcc.Dropdown(
            options=[
                {'label': 'Index: ' + i, 'value': i}
                for i in files
            ],
            value=files[0],
            id='datasets-dropdown'
        ),
        html.Div(id='datasets-container')
    ])
