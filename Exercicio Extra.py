import numpy as np

# questao 1
musicas = []

while True:
    musica = {}
    musica["nome"] = input("Nome da música: ")
    musica["ano"] = int(input("Ano da música: "))
    musicas.append(musica)

    continuar = input("Deseja cadastrar outra? (s/n): ").strip().lower()
    if continuar != "s":
        break

# a)
print(f"\nTotal de músicas cadastradas: {len(musicas)}")

# b)
ano_mais_antigo = min(m["ano"] for m in musicas)
print(f"\nMúsica(s) do ano mais antigo ({ano_mais_antigo}):")
for m in musicas:
    if m["ano"] == ano_mais_antigo:
        print(f"Nome: {m['nome']} | Ano: {m['ano']}")
        
        
# questao 2

# a)
nomes1 = np.array(["Daniel", "Ana", "Pedro", "Julia"])
nomes2 = np.array(["Bruno", "Marina", "Carlos", "Leticia"])

# b)
nomes = np.concatenate((nomes1, nomes2))
print(nomes)

# c)
nomes_2d = nomes.reshape(2, 4)
print(nomes_2d)

# d)
ordenado = np.sort(nomes_2d, axis=None)[::-1].reshape(2, 4)
print(ordenado)

# questao 3

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1], "hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1], "hex": "#0F0"}},
    {"color": "yellow", "type": "primary", "code": {"rgba": [255,255,0,0.7], "hex": "#FF0"}},
    {"color": "blue", "type": "primary", "code": {"rgba": [0,0,255,1], "hex": "#00F"}}
]

# a)
print("Cores primárias:")
for cor in colors:
    if cor["type"] == "primary":
        print(cor["color"])

# b)
print("\nCores com azul = 255:")
for cor in colors:
    if cor["code"]["rgba"][2] == 255:
        print(cor["code"]["hex"])

# c)
valores = []
for cor in colors:
    valores.append(cor["color"])
    valores.append(cor["code"]["hex"])
arr = np.array(valores, dtype="U20")
print(arr)

# d)
arr_2d = arr.reshape(4, 2)
print(arr_2d)

# e)
traducao = {"black": "preto", "green": "verde", "yellow": "amarelo", "blue": "azul"}
for i in range(arr_2d.shape[0]):
    arr_2d[i, 0] = traducao[arr_2d[i, 0]]
print(arr_2d)