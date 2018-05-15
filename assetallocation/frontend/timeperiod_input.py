import dash_core_components as dcc


def get_component(years=[2013 + i for i in range(6)]):
    return dcc.RangeSlider(
        id='timeperiod_input',
        marks={i: '{}'.format(i) for i in years},
        min=min(years),
        max=max(years),
        value=[2013, 2018]
    )
