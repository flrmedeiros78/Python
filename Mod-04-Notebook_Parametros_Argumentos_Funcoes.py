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
#     display_name: .venv (3.14.6)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Atividade Prática – Parâmetros e Argumentos em Funções

# %% [markdown]
# Exercício 1 – Argumentos posicionais
#
# Crie uma função chamada apresentar_jogador que receba:
#
# nome
# posicao
# A função deve exibir uma mensagem semelhante a:
#
# Jogador: Marta | Posição: Atacante
# Faça a chamada da função passando os dois argumentos por posição.
#
# Exemplo:
# apresentar_jogador("Marta", "Atacante")

# %%
# Exercício 1 – Argumentos posicionais



# %% [markdown]
# Exercício 2 – A ordem dos argumentos
#
# Crie uma função chamada mostrar_partida que receba:
#
# mandante
# visitante
# A função deve exibir os dois times no formato:
#
# Brasil x Argentina
#
# Faça as seguintes chamadas:
# mostrar_partida("Brasil", "Argentina")mostrar_partida("Argentina", "Brasil")
#
# Observe como a ordem dos argumentos posicionais altera o resultado.

# %%
# Exercício 2 – A ordem dos argumentos

# %% [markdown]
# Exercício 3 – Argumentos nomeados
#
# Crie uma função chamada cadastrar_jogador que receba:
#
# nome
# idade
# posicao
#
# Faça a chamada utilizando argumentos nomeados e passe os valores em uma ordem diferente da definida na função.
#
# Exemplo:
# cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)

# %%
# Exercício 3 – Argumentos nomeados

# %% [markdown]
# Exercício 4 – Posicionais e nomeados juntos
#
# Crie uma função chamada registrar_gol que receba:
#
# jogador
# time
# minuto
#
# Na chamada da função:
#
# Passe jogador por posição.
# Passe time por posição.
# Passe minuto pelo nome.
#
# A função deve exibir uma mensagem semelhante a:
#
# Vini Jr marcou para o Brasil aos 34 minutos.

# %%
# Exercício 4 – Posicionais e nomeados juntos

# %% [markdown]
# Exercício 5 – Parâmetro com valor padrão
#
# Crie uma função chamada criar_partida que receba:
#
# time_a
# time_b
# estadio
#
# O parâmetro estadio deve possuir o seguinte valor padrão:
#
# "Estádio Nacional"
#
# Depois, faça duas chamadas:
# 1. Uma sem informar o estádio.
# 2. Outra informando um estádio diferente.

# %%
# Exercício 5 – Parâmetro com valor padrão

# %% [markdown]
# Exercício 6 – Mais de um valor padrão
#
# Crie uma função chamada registrar_jogador com os seguintes parâmetros:
#
# nome
# posicao="Não informada"
# titular=False
#
# A função deve mostrar os dados do jogador.
#
# Teste as seguintes chamadas:
#
# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)
#
# Depois, faça mais uma chamada alterando apenas o valor de titular, utilizando um argumento nomeado.

# %%
# Exercício 6 – Mais de um valor padrão

# %% [markdown]
# Exercício 7 – Alterando apenas um valor padrão
#
# Crie uma função chamada configurar_camisa que receba:
#
# nome
# numero
# tamanho="M"
# cor="amarela"
#
# Faça uma chamada informando uma cor diferente, mas mantendo o tamanho padrão.
#
# Exemplo:
# configurar_camisa("Marta", 10, cor="azul")
# Observe como o argumento nomeado permite alterar cor sem precisar passar um novo valor para tamanho.

# %%
# Exercício 7 – Alterando apenas um valor padrão

# %% [markdown]
# Exercício 8 – Recebendo vários argumentos com *args
#
# Crie uma função chamada listar_jogadores que receba uma quantidade variável de nomes utilizando *args.
#
# def listar_jogadores(*jogadores):
#
# A função deve percorrer os jogadores recebidos e exibir cada nome.
#
# Teste a função com diferentes quantidades de argumentos:
#
# listar_jogadores("Marta")listar_jogadores("Marta","Vini Jr","Alisson")

# %%
# xercício 8 – Recebendo vários argumentos com *args

# %% [markdown]
# Exercício 9 – Trabalhando com os valores de *args
#
# Crie uma função chamada somar_gols que receba uma quantidade indefinida de números utilizando *args.
#
# A função deve retornar a soma de todos os valores recebidos.
#
# Exemplo:
#
# total = somar_gols(2, 1, 3, 2)
# print(total)
#
# Resultado esperado:
# 8

# %%
# Exercício 9 – Trabalhando com os valores de *args

# %% [markdown]
# Exercício 10 – Parâmetro normal e *args
#
# Crie uma função chamada:
# convocar_selecao(pais, *jogadores)
#
# O primeiro argumento deve representar o país da seleção.
#
# Todos os argumentos posicionais seguintes devem representar os jogadores convocados.
#
# Exemplo de chamada:
# convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")
# A função deve mostrar primeiro o país e depois cada jogador convocado.

# %%
# Exercício 10 – Parâmetro normal e *args


# %% [markdown]
# Exercício 11 – Recebendo argumentos nomeados com **kwargs
#
#
# Crie uma função chamada mostrar_jogador que receba uma quantidade variável de argumentos nomeados utilizando **kwargs.
#
# def mostrar_jogador(**dados):
#
# Faça uma chamada semelhante a:
#
# mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")
# Dentro da função, percorra os dados recebidos e mostre cada chave junto com seu respectivo valor.

# %%
# Exercício 11 – Recebendo argumentos nomeados com **kwargs

# %% [markdown]
# Exercício 12 – Parâmetro normal e **kwargs
#
# Crie uma função chamada:
#
# cadastrar_time(nome, **informacoes)
# O nome do time deve ser obrigatório.
#
# As demais informações podem variar de uma chamada para outra.
#
# Exemplo:
# cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)
# A função deve mostrar o nome do time e depois todas as informações adicionais recebidas.

# %%
# Exercício 12 – Parâmetro normal e **kwargs

# %% [markdown]
# Exercício 13 – *args e **kwargs juntos
#
# Crie uma função chamada:
#
# registrar_partida(time_a, time_b, *eventos, **informacoes):
# Os dois primeiros argumentos devem representar os times da partida.
#
# Os argumentos posicionais extras devem representar eventos ocorridos durante o jogo.
#
# Os argumentos nomeados extras devem representar outras informações sobre a partida.
#
# Exemplo:
#
# registrar_partida(
# "Brasil",
# "Argentina",
# "Gol do Brasil",
# "Cartão amarelo",
# "Gol da Argentina",
# estadio="Maracanã",
# publico=70000
# ):
#
# A função deve mostrar:
#
# Os dois times.
# Todos os eventos recebidos.
# Todas as informações adicionais.

# %%
# Exercício 13 – *args e **kwargs juntos
