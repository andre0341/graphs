# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def creategenericradargraph(nome, x_axis, y_axis, strut_azien, ottimiz_hr, scarti, gest_magaz, quality, automaz, nome_file):
    # random create a dataframe
    df = pd.DataFrame({
         'group': list(map(chr, range(65, 85))),
         'values': np.random.uniform(size=20)})

    # convert values from % to integers
    strut_azien = int(strut_azien)
    ottimiz_hr = int(ottimiz_hr)
    scarti = int(scarti)
    gest_magaz = int(gest_magaz)
    quality = int(quality)
    automaz = int(automaz)

    df = pd.DataFrame({
        'group': ['Ristrutturazione\nAziendale', 
                  'Ottimizazione\nRisorse umane', 
                  'Gestione degli\nScarti',
                  'Gestione\nMagazzino', 
                  'Controllo\nQualità',
                  'Automazione\nI1ndustriale'],
        'values': [strut_azien, ottimiz_hr, scarti, gest_magaz, quality, automaz]
    })

    # Reorder it following the values:
    ordered_df = df.sort_values(by='values')
    print("df index = ", df.index)
    my_range = range(1, len(df.index) + 1)

    # The vertival plot is made using the hline function
    # Sns is the seaborn library. Only to benefit the nice looking features
    sns.set()
    plt.hlines(y=my_range, xmin=0, xmax=ordered_df['values'], color='skyblue')
    plt.plot(ordered_df['values'], my_range, "o")

    # Add titles and Axis names
    plt.yticks(my_range, ordered_df['group'])
    plt.title(nome, loc='center')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    # plt.show()
    # Name of the file must be the same as imported in create_docs.py
    plt.savefig(nome_file + '.png', bbox_inches="tight")
    plt.clf()
