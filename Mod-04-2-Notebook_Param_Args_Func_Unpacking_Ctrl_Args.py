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
def apresentar_jogador(
    nome= "Marta",
    posicao= "Atacante"
)-> str:
    print(f"Jogadora: {nome} | Posição: {posicao}")
apresentar_jogador()

# Jogadora: Marta | Posição: Atacante

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
def mostrar_partida(mandante = 'Brasil', visitante = 'Argentina')-> str:
    print(f"{mandante} x {visitante}")

mostrar_partida("Brasil", "Argentina")
mostrar_partida("Argentina", "Brasil")

# Brasil x Argentina
# Argentina x Brasil

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

def cadastrar_jogador(
    nome='Alisson',
    idade=33,
    posicao='Goleiro'
    )->None:
    print(f"{nome} - {idade} - {posicao}","\n")
  
cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)
cadastrar_jogador(nome="Alisson", posicao="Goleiro", idade=33)
cadastrar_jogador(nome="Alisson", idade=33, posicao="Goleiro")
cadastrar_jogador(idade=33, posicao="Goleiro", nome="Alisson") 


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

def registrar_gol(jogador, time, minuto)-> None:
    
    print(f"{jogador} marcou para o {time} aos {minuto} minutos")
    
registrar_gol('Vini Jr', 'Brasil', minuto=34)


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
def criar_partida(time_a, time_b, estadio='Estádio Nacional')-> None:
    print(time_a,time_b,estadio)
criar_partida('brasil', 'argentina')
criar_partida('brasil', 'argentina', 'Maracanã')


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
def registrar_jogador(
    nome,
    posicao="Não informada",
    titular=False
)-> None:
    
    print(f"{nome}, {posicao} {titular}")

registrar_jogador("Marta")
registrar_jogador("Marta", "Atacante")
registrar_jogador("Marta", "Atacante", True)
registrar_jogador("Marta", titular=True)


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
def configurar_camisa(
    nome,
    numero,
    tamanho="M",
    cor="amarela"
)->None:
    print(f"{nome} - {numero} - {tamanho} - {cor}")
    
configurar_camisa("Marta", 10, cor="azul")
configurar_camisa("Marta", 10, cor="verde")


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
# listar_jogadores("Marta")
# listar_jogadores("Marta","Vini Jr","Alisson")

# %%
# xercício 8 – Recebendo vários argumentos com *args

def lsitar_jogadores(*jogadores):
    for jogador in jogadores:
        print(jogador)
 
lsitar_jogadores("Marta\n")   
lsitar_jogadores("Marta", "Vini Jr", "Alisson")


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

def somar_gols(*qtd_gols: int)-> int:
    return sum(qtd_gols)   
total = somar_gols(2, 1, 3, 2)
print(total)


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

def convocar_selecao(pais, *jogadores):

    for jogador in jogadores:
        print(f"{pais} - {jogador}")

convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")


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

def mostrar_jogador(**dados)-> None:
    for k, v in dados.items():
        
        print(f"{k.capitalize()} - {v}")
    
mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")


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
def cadastrar_time(nome, **informacoes)->None:
    print(f"{nome}:")
    for k, v in informacoes.items():
        
        print(f"{k.capitalize()}: {v}")

cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)


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
def registrar_partida(
    time_a, 
    time_b, 
    *eventos, 
    **informacoes)-> None:
    print("----------------------------------------------------")
    print(f"Os dois times: {time_a} e {time_b}")
    print("----------------------------------------------------") 
    for ev in eventos:
        print(f"Todos os eventos recebidos: {ev}")
    print("----------------------------------------------------") 
    for k, v in informacoes.items():
        print(f"Todas as informações adicionais: {k.capitalize()}: {v}")
    print("----------------------------------------------------")
registrar_partida(
   "Brasil","Argentina",
   "Gol do Brasil",
   "Cartão amarelo",
   "Gol da Argentina",
   estadio="Maracanã",
   publico=70000
   )       
    
# ----------------------------------------------------
# Os dois times: Brasil e Argentina
# ----------------------------------------------------
# Todos os eventos recebidos: Gol do Brasil
# Todos os eventos recebidos: Cartão amarelo
# Todos os eventos recebidos: Gol da Argentina
# ----------------------------------------------------
# Todas as informações adicionais: Estadio: Maracanã
# Todas as informações adicionais: Publico: 70000
# ----------------------------------------------------

# %% [markdown]
# Exercício 14 – Unpacking com * e retorno
#
# Considere a seguinte lista:
#
# times = ["Brasil", "Argentina"]
# Crie uma função chamada montar_confronto que receba dois parâmetros:
#
# time_a
# time_b
#
#
# A função deve:
#
# Utilizar type hints nos parâmetros e no retorno.
# Possuir uma docstring explicando o que ela faz.
# Retornar uma string no formato Brasil x Argentina.
# Depois, chame a função desempacotando a lista com *.
#
# Você não deve acessar os valores manualmente com:
#
# times[0]
# times[1]
#
#
# Exemplo esperado de uso:
#
# confronto = montar_confronto(*times)
# print(confronto)

# %%
# Exercício 14 – Unpacking com * e retorno
def montar_confronto(
    time_a: str,
    time_b: str
    ) -> str: 
    """
        Retorna uma string no formato time A x time B
    Args:
        time_a: Nome do time
        time_b: Nome do time
    """
    return (f"{time_a} x {time_b}") 

times = ["Brasil", "Argentina"]    
       
confronto = montar_confronto(*times)
print(confronto)


# %% [markdown]
# Exercício 15 – Unpacking com * e valores padrão
#
# Crie uma função chamada calcular_media com os seguintes parâmetros:
#
# nota1
# nota2
# nota3
# bonus=0
#
# A função deve:
#
# Utilizar type hints em todos os parâmetros e no retorno.
# Possuir uma docstring.
# Calcular a média das três notas.
# Somar o valor de bonus ao resultado final.
# Retornar a média calculada.
#
# Considere:
# notas = [8.5, 7.0, 9.5]
#
# Chame a função utilizando * para desempacotar as notas:
#
# resultado = calcular_media(*notas)
# print(resultado)
#
# Depois, faça uma segunda chamada utilizando a mesma lista, mas informe bonus como argumento nomeado.
#
# Por fim, altere a lista para possuir quatro notas:
# notas = [8.5, 7.0, 9.5, 10.0]
#
# Tente realizar novamente:
#
# calcular_media(*notas)
#
#
# Observe o comportamento e explique por que o quarto valor deixa de representar uma nota e passa a ocupar o parâmetro bonus.

# %%
# Exercício 15 – Unpacking com * e valores padrão
def calcular_media(n1:float, n2:float, n3:float, bonus=0)->float:
    """
        Calcula média das notas:
    Args:
        n1: Nota da primeira prova:
        n2: Nota da segunda prova:
        n3: Nota da terceira prova:
        bonus: recebe o valor 0
    """
    return (n1 + n2 + n3) / 3 + bonus

notas = [8.5, 7.0, 9.5]
resultado = calcular_media(*notas, bonus=2)
print(f"{resultado:.2f}")
# como o valor do banus=2 foi somado + 2 a média.

print("-------------------------------------")

notas1 = [8.5, 7.0, 9.5, 10.0]
print(calcular_media(*notas1))

# Resposta:
# o 4º Valor ficou sendo o bonus e somou + 10 a média passando a ser 18.33 onde seria 8.33


# %% [markdown]
# Exercício 16 – Unpacking com ** e argumentos nomeados
#
# Considere o seguinte dicionário:
# jogador = {"nome": "Marta","idade": 40,"posicao": "Atacante"}
#
# Crie uma função chamada apresentar_jogador que receba:
# nome
# idade
# posicao
#
# A função deve:
#
# Utilizar type hints em todos os parâmetros.
# Indicar através do type hint que a função não retorna nenhum valor.
# Possuir uma docstring.
# Exibir uma mensagem com os dados do jogador.
#
# Chame a função desempacotando o dicionário com **.
#
# Você não deve acessar manualmente:
# jogador["nome"]
# jogador["idade"]
# jogador["posicao"]
#
# Depois, responda em um comentário no código:
#
# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?

# %%
# Exercício 16 – Unpacking com ** e argumentos nomeados

def apresentar_jogador(nome: str, idade:int, posicao:str)-> None:
    """
     Apresenta jogadores: imprime na tela informações dos jogadores
    *Args:
        nome:
        idade:
        posicao:
     """
    print(f"{nome} - {idade} - {posicao}")
            
jogador1 = {"nome": "Marta","idade": 40,"posicao": "Atacante"}
jogador2 = {"nome": "Neymar","idade": 37,"posicao": "Atacante"}

apresentar_jogador(**jogador1)
apresentar_jogador(**jogador2)

# Por que as chaves do dicionário precisam possuir os mesmos nomes dos parâmetros da função?
# Resposta:
# Por que, desempacota valores como argumentos nomeados e se os parâmetros são nomeados devem seguir todos.
#  **jogador transforma a chave em argumento nomeado (chave=valor) e se a chave for diferente da do parâmetro da TypeError.



# %% [markdown]
# Exercício 17 – *args recebendo e * desempacotando
#
# Crie uma função chamada calcular_total_gols que receba uma quantidade variável de números utilizando *args.
#
# A função deve:
#
# Utilizar type hint no *args.
# Possuir uma docstring.
# Somar todos os valores recebidos.
# Retornar o total de gols.
# Considere as listas:
#
# primeiro_tempo = [1, 2, 1]
# segundo_tempo = [2, 1]
#
# Chame a função desempacotando as duas listas na mesma chamada:
#
# total = calcular_total_gols(*primeiro_tempo,*segundo_tempo)
# print(total)
#
# Depois, escreva comentários no código explicando a diferença entre:
#
# def calcular_total_gols(*gols):...
# e: calcular_total_gols(*primeiro_tempo)
#
# Explique qual * está recebendo vários argumentos e qual está desempacotando uma coleção.

# %%
# Exercício 17 – *args recebendo e * desempacotando

def calcular_total_gols(*qtd_num:int)->int: # recebe vários dados dentro de qtd_num
    """
        Calula o total de gols:
    *Args
        qtd_num: Recebe uma quantidade de números variados    
    """
    return sum(qtd_num)
    
primeiro_tempo=[1,2,1]
segundo_tempo=[2,1]    
    
total=calcular_total_gols(*primeiro_tempo, *segundo_tempo) # Desempacota as variavel primeiro e segndo tempo.
print(total)
# def calcular_total_gols(*gols):... : aqui está recebendo vários argumentos e agrupa um uma tupla (gols)
# calcular_total_gols(*primeiro_tempo) : Aqui está desempacotando a lista . 



# %% [markdown]
# Exercício 18 – Parâmetros somente posicionais com /
#
# Crie uma função chamada registrar_placar com a seguinte assinatura:
#
# def registrar_placar(time_a: str,time_b: str,/,gols_a: int,gols_b: int) -> str:...
#
# A função deve:
#
# Possuir uma docstring.
# Utilizar os type hints indicados.
# Retornar uma string contendo o placar da partida.
# Exigir que time_a e time_b sejam passados somente por posição.
# Permitir que gols_a e gols_b sejam passados por posição ou pelo nome.
#
# Faça uma chamada válida utilizando:
#
# resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
# print(resultado)
#
# Depois, tente:
# registrar_placar(time_a="Brasil",time_b="Argentina",gols_a=2,gols_b=1)
#
# Observe o erro e explique em um comentário qual é a função do / na assinatura.

# %%
# Exercício 18 – Parâmetros somente posicionais com /

def registrar_placar(time_a: str, time_b: str, /, gols_a: int, gols_b: int) -> str:
    """
        Registra placar do jogo:
    Args:
        time_a: Nome do time A
        time_b: Nome do time B
        /     : Indica que parametros a ESQUERDA serão obrigatóriamente POSICIONAL
        gols_a: Quantidade de gols do time A
        gols_b: Quantidade de gols do time B
    """
    return(f"{time_a} x {time_b} - {gols_a} x {gols_b}")
   
resultado = registrar_placar("Brasil","Argentina",gols_a=2,gols_b=1)
# resultado = registrar_placar(time_a = "Brasil", time_b = "Argentina",gols_a=2,gols_b=1)
print(resultado)

# TypeError: registrar_placar() got some positional-only arguments passed as keyword arguments: 'time_a, time_b'
# o erro indica que quando está sendo utilizado / os argumento a esquerda são obrigatório serem passados apenas posicional e não nomeados




# %% [markdown]
# Exercício 19 – Parâmetros somente nomeados com *
#
# Crie uma função chamada criar_jogador com a seguinte assinatura:
#
# def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:...
#
# A função deve:
#
# Possuir uma docstring.
# Utilizar type hints.
# Utilizar um valor padrão para titular.
# Retornar uma string com os dados do jogador.
# O parâmetro nome pode ser informado por posição.
#
# Os parâmetros após * devem ser informados pelo nome.
#
# Faça uma chamada válida:
#
# jogador = criar_jogador("Marta",posicao="Atacante",numero=10)
# print(jogador)
#
#
# Depois, faça outra chamada informando:
# titular=True
#
# Por fim, tente executar:
# criar_jogador("Marta","Atacante",10)
#
# Observe o erro e explique em um comentário por que posicao e numero não podem ser passados por posição.
#
#

# %%
# Exercício 19 – Parâmetros somente nomeados com *

def criar_jogador(nome: str,*,posicao: str,numero: int,titular: bool = False) -> str:
    """
        Cria cadastro de jogadores:
    Args:
        nome: Nome do jogador
        *   : tudo direita do * é somente nomeado
        posicao: posição do jogador
        numero: Numero da camisa do jogador
        titular: Resposta booleana diz se o jogador é titular : sim ou não (True ou False)
    """
    return(f"{nome} x {posicao} - {numero} - {titular}")

jogador1 = criar_jogador("Neymar", posicao="Atacante", numero=10) # ok
jogador2 = criar_jogador("Marta", posicao="Atacante", numero=10, titular=True) # ok
jogador3 = criar_jogador("Neymar", "Atacante", titular=True) # erro: 
print(jogador1)
print(jogador2)
print(jogador3)

# TypeError: criar_jogador() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
# O (*) faz com que os argumentos (posicoes, numero e titular) sejam SOMENTE NOMEADOS obrigatóriamente ex: posicao="Atacante".



# %% [markdown]
# Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos
#
# Crie uma função chamada registrar_jogo com a seguinte assinatura:
#
# def registrar_jogo(
# mandante: str,visitante: str,
# /,
# competicao: str,
# *eventos: str,
# estadio: str,
# encerrado: bool = True,
# **informacoes
# ) -> dict:
#
# A função deve possuir uma docstring completa explicando:
#
# O objetivo da função.
# O que cada parâmetro representa.
# O que a função retorna.
#
# A função também deve seguir estas regras:
#
# mandante e visitante devem ser informados somente por posição.
# competicao pode ser passada por posição ou pelo nome.
# *eventos deve receber uma quantidade variável de eventos da partida.
# estadio deve obrigatoriamente ser informado pelo nome.
# encerrado deve possuir True como valor padrão.
# **informacoes deve receber informações adicionais da partida.
#
# Dentro da função, crie e retorne um dicionário contendo:
#
# Mandante.
# Visitante.
# Competição.
# Eventos.
# Estádio.
# Situação da partida.
# Informações adicionais.
# Teste a função com:
#
# partida = registrar_jogo(
# "Brasil",
# "Argentina",
# "Copa do Mundo",
# "Gol do Brasil",
# "Cartão amarelo",
# "Substituição",
# estadio="Maracanã",
# publico=70000,
# transmissao="TV"
# )
# print(partida)
#
# Depois, considere os seguintes dados:
#
# times = ["França", "Espanha"]
# dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}
#
#
# Faça uma segunda chamada utilizando:
#
# *times para desempacotar os dois primeiros argumentos.
# Uma competição informada normalmente.
# Dois ou mais eventos posicionais.
# **dados para desempacotar as informações nomeadas.
#
#
# Ao final, escreva comentários identificando o papel de cada elemento da assinatura:
#
# /
# *eventos
# estadio
# encerrado=True
# **informacoes
#
# Explique também a diferença entre:
#
# *eventos
# na definição da função e:
#
# *times
# na chamada, assim como a diferença entre:
#
# **informacoes
# na definição e:
#
# **dados
# na chamada.
#
#

# %%
# Exercício 20 – Desafio final: trabalhando com todos os tipos de argumentos
def registrar_jogo(
mandante: str,
visitante: str,
/,
competicao: str,
*eventos: str,
estadio: str,
encerrado: bool = True,
**informacoes
) -> dict:   
    """
        Registra partida de futebol: 
    Args
        mandante: informa o nome do time mandante da partida.
        visitante: informa o nome do time visitante da partida.
        competicao: é informado qual nome da competição ou campeonato.
        *eventos: armazena uma lista de eventos ocorridos na partida.
        estadio: informa o nome do estádio onde a partida ocorrerá.
        encerrado: retorna um sim ou não, se a partida está em andamento ou se foi encerrada.
        informacoes: armazena todas as informações da partida, se houve falta, cartão amarelo, penaltis etc..
        dict: retorna um dicionário.
    """
    return{"Mandante": mandante, "Visitante":visitante, 
           "Competição":competicao, "Eventos":eventos, 
           "Estádio":estadio, "Situação da partida":encerrado, 
           "Informações adicionais":informacoes}    
# Primeira chamada
partida = registrar_jogo(
    "Brasil"
    ,"Argentina"
    ,"Copa do Mundo"
    ,"Gol do Brasil"
    ,"Cartão Amarelo"
    ,"Substituição"
    ,estadio="Maracanã"
    ,publico= 70000
    ,transmissão="TV")
print(partida)

# Segunda chamada
times = ["França", "Espanha"]
dados = {"estadio": "Stade de France","publico": 65000,"transmissao": "Streaming"}
partida2 = registrar_jogo(*times,"Amistoso", "Gol da França", "Gol da Espanha", **dados)
print(partida2)

# Ao final, escreva comentários identificando o papel de cada elemento da assinatura:

# /              -> os argumentos que estiverem a esquerda serão obrigatóriamente usados como POSICIONAIS
# *eventos       -> Recebe vários argumentos
# estadio        -> é um parâmetro que por obrigação deverá ser nomeado ex: estadio="Maracanã"
# encerrado=True -> retorna um sim ou não, se a partida está em andamento ou se foi encerrada.
# **informacoes  -> Recebe vários argumentos nomeados e agrupa em um dicionário


# Explique também a diferença entre:
# *eventos --> na função está recebendo vários argumentos e agrupando numa (tupla)

# na definição da função e:
# *times --> desempacota a lista, espalhando cada elemento com argumentos posicionais

# na chamada, assim como a diferença entre:
# **informacoes --> recebe vários argumentos nomeados e agrupa em um dicionário

# na definição e: 

# **dados     --> desempacota o dicionário, espalhando cada chave=valor como argumentos nomeados.
# na chamada. 





