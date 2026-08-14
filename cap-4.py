#  exercicio (parte 1)
#1
import numpy as np

mtz1 = np.ones([8,])
mtz2 = np.random.randint(0, 10, 8)
mtz3 = mtz1 + mtz2
soma = mtz3.sum()

if mtz3.sum() >= 40:
    mtz3 = mtz3.reshape(4,2)
else:
    mtz3 = mtz3.reshape(2,4)

#2
mtz4 = np.arange (0, 51, 2)
mtz5 = np.arange (50, 101, 2)
mtzConcatenada = np.concatenate([mtz4, mtz5])
print(mtzConcatenada)

#3
arr = np.zeros(4)
arr = arr.reshape(2,2)
linha = np.random.randint(0,2)
coluna = np.random.randint(0,2)
arr[linha, coluna] += 1

print(arr)

for tentativa in range(3):
    linha_jogador = int(input("Escolha a linha (0 ou 1): "))
    coluna_jogador = int(input("Escolha a coluna (0 ou 1): "))
    if arr[linha_jogador, coluna_jogador] == 1:
        print("Game Over! :( Try Again!")
        break
else:
    print("Congratulations! You beat the game! :)")

# (Parte 2)
# 4
mtz7 = np.random.randint(1, 10, (3, 5))
linhas, colunas = mtz7.shape
total = linhas * colunas

if total % 2 == 0:
    print("A matriz pode virar um vetor com número par de elementos:", total)
else:
    print("A matriz pode virar um vetor com número ímpar de elementos:", total)


#5
np.random.seed(10)
mtz6 = np.random.randint(1, 51, 16)
mtz6 = mtz6.reshape (4,4)
print (mtz6)

print("Média de cada linha:", mtz6.mean(axis=1))
print("Média de cada coluna:", mtz6.mean(axis=0))

print("Maior média entre as linhas:", mtz6.mean(axis=1).max())
print("Maior média entre as colunas:", mtz6.mean(axis=0).max())

valores, contagens = np.unique(mtz6, return_counts=True)
print("Valores:", valores)
print("Contagens:", contagens)

repetidos = valores[contagens == 2]
print("Números que aparecem 2x:", repetidos)
