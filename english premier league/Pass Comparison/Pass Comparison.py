import pandas
import pygal

homeData = pandas.read_csv("home passes.csv")
awayData = pandas.read_csv("away passes.csv")

homeData = homeData.sort_values("Short Passes")
awayData = awayData.sort_values("Short Passes")

line_chart = pygal.Line(stroke=False)
line_chart.title = 'Home/Away Average Pass Comparison'
line_chart.x_labels = homeData["Team"].to_list()
line_chart.add("Home", [passes for passes in homeData["Short Passes"]])
line_chart.add("Home", [passes for passes in awayData["Short Passes"]])
line_chart.render_to_file('render.svg')