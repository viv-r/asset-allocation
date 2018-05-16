import dash_core_components as dcc


def get_component(years=[2014 + i for i in range(6)]):
    return dcc.RangeSlider(
        id='timeperiod_input',
        marks={i: '{}'.format(i) for i in years},
        min=min(years),
        max=max(years),
        value=[min(years), max(years)]
    )
