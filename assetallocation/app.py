import dash
import dash_core_components as dcc
import dash_html_components as html
import functions
from datetime import date

app = dash.Dash()


data = getOutput()
print(data.head())

x, y = [], []
app.layout = html.Div(children=[
    html.H1(children='Asset allocation'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [{
                'x': x,
                'y': y,
                'type': 'line'
            }],
            'layout': {
                'title': 'Risk-Return Chart'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
