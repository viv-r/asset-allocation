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
from backend.demo_portfolios import TEST_USER_PARAM_A as options


def name_component(template):
    """
    Renders the name input for a portfolio

    Args:
        template: Portfolio template

    Returns:
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

    Args:
        app = the dash app
        template = portfolio object
    Returns:
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

    Args:
        template: Portfolio template

    Returns:
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

    Args:
        app = the dash app
        template = portfolio object
    Returns:
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

    Args:
        template: Portfolio template

    Returns:
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

    Args:
        app = the dash app
        template = portfolio object
    Returns:
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

    :
        template: Portfolio template

    Returns:
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

    Args:
        app = the dash app
        template = portfolio object
    Returns:
        None
    """
    component_id = 'time-period-' + template['id']

    @app.callback(
        Output(component_id + 'out', 'children'),
        [Input(component_id, 'value')])
    def _callback(value):

        new_st = pd.Timestamp(str(value[0]) + '-01-01 00:00:00')
        old_st = options['Start of period to display']
        new_et = pd.Timestamp(str(value[1]) + '-01-01 00:00:00')
        old_et = options['End of period to display']

        if new_st > old_st:
            options['Start of period to display'] = new_st
        if new_et < old_et:
            options['End of period to display'] = new_et

        template['input']['Start date'] = new_st
        template['input']['End date'] = new_et
        return ''


def investment_classes_component(template):
    """
    Renders the input block that contains the list
    of assets in the portfolio template given and inputs to
    specify the weights of each asset.

    Args:
        template: Portfolio template

    Returns:
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

    Args:
        app = the dash app
        template = portfolio object
    Returns:
        None
    """
    component_id = 'investment-classes-' + template['id']

    def create_callback(cid, investment_class):
        """
        Wrapper function to capture the ID and investment_class
        of this asset in a closure, both of which are needed in
        the actual callback function.

        Args:
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

    Args:
        None

    Returns:
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

    Args:
        app = the dash app
    Returns:
        None
    """
    for template in state:
        name_callback(app, template)
        initial_investment_callback(app, template)
        rebal_freq_callback(app, template)
        time_period_callback(app, template)
        investment_classes_callback(app, template)
