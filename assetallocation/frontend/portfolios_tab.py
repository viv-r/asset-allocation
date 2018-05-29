import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import user_input as ui
import pandas as pd
from frontend.state import portfolios as state


def get_component():
    return html.Div(children=[
        html.Div(style={'margin': '10px', "padding": '10px', 'border': 'solid 1px gray'}, children=[
            dcc.Dropdown(
                options=[{
                    'label': template['name'],
                    'value': template['name']
                } for template in state],
                multi=False,
                value=template['name'],
                id='portfolio-template-' + str(tid)
            ),
            html.Span(children=[
                "Initial Investment",
                dcc.Input(
                    placeholder='Enter a value...',
                    type='text',
                    id='portfolio-intital-investment-' + str(tid),
                    value=template['input']['Initial investment']
                )
            ]),
            html.Div(),
            html.Span(children=[
                "Rebalancing frequency (days)",
                dcc.Input(
                    placeholder='Enter a value...',
                    type='number',
                    id='portfolio-rebal-' + str(tid),
                    value=template['input']['Rebalancing frequency (days)']
                )
            ]),
            html.Div(),
            html.Div(style={'padding-bottom': '5px'}, children=[
                "Time period",
                html.Div(style={'margin': '10px', "padding": '5px'}, children=[
                    dcc.RangeSlider(
                        id='portfolio-time-' + str(tid),
                        marks={i: '{}'.format(i) for i in range(1990, 2019)},
                        min=1990,
                        max=2019,
                        value=[template['input']['Start date'].year,
                               template['input']['End date'].year]
                    )
                ])
            ]),
            html.Div(),
            html.Div(style={'margin': '10px', "padding": '10px', 'border': 'solid 1px gray'}, children=["Invetment classes"] + [
                html.Div(children=[

                    html.Span(children=[
                        c,
                        dcc.Input(
                            placeholder='Enter a value...',
                            type='number',
                            id='portfolio-weight-' + str(tid) + '-' + str(cid),
                            value=template['input']['Investment classes'][c]
                        )
                    ])
                ]) for cid, c in enumerate(template['input']['Investment classes'])
            ])
        ])
        for tid, template in enumerate(state)
    ])


def attach_callbacks(app):
    @app.callback(
        Output('portfolio-inputs-container', 'children'),
        [Input('portfolio-dropdown', 'value')])
    def update_output(value):
        # dash bug: first call might not be a list.
        if not isinstance(value, (list,)):
            value = [value]
        if not len(value) > 0:
            return '^ Select portfolios'

        print(value)
        p = html.Div(children=[
            html.Div(children=[
                p,
                dcc.Input(
                    placeholder='Enter a value...',
                    type='text',
                    value=''
                )
            ]) for p in value
        ])
        return p
