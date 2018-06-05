import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import backend.user_input as ui
import pandas as pd
from frontend.state import portfolios as state


def name_component(template):
    id = 'name-' + template['id']
    component = html.Span(children=[
        "Portfolio name: ",
        html.Span(id=id + 'out', children=''),
        dcc.Input(value=template['name'], id=id),
        html.Div()
    ])
    return component


def name_callback(app, template):
    id = 'name-' + template['id']

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        template['name'] = value
        return ''


def initial_investment_component(template):
    id = 'initial-investment-' + template['id']
    component = html.Span(children=[
        "Initial investment: ",
        html.Span(id=id + 'out', children=''),
        dcc.Input(type='number', value=template['input']['Initial investment'], id=id),
        html.Div()
    ])
    return component


def initial_investment_callback(app, template):
    id = 'initial-investment-' + template['id']

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        template['input']['Initial investment'] = value
        return ''


def rebal_freq_component(template):
    id = 'rebal-freq-' + template['id']
    component = html.Span(children=[
        "Rebalancing frequency (days): ",
        html.Span(id=id + 'out', children=''),
        dcc.Input(type='number', value=template['input']['Rebalancing frequency (days)'], id=id),
        html.Div()
    ])
    return component


def rebal_freq_callback(app, template):
    id = 'rebal-freq-' + template['id']

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        template['input']['Rebalancing frequency (days)'] = value
        return ''


def time_period_component(template):
    id = 'time-period-' + template['id']
    component = html.Div(style={'padding-bottom': '5px'}, children=[
        "Rebalancing frequency (days): ",
        html.Span(id=id + 'out', children=''),
        html.Div(style={'margin': '10px', "padding": '5px'}, children=[
            dcc.RangeSlider(
                id=id,
                marks={i: '{}'.format(i) for i in range(2008, 2019)},
                min=2008,
                max=2019,
                value=[template['input']['Start date'].year,
                       template['input']['End date'].year]
            )
        ])
    ])
    return component


def time_period_callback(app, template):
    id = 'time-period-' + template['id']

    @app.callback(
        Output(id + 'out', 'children'),
        [Input(id, 'value')])
    def callback(value):
        # template['input']['Start date'] = pd.Timestamp(year=value[0], month=1, day=1, hour=12)
        # template['input']['End date'] = pd.Timestamp(year=value[1], month=1, day=1, hour=12)
        return ''


def investment_classes_component(template):
    id = 'investment-classes-' + template['id']
    component = html.Div(style={'margin': '10px', "padding": '10px', 'border': 'solid 1px gray'}, children=["Invetment classes"] + [
        html.Div(children=[
            html.Span(children=[
                c,
                html.Span(id=id + str(cid) + 'out', children=''),
                dcc.Input(
                    placeholder='Enter a value...',
                    type='number',
                    id=id + str(cid),
                    value=template['input']['Investment classes'][c]
                )
            ])
        ]) for cid, c in enumerate(template['input']['Investment classes'])
    ])
    return component


def investment_classes_callback(app, template):
    id = 'investment-classes-' + template['id']

    def create_callback(cid, c):
        @app.callback(
            Output(id + str(cid) + 'out', 'children'),
            [Input(id + str(cid), 'value')])
        def callback(value):
            print(c)
            template['input']['Investment classes'][c] = value
            return ''

    for cid, c in enumerate(template['input']['Investment classes']):
        create_callback(cid, c)


def get_component():
    return html.Div(children=[
        html.Div(style={'margin': '10px', "padding": '10px', 'border': 'solid 1px gray'}, children=[
            name_component(template),
            initial_investment_component(template),
            rebal_freq_component(template),
            time_period_component(template),
            investment_classes_component(template)
        ])
        for tid, template in enumerate(state)
    ])


def attach_callbacks(app):
    for template in state:
        name_callback(app, template)
        initial_investment_callback(app, template)
        rebal_freq_callback(app, template)
        time_period_callback(app, template)
        investment_classes_callback(app, template)
