import dash
import dash_core_components as dcc
import dash_html_components as html
import functions
from datetime import date

app = dash.Dash()


def getData():
    sp = functions.invest_dataframe('./data/SP500.csv')
    ru2 = functions.invest_dataframe('./data/RU200TR.csv')
    ru3 = functions.invest_dataframe('./data/RU300TR.csv')
    a = functions.track_portfolio(
        [(sp, 0.4), (ru2, 0.3), (ru3, 0.3)], date('1990'), date('2000'))


getData()

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
