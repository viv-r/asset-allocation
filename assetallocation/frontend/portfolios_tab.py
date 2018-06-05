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

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from backend.demo_portfolios import TEST_DEMO_PORTFOLIOS_A as state


def name_component(template):
    """
    Renders the name input for a portfolio

    INPUTS:
        template: Portfolio template

    OUTPUTS:
        dcc.Div object containing the input
    """
    component_id = 'name-' + template['id']
    component = html.Span(children=[
        "Portfolio name: ",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(value=template['name'], id=component_id),
        html.Div()
    ])
    return component


def name_callback(app, template):
    """
    Attaches the callback function for the portfolio
    name input component

    INPUTS:
        app = the dash app
        template = portfolio object
    OUTPUTS:
        None
    """
    component_id = 'name-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        template['name'] = value
        return ''


def initial_investment_component(template):
    """
    Renders the input for initial investment amount of the portfolio

    INPUTS:
        template: Portfolio template

    OUTPUTS:
        dcc.Div object containing the input
    """
    component_id = 'initial-investment-' + template['id']
    component = html.Span(children=[
        "Initial investment: ",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(type='number', value=template['input']['Initial investment'], id=component_id),
        html.Div()
    ])
    return component


def initial_investment_callback(app, template):
    """
    Attaches the callback function for the portfolio
    initial investment amount input

    INPUTS:
        app = the dash app
        template = portfolio object
    OUTPUTS:
        None
    """
    component_id = 'initial-investment-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        template['input']['Initial investment'] = value
        return ''


def rebal_freq_component(template):
    """
    Renders the input component to capture the rebalancing
    frequency

    INPUTS:
        template: Portfolio template

    OUTPUTS:
        dcc.Div object containing the input
    """
    component_id = 'rebal-freq-' + template['id']
    value = template['input']['Rebalancing frequency (days)']
    component = html.Span(children=[
        "Rebalancing frequency (days): ",
        html.Span(id=component_id + 'out', children=''),
        dcc.Input(type='number', value=value, id=component_id),
        html.Div()
    ])
    return component


def rebal_freq_callback(app, template):
    """
    Attaches the callback function for the portfolio
    rebalancing frequency

    INPUTS:
        app = the dash app
        template = portfolio object
    OUTPUTS:
        None
    """
    component_id = 'rebal-freq-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        template['input']['Rebalancing frequency (days)'] = value
        return ''


def time_period_component(template):
    """
    Renders the time period slider for the start and end dates of the
    portfolio

    INPUTS:
        template: Portfolio template

    OUTPUTS:
        dcc.Div object containing the input
    """
    component_id = 'time-period-' + template['id']
    component = html.Div(style={'padding-bottom': '5px'}, children=[
        "Start and End dates",
        html.Span(id=component_id + 'out', children=''),
        html.Div(style={'margin': '10px', "padding": '5px'}, children=[
            dcc.RangeSlider(
                id=component_id,
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
    """
    Attaches the callback function for the portfolio
    time period

    INPUTS:
        app = the dash app
        template = portfolio object
    OUTPUTS:
        None
    """
    component_id = 'time-period-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):
        template['input']['Start date'] = pd.Timestamp(year=value[0], month=1, day=1, hour=12)
        template['input']['End date'] = pd.Timestamp(year=value[1], month=1, day=1, hour=12)
        return ''


def investment_classes_component(template):
    """
    Renders the input block that contains the list
    of assets in the portfolio template given and inputs to
    specify the weights of each asset.

    INPUTS:
        template: Portfolio template

    OUTPUTS:
        dcc.Div object containing the input
    """
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
    """
    Attaches the callback function for all the asset weight
    input components.

    INPUTS:
        app = the dash app
        template = portfolio object
    OUTPUTS:
        None
    """
    component_id = 'investment-classes-' + template['id']

    def create_callback(cid, investment_class):
        """
        Wrapper function to capture the ID and investment_class
        of this asset in a closure, both of which are needed in
        the actual callback function.

        INPUTS:
            cid: the id of the asset.
            investment_class: the name of the asset.
        """
        @app.callback(
            Output(component_id + str(cid) + 'out', 'children'),
            [Input(component_id + str(cid), 'value')])
        def _callback(value):
            template['input']['Investment classes'][investment_class] = value
            return ''

    for cid, investment_class in enumerate(template['input']['Investment classes']):
        create_callback(cid, investment_class)


def get_component():
    """
    Renders all the input component in this tab.

    INPUTS:
        None

    OUTPUTS:
        dcc.Div object containing all the inputs on this tab
    """
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
    """
    Attaches the callbacks for all the inputs in this tab.

    INPUTS:
        app = the dash app
    OUTPUTS:
        None
    """
    for template in state:
        name_callback(app, template)
        initial_investment_callback(app, template)
        rebal_freq_callback(app, template)
        time_period_callback(app, template)
        investment_classes_callback(app, template)
