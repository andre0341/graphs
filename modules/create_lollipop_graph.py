# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def createlollipopgraph(d):
    # Create a dataframe
    # random create a dataframe
    df = pd.DataFrame({
         'group': list(map(chr, range(65, 85))),
         'values': np.random.uniform(size=20)})

    # convert values from % to integers
    cap_prod = int(d['Aumento capacità produttiva'][:-1])
    eff_prod = int(d['Aumento efficienza produttiva'][:-1])
    div_serv = int(d['Diversificazione Servizi'][:-1])
    div_prod = int(d['Diversificazione Prodotti'][:-1])

    df = pd.DataFrame({
        'group': ['Aumento Cap.\n Produttiva', 'Aumento\n Efficienza prod.',
                   'Divers.\nProdotti', 'Divers.\nServizi'],
        'values': [cap_prod, eff_prod, div_serv, div_prod]
    })

    # df['values'] = [100, 100, 50, 50]

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
    plt.title('Priorità: Produzione Aziendale', loc='center')
    plt.xlabel('Value of the variable')
    plt.ylabel('Priorities')
    # plt.show()
    # Name of the file must be the same as imported in create_docs.py
    plt.savefig('produzione.png', bbox_inches="tight")
    plt.clf()
