# Exercicios (Parte 1)
#1
classificacao = ['Time A', 'Time B', 'Time C', 'Time D', 'Barcelona']
print(classificacao)
print(classificacao[0:3])
print(classificacao[-2:])

ordem_alfabetica = sorted(classificacao)
print(ordem_alfabetica)

posicao = classificacao.index('Barcelona')
print(posicao + 1)

#2
loja1 = {'iPhone 15', 'Galaxy S23', 'Moto G54', 'Redmi Note 12'}
loja2 = {'Galaxy S23', 'Pixel 8', 'Moto G54', 'iPhone 14'}

print(loja1)
print(loja2)

todos_modelos = loja1 | loja2
print(todos_modelos)

modelos_em_comum = loja1 & loja2
print(modelos_em_comum)

#3
nome = input('Digite o nome do aluno: ')
media = float(input('Digite a média do aluno: '))

aluno = {'nome': nome, 'media': media}

if media >= 50:
    situacao = 'AP'
else:
    situacao = 'RP'

aluno['situacao'] = situacao

print(aluno)

#(Parte 2)
#4
nome1 = input('Digite o nome da pessoa 1: ')
peso1 = float(input('Digite o peso da pessoa 1: '))

nome2 = input('Digite o nome da pessoa 2: ')
peso2 = float(input('Digite o peso da pessoa 2: '))

nome3 = input('Digite o nome da pessoa 3: ')
peso3 = float(input('Digite o peso da pessoa 3: '))

if peso1 >= peso2 and peso1 >= peso3:
    mais_pesada = nome1
elif peso2 >= peso1 and peso2 >= peso3:
    mais_pesada = nome2
else:
    mais_pesada = nome3

if peso1 <= peso2 and peso1 <= peso3:
    mais_leve = nome1
elif peso2 <= peso1 and peso2 <= peso3:
    mais_leve = nome2
else:
    mais_leve = nome3

print(f'Pessoa mais pesada: {mais_pesada}')
print(f'Pessoa mais leve: {mais_leve}')

#5
NumeroDePessoas = int(input('Digite Quantas pessoas: '))

soma_idades = 0
counter = 0

for i in range(0, NumeroDePessoas):
    Pessoa = input('Nome: ')
    Idade = int(input('Idade: '))
    Sexo = input('Sexo: ').upper()

    soma_idades += Idade

    if Sexo == 'F' and Idade < 20:
        counter += 1

Media = soma_idades / NumeroDePessoas
print(f'Média de idade: {Media}')
print(f'Mulheres com menos de 20 anos: {counter}')

#6
ingredientes = ['Farinha', 'Açúcar', 'Ovos', 'Fermento', 'Leite']
print(ingredientes)

ingredientes.append('Manteiga')
print(ingredientes)

ingredientes.insert(2, 'Chocolate em pó')
print(ingredientes)

ingredientes.remove('Leite')
print(ingredientes)

#(Parte 3)
#7
receita = set(ingredientes)
print(receita)

pessoa1 = {'Farinha', 'Ovos', 'Manteiga'}
pessoa2 = {'Açúcar', 'Ovos', 'Fermento'}

falta_pessoa1 = receita - pessoa1
falta_pessoa2 = receita - pessoa2

print(f'Falta comprar (pessoa 1): {falta_pessoa1}')
print(f'Falta comprar (pessoa 2): {falta_pessoa2}')

#8
nome1 = input('Nome do produto 1: ')
preco1 = float(input('Preço do produto 1: '))
quantidade1 = int(input('Quantidade em estoque do produto 1: '))
produto1 = {'nome': nome1, 'preco': preco1, 'quantidade': quantidade1}

nome2 = input('Nome do produto 2: ')
preco2 = float(input('Preço do produto 2: '))
quantidade2 = int(input('Quantidade em estoque do produto 2: '))
produto2 = {'nome': nome2, 'preco': preco2, 'quantidade': quantidade2}

nome3 = input('Nome do produto 3: ')
preco3 = float(input('Preço do produto 3: '))
quantidade3 = int(input('Quantidade em estoque do produto 3: '))
produto3 = {'nome': nome3, 'preco': preco3, 'quantidade': quantidade3}

produtos = [produto1, produto2, produto3]

for produto in produtos:
    valor_total = produto['preco'] * produto['quantidade']
    print(f"{produto['nome']} - Valor total em estoque: {valor_total}")




