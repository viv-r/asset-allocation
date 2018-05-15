import dash_core_components as dcc


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


def get_component(x, y, text):
    return dcc.Graph(
        id='riskreturn_graph',
        figure=get_params(x, y, text)
    )
