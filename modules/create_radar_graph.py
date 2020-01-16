# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Priorità - Ricerca e Innovazione
def createradargraph(d):
    df = pd.DataFrame({
         'group': list(map(chr, range(65, 85))),
         'values': np.random.uniform(size=20)})

    # convert values from % to integers
    prop_ind = int(d['Proprietà industriale'][:-1])
    collab = int(d['Collaborazioni'][:-1])
    comm_int = int(d['Miglioramento comunicazione INTERNA'][:-1])
    comm_ext = int(d['Miglioramento comunicazione ESTERNA'][:-1])
    r_and_d = int(d['Ricerca e Sviluppo'][:-1])

    df = pd.DataFrame({
        'group': ['Proprietà\nIndustriale', 'Collaborazioni',
                   'Internal\nCommunication', 'External\nCommunication', 
                   'R & D'],
        'values': [prop_ind, collab, comm_int, comm_ext, r_and_d]
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
    plt.title('Priorità: Ricerca e Innovazione', loc='center')
    plt.xlabel('Value of the variable')
    plt.ylabel('Priorities')
    # plt.show()
    # Name of the file must be the same as imported in create_docs.py
    plt.savefig('ricerca_e_innovazione.png', bbox_inches="tight")
    plt.clf()
