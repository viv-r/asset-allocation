import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from generate_portfolios import get_graph_data


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
    x, y, text = get_graph_data()
    return html.Div(children=[
        dcc.Graph(
            id='riskreturn_graph',
            figure=get_params(x, y, text)),
        get_timeperiod_component()
    ])


def get_timeperiod_component(years=[2014 + i for i in range(6)]):
    return dcc.RangeSlider(
        id='timeperiod_input',
        marks={i: '{}'.format(i) for i in years},
        min=min(years),
        max=max(years),
        value=[min(years), max(years)]
    )


def attach_callbacks(app):
    @app.callback(
        Output(component_id='riskreturn_graph', component_property='figure'),
        [Input(component_id='timeperiod_input', component_property='value')]
    )
    def update_timeperiod(value):
        print(value)
        return get_params(*get_graph_data(*value))
