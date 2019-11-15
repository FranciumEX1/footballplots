import pandas
import sys
import pygal
from pygal.style import Style

customLayout = Style(
  background="#ccccc8",
  plot_background="#918c8c",
  title_font_family="Helvetica",
  title_font_size=18,
  legend_font_family="Arial",
  value_font_family="Arial",
  colors=["#f00505", "#f0b905"],
  opacity=0.6)

fullData = pandas.read_csv("{}/data/season-1819_csv.csv".format(sys.path[0]))
averageGoals = fullData.groupby("HomeTeam").mean()[["FTHG", "FTAG"]].round(1).reset_index()
visualChart = pygal.Bar(rounded_bars=4, style=customLayout)
visualChart.title = "Average Goals For Home And Away 18/19"
visualChart.x_labels = averageGoals["HomeTeam"].to_list()
visualChart.add("Home Goals", averageGoals["FTHG"])
visualChart.add("Away Goals", averageGoals["FTAG"])
visualChart.render_to_file("average goals scored.svg")
