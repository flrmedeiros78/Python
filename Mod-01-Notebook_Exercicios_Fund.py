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

# %% [markdown]
# Exercício 1 – Criando suas primeiras variáveis
# Crie um programa para armazenar algumas informações sobre uma seleção:
#
# nome da seleção;
# quantidade de títulos;
# posição no ranking;
# se está classificada para a Copa.
#
# Ao final, imprima todos os valores na tela.

# %%
n_selecao = 'Brasil'
qtd_titulos = 5
pos_rank = 4
classificado_copa = True

print(f" A seleção: {n_selecao}\n Tem: {qtd_titulos} Títulos,\n Está na posição {pos_rank} do Ranking \n Classificada para a Copa do Mundo !")

# %% [markdown]
# Exercício 2 – Calculando o placar
#
# Uma seleção marcou 3 gols no primeiro tempo e 2 gols no segundo tempo.
#
# Crie variáveis para armazenar essas duas informações e calcule:
#
# o total de gols da partida;
# quantos gols foram marcados a mais no primeiro tempo em relação ao segundo.
#
# Ao final, imprima os resultados na tela.

# %%
gols_1_tempo = 3
gols_2_tempo = 2

print(f" A Seleção marcou no primeiro tempo: {gols_1_tempo} Gols\n No segundo tempo marcou {gols_2_tempo} Gols\n Qtd de gols marcados a mais no primeiro tempo foi de: {gols_1_tempo - gols_2_tempo}")

# %% [markdown]
# Exercício 3 – Trabalhando com operadores
#
# Considere:
#
# pontos = 7
# vitorias = 2
# saldo_gols = 4
#
# Crie expressões que respondam às seguintes perguntas:
#
# 1. A seleção possui mais de 5 pontos?
# 2. A seleção possui exatamente 3 vitórias?
# 3. O saldo de gols é maior ou igual a 0?
# 4. A seleção possui mais de 5 pontos e saldo de gols positivo?
# 5. A seleção possui 3 vitórias ou mais de 6 pontos?
#
# Mostre o resultado de cada expressão.

# %%
pontos = 7
vitorias = 2
saldo_gols = 4

if pontos > 5 and vitorias == 3 and saldo_gols >= 0: # false and false and true
    print(f" A seleção tem mais de 5 pontos e saldo positivo")
elif vitorias > 3 or pontos > 6: # false or true
    print(f" A seleção tem mais de 5 pontos e saldo positivo")
else:
    print(f" A seleção não tem mais de 5 pontos e saldo positivo")

    #resumo:
# 1	pontos > 5 → 7 > 5 => True
# 2	Vitorias == 3 → 2 == 3 => False
# 3	saldo_gols >= 0 → 4 >= 0 => True
# 4	pontos > 5 AND saldo_gols > 0 → True AND True => True
# 5	vitorias == 3 OR pontos > 6 → False OR True => True 

# %% [markdown]
# Exercício 4 – Seleção classificada ou eliminada?
#
# Crie uma variável chamada pontos e atribua a ela uma quantidade de pontos.
#
# Depois, utilizando if e else, faça o programa mostrar: "Seleção classificada!"
# caso tenha 6 pontos ou mais.
#
# Caso contrário, mostre: "Seleção eliminada."
# Teste o programa alterando manualmente o valor da variável para verificar os dois caminhos.

# %%
pontos = 5
if pontos > 6:
    print(' A seleção Classificada com mais de 6 pontos')
else:
    print('Seleção eleiminada')

# %% [markdown]
# Exercício 5 – Avaliando o desempenho da seleção
# Crie uma variável chamada pontos.
#
# Utilizando if, elif e else, classifique o desempenho da seleção da seguinte forma:
#
# 7 pontos ou mais → Excelente campanha
# de 4 a 6 pontos → Campanha regular
# menos de 4 pontos → Campanha ruim
# Teste o programa utilizando diferentes valores para pontos.

# %%
# 7 pontos ou mais → Excelente campanha
# 4 a 6 pontos → Campanha regular 
# menos de 4 pontos → Campanha ruim 
# Teste o programa utilizando diferentes valores para pontos.
pontos = 8
if pontos >= 7:
    print(' Excelente campanha')
elif pontos > 3 and pontos < 7:
    print('Campanha regular')
else:
    print('Campanha ruim')

#Testes:
# pontos = 7 → Excelente campanha
# pontos = 4 → Campanha regular
# pontos = 3 → Campanha ruim


# %% [markdown]
# Exercício 6 – Posição do jogador
#
# Utilizando o input(), peça ao usuário para informar a posição de um jogador. As opções esperadas são:
#
# - goleiro
# - defesa
# - meio
# - ataque
#
# Armazene a resposta em uma variável chamada posicao.
#
# Depois, utilize match case para verificar a posição informada e mostrar uma mensagem correspondente à função daquele jogador em campo.
#
# Por exemplo: Digite a posição do jogador: ataque
# Saída esperada: Responsável principalmente pela criação e finalização das jogadas ofensivas.
#
# Crie também um caso para quando o usuário digitar uma posição diferente das opções esperadas. Nesse caso, mostre: Posição inválida.

# %%
posicao = input('Digite a posição do jogador').lower()

match posicao:
    case 'goleiro':
        print('Responsável por defender o Gol')
    case 'defesa':
        print('Empedir que o adversário cute a gol')
    case 'Meio':
        print('Responsável por fazer passe e criar jogadas ofensivas e defensivas')
    case 'atacante':
        print('Responsável por marcar gol, e também ajudar a criar jogadas ofensivas')
    case _:
        print('Posição inválida !')   

# Usei o .lower() para deir que independente se o usuário digitar em maiusculo ou minusculo ele vai funcionar:


# %% [markdown]
# Exercício 7 – Simulando as cinco cobranças de pênalti
# Uma disputa de pênaltis começa com cinco cobranças para uma equipe.
#
# Utilize for e range() para mostrar na tela:
#
# - Cobrança 1
# - Cobrança 2
# - Cobrança 3
# - Cobrança 4
# - Cobrança 5
#
# Depois das cinco repetições, mostre: "Fim das cobranças iniciais."

# %%

for cobranca in range(1,6):
    if cobranca == 5:
        print(f'Fim da Cobrança')
       

# %% [markdown]
# Exercício 8 – Contando gols
# Crie uma variável: gols = 0
#
# Depois, utilize um for para simular 5 oportunidades de gol.
#
# A cada repetição, acrescente 1 à variável gols e mostre a quantidade atual.
#
# O resultado deve seguir esta ideia:
#
#
# Gol! Total: 1
# Gol! Total: 2
# Gol! Total: 3
# ...
#
# Ao final, mostre a quantidade total de gols.

# %%
gols = 0
for oport in range(1, 6):
  gols += 1
  print(f' Gol! Total: {gols}')
else:
  print(f' Total de gols: {gols}')


# Resultado:
# Gol! Total: 1
# Gol! Total: 2
# Gol! Total: 3
# Gol! Total: 4
# Gol! Total: 5
# Total de gols: 5

# %% [markdown]
# Exercício 9 – Continue até o usuário decidir parar
#
# Crie um programa que permaneça em execução enquanto o usuário responder: "sim"
#
# A cada repetição, mostre: "Treino iniciado!"
#
# Depois, pergunte novamente: "Deseja realizar outro treino?"
#
# Quando a resposta for diferente de sim, o while deve terminar e o programa deve mostrar: "Treino encerrado."
#
# Não é necessário trabalhar com números neste exercício. Utilize a resposta do input() como texto.

# %%
while True:
    resposta = input('Digite (S) para sim ou (N) para não').lower()
    if resposta == 's':
        print('\nTreino iniciado!')
    elif resposta == 'n':
        print('\nTreino encerrado.')
        break
    else:
       print('\n Resposta inválida, Tente novamente.\n')

# %% [markdown]
# Exercício 10 – Simulando uma sequência de cobranças
#
# Crie um pequeno programa para representar uma disputa de cinco pênaltis.
#
# Para cada cobrança, o programa deve perguntar ao usuário: "Resultado da cobrança: gol ou perdeu?"
#
# Utilize um for para garantir que sejam realizadas exatamente 5 cobranças.
#
# A cada resposta:
#
#
# se for gol, aumente o contador de gols em 1;
# se for perdeu, não aumente o contador;
# se for qualquer outro valor, mostre que a opção informada não foi reconhecida.
#
# Ao final das cinco cobranças:
#
# se a seleção tiver marcado 4 ou 5 gols, mostre: "Ótimo desempenho nos pênaltis!";
# se tiver marcado 2 ou 3, mostre: "Desempenho regular nos pênaltis.";
# se tiver marcado 0 ou 1, mostre: "Desempenho ruim nos pênaltis."
#
#
# Por fim, mostre também a quantidade total de gols marcados.
#
# Para resolver esta questão, combine conteúdos estudados ao longo do módulo, como:
#
# variáveis;
# - valores booleanos e comparações;
# - input();
# - if, elif e else;
# - for;
# - contador com +=.
#

# %%
#disputa de pênaltis:
gol = 0
perdeu = 0

for i in range(1, 6):
    resp = input('Digite Gol ou Perdeu').lower()
    if resp == 'gol':
        gol += 1
    elif resp == 'perdeu':
       pass
    else:
        print('informada não foi reconhecida')

if gol >= 4:
    print('Ótimo desempenho nos pênaltis!') 
elif gol >=2 and gol <=3:
    print('Desempenho regular nos pênaltis.')
else:
    print('Desempenho ruim nos pênaltis.')

print(f'Gols: {gol}')
