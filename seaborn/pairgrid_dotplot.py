# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
"""
Dot plot with several variables
===============================

_thumb: .3, .3
"""

# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# Load the dataset
crashes = sns.load_dataset("car_crashes")
#path_to_datasets = "/Users/andre/Google\ Drive/Projects/Python/Useful\ Python\ Stuff/graphs/seaborn/seaborn-data"
crashes = sns.load_dataset("car_crashes")
# Make the PairGrid
g = sns.PairGrid(crashes.sort_values("total", ascending=False),
                 x_vars=crashes.columns[:-3], y_vars=["abbrev"],
                 height=10, aspect=.25)

# Draw a dot plot using the stripplot function
g.map(sns.stripplot, size=10, orient="h",
      palette="ch:s=1,r=-.1,h=1_r", linewidth=1, edgecolor="w")

# Use the same x axis limits on all columns and add better labels
g.set(xlim=(0, 25), xlabel="Crashes", ylabel="")

# Use semantically meaningful titles for the columns
titles = ["Total crashes", "Speeding crashes", "Alcohol crashes",
          "Not distracted crashes", "No previous crashes"]

for ax, title in zip(g.axes.flat, titles):

    # Set a different title for each axes
    ax.set(title=title)

    # Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left=True, bottom=True)

plt.hlines(y=my_range, xmin=0, xmax=ordered_df['values'], color='skyblue')

# Add titles and Axis names
plt.yticks(my_range, ordered_df['group'])
plt.title('Priorità: Produzione Aziendale', loc='center')
plt.xlabel('Value of the variable')
plt.ylabel('Priorities')
# plt.show()
# Name of the file must be the same as imported in create_docs.py
plt.savefig('pairgrid.png', bbox_inches="tight")
plt.clf()

