import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import itertools

religion_df = create_religion(religion_source)
# vytvoříme pomocnou tabulku
df = religion_df.copy()
# Menší náboženství sloučíme s `Other`
small_religions = ['Buddhist', 'Hindu', 'Jewish', 'Sikh']
df['Other'] = df['Other'] + df[small_religions].sum(axis=1)
df = df.groupby("Year").sum()/df[['Total']].groupby("Year").sum().values
df.drop(small_religions + ['Total'], axis=1, inplace=True)
print(df.head())
mpl.rc('axes', titlesize=16)
fig, axes = plt.subplots(1, 4, figsize=(22,6))
common_pie_kwargs = {'pctdistance': 0.65, 'autopct': '%.2f',
                     'wedgeprops': {'edgecolor': 'black'},
                     'textprops': {'size': 12}}
for ax, year in zip(axes, [2006, 2010, 2014, 2018]):
    ax.pie(df.loc[year], labels=df.columns, explode=np.repeat(0.05, df.shape[1]), **common_pie_kwargs)
    ax.set_title(year)
plt.savefig('pictures\L04_ch04_p03.png', bbox_inches = "tight")
plt.show()
