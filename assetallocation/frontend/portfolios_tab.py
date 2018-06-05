"""
UI component loaded on the 'Portfolios' tab.

Functions:
    get_component():
        Returns all of the input components that make up
        the portfolios that the user wants to compare on the
        risk_return tab.

    attach_callbacks():
        attaches the callbacks for the input components.

Classes:
    None
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from backend.demo_portfolios import test_demo_portfolios_A as state


def name_component(template):
    component_id = 'name-' + template['id']
    component = html.Span(children=[
        "Portfolio name: ",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(value=template['name'], id=id),
        html.Div()
    ])
    return component


def name_callback(app, template):
    component_id = 'name-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(id, 'value')])
    def _callback(value):
        template['name'] = value
        return ''


def initial_investment_component(template):
    component_id = 'initial-investment-' + template['id']
    component = html.Span(children=[
        "Initial investment: ",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(type='number', value=template['input']['Initial investment'], id=id),
        html.Div()
    ])
    return component


def initial_investment_callback(app, template):
    component_id = 'initial-investment-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(id, 'value')])
    def _callback(value):
        template['input']['Initial investment'] = value
        return ''


def rebal_freq_component(template):
    component_id = 'rebal-freq-' + template['id']
    component = html.Span(children=[
        "Rebalancing frequency (days): ",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(type='number', value=template['input']['Rebalancing frequency (days)'], id=id),
        html.Div()
    ])
    return component


def rebal_freq_callback(app, template):
    component_id = 'rebal-freq-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(id, 'value')])
    def _callback(value):
        template['input']['Rebalancing frequency (days)'] = value
        return ''


def time_period_component(template):
    component_id = 'time-period-' + template['id']
    component = html.Div(style={'padding-bottom': '5px'}, children=[
        "Rebalancing frequency (days): ",
        html.Span(id=component_id + 'out', children=''),
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
    component_id = 'time-period-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(id, 'value')])
    def _callback(_value):
        # template['input']['Start date'] = pd.Timestamp(year=value[0], month=1, day=1, hour=12)
        # template['input']['End date'] = pd.Timestamp(year=value[1], month=1, day=1, hour=12)
        return ''


def investment_classes_component(template):
    component_id = 'investment-classes-' + template['id']
    class_components = [html.Div(children=[
        html.Span(children=[
            c,
            html.Span(id=component_id + str(cid) + 'out', children=''),
            dcc.Input(
                placeholder='Enter a value...',
                type='number',
                id=component_id + str(cid),
                value=template['input']['Investment classes'][c]
            )
        ])
    ]) for cid, c in enumerate(template['input']['Investment classes'])]
    component = html.Div(style={'margin': '10px',
                                "padding": '10px',
                                'border': 'solid 1px gray'},
                         children=["Invetment classes"] + class_components)
    return component


def investment_classes_callback(app, template):
    component_id = 'investment-classes-' + template['id']

    def create_callback(cid, investment_class):
        @app.callback(
            Output(component_id + str(cid) + 'out', 'children'),
            [Input(component_id + str(cid), 'value')])
        def _callback(value):
            template['input']['Investment classes'][investment_class] = value
            return ''

    for cid, investment_class in enumerate(template['input']['Investment classes']):
        create_callback(cid, investment_class)


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
