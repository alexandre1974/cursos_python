import forca
import advinhacao

def escolha_jogo():
    print("**************************")
    print(" Bem vindo escolha um jogo")
    print("**************************")

    print("Escolha o jogo: (1) forca (2) advinhaçao")
    jogo= int(input("Digite qual jogo voce deseja: "))

    if(jogo==1):
        print("jogando forca")
        forca.jogar()
    elif(jogo==2):
        print("jogado advinhaçao")
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolha_jogo()