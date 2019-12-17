# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# Draw radar charts from numerical serie

# Libraries
import matplotlib.pyplot as plt
# import sys
# print sys.executable 
import pandas as pd
import numpy as np
from math import pi

# Tecnologie 4.0
def createspidergraph(d):
    # convert values from % to integers
    real_aug = int(d['Realtà aumentata'][:-1])
    int_vert = int(d['Integrazione orizzontale/verticale'][:-1])
    simul = int(d['Simulazione'][:-1])
    iot = int(d['Internet delle cose (IOT)'][:-1])
    cloud = int(d['Cloud'][:-1])
    cyber_sec = int(d['Cyber-Security'][:-1])
    big_data = int(d['Big data e analitiche'][:-1])

    # Radar charts with 0 value are ugly. Prettify.
    if real_aug == 0:
        real_aug = 5
    if int_vert == 0:
        int_vert = 5
    if simul == 0:
        simul = 5
    if iot == 0:
        iot = 5
    if cloud == 0:
        cloud = 5
    if cyber_sec == 0:
        cyber_sec = 5
    if big_data == 0:
        big_data = 5


    # Set data - Already ready to make multi comparison 
    df = pd.DataFrame({
        'group': ['A', 'B', 'C', 'D'],
        'Realtà Aumentata': [real_aug, 75, 30, 4],
        'Integrazione Oriz/Vert': [int_vert, 50, 23, 24],
        'Simulazione': [simul, 75, 9, 34],
        'IoT': [iot, 15, 32, 14],        
        'Cloud': [cloud, 90, 33, 14],
        'Cybersecurity': [cyber_sec, 30, 9, 34],
        'Big Data & Analytics': [big_data, 60, 9, 34]
    })

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot?
    # (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1, 25, 50, 75, 100], ["1", "25", "50", "75", "100"], color="grey", size=7)
    plt.ylim(0, 100)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    # To print a second Group
    '''values=df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
    ax.fill(angles, values, 'r', alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))'''

    # To Show the graph, but conflicts with savings below
    # plt.show()
    # plt.savefig('spider.png')
    # fig = plt.figure()
    ax.figure.savefig('tecnologie40.png', bbox_inches="tight")
    '''extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('spider.png', bbox_inches=extent)
    fig.savefig('ax2_figure_expanded.png', bbox_inches=extent.expanded(1.1, 1.2))'''
    ax.clear()
    plt.clf()

# createspidergraph()