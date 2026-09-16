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

# %%
# Funções
# Procedimentos
# Parâmetros, Argumentos e Retornos

# def imprimir_itens(lista):
#     for item in lista:
#         print(item)
  
# l1 = [1,2,3,4,5,6]
# imprimir_itens(l1)

# l2 = ["Luiza", "Luciano", "Caio", "Michelle"]
# imprimir_itens(l2)

# l3 = [12, "Luiza", 2512.24, True]
# imprimir_itens(l3)

def mostrar_inicio_processamento(numero_pedido: int) -> None:
    """
    Mostra na tela o início do processamento de um pedido.
    """
    print(f"Iniciando processamento do pedido #{numero_pedido}...")
    

def calcular_total(preco: float, 
                   quantidade: int, 
                   desconto: float
            ) -> float:
    """
    Calcula o valor final de um item após aplicar o desconto.
    
    Args:
        preco: Preço unitário do produto.
        quantidade: Quantidade comprada.
        desconto: Percentual de desconto em formato decimal.
        
    Returns:
        Valor final da compra.
    """
    subtotal: float = preco * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto
    
    return total


def registrar_processamento(
    numero_pedido: int,
    valor: float
) -> None:
    """
    Exibe uma confirmaçÃo do processamento de um pedido.
    
    Args:
        numero_pedido: Identificador do pedido (id).
        valor: Valor final do produto.
    """
    
    print(f"Pedido #{numero_pedido} processado com valor de R$ {valor:.2f}")
    

numero_pedido: int = 1058
mostrar_inicio_processamento(numero_pedido)

valor_final = calcular_total(
    preco=89.90,
    quantidade=3,
    desconto=0.10
)

registrar_processamento(numero_pedido, valor_final)


# %%
# Argumento Posicional
def cadastro_produtos(
        nome: str, 
        preco:float, 
        estoque: int
        ) -> str: #None:
    #cadastro_produtos('garrafa', 2.00, 5 )
    #return cadastro_produtos
    cadastro_produtos('teclado', 100.00, 5)
print(cadastro_produtos)
    
    #print(f"Produto{nome}",'\n',f"Preço{preco:.2f}",'\n',f"Estoque{estoque} unidades")
    #print(f"Produto{nome}")
    #print(f"Preço{preco:.2f}")
    #print(f"Estoque{estoque} unidades")
    
    
# cadastrar_produto2("Teclado", 150.0, 20)
# Teclado -> nome
# 150.0 -> preco
# 20 -> estoque

# Argumento Nomeado
# cadastrar_produto2(
#     "Mouse",      
#     200.50, 
#     estoque=50    
# )

# Parâmetros com valores padrão
 
 
 # *args
def calsular_total_modo_raiz(
     valor1: float,
     valor2: float,
     valor3: float
 ) -> float:
    
   return valor1 + valor2 + valor3
total = calsular_total_modo_raiz(89.90, 200.0, 510.0)
print(total)


def calcular_total(*valores: float)->float:
    #print(valores) 
    return sum(valores)

total2 = calcular_total(89.90, 200.00, 510.0, 731.21, 922.2)
print(total2)

def mostra_produtos(*produtos: str) -> None:
    print(produtos)
    
 # mostrar_produtos("Teclado", "Fone de Ouvido", "Mouse")
 
def calcular_total_pedido(*valores: float) -> float:
    # total = 0
    # print(valores)
    # for valor in valores:
        # total += valor

    return sum(valores)

total3 = calcular_total_pedido(
    120.0,
    89.90,
    45.50,
    199.90,
    491.34
)
print (f"Total de pedido: R${total:.2f}")
    
# Parâmetros normais + args
def registrar_pedido(
    num_pedido: int,
   *produtos: str
)-> None:
    
    print(f"Pedido #{num_pedido}")
    
    for produto in produtos:
        print(f"- {produto}")

# registrar_pedido(
#     1025,
#     "Notebook",
#     "Mouse",
#     "Fone de ouvido"
# )

# Kwargs
def cadastrar_cliente(**dados)->None:
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

# cadastrar_cliente(
#     nome="Luiza",
#     email="luiza@élegal.com",
#     cidade="Recife"
# )


# Parametros normais + **Kwargs
def cadastrar_cliente2(
    nome: str,
    email: str,
    **dados_adicionais
)-> None:
        
    print(f"nome: {nome}")
    print(f"email: {email}")

    for k, v in dados_adicionais:
        print(f"{k.capitalize()}:{v.capitalize()}")

# cadastrar_cliente2(
#     nome="Luiza",
#     email="luiza@élegal.com",
#     cidade="Recife",
#     estado="Pernambuco",
#     profissao="Engenheira de Dados"
# )

# *args e **kwargs juntos
def registrar_venda(
    cliente: str,
    *produtos: str,
    **dados_adicionais
) -> None:
    print(f"Cliente: {cliente}")
    
    print("\nProdutos")
    for produto in produtos:
        print(f"- {produto.capitalize()}")
        
    print("\nInformações da Venda")
    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v}")
        
# registrar_venda(
#     "Luiza",
#     "Notebook",
#     "Telefone",
#     "Mouse",
#     forma_pagamento="pix",
#     vendedor="Caio",
#     entrega=True
# )

# Unpacking (desempacotar) com *
def cadastrar_produto(
    nome: str,
    preco: float,
    estoque: int = 0,
    # ativo: bool = True
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")
    #print(f"Ativo: {ativo}")
    
# cadastrar_produto("Fone de Ouvido", 300.0, estoque=50)
produto = ["Teclado", 4500.0, 120]
produto2 = ("Notebook", 5000.0, 3)
# cadastrar_produto(
#     produto[0],
#     produto[1],
#     produto[2]
# )
cadastrar_produto(*produto)
#cadastrar_produto2(**produto2)

# Unpacking (desempacotar) com **
# cadastrar_produto2(
    # nome="Mouse",
    # preco=300.0,
    # estoque=8
# )
produto3 = {
    "nome": "Mouse",
    "preco": 300.0,
    "estoque": 8
}
#cadastrar_produto2(**produto3)

# * -> desempacota como argumentos POSICIONAIS (tupla)
# ** -> desempacota como argumentos NOMEADOS (dicionário)

"""
def funcao(*args)
* está recebendo (tupla)

def funcao(**kwargs)
** estão recebendo (dicionário)

funcao(*lista)
* está desempacotando

funcao(**dicionario)
** estão desempacotando
Precisamos que as chaves do dicionário sejam correspondentes aos parâmetros
"""

# / - Parâmetros somente POSICIONAIS (tudo a esquerda)
def calcular_desconto(
    preco: float,
    desconto: float,
    / # Tudo que aparece antes da / deve ser passado como um argumento posicional
) -> float:
    return preco - (preco * desconto)

calcular_desconto(500, 0.10)
#calcular_desconto(preco=500, desconto=0.10)
#calcular_desconto(500, desconto=0.10)

def registrar_venda2(
    codigo: int,
    /,
    cliente: str
) -> None:
    print(codigo)
    print(cliente)
    
registrar_venda2(500, "Luiza")
registrar_venda2(500, cliente="Luiza")

# * - Parâmetros somentos NOMEADOS (tudo a direita)
def exportar_relatorio(
    nome_arq: str,
    *,
    incluir_cabecalho: bool,
    compactar: bool
) -> None:
    print(nome_arq)
    print(incluir_cabecalho)
    print(compactar)
    
exportar_relatorio("vendas.csv", incluir_cabecalho=True, compactar=True)
# Atenção: esse * não é o *args
def funcao(*args):
    pass

def funcao(a, *, b): 
    ...
    
# / e * juntos
def processar_pagamento(
    numero_pedido: int, # ARG. POSICIONAL
    valor: float,       # ARG. POSICIONAL
    /, # / -> separador que indica que tudo a esquerda deve ser passado como um argumento POSICIONAL
    forma_pagamento: str, # ARG. TANTO PODE SER POSICIONAL QUANTO NOMEADO
    *, # * -> separador que indica que tudo a direita deve ser passado como um argumento NOMEADO
    enviar_comprovante: bool = True # ARG. NOMEADO
) -> None:
    print(f"Pedido: {numero_pedido}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Pagamento: {forma_pagamento}")
    print(f"Enviar comprovante: {enviar_comprovante}")
    
processar_pagamento(
    1050,
    500,
    "Pix",
    enviar_comprovante=True
)

def funcao(
    a, # ARG. POSICIONAL
    b, # ARG. POSICIONAL
    /, # SEPARADOR (TUDO A ESQUERDA É UM ARGUMENTO OBRIGATÓRIAMENTE POSICIONAL)
    c, # RECEBE ARG. POSICIONAL OU NOMEADO
    d, # RECEBE ARG. POSICIONAL OU NOMEADO
    *args, # RECEBE ARG. POSICIONAL EXTRA (EMPACOTA NUMA TUPLA)
    e, # COMO O *ARGS JÁ CAPTURA OS ARGUMENTOS POSICIONAIS QUE SOBRAREM, O PARÂMETRO e E f FICA SENDO OBRIGATORIAMENTE COMO ARGUMENTOS NOMEADODS
    f,
    **kwargs # NOMEADOS RESTANTES (QUE VAO SER EMPACOTADOS COMO UM DICIONÁRIO)
):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("args:", args)
    print("e:", e)
    print("f:", f)
    print("kwargs:", kwargs)




# %%
def calcular_total(preco: float, quantidade: int, desconto: float) -> float:
    """
        Calcula o valor final de um item após o desconto
    
    Args:
        preco: Preço unitário do produto
        quantidade: quantidade comprada
        desconto: Percentual de desconto em formato decimal
    
    Returns:
        Valor final da compra.
    
    """
    subtotal = preco * quantidade
    valor_desconto = subtotal - desconto
    total = valor_desconto
    
    return total
#help(calcular_total)

#valor_final = calcular_total(89.90, 3, 0.10)

#print(f'Valor do pedido foi: {valor_pedido:.2f}')
#print(f"O valor final do pedido {valor_final:.2f}")

print()

def regitra_proessamento(num_pedido: int, valor: float) -> None:
    """
        Exibe uma confirmação do processamento de um pedido.
    
    args:
        num_pedido: Número do pedido
        valor: Valor do pedido 
    """
    print(f"Pedido #{num_pedido} processado com valor de R${valor:.2F}")


def mostra_ini_processamento(num_pedido: int) -> None:
    """
        Mostra na tela o início do processamento de um pedido
       
    """
          
    num_pedido: int = 1058
    mostra_ini_processamento(num_pedido)
    
    valor_final = calcular_total()


# %% [markdown]
# Exercício 1 – Exibindo uma mensagem
#
# Crie uma função chamada exibir_boas_vindas() que exiba a mensagem: Bem-vindo ao sistema!
#
# Depois, chame a função para executar a mensagem.
#
# Requisitos:
#
# Utilize def.
# A função não deve receber parâmetros.
# A função não precisa retornar nenhum valor.

# %%
# Exercicio 01 - ok

def exibir_boas_vindas()-> None:
    print("Seja Bem-Vindo ao Sistema!")
exibir_boas_vindas()

# Seja Bem-Vindo ao Sistema!


# %% [markdown]
# Exercício 2 – Identificando um produto
#
# Crie uma função chamada exibir_produto() que receba:
#
# o nome de um produto;
# o preço do produto.
#
# A função deve exibir uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00
#
# Depois, chame a função passando um produto e um preço como argumentos.
#
# Requisitos:
# Utilize parâmetros.
# Adicione type hints nos parâmetros.
# A função deve retornar None.

# %%
# Exercicio 02 - ok
def exibir_produto(nm_produto: str, preco: float )->None:
       
    print(f"Produto: {nm_produto} | Preço: R$ {preco:.2f}")
  
exibir_produto(nm_produto='Teclado', preco=150.00)
# Produto: Teclado | Preço: R$ 150.00

# %% [markdown]
# Exercício 3 – Calculando o valor de uma compra
#
# Crie uma função chamada calcular_total() que receba:
#
# o preço de um produto;
# a quantidade comprada.
#
# A função deve calcular e retornar o valor total da compra.
#
# Exemplo:
#
# total = calcular_total(50.0, 3)
# print(total)
#
# Resultado esperado: 150.0
#
# Requisitos:
# preco deve possuir type hint float.
# quantidade deve possuir type hint int.
# A função deve indicar que retorna um float.
# Utilize return para devolver o resultado.

# %%
# Exercício 03
def calcular_total(preco_prod: float, qtd: int)-> float:
    
    valor_total = preco_prod * qtd
    return (valor_total)

vtotal = calcular_total(50.0, 3)
print(vtotal)


# %% [markdown]
# Exercício 4 – Calculando a média de avaliações
#
# Uma plataforma armazena três avaliações dadas por usuários para um produto.
#
# Crie uma função chamada calcular_media_avaliacoes() que receba três notas e retorne a média entre elas.
#
# Depois, utilize o resultado retornado pela função para exibir a média das avaliações
#
# Requisitos:
#
# Utilize parâmetros e argumentos.
# Adicione type hints.
# Utilize return.
# Adicione uma docstring explicando o que a função recebe e o que retorna.
# Guarde o resultado da função em uma variável antes de exibi-lo.

# %%
# Exercício 04 - ok

def calcular_media_avaliacoes(nota1: float, nota2: float, nota3: float) -> float:
    """
        Calcula a média entre três notas:
    args:
        nota1: recebe o valor da primeira nota
        nota2: recebe o valor da segunda nota
        nota3: recebe o valor da terceira nota
    """
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return (media)
nfinal = calcular_media_avaliacoes(7.0, 4.5, 8.9)
print(f"A Nota Final: {nfinal:.2f}")


# %% [markdown]
# Exercício 5 – Processando um pedido
#
# Você precisa criar duas funções para representar uma pequena parte de um sistema de pedidos.
#
# A primeira função deve se chamar: calcular_valor_final()
#
# Ela deve receber:
#
# preço unitário;
# quantidade;
# desconto em formato decimal.
# Por exemplo, 0.10 representa 10% de desconto.
#
# A função deve calcular e retornar o valor final do pedido após o desconto.
#
# Depois, crie uma segunda função chamada: exibir_resumo_pedido()
#
# Ela deve receber:
# número do pedido;
# valor final.
#
# E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00
#
# Requisitos:
# 1. As duas funções devem possuir type hints. 
# 2. calcular_valor_final() deve retornar um float.
# 3. exibir_resumo_pedido() deve retornar None.
# 4. As duas funções devem possuir docstrings.
# 5. O valor retornado por calcular_valor_final() deve ser passado como argumento para exibir_resumo_pedido().
# 6. Não faça o cálculo diretamente fora da função.

# %%
# Exercício 05 - ok

def calcular_valor_final(preco_un: float, qtd: int, desconto: float)-> float:
    """
        Calcula valor com desconto:
    Args:
        preco: Valor do produto.
        qtd: Quantidade de produtos
        desconto:  Desconto percentual em formato decimal    
    """
    subtotal:float = preco_un * qtd
    valor_desc: float = subtotal * desconto
    valor_total:float = subtotal - valor_desc
       
    return (valor_total)

vtotal = calcular_valor_final(100, 2, 0.10)
print(f"Valor Total com desconto: R${vtotal:.2f}")

def exibe_resumo_pedido(
    num_pedido: int, 
    valor_final: float 
    )-> None:
      
    """
        Calcula valor com desconto:
    Args:
        num_pedido: Numero do pedido [Código Id].
        valor_final: Valor final do pedido. 
    """
    
    print(f"Pedido #{num_pedido} Finalizado. Total: R${valor_final:.2f}")
Resumo = exibe_resumo_pedido(1025, vtotal)   
    
#Valor Total com desconto: R$900.00
#Pedido #1025 Finalizado. Total: R$900.00



# %% [markdown]
# Exercício 6 – Convertendo temperatura
#
# Crie uma função chamada converter_celsius_para_fahrenheit().
#
# A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.
#
# Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32
#
# Depois, armazene o resultado em uma variável e imprima a temperatura convertida.
#
# Requisitos:
#
# Receba a temperatura por parâmetro.
# Utilize type hint float.
# A função deve retornar um float.
# Utilize return.
# Adicione uma docstring explicando a função.

# %%
# Exercício 06 - ok
def converter_celsius_para_fahrenheit(Celsius: float)-> float:
    """
        Converte Celsius para Fahrenheit
    Args:
        temperatura: temperatura em Celsius
    """
    fahrenheit:float = (Celsius * 9/5)+32
    #conv:float = fahrenheit
    return(fahrenheit)
fahrenheit = converter_celsius_para_fahrenheit(50.00)
print(f"A Temperatura em fahrenheit:{fahrenheit:.2f}") 
# A Temperatura em fahrenheit:212.00

# %% [markdown]
# Exercício 7 – Calculando consumo médio
#
# Um veículo percorreu determinada distância utilizando uma quantidade de combustível.
#
# Crie uma função chamada calcular_consumo_medio() que receba:
#
# distância percorrida em quilômetros;
# quantidade de litros utilizados.
#
# A função deve retornar quantos quilômetros o veículo percorreu por litro.
#
# Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
# Resultado: 12.0
#
# Depois, crie uma segunda função chamada exibir_consumo() que receba o resultado e exiba: Consumo médio: {resultado} km/l
#
# Requisitos:
# As duas funções devem possuir type hints.
# calcular_consumo_medio() deve retornar float.
# exibir_consumo() deve retornar None.
# As duas funções devem possuir docstrings.
# O resultado da primeira função deve ser passado como argumento para a segunda.

# %%
# Exercício 07 - ok
def  calcular_consumo_medio(dist_km: float, qtd_litros: float)-> float:
    """
        Calcula a média de consumo km/l
    Args:
        dist_km: Distância percorrida em Km
        qtd_litros: Quantidade de litros
    """
    km_litros = dist_km / qtd_litros

    return (km_litros)
consumo_medio = calcular_consumo_medio(420.00, 35.0)

def exibir_consumo(consumo_medio: float)-> None:
    """
        Exibe o consumo médio calculado:
      Args:
          consumo_medio: resultado calculado pela função Calcula_consumo_medio.
    """
    print(f"Consumo médio: {consumo_medio:.2f} km/l")
exibir_consumo(consumo_medio)

# Consumo médio: 12.00 km/l

# %% [markdown]
# Exercício 8 – Verificando uma meta de vendas
#
# Crie uma função chamada calcular_percentual_meta() que receba:
# valor da meta;
# valor vendido.
#
# A função deve calcular e retornar o percentual da meta que foi atingido.
#
# Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
# Resultado: 75.0
#
# Depois, crie uma função chamada exibir_status_meta() que receba esse percentual.
#
# Ela deve exibir: Meta atingida!
# caso o percentual seja maior ou igual a 100.
#
# Caso contrário, deve exibir: Meta ainda não atingida.
#
# Requisitos:
# Utilize type hints.
# calcular_percentual_meta() deve retornar float.
# exibir_status_meta() deve retornar None.
# Utilize o valor retornado por uma função como argumento da outra.
# Adicione docstrings nas duas funções.
# Não repita o cálculo do percentual fora da função.

# %%
# Exercício 08 - ok
def calcular_percentual_meta(v_meta: float, v_vendido:float)-> float:
    """
        Calcula média percentual de vendas de produtos:
    Args:
        v_meta: Valor da meta a ser alcançada, pelo vendedor.
        v_vendido: Valor do produto vendido
    """
    percentual = (v_vendido / v_meta)*100
    
    #percentual = v_meta
    return(percentual)
percentual = calcular_percentual_meta(10000.0, 7500.0)

def exibir_status_meta(percentual: float)-> None:
    """
        Exibe o status da meta:
    Args:
        percentual: Percentual da meta alcançada.
    """
    if percentual >= 100.00:
        print(f'Meta atingida! {percentual}')
    else:
        print(f'Meta ainda não atingida! {percentual}')

exibir_status_meta(percentual)

# Meta ainda não atingida! 75.0


# %% [markdown]
# Exercício 9 – Analisando uma entrega
#
# Você está desenvolvendo uma pequena parte de um sistema de entregas.
#
# Crie uma função chamada calcular_tempo_estimado() que receba:
#
# distância da entrega em quilômetros;
# velocidade média do veículo em km/h.
#
# A função deve calcular e retornar o tempo estimado da entrega em horas.
#
# Use: tempo = distancia / velocidade
#
# Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:
#
# "Entrega rápida" se o tempo for menor ou igual a 1;
# "Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
# "Entrega demorada" se o tempo for maior que 3.
#
# Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:
# o tempo estimado;
# a classificação.
#
# Ela deve exibir algo como:
# Tempo estimado: 2.5 horas
# Classificação: Entrega normal
#
#
# Requisitos:
# As três funções devem possuir type hints.
# calcular_tempo_estimado() deve retornar float.
# classificar_entrega() deve retornar str.
# exibir_resumo_entrega() deve retornar None.
# Todas devem possuir docstrings.
# O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
# Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
# Cada função deve possuir apenas uma responsabilidade.

# %%
# Exercício 9 - ok

def calcular_tempo_estimado(dist_entrega_km: float, veloc_med_km: float)-> float:
    """
        Calcula o tempo estimado para entrega
    Args:
        dist_entrega_km: Distancia da entrega em kilometros
        veloc_med_km: velocidade média do veículo em km/h
    """
    t_estimado = dist_entrega_km / veloc_med_km
    return(t_estimado)

t_estimado = calcular_tempo_estimado(20.00, 5)

def classificar_entrega(t_estimado: float)-> str:
    """
        Classificação por tempo de entrega
    Args:
        t_estimado: Tempo estimado para entrega em Horas   
    """
    if t_estimado <= 1:
        return("Entrega rápida")
    elif t_estimado <= 3:
        return("Entrega normal")
    else:
        return("Entrega demorada")
       
classificacao = classificar_entrega(t_estimado)

def exibir_resumo_entrega(t_estimado: float, classificacao: str ) -> None:
    """
        Exibe o resumo da entrega
    Args:
        t_estimado: Tempo estimado para entrega em horas.   
    """
    print(f"O tempo estimado foi: {t_estimado:.2f} h/s")
    print(f"A classificação do tempo de entrega: {classificacao}")

exibir_resumo_entrega(t_estimado, classificacao)    

# Testes : t_estimado = calcular_tempo_estimado(20.00, 20)
#  O tempo estimado foi: 1.00 h/s
#  A classificação do tempo de entrega: Entrega rápida

# Testes : t_estimado = calcular_tempo_estimado(20.00, 15)
#  O tempo estimado foi: 1.33 h/s
#  A classificação do tempo de entrega: Entrega normal

# Testes : t_estimado = calcular_tempo_estimado(20.00, 5)
#  O tempo estimado foi: 4.00 h/s
#  A classificação do tempo de entrega: Entrega demorada

# %% [markdown]
# Exercício 10 – Sistema de Aprovação de Empréstimo
#
# Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.
#
# O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.
#
# 1. Calcular comprometimento da renda
# Crie uma função chamada calcular_comprometimento_renda() que receba:
#
# renda mensal;
# valor da parcela do empréstimo.
# Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.
#
# Use: percentual = (parcela / renda) * 100
#
# A função deve retornar esse percentual.
#
# 2. Analisar o empréstimo
# Crie uma segunda função chamada analisar_emprestimo() que receba:
#
# renda mensal;
# valor solicitado;
# percentual de comprometimento da renda.
# A função deve retornar uma das seguintes classificações:
#
# "Aprovado"
# "Análise manual"
# "Recusado"
#
# Utilize estas regras:
#
# Se o comprometimento da renda for maior que 40%, retorne "Recusado".
# Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
# Caso contrário, retorne "Aprovado".
#
# 3. Calcular o total do pagamento
# Crie uma terceira função chamada calcular_total_pagamento() que receba:
#
# valor da parcela;
# quantidade de parcelas.
# Ela deve retornar o valor total que será pago ao final do empréstimo.
#
# Exemplo:
# Parcela: R$ 850.00
# Quantidade: 24
#
# Total pago: R$ 20400.00
#
# 4. Exibir o resultado final
# Por fim, crie uma função chamada exibir_resultado() que receba:
#
# valor solicitado;
# percentual de comprometimento;
# total que será pago;
# resultado da análise.
# Ela deve apenas exibir um resumo como:
#
# --- Análise do empréstimo ---
#
# Valor solicitado: R$ 15000.00
# Comprometimento da renda: 28.3%
# Total a pagar: R$ 20400.00
#
# Resultado: Aprovado
#
# Essa função não deve retornar nenhuma informação.
#
# Requisitos
# 1. Todas as funções devem possuir type hints.
# 2. Todas devem possuir docstrings.
# 3. calcular_comprometimento_renda() deve retornar float.
# 4. analisar_emprestimo() deve retornar str.
# 5. calcular_total_pagamento() deve retornar float.
# 6. exibir_resultado() deve retornar None.
# 7. Os cálculos devem acontecer dentro das funções responsáveis por eles.
# 8. Não repita cálculos fora das funções.
# 9. Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
# 10. A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
# 11. Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.
#
# Fluxo esperado
#
# dados do empréstimo
# ↓
# calcular comprometimento da renda
# ↓
# analisar empréstimo
# ↓
# calcular total do pagamento
# ↓
# exibir resultado final
#
# O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.

# %%
# Exercício 10 - ok
def calcular_comprometimento_renda(renda_mensal:float, v_parcela_emprestimo: float)->float:
    """
        Calcular comprometimento da renda
    Args:
        renda_mensal: Renda mensal recebida
        v_parcela_emprestimo: valor da parcela do emprestimo
    """
    percentual = (v_parcela_emprestimo / renda_mensal) * 100
    #print(f"{percentual:.2f}")
    return (percentual)
        
percentual = calcular_comprometimento_renda(12000.00, 1500.00)

def analisar_emprestimo(renda_mensal: float, v_solicitado: float, percentual: float)-> str:
    """
        Analise de empréstimo
    Args:
        renda: Renda mensal recebida
        v_solicidado: Valor solicitado do empréstimo
        parcela: valor da parcela do empréstimo
     """
    
    if percentual > 40 :
        return("Recusado")
    elif v_solicitado > 5 * renda_mensal:
        return("Análise Manual")
    else:
        return("Aprovado")

def calcular_total_pagamento(v_parcela: float, qtd_parcelas: int)-> float:
    """
        Calcula o total do pagamento
    Args:
        v_parcela: valor da parcela.
        qtd_parcelas: quantidade de parcelas.
     """
    total = v_parcela * qtd_parcelas
    #print(f"{total:.2f}")
    return(total)
total = calcular_total_pagamento(850.00, 24)

def exibir_resultado(v_solicitado: float, percentual: float, total: float, resultado: str)-> None:
    """
        Exibe o resultado final
    Args:
        v_solicidado: Valor solicitado do empréstimo
        percentual: Percentual do comprometimento
        total: Valor total que será pago.
        resultado: Resultado da análise
     """ 
    print("--- Análise do empréstimo ---\n")
    print(f"Valor solicitado: R${v_solicitado:.2f}")
    print(f"Comprometimento da renda: {percentual:.2f}%")
    print(f"Total a pagar: R${total:.2f}")
    print(f"Resultado: {resultado}")
    print("-----------------------------")

# Testes realizados: Recusado (percentual > 40):
percentual = calcular_comprometimento_renda(renda_mensal=10000.00, v_parcela_emprestimo=5000.00)
resultado  = analisar_emprestimo(renda_mensal=10000.00, v_solicitado=50000.00, percentual=percentual)
total      = calcular_total_pagamento(v_parcela=5000.00, qtd_parcelas=24)
exibir_resultado(v_solicitado=50000.00, percentual=percentual, total=total, resultado=resultado)

#--- Análise do empréstimo ---
#
#Valor solicitado: R$50000.00
#Comprometimento da renda: 50.00%
#Total a pagar: R$120000.00
#Resultado: Recusado


# Testes realizados: Análise manual (percentual ≤ 40, mas v_solicitado > 5×renda):
percentual = calcular_comprometimento_renda(renda_mensal=10000.00, v_parcela_emprestimo=3000.00)
resultado  = analisar_emprestimo(renda_mensal=10000.00, v_solicitado=60000.00, percentual=percentual)
total      = calcular_total_pagamento(v_parcela=3000.00, qtd_parcelas=24)
exibir_resultado(v_solicitado=60000.00, percentual=percentual, total=total, resultado=resultado)   

#--- Análise do empréstimo ---
#
#Valor solicitado: R$60000.00
#Comprometimento da renda: 30.00%
#Total a pagar: R$72000.00
#Resultado: Análise Manual


# Testes realizados: Aprovado (percentual ≤ 40 e v_solicitado ≤ 5×renda):
percentual = calcular_comprometimento_renda(renda_mensal=10000.00, v_parcela_emprestimo=3000.00)
resultado = analisar_emprestimo(renda_mensal=10000.00, v_solicitado=40000.00, percentual=percentual)
total = calcular_total_pagamento(v_parcela=3000.00, qtd_parcelas=24)
exibir_resultado(v_solicitado=40000.00, percentual=percentual, total=total, resultado=resultado)   

#--- Análise do empréstimo ---
#
#Valor solicitado: R$40000.00
#Comprometimento da renda: 30.00%
#Total a pagar: R$72000.00
#Resultado: Aprovado
#-----------------------------
