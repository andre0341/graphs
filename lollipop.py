# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dataframe
# random create a dataframe
df = pd.DataFrame({
    'group': list(map(chr, range(65, 85))),
    'values': np.random.uniform(size=20)})

# Data Set
df = pd.DataFrame({
    'group': ['Capacità\n Produttiva', 'Aumento\ndell\'efficienza',
              'Diversificazione\nProdotti', 'Diversificazione\nServ.'],
    'values': [100, 75, 25, 50]
})


# Reorder it following the values:
ordered_df = df.sort_values(by='values')
print("df index = ", df.index)
my_range = range(1, len(df.index) + 1)

# The vertival plot is made using the hline function
# I load the seaborn library only to benefit the nice looking feature
import seaborn as sns
sns.set()
plt.hlines(y=my_range, xmin=0, xmax=ordered_df['values'], color='skyblue')
plt.plot(ordered_df['values'], my_range, "o")

# Add titles and axis names
plt.yticks(my_range, ordered_df['group'])
plt.title("Priorità: Produzione Aziendale", loc='left')
plt.xlabel('Value of the variable')
plt.ylabel('Priorities')
# plt.show()
plt.savefig('lollipop.png')
