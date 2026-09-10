# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: .venv (3.14.6.final.0)
#     language: python
#     name: python3
# ---

# %%
# Aula 1 — Entendendo tipos e erros

numero_inteiro = 10
numero_decimal = 3.14
texto = "Python"
verdadeiro = True

print(type(numero_inteiro))
print(type(numero_decimal))
print(type(texto))
print(type(verdadeiro))

# Erro comum: tentar somar texto e número
try:
    resultado = texto + numero_inteiro
except TypeError as erro:
    print(f"Erro encontrado: {erro}")

# %%
# TypeError
try:
    resultado = numero_inteiro + texto
except TypeError as erro:
    print(f"TypeError: {erro}")

# type(): retorna o tipo exato do valor
print(type(numero_decimal))   # <class 'float'>
print(type(texto))            # <class 'str'>

# isinstance(): verifica se o valor pertence a um tipo
print(isinstance(numero_inteiro, int))  # True
print(isinstance(texto, int))            # False

# Type hint: indica os tipos esperados
def saudacao(nome: str, idade: int) -> str:
    return f"{nome} tem {idade} anos."

print(saudacao(texto, numero_inteiro))

# %% [markdown]
# Exercício 1 – Descobrindo os tipos
# Observe os valores abaixo:
#
# nome = "Brasil"
# gols = 3
# posse_bola = 58.7
# classificado = True
#
# Crie um programa que mostre o tipo de cada uma dessas variáveis utilizando type().
# Ao executar, o programa deve permitir identificar quais valores são str, int, float e bool.

# %%
nome = "Brasil"
gols = 3
posse_bola = 58.7
classificado = True
print(type(nome), "\n", type(gols), "\n", type(posse_bola), "\n", type(classificado), "\n")    
  

# %% [markdown]
# Exercício 2 – Verificando os tipos
# Considere as variáveis:
#
# numero_camisa = 10
# jogador = "Raphinha"
#
# Utilize isinstance() para verificar:
#
# se numero_camisa é um int;
# se numero_camisa é uma str;
# se jogador é uma str.
#
# Mostre o resultado de cada verificação na tela.

# %%
numero_camisa = 10
jogador = "Raphinha"

print(isinstance(numero_camisa, int))
print(isinstance(numero_camisa, str))
print(isinstance(jogador, str))

# %% [markdown]
# Exercício 3 – Encontre o Erro e Corrija
# O código abaixo apresenta um erro:
#
# gols = "2"
# novo_gol = gols + 1
#
# print(novo_gol)
#
# Execute o código, observe a mensagem apresentada pelo Python e responda:
# Qual erro ocorreu?
# Quais são os tipos dos valores envolvidos?
# Por que esses valores não podem ser utilizados dessa forma?
# Corrija o programa para que o resultado exibido seja 3.

# %%
gols = "2"
#novo_gol = gols + 1
n_gols = int(gols) + 1

print(n_gols)


# Execute o código, observe a mensagem apresentada pelo Python e responda:
# Resp:
# TypeError: can only concatenate str (not "int") to str

# Qual erro ocorreu?
# Resp:
# Não é possível somar uma string com um inteiro.

# Quais são os tipos dos valores envolvidos?
# Resp:
# gols é uma string e 1 é um inteiro.

# Por que esses valores não podem ser utilizados dessa forma?
# Resp:
# Porque o Python não permite a concatenação de strings com inteiros diretamente.

# Corrija o programa para que o resultado exibido seja 3.
# Resp: 3

# %% [markdown]
# Exercício 4 – Trabalhando com input()
# Crie um programa que pergunte ao usuário quantos gols uma seleção marcou em uma partida.
#
# Depois:
#
# descubra o tipo do valor recebido diretamente pelo input();
# converta esse valor para int;
# mostre novamente o tipo depois da conversão;
# calcule quantos gols a seleção teria caso marcasse mais um.
#
# Exemplo de entrada:
#
# Quantos gols a seleção marcou? 2
# Resultado esperado ao final:
# Com mais um gol, a seleção teria 3 gols.

# %%
qtd_gols = input("Quantos gols a seleção marcou? ")

try:
    qtd_gols_int = int(qtd_gols)
    print(f"A seleção marcou {qtd_gols_int} gols.")
    print(f"Com mais um gol, a seleção teria {qtd_gols_int + 1} gols.")
    
except ValueError:
    print("Por favor, insira um número inteiro.")
        

# %% [markdown]
# Exercício 5 – Convertendo valores decimais
# Crie um programa que peça ao usuário:
#
# o nome de um jogador;
# sua nota na partida.
#
# A nota pode possuir casas decimais, como 8.5.
#
# Converta a nota para o tipo adequado e exiba uma mensagem semelhante a:
#
# Vinicius recebeu a nota 8.5.
#
# Antes de finalizar, utilize type() para verificar se a nota foi realmente convertida para o tipo esperado.

# %%
n_jogador = input("Digite o Nome do jogador: ")
nota = input(f"Digite a nota do jogador")

try:
    nota_float = float(nota)
    print(f"O jogador {n_jogador} recebeu a nota {nota_float}.")
except ValueError:
    print("Por favor, insira um valor decimal, com (.)ponto.")
    
# Resp:

    # digitando valor com vírgula, o programa retorna a mensagem: "Por favor, insira um valor decimal, com (.)ponto."
    # Digitando com ponto, o programa retorna a mensagem: "O jogador {n_jogador} recebeu a nota {nota_float}."
    # O jogador Jogador2 recebeu a nota 9.5.
    


# %% [markdown]
# numero = 10
# jogador = "Rodrygo"
#
# Crie uma mensagem que resulte em:
# O jogador Rodrygo veste a camisa 1.
#
# Para este exercício, faça a construção da mensagem utilizando +.
#
# Observe o erro que acontece ao tentar concatenar diretamente numero com os textos e depois utilize str() para corrigir o problema.
#
# Explique por que a conversão foi necessária.

# %%
numero = 10
jogador = "Rodrygo"

resultado = str(numero) +" "+ jogador
print (resultado)
# Poderia exibir dessa forma também:
#print(f"O jogador {jogador} veste a camisa número {numero}")

# Resp:
# Não pode somar um inteiro com uma string, resultando em um erro de tipo.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# %% [markdown]
# Exercício 7 – Deixando os valores explícitos
#
# Crie as seguintes variáveis utilizando Type Hint:
#
# nome da seleção → texto;
# quantidade de vitórias → número inteiro;
# aproveitamento → número decimal;
# seleção classificada → valor booleano.
#
# Atribua um valor para cada variável.
#
# Depois, altere propositalmente uma delas para um valor de outro tipo e observe o comportamento do Python.
#
# Com base no que aconteceu, responda:
#
# O Type Hint impede que uma variável receba outro tipo de valor durante a execução?

# %%
nome_selecao = "Brasil"
qtd_vitorias = 5
aproveitamento = 9.5
classificada = True

qtd_vitorias = "cinco"  # atribuindo uma string a uma variável anotada como int

print(qtd_vitorias)  # imprime normalmente: cinco

print(nome_selecao, qtd_vitorias, aproveitamento, classificada)

# Resp:
# Não. O Type Hint em Python Não impede que uma variável seja atribuido a um valor do tipo diferente do especificado.




# %% [markdown]
# Exercício 8 – Impedindo o programa de quebrar
# Crie um programa que pergunte a idade do usuário:
#
# Converta a resposta para int.
#
# Use try/except para impedir que o programa seja encerrado caso alguém digite algo como: vinte
#
# Se a conversão funcionar, mostre:
# Idade registrada com sucesso.
# Se ocorrer um ValueError, mostre:
# Digite a idade utilizando apenas números.

# %%

try:
     idade = int(input("Digite sua Idade: "))
     print(f"Sua idade é {idade}: Idade registrada com sucesso")
except ValueError:
     print("Digite a idade com apenas numeros inteiros")



# %% [markdown]
# Exercício 9 – Tratando entrada e validando o valor
#
# Uma avaliação de jogador deve receber uma nota entre 0 e 10.
#
# Crie um programa que peça essa nota ao usuário.
#
# O programa deve:
#
#
# tentar converter a entrada para float;
# tratar um possível ValueError;
# verificar se a nota está entre 0 e 10;
# informar quando a nota estiver fora desse intervalo.
#
# Exemplos:
#
# Digite a nota: oito
# Valor inválido. Digite um número.
#
# Digite a nota: 15
# A nota deve estar entre 0 e 10.
#
# Digite a nota: 8.5
# Nota registrada: 8.5

# %%
# Uma avaliação de jogador deve receber uma nota entre 0 e 10.

try:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota > 0 and nota < 11:
        print(f"A nota {nota} Nota foi regitrada com sucesso.")
    elif nota > 10:
        print("A nota deve estar entre 0 e 10.")
except ValueError:
    print("Digite um número")
    
        
       

# %% [markdown]
# Exercício 10 – Continue perguntando até receber um valor válido
#
# Crie um programa para registrar a quantidade de gols de uma seleção.
#
# O programa deve continuar perguntando:
#
# Quantos gols a seleção marcou?
#
# até que o usuário forneça um número inteiro válido e maior ou igual a zero.
#
# Considere situações como:
#
# Quantos gols a seleção marcou? três
# Entrada inválida.
#
# Quantos gols a seleção marcou? -2
# A quantidade de gols não pode ser negativa.
#
# Quantos gols a seleção marcou? 4
# Quantidade de gols registrada: 4
#
# Para resolver o exercício, utilize os conteúdos estudados até aqui, incluindo:
#
# input();
# conversão com int();
# try/except;
# ValueError;
# condição;
# while.
#
# O programa só deve parar de solicitar a informação quando receber um valor válido.

# %%
while True:
    try:
        gols = int(input("Quantos gols a seleção marcou? "))
        if gols < 0:
            print("A quantidade de gols não pode ser negativa.")
        else:       
            print(f"Quantidade de gols registrada: {gols}")
            break
    except ValueError:
       print("Entrada inválida.")
        
#Resp:
        
# três -> Entrada inválida.
# -2 -> A quantidade de gols não pode ser negativa.
# 4  -> Quantidade de gols registrada: 4

