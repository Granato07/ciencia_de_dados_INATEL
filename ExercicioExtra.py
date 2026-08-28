import numpy as np

# Questão 1
dataset = np.loadtxt('paises (1).csv', delimiter= ';', dtype= 'str', encoding='utf-8')
paises_info = dataset[:, 0:4]

print(paises_info)

# Questão 2
regioes = np.unique([regiao.strip() for regiao in dataset[1:, 1]])

print(f"\nQuantidade de regiões diferentes: {len(regioes)}")
print("Regiões:")
print(regioes)

# Questão 3
alfabetizacao = dataset[1:, 9].astype(float)

print(f"\nTaxa média de alfabetização do planeta: {alfabetizacao.mean():.2f}%")

# Questão 4
regiao_paises = np.array([regiao.strip() for regiao in dataset[1:, 1]])
qtd_america_norte = np.sum(regiao_paises == 'NORTHERN AMERICA')

print(f"\nQuantidade de países da América do Norte: {qtd_america_norte}")

# Questão 5
mascara_latam = regiao_paises == 'LATIN AMER. & CARIB'
paises_latam = dataset[1:, 0][mascara_latam]
gdp_latam = dataset[1:, 8][mascara_latam].astype(float)

pais_maior_gdp = paises_latam[np.argmax(gdp_latam)].strip()
maior_gdp = gdp_latam.max()

print(f"\nPaís da América Latina/Caribe com maior GDP per capita: {pais_maior_gdp} (${maior_gdp:.2f})")
