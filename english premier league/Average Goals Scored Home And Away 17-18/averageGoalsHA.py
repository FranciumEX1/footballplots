import pandas
import sys
import pygal
from pygal.style import Style

customLayout = Style(
  background="#c9c3c3",
  plot_background="#e3e3e3",
  title_font_family="Helvetica",
  title_font_size=18,
  legend_font_family="Arial",
  label_font_family="Arial",
  colors=["#f00505", "#f0b905"],
  opacity=0.6)

fullData = pandas.read_csv("{}/data/season-1718_csv.csv".format(sys.path[0]))
averageGoals = fullData.groupby("HomeTeam").mean()[["FTHG", "FTAG"]].round(1).reset_index()
visualChart = pygal.Bar(rounded_bars=4, style=customLayout, width=1600)
visualChart.title = "Average Goals In Each Half 17/18"
visualChart.x_labels = averageGoals["HomeTeam"].to_list()
visualChart.add("Home Goals", averageGoals["FTHG"])
visualChart.add("Away Goals", averageGoals["FTAG"])
visualChart.render_to_file("average goals scored.svg")