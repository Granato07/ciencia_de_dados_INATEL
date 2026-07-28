# ===== Exercício 1 =====
nome = "Daniel Granato Botelho Poscidonio"
print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome.replace("Poscidonio", "Do Inatel"))

# ===== Exercício 2 =====
numero = int(input("Digite um número: "))
inicio_intervalo = int(input("Digite o início do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))

for c in range(inicio_intervalo, fim_intervalo + 1):
    print(f"{numero} x {c} = {numero * c}")

# ===== Exercício 3 =====
sexo = input("Digite seu sexo (M/F): ")
while sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
    print("Sexo inválido, tente novamente.")
    sexo = input("Digite seu sexo (M/F): ")

if sexo == "m" or sexo == "M":
    print("Sexo masculino")
else:
    print("Sexo feminino")

# ===== Exercício 4 =====
distancia = float(input("Digite a distância em quilômetros: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Preço total da viagem R${preco:.2f}")

# ===== Exercício 5 =====
numero = int(input("Digite um número entre 1000 e 9999: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")

# ===== Exercício 6 =====
import math

numero_decimal = float(input("Digite um número decimal: "))

raiz = math.sqrt(numero_decimal)
teto = math.ceil(numero_decimal)
chao = math.floor(numero_decimal)
parte_inteira = int(numero_decimal)

print(f"Raiz quadrada: {raiz}")
print(f"Teto: {teto}")
print(f"Chão: {chao}")
print(f"Parte inteira: {parte_inteira}")

# ===== Exercício 7 =====
palavra = input("Digite uma palavra: ")
contador_vogais = 0

for letra in palavra:
    print(letra.upper())
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador_vogais = contador_vogais + 1

print(f"Quantidade de vogais: {contador_vogais}")

if "a" in palavra:
    print("A letra A está presente")
else:
    print("A letra A não está presente")

# ===== Exercício 8 =====
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
resto = numero1 % numero2
potencia = numero1 ** numero2

print(f"Adição: {adicao}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão: {resto}")
print(f"Potência: {potencia}")
