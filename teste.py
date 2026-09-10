album = []

print(
    " ======== Menu ========"
    "\n 1 - Adicionar_figurinha"
    "\n 2 - Remover_figurinha"
    "\n 3 - Buscar_figurinha"
    "\n 4 - Mostrar_álbum"
    "\n 5 - Encerrar"
    "\n========================"
)
while True:
    try:
        opcao = int(input("\n Escolha uma opção: \n"))

        if opcao == 1:
            figurinha = input("Cadastre uma figurinha com numeros de 0 a 100: ").strip()
            if figurinha not in album:
                album.append(figurinha)
                print("Figurinha cadastrada!")
            else:
                print("Essa figurinha já está no álbum.")

        elif opcao == 2:
            figurinha = input("Digite o número da figurinha para remover: ").strip()
            if figurinha in album:
                album.remove(figurinha)
                print("Figurinha removida!")
            else:
                print("Figurinha não encontrada, não pode ser removida.")

        elif opcao == 3:
            figurinha = input("Digite qual figurinha quer buscar: ").strip()
            if figurinha in album:
                print(f"Figurinha {figurinha} encontrada no álbum!")
            else:
                print(f"Figurinha {figurinha} não encontrada no álbum.")

        elif opcao == 4:
            if album:
                print(f"Álbum atual ({len(album)}): {album}")
                for figurinha in album:
                    print(figurinha)
            else:
                print("album vazio")

        elif opcao == 5:
            break

        else:
            print("Digite um número de 1 a 5.")

    except ValueError:
        print("Digite um valor válido.")
    
