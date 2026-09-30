import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfPaises = pd.read_csv('paises.csv', delimiter=';', decimal=',')
dfSpace = pd.read_csv('space.csv')

# PARTE 3

# 1
ds_iris = sns.load_dataset('iris')
ds_setosa = ds_iris[ds_iris['species'] == 'setosa']
corrSetosa = ds_setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()
plt.figure()
plt.title('Correlação - Iris Setosa')
sns.heatmap(corrSetosa, annot=True, fmt='.2f')
plt.show()

# 2
ds_titanic = sns.load_dataset('titanic')
plt.figure()
plt.xlabel('Idade')
plt.title('Distribuição das Idades por Sexo')
sns.histplot(data=ds_titanic, x='age', hue='sex', kde=True)
plt.show()

# 3
plt.figure()
plt.title('Idades por Classe e Sexo')
sns.boxplot(data=ds_titanic, x='class', y='age', hue='sex')
plt.show()

# 4
ds_mpg = sns.load_dataset('mpg')
plt.figure()
plt.xlabel('Potência (horsepower)')
plt.ylabel('Consumo (mpg)')
plt.title('Potência x Consumo')
sns.regplot(data=ds_mpg, x='horsepower', y='mpg', line_kws={'color': 'red'})
plt.show()

# PARTE 4

# 5
corrPaises = dfPaises[['GDP ($ per capita)', 'Literacy (%)',
                       'Infant mortality (per 1000 births)', 'Phones (per 1000)']].corr()
plt.figure()
plt.title('Correlação - Paises')
sns.heatmap(corrPaises, annot=True, fmt='.2f')
plt.show()

# 6
dfDuasRegioes = dfPaises[dfPaises['Region'].str.contains('LATIN AMER|WESTERN EUROPE')]
plt.figure()
plt.title('GDP - América Latina x Europa Ocidental')
sns.boxplot(data=dfDuasRegioes, x='Region', y='GDP ($ per capita)')
plt.show()

# 7
plt.figure()
plt.title('Alfabetização x Mortalidade Infantil')
sns.regplot(data=dfPaises, x='Literacy (%)', y='Infant mortality (per 1000 births)',
            line_kws={'color': 'red'})
plt.show()

# 8
dfComCusto = dfSpace[dfSpace['Cost'] > 0]
plt.figure()
plt.title('Custo das Missões por Status do Foguete')
sns.boxplot(data=dfComCusto, x='Status Rocket', y='Cost')
plt.show()