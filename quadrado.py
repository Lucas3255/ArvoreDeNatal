import os
import platform
import time

#função responsavel por limpar tela independente do OS.
def limpaTela():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

while True:     #manter um loop para o usuário repetir quantas vezes quiser.
    limpaTela()
    tamanho = int(input("Qual o tamanho do quadrado: "))
    print("")
    
    for i in range(tamanho):    #faz a primeira linha do quadrado.
        print("#", end= " ")

    print("")
    
    for j in range(tamanho - 2):    #imprime as laterais do quadrado.
        for i in range(tamanho):
            if i == 0 or i == tamanho - 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print("")
    
    for i in range(tamanho):    #faz a ultima linha do quadrado
        print("#", end=" ")

    # loop para garantir que o usuário vai escolher uma opção existente.
    while True:
        escolha = int(input("\n\nGostaria de fazer de novo?\n1 - Sim.\n2 - Não.\n\n>> "))
        if escolha == 2:
            limpaTela()
            print("Encerrando Programa.")
            time.sleep(2)
            exit()
        elif escolha == 1:
            limpaTela()
            break
        elif escolha != 1 or escolha != 2:
            limpaTela()
            print(f"Ops... A opção {escolha} é inválido!\n")
            time.sleep(2)
            input("Clique qualquer tecla para tentar de novo.")
            limpaTela()