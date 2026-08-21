#(Parte 3)
#1

import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

status_missao = dataset[1:, 7]

sucesso = status_missao[status_missao == 'Success']

total_missoes = status_missao.size
missoes_sucesso = sucesso.size

porcentagem_sucesso = (missoes_sucesso / total_missoes) * 100

print(f'Total de missões: {total_missoes}')
print(f'Missões com sucesso: {missoes_sucesso}')
print(f'Porcentagem de sucesso: {porcentagem_sucesso:.2f}%')

#2
custos = np.loadtxt('space.csv', delimiter=';', dtype='float', skiprows=1, usecols=6, encoding='utf-8')

custos_disponiveis = custos[custos > 0]

media_custo = custos_disponiveis.sum() / custos_disponiveis.size

print(f'Missões com valor de custo disponível: {custos_disponiveis.size}')
print(f'Média de gastos: {media_custo:.2f}')

#3
localizacao = dataset[1:, 2]

cond_eua = np.char.find(localizacao, 'USA') >= 0
missoes_eua = localizacao[cond_eua]

print(f'Missões realizadas pelos EUA: {missoes_eua.size}')

#4
empresa = dataset[1:, 1]
detalhe = dataset[1:, 4]

cond_spacex = (empresa == 'SpaceX') & (custos > 0)

custos_spacex = custos[cond_spacex]
detalhes_spacex = detalhe[cond_spacex]

custo_maximo = custos_spacex.max()
missao_mais_cara = detalhes_spacex[custos_spacex == custo_maximo]

print(f'Missão mais cara da SpaceX: {missao_mais_cara[0]} (Custo: {custo_maximo})')

#5
empresas, quantidades = np.unique(empresa, return_counts=True)

for i in range(empresas.size):
    print(f'{empresas[i]}: {quantidades[i]}')

#6
status_rocket = dataset[1:, 5]

foguetes_aposentados = status_rocket[status_rocket == 'StatusRetired']

porcentagem_aposentados = (foguetes_aposentados.size / status_rocket.size) * 100

print(f'Porcentagem de foguetes StatusRetired: {porcentagem_aposentados:.2f}%')

#7
cond_russia = np.char.find(localizacao, 'Russia') >= 0
missoes_russia = localizacao[cond_russia]

print(f'Missões lançadas na Rússia: {missoes_russia.size}')

#8
custos_validos = custos[custos > 0]
empresas_validas = empresa[custos > 0]

custo_maximo_geral = custos_validos.max()
empresa_mais_cara = empresas_validas[custos_validos == custo_maximo_geral]

print(f'Empresa com a missão mais cara: {empresa_mais_cara[0]} (Custo: {custo_maximo_geral})')
