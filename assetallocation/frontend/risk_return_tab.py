import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import user_input as ui
import pandas as pd
import frontend.portfolios_tab as pt
from frontend.state import options
import plotly.graph_objs as go


def get_params(x, y, text):
    # return go.Figure(
    #     data=[
    #         go.Scatter(
    #             x=x,
    #             y=y,
    #             text=text,
    #             marker=go.Marker(
    #                 color='rgb(55, 83, 109)'
    #             )
    #         )
    #     ],
    #     layout=go.Layout(
    #         title='Risk-return graph',
    #         margin=go.Margin(l=40, r=0, t=40, b=30)
    #     )
    # )
    print(x.shape, y.shape)
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


def get_component():
    s = ui.export_user_portfolios(
        [s['input'] for s in pt.state],
        [s['name'] for s in pt.state], options)
    print(s)
    x, y, text = s['Risk'].values, s['Return'].values, s['Label'].values
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
            "Threshold rate of return",
            dcc.Input(
                placeholder='Enter a value...',
                type='number',
                id='period-of-return',
                value=options['Threshold rate of return']
            )
        ]),
        html.Div(),
        html.Span(children=[
            "Frequency to measure return",
            dcc.Input(
                placeholder='Enter a value...',
                type='number',
                id='period-of-return',
                value=options['Frequency to measure return']
            )
        ]),
        html.Div(children=[
            "Use annualized return",
            dcc.Checklist(
                options=[
                    {'label': 'Return', 'value': 'return'},
                    {'label': 'Risk', 'value': 'risk'},
                ],
                values=(['return'] if options['Display annualized return'] else []) +
                (['risk'] if options['Use annualized return for risk measure'] else [])
            )
        ]),

        dcc.Graph(
            id='riskreturn_graph',
            figure=get_params(x, y, text)),
    ])


def attach_callbacks(app):
    return None