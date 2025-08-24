import os
import platform
import time

def limpa_tela():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

while True:
    limpa_tela()
    tamanho = int(input("Qual o tamanho da arvore: "))
    tronco = int(max(1, tamanho / 2))
    galhos = 1
    limpa_tela()

    for i in range(tamanho):    #define a altura da arvore.
        for j in range(tamanho - i - 1):    #dá espaçamentos.
            print(" ", end="")
    
        for k in range(galhos):     #coloca os galhos.
            print("o", end="")

        #lógica para fazer com q os galhos aumentem gradativamente.
        galhos = galhos + 1 * 2
        print("")

    espacos_tronco = tamanho - 1  

    for j in range(espacos_tronco):
        print(" ", end="")

    for i in range(tronco):
        print("|", end="")

    time.sleep(2)
    while True:
        escolha = int(input("\n\nGostaria de fazer de novo?\n1 - Sim.\n2 - Não.\n\n>> "))
        
        if escolha == 2:
            limpa_tela()
            print("Encerrando Programa")
            break
        elif escolha != 1 and escolha != 2:
            limpa_tela()
            print(f"Ops... A opção {escolha} é inválida!")
            time.sleep(1)
            print("\nClique qualquer tecla para continuar.")
    