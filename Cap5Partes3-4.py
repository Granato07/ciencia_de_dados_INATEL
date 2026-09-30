import pandas as pd
import numpy as np

dfPaises = pd.read_csv('paises.csv', delimiter=';', decimal=',')

# PARTE 3

# 1
oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print(oceania['Country'])
print(len(oceania))

# 2
idx = dfPaises['Population'].idxmax()
print(dfPaises.loc[idx, ['Country', 'Region']])

# 3
group_region = dfPaises.groupby('Region')
print(group_region.mean()['Literacy (%)'])

# 4
noCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
noCoast['Country'].to_csv('noCoast.csv', sep=';')

# 5
def humanitarianHelp(x):
    if x < 9:
        return 'Balanced'
    else:
        return 'Urgent'

dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(humanitarianHelp)
print(dfPaises)

# PARTE 4

# 6
group_region = dfPaises.groupby('Region')
print(group_region.describe()['Population'].head(5))

# 7
def reduz15(x):
    return x * 0.85

mortality1 = dfPaises['Infant mortality (per 1000 births)']
mortality2 = dfPaises['Infant mortality (per 1000 births)'].apply(reduz15)
print(pd.concat([mortality1, mortality2], axis=1))

# 8
dfSemCoastline = dfPaises.drop('Coastline (coast/area ratio)', axis=1)
dfSemCoastline.to_csv('paises_sem_coastline.csv', sep=';')