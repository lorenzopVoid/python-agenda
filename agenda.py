def adicionar_contato(contatos, nome, telefone, email): 
    # contato: armazena os dados do contato
    # favorito: indica se o contato está marcado como favorito
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else " "
        print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']} {favorito}")
    return

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome or contatos[indice_contato_ajustado]["nome"]
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone or contatos[indice_contato_ajustado]["telefone"]
        contatos[indice_contato_ajustado]["email"] = novo_email or contatos[indice_contato_ajustado]["email"]
        print(f"Contato {indice_contato} atualizado com sucesso!")
    else:
        print("Índice de contato inválido.")
    return

def marcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
        status = "favorito" if contatos[indice_contato_ajustado]["favorito"] else "não favorito"
        print(f"Contato {contatos[indice_contato_ajustado]['nome']} agora é {status}.")
    else:
        print("Índice de contato inválido.")
    return

def ver_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        print("\nLista de contatos favoritos:")
        for indice, contato in enumerate(favoritos, start=1):
            print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contato_removido = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato_removido['nome']} foi removido.")
    else:
        print("Índice de contato inválido.")
    return

contatos = []

# Loop do menu
while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar um contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja editar: ")
        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
        novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
        novo_email = input("Digite o novo email (ou pressione Enter para manter o atual): ")
        editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato para marcar/desmarcar como favorito: ")
        marcar_favorito(contatos, indice_contato)
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        apagar_contato(contatos, indice_contato)
    elif escolha == "7":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida! Tente novamente.")