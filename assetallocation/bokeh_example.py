# myapp.py

from random import random

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from generate_portfolios import getOutput

p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)

data = getOutput()
print(data.head())

x, y, text = data.Return, data.Risk, data.Label
r = p.line(x=[], y=[], linewidth=3)
ds = r.data_source

ds.data = {
    'x': x,
    'y': y
}
# put the button and plot in a layout and add to the document
curdoc().add_root(column(p))
