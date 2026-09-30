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
#import pandas as pd
#df = pd.read_csv("data/Dados.csv")
#df.head()
#print(df)
# executando com Jupytext salvando em memoria e escrevendo em disco no arquivo.py

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
        opcao = int(input("Escolha uma opção: "))
                   
        if opcao == 1:
            figurinha = int(input("Digite o número da figurinha:: "))
            if figurinha not in album:
                album.append(figurinha)
                print("figurinha Cadastrada")
            else:
                print("Essa figurinha já está no álbum.")
        
        elif opcao == 2:
            figurinha = int(input("Digite 2 para REMOVER uma figurinha: "))
            if figurinha in album:
                album.remove(figurinha)
                print("Figurinha removida!")
            else:
                print("Figurinha não encontrada não pode ser Removida")
                
        elif opcao == 3:
            figurinha = int(input("Digite qual figurinha quer BUSCAR uma figurinha: "))
            
            if figurinha in album:
                print(f"figurinha {figurinha} Encontrada no Album")
            else:
                print(f"figurinha {figurinha} Não Encontrad no Album")
        
        elif opcao == 4:
            #if figurinha in album:
            print(f"Álbum : {album}")
             
        
        elif opcao == 5:
            break
        else:
            print("Digite um  numero de 1 até 4 e se quiser sair digite 5")
        
    except ValueError:
        print("Digite um valor válido")
