import dash
import dash_core_components as dcc
import dash_html_components as html
from generate_portfolios import getOutput

app = dash.Dash()
data = getOutput()
print(data.head())

x, y, text = data.Return, data.Risk, data.Label
app.layout = html.Div(children=[
    html.H1(children='Asset allocation'),
    dcc.Graph(
        id='example-graph',
        figure={
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
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
