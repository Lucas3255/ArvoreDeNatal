import os
import platform
import time

#Função para limpar tela
def limpa_tela():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

#loop para manter o sistema funcionando até o usuário n querer mais.
while True:
    limpa_tela()
    tamanho = int(input("Qual o tamanho da arvore: "))
    galhos = 1
    tronco = 0

    if tamanho // 2 - 1 > 1:
        tronco = tamanho // 2 - 1
    else:
        tronco = 1

    limpa_tela()

    #desenho da arvore
    for i in range(tamanho):    #define a altura da arvore.
        for j in range(tamanho - i - 1):    #dá espaçamentos.
            print(" ", end="")
    
        for k in range(galhos):     #coloca os galhos.
            print("*", end="")

        #lógica para fazer com q os galhos aumentem gradativamente.
        galhos = galhos + 1 * 2
        print("")

    #lógica para por os espaços do tronco da arvore.
    espacos_tronco = int(tamanho - tronco / 2)

    #fazer o desenho do tronco
    for j in range(espacos_tronco): #coloca os espaçamentos.
        print(" ", end="")

    for i in range(tronco): # serve para aplicar o tronco em si.
        print("|", end="")

    #função para saber se o usuário que continuar o programa.
    time.sleep(2)
    while True:
        escolha = int(input("\n\nGostaria de fazer de novo?\n1 - Sim.\n2 - Não.\n\n>> "))
        
        if escolha == 1:
            break
        elif escolha == 2:
            limpa_tela()
            print("Encerrando Programa")
            for i in range(0, 6, 1):
                print(" o", end="", flush=True)
                time.sleep(1)
            exit()
        else:
        #elif escolha != 1 and escolha != 2:
            limpa_tela()
            print(f"Ops... A opção {escolha} é inválida!")
            time.sleep(1)
            input("\nClique qualquer tecla para continuar.")
            limpa_tela()
    