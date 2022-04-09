import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letra_acertada = inicialisa_palavra_acertada(palavra_secreta)
    print(letra_acertada)

    acertou = False
    enforcou = False
    erros = 0


    while(not acertou and not enforcou):
        letras_faltando = str(letra_acertada.count("_"))
        print("Ainda faltam acertar {}".format(letras_faltando))

        chute = pede_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letra_acertada, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)
        #print("Voce utilizou {} tentativas de 6 erros".format(erro))

        enforcou = erros == 7
        acertou ="_" not in letra_acertada
        print(letra_acertada)
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("fim do jogo")


def imprime_mensagem_abertura():
    print("*****************************")
    print(" Bem vindo ao jogo da forca!")
    print("*****************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt","r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicialisa_palavra_acertada(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("escolhe uma letra: ").strip().upper()
    return chute

def marcar_chute_correto(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letra_acertada[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
