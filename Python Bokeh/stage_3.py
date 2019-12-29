import pandas as pd 
from bokeh.io import output_file, show 
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.layouts import column, row

output_file('pop-life.html')
file = 'country-pops.csv'

countries  = pd.read_csv(file)

country_data=ColumnDataSource(countries)

color_mapper = CategoricalColorMapper(factors=['ASIA (EX. NEAR EAST)         ' ,'EASTERN EUROPE                     ',
 'NORTHERN AFRICA                    ',
 'OCEANIA                            ',
 'WESTERN EUROPE                     ',
 'SUB-SAHARAN AFRICA                 ' ,'LATIN AMER. & CARIB    ',
 'C.W. OF IND. STATES '], 
 palette=['#00FF00', '#FFD343', 'darkgray', 'brown', 'cyan', 'crimson', 'red', '#0000FF'])

TOOLTIPS = 'pan,wheel_zoom,box_zoom,reset,hover,save'

# put hover in the tools arguement to have a hover funtionality
plot = figure(x_axis_label='Population', y_axis_label='Life Expectancy',
	tools='pan,wheel_zoom,box_zoom,reset,hover,save', title='Population vs. Life Expectancy')

plot_birth_rate = figure(x_axis_label='Population', y_axis_label='Birth Rate',
	title='Population vs. Birth Rate',
	tools='pan,wheel_zoom,box_zoom,reset,hover,save')

plot_death_rate = figure(x_axis_label='Population', y_axis_label='Death Rate', title='Population vs Death Rate',
	tools='pan,wheel_zoom,box_zoom,reset,hover,save')

# match x and y values to the names in the dataset
plot.diamond(x='Population', y='Area', source=country_data, size=10,
	# color takes a dict of **kwargs apprently
	color=dict(field='Region', transform=color_mapper),
	legend='Region')

plot_birth_rate.circle(x='Population', y='Birthrate', source=country_data, size=10,
	# color takes a dict of **kwargs apprently
	color=dict(field='Region', transform=color_mapper),
	legend='Region')

plot_death_rate.triangle(x='Population', y='Deathrate', source=country_data, size=10,
	# color takes a dict of **kwargs apprently
	color=dict(field='Region', transform=color_mapper),
	legend='Region')

plot.legend.location = 'bottom_right'
plot.legend.background_fill_color = 'lightgrey'

hover = plot.select_one(HoverTool)
hover.tooltips = [('Country', '@Country'),
('Population', '@Population'),
('Area', '@Area')]

#link elements from different graphs together
# now when zooming in all graphs will zoom in together for the x axis
plot_birth_rate.x_range=plot.x_range
plot_death_rate.x_range = plot.x_range

show(row(column(plot, plot_birth_rate),column(plot_death_rate)))
