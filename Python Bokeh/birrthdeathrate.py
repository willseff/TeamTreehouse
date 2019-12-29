import pandas as pd 
from bokeh.io import output_file, show 
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.layouts import column, row

output_file('pop-life.html')
file = 'country-pops.csv'

countries  = pd.read_csv(file)

country_data=ColumnDataSource(countries)

plot_birth_rate = figure(x_axis_label='Population', y_axis_label='Birth Rate',
	title='Population vs. Birth Rate',
	tools='pan,wheel_zoom,box_zoom,reset,hover,save')

plot_birth_rate.circle(x='Population', y='Birthrate', source=country_data, size=10,
	# color takes a dict of **kwargs apprently
	legend='Region')

hover = plot_birth_rate.select_one(HoverTool)
hover.tooltips = [('Country', '@Country'),
('Population', '@Population'),
('Birth Rate', '@Birthrate')]

show(plot_birth_rate)