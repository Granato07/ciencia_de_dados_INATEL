import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfSpace = pd.read_csv('space.csv', delimiter=';')
dfSpace.columns = dfSpace.columns.str.strip()

# PARTE 1

# 1
dfNorteAmerica = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]
plt.figure()
plt.xlabel('Países')
plt.ylabel('Taxa')
plt.title('Mortalidade x Natalidade - América do Norte')
plt.plot(dfNorteAmerica['Country'], dfNorteAmerica['Deathrate'], 'r-',
         dfNorteAmerica['Country'], dfNorteAmerica['Birthrate'], 'b--')
plt.show()

# 2
dfEUA = dfSpace[dfSpace['Location'].str.contains('USA')]
dfChina = dfSpace[dfSpace['Location'].str.contains('China')]
qtEUA = len(dfEUA['Company Name'].unique())
qtChina = len(dfChina['Company Name'].unique())
plt.figure()
plt.ylabel('Empresas diferentes')
plt.title('Empresas Espaciais')
plt.bar(['EUA', 'CHINA'], [qtEUA, qtChina], color='green')
plt.show()

# 3
dfRoscosmos = dfSpace[dfSpace['Company Name'] == 'Roscosmos']
qtSucesso = len(dfRoscosmos[dfRoscosmos['Status Mission'] == 'Success'])
qtFalha = len(dfRoscosmos) - qtSucesso
plt.figure()
plt.title('Missões Roscosmos')
plt.pie(x=[qtSucesso, qtFalha], labels=['% Sucesso', '% Falha'], autopct='%1.1f%%')
plt.show()

# 4
dfFailure = dfSpace[dfSpace['Status Mission'] == 'Failure']
top5Failure = dfFailure['Company Name'].value_counts().head(5)
plt.figure()
plt.ylabel('Missões com falha')
plt.title('5 Empresas com Mais Falhas')
plt.bar(top5Failure.index, top5Failure.values, color='red')
plt.show()

# PARTE 2

# 5
dfLatina = dfPaises[dfPaises['Region'].str.contains('LATIN AMER')]
plt.figure()
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy (%)')
plt.title('Renda x Alfabetização - América Latina')
plt.scatter(dfLatina['GDP ($ per capita)'], dfLatina['Literacy (%)'],
            s=dfLatina['Population'] / 1000000)
plt.show()

# 6
qtAtivos = len(dfSpace[dfSpace['Status Rocket'] == 'StatusActive'])
qtAposentados = len(dfSpace[dfSpace['Status Rocket'] == 'StatusRetired'])
plt.figure()
plt.title('Status dos Foguetes')
plt.pie(x=[qtAtivos, qtAposentados], labels=['% Ativos', '% Aposentados'], autopct='%1.1f%%')
plt.show()

# 7
dfEuropa = dfPaises[dfPaises['Region'].str.contains('WESTERN EUROPE')]
plt.figure()
plt.xlabel('Países')
plt.title('GDP x Phones - Europa Ocidental')
plt.plot(dfEuropa['Country'], dfEuropa['GDP ($ per capita)'], 'o-g',
         dfEuropa['Country'], dfEuropa['Phones (per 1000)'], 's--m')
plt.show()

# 8
dfSuccess = dfSpace[dfSpace['Status Mission'] == 'Success']
top5Success = dfSuccess['Company Name'].value_counts().head(5)
dfFailure = dfSpace[dfSpace['Status Mission'] == 'Failure']
top5Failure = dfFailure['Company Name'].value_counts().head(5)

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Mais Sucessos')
plt.bar(top5Success.index, top5Success.values, color='green')

plt.subplot(1, 2, 2)
plt.title('Mais Falhas')
plt.bar(top5Failure.index, top5Failure.values, color='red')
plt.show()
