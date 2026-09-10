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
# # Aula 1 – Fundamentos das Estruturas de Dados e Listas
# # Aula 2 – Índices, Tuplas, Sets e Dicionários
# # Aula 3 – Trabalhando com Listas, Tuplas, Sets e Dicionários
# # Aula 4 – Integrando Estruturas de Dados e Fluxos de Controle

# %%
# Aula 1 – Fundamentos das Estruturas de Dados e Listas

# Tipos básicos de dados
nome = "Ana"
idade = 20
altura = 1.65
estudante = True

print(nome, idade, altura, estudante)

# Criando uma lista
frutas = ["maçã", "banana", "laranja"]
print("Lista:", frutas)

# Acessando elementos
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Adicionando e removendo elementos
frutas.append("uva")
frutas.remove("banana")
print("Lista atualizada:", frutas)

# Percorrendo a lista
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Quantidade de elementos
print("Total de frutas:", len(frutas))


# %%
# Aula 2 – Índices, Tuplas, Sets e Dicionários

# Índices em listas
frutas = []
print("Fruta pelo índice 0:", frutas[0])
print("Fruta pelo índice -1:", frutas[-1])

# Tupla: coleção ordenada e imutável
coordenadas = (10, 20)
cores = ("vermelho", "verde", "azul")

print("Coordenadas:", coordenadas)
print("Primeira cor:", cores[0])

# Set: coleção sem elementos repetidos
numeros = {1, 2, 2, 3, 4, 4}
numeros.add(5)

print("Set de números:", numeros)
print("3 está no set?", 3 in numeros)

# Dicionário: estrutura de chave e valor
aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Python"
}

print("Nome:", aluno["nome"])
aluno["idade"] = 21
aluno["cidade"] = "São Paulo"

print("Dicionário atualizado:", aluno)

# %%
# Aula 3 – Trabalhando com Listas, Tuplas, Sets e Dicionários

# Listas: adicionar, remover e ordenar
frutas=[]
frutas.append("manga")
frutas.sort()
print("Frutas ordenadas:", frutas)

# Tuplas: desempacotamento
coordenadas = []
x, y = coordenadas
print("Coordenada X:", x)
print("Coordenada Y:", y)

# Sets: união, interseção e diferença
numeros = []
outros_numeros = {4, 5, 6, 7}
print("União:", numeros | outros_numeros)
print("Interseção:", numeros & outros_numeros)
print("Diferença:", numeros - outros_numeros)

# Dicionários: acesso seguro e iteração
aluno={'aluno'}
print("Curso:", aluno.get("curso"))

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# %%
# Aula 4 – Integrando Estruturas de Dados e Fluxos de Controle

# Filtrando frutas com estrutura de repetição e condição
frutas_com_a = []

for fruta in frutas_com_a:
    if "a" in fruta:
        frutas_com_a.append(fruta)

print("Frutas que contêm a letra 'a':", frutas_com_a)

# Classificando números
numeros = []
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print("Números pares:", pares)
print("Números ímpares:", impares)

# Criando um resumo do aluno
aluno = []
resumo_aluno = {
    "nome": aluno["nome"],
    "idade": aluno["idade"],
    "curso": aluno["curso"],
    "maior_de_idade": aluno["idade"] >= 18
}

for chave, valor in resumo_aluno.items():
    print(f"{chave}: {valor}")

# %% [markdown]
# # Atividade Prática – Organizando Dados com Python

# %% [markdown]
# Exercício 1 – Cadastro de Figurinhas
# Você foi contratado para desenvolver um sistema simples para controlar um álbum de figurinhas da Copa do Mundo.
# O programa deve permitir que o usuário cadastre figurinhas até que ele digite a palavra "fim".
#
# Ao final, exiba:
#
# Todas as figurinhas cadastradas.
# A quantidade total de figurinhas.
# A primeira figurinha cadastrada.
# A última figurinha cadastrada.
#
# Desafio: não permita que o usuário cadastre uma figurinha vazia.

# %%
# Exercicio 01 - ok
fig_cad = []

while True:
    #try:
        figurinhas = input("Cadastre uma figurinha, ou digite 'fim' para encerrar: ")
        if figurinhas.strip() == '':
            print("Não é possível cadastrar uma figurinha vazia, Digite uma figurinha válida.\n")
        
        elif figurinhas.lower() == 'fim':
            break
        else:
            fig_cad.append(figurinhas)
    
    #except ValueError:
    #    print("Erro: Por favor, insira uma figurinha válida.\n")

if fig_cad:
    print("Lista de figurinhas cadastradas: ==>", fig_cad,"\n",
          "Quantidade de Figurinhas cadastradas :==> ", len(fig_cad),
          "\n Primeira figurinha cadastrada: :==> ", fig_cad[0],
          "\n Última figurinha cadastrada: :==>", fig_cad[-1])   
else:
    print("Nenhuma figurinha cadastrada.")
       


# %% [markdown]
# Crie um programa que solicite ao usuário as seguintes informações de uma partida:
#
# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante
#
# Armazene essas informações em um dicionário.
#
# Depois:
# Exiba todas as informações utilizando um for com .items().
# Informe qual seleção venceu a partida.
# Caso os gols sejam iguais, informe que a partida terminou empatada.
#
# Desafio: utilize try/except para garantir que a quantidade de gols seja um número inteiro válido.

# %%
#Exercício 02
sele_mandante = input("Digite o nome do Selecao Mandante: ")
sele_visitante = input("Digite o nome do Selecao Visitante: ")

while True:
    try:
        gols_mandante = int(input("Digite a quantidade de gols do Selecao Mandante: "))
        gols_visitante = int(input("Digite a quantidade de gols do Selecao Visitante: "))
        if gols_mandante < 0 or gols_visitante < 0:
            print("Digite valor maior ou igual a zero (0).")
            continue
        break
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido para os gols.")

inf_jogo = {
    "Selecao Mandante": sele_mandante,
    "Selecao Visitante": sele_visitante,
    "Gols Mandante": gols_mandante,
    "Gols Visitante": gols_visitante
}

for chave, valor in inf_jogo.items():
    print(f"{chave}: {valor}")

if gols_mandante > gols_visitante:
    print(f"Selecao", sele_mandante," Mandante venceu a partida")
elif gols_mandante < gols_visitante:
    print(f"Selecao", sele_visitante," Visitante venceu a partida")
else:
    print("A partida terminou empatada entre as Selecoes" )


# %%
#Exercício 02
inf_jogo = {}

inf_jogo["Selecao Mandante"] =  input("Digite o nome do Selecao Mandante: ")
inf_jogo["Selecao Visitante"] = input("Digite o nome do Selecao Visitante: ")

while True:
    try:
        inf_jogo["Gols Mandante"]  = int(input("Digite a quantidade de gols do Selecao Mandante:  "))
        inf_jogo["Gols Visitante"] = int(input("Digite a quantidade de gols do Selecao Visitante: "))
        
        if inf_jogo["Gols Mandante"] < 0 or inf_jogo["Gols Visitante"] < 0 :
            print("Digite um valor maior que zero(0)")
            continue
        break
    except ValueError:
        print("Insira um numero inteiro")
        
for chave, valor in inf_jogo.items():
    print(f"{chave}: {valor}")
    
if inf_jogo["Gols Mandante"] > inf_jogo["Gols Visitante"]:
    print(f"Selecao", inf_jogo ["Selecao Mandante"],"foi a Mandante do jogo e venceu a partida")
elif inf_jogo["Gols Mandante"] < inf_jogo["Gols Visitante"]:
    print(f"Selecao", inf_jogo ["Selecao Visitante"],"Foi a Visitante do jogo e venceu a partida")  
else:
    print("A partida terminou empatada entre as Seleções" )    

# %%
#Exercício 02 --> ok
inf_jogo = {}

inf_jogo['sele_mandante']  = input("Digite o nome do Selecao Mandante: ")
inf_jogo['sele_visitante'] = input("Digite o nome do Selecao Visitante: ")

while True:
    try:
        inf_jogo['gols_mandante'] = int(input("Digite a quantidade de gols do Selecao Mandante: "))
        inf_jogo['gols_visitante'] = int(input("Digite a quantidade de gols do Selecao Visitante: "))
        
        if inf_jogo['gols_mandante'] < 0 or inf_jogo['gols_visitante'] < 0:
            print("Digite valor maior ou igual a zero (0).")
            continue
        break
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido para os gols.")

print(inf_jogo,"\n")

for chave, valor in inf_jogo.items():
    print(f"{chave}, {valor}")

if inf_jogo['gols_mandante'] > inf_jogo['gols_visitante']:
    print(f"Seleção ",inf_jogo['sele_mandante']," venceu a apartida")
elif inf_jogo['gols_mandante'] < inf_jogo['gols_visitante']:
    print(f"Seleção ",inf_jogo['sele_visitante']," venceu a apartida")
else:
    print("A partida terminou empatada entre as Seleções", inf_jogo['sele_mandante'] ,"e", inf_jogo['sele_visitante'] )  
     



# %% [markdown]
# Exercício 3 – Seleções Classificadas
#
# Durante a fase de grupos, várias seleções foram sendo classificadas.
#
# Peça ao usuário para informar o nome de 8 seleções.
#
# Armazene essas seleções em um set.
#
# Ao final:
#
# Exiba todas as seleções classificadas.
# Informe quantas seleções diferentes foram cadastradas.
#
# Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.
#
# Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.

# %%
# Exercicio 3 -- ok
selecoes = set()
cadastro = 8

for ind in range(cadastro):
    cadastro = input(f"Cadastro  o nome da 8 seleções para cadastrar")

    selecoes.add(cadastro)
    cadastro = ind + 1
    
print(" Seleções classificadas: ", selecoes,'\n',f"Quantidade de seleções cadastradas: {len(selecoes)}")

while True:
    try:
        classificada = input("Digite o nome da seleção Classificada)")
        if classificada in selecoes:
            print("Seleção classificada")
            break
        else:
            print("Seleção não está classificada")
    except ValueError:
            print("Digite uma seleção cadastrada!")

# Exiba todas as seleções classificadas.
# Informe quantas seleções diferentes foram cadastradas.
# Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.  


# %% [markdown]
# Exercício 4 – Menu do Álbum
#
# Desenvolva um programa que simule um álbum de figurinhas.
#
# Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:
#
# 1. - Adicionar figurinha
# 2. - Remover figurinha
# 3. - Buscar figurinha
# 4. - Mostrar álbum
# 5. - Encerrar
#
# O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.
#
# Regras:
#
# Ao adicionar, a figurinha deve ser inserida no final da lista.
# Ao remover, informe caso a figurinha não exista.
# Na busca, informe se a figurinha está ou não no álbum.
# Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.
#
# Desafio: utilize if, elif, else e while.

# %%
# Exercicio 4 - ok mas quero fazer outra vez  
album = []

print(
" ======== Menu ========","\n"
"1 - Adicionar_figurinha","\n"
"2 - Remover_figurinha","\n"
"3 - Buscar_figurinha","\n"
"4 - Mostrar_álbum","\n"
"5 - Encerrar","\n"
"========================"
)
while True:
   
    try:
        opcao = int(input("\n Escolha uma opção: \n"))
                   
        if opcao == 1:
            figurinha = input("Cadastre uma figurinha com numeros de 0 a 100: ").strip()
            if figurinha not in album:
                album.append(figurinha)
                print(f"figurinha Cadastrada: {figurinha}")
            else:
                print(f"figurinha já foi cadastrada: {album}")
        
        elif opcao == 2:
            figurinha = input("Digite um numero de figurinha para REMOVER: ").strip()
            if figurinha in album:
                album.remove(figurinha)
                print(f"Figurinha removida foi :{figurinha}")
        
        elif opcao == 3:
            figurinha = input("Digite qual figurinha quer BUSCAR uma figurinha: ").strip()
         
            if figurinha in album:
                print(f"figurinha {figurinha} Encontrada no Album")
            else:
                print(f"figurinha {figurinha} Não Encontrad no Album")
        
        elif opcao == 4:
            if album:
                print(f"Quantidade de figurinhas no Album : ({len(album)}): {album}")
                for figurinha in album:
                    print("figurinha: ",figurinha)
            else:
                print("Album vazio: ") 
        
        elif opcao == 5:
            break
        else:
            print("Digite um numero de [1] até 4 e se quiser sair digite [5]")
        
    except ValueError:
        print("Digite um valor válido")
    


# %% [markdown]
# Exercício 5 – Ranking de Artilheiros
#
# Crie uma lista de dicionários para armazenar informações de jogadores.
#
# O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.
#
# Para cada jogador, solicite:
#
# Nome
# Seleção
# Quantidade de gols
#
# Cada jogador deverá ser armazenado como um dicionário dentro da lista.
#
# Ao final:
#
# Exiba todos os jogadores cadastrados.
# Informe qual jogador marcou mais gols.
# Informe a média de gols dos jogadores cadastrados.
#
# Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.

# %%
# Exercício 5 – Ranking de Artilheiros - ok
info_jogadores = [] 

qtd_jogadores = int(input("Digite a Quantidade de jogadores de Deseja Cadastrar: \n"))

# Lista de dicionário:        
for ind in range(qtd_jogadores):
     # está parando aqui        
    while True:
        try:  # Valida a quantidade de gols
            nome = input("Digite o nome do jogador: \n").strip()
            selecao = input("Digite a Seleção do Jogador: \n").strip()
            qtd_gols = int(input("Digite Quantidade de Gols: \n"))
            
            if qtd_gols < 0:
                print("Favor informar um numero interiro maior que zero(0)")
                continue
            
            jogador = {
                'nome': nome,
                'selecao': selecao,
                'qtd_gols': qtd_gols,
            }
            info_jogadores.append(jogador)
            break
        
        except ValueError:
            print("Digite um valor válido! ")

print(info_jogadores,"\n")

for jogador in info_jogadores:
    print("\nInformações de Jogadores: \n\n"
        f" Nome do Jogador: {jogador['nome']}","\n",
        f"Seleção: {jogador['selecao']}","\n",
        f"Quantidade de Gols: {jogador['qtd_gols']}")

# Informe qual jogador marcou mais gols.   
mais_gol = info_jogadores[0]
for jogador in info_jogadores:
    if jogador['qtd_gols'] > mais_gol['qtd_gols']:
        mais_gol = jogador
print("")
print(f"O jogador com mais gol é: {mais_gol['nome']}")
print("")     

# Calcula a Média de Gols marcados
total = 0
for jogador in info_jogadores:
    total = total + jogador['qtd_gols']
if qtd_jogadores > 0:
    media = total / qtd_jogadores     
    print("A Média de gol dos jogadores cadastrados é :",media)
   

# %% [markdown]
# Exercício 6 – Desafio Final: Sistema da Copa do Mundo
#
# Desenvolva um programa para cadastrar partidas da Copa do Mundo.
#
# O programa deverá permanecer em execução até que o usuário decida encerrá-lo.
#
# Para cada partida, solicite:
#
# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante
#
# Cada partida deverá ser armazenada em um dicionário, e todos os dicionários deverão ser armazenados em uma lista.
#
# Ao finalizar o cadastro, exiba:
#
# A quantidade de partidas cadastradas.
# Todas as partidas registradas.
# Quantas partidas terminaram empatadas.
# A partida com o maior número total de gols.
# A média de gols por partida.
#
# Requisitos:
#
# Utilize listas e dicionários.
# Utilize while para controlar o cadastro.
# Utilize for para percorrer as partidas.
# Utilize if, elif e else para identificar o resultado de cada jogo.
# Utilize try/except para validar os gols informados.
# Utilize len() para calcular a quantidade de partidas cadastradas.

# %%
# teste andrea
