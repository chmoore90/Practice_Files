# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
# Just parse out the months and draw your histogram.

import json
import calendar
from collections import Counter
from bokeh.plotting import figure, show, output_file

output_file("birthday_plot.html")

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

all_months = []
for i in range(1,13):
    all_months.append(calendar.month_name[i])

months = []
for value in birthdays.values():
    month_no = int(value.split("/")[0])
    month = calendar.month_name[month_no]
    months.append(month)

month_count = Counter(months)
months, counts = list(zip(*month_count.items()))
p = figure(x_range=all_months)
p.vbar(x=months, top=counts, width=0.5)

show(p)
