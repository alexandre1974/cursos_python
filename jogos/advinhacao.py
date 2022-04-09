
import random

def jogar():

    print("************************")
    print(" Bem vindo a advinhação!")
    print("************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade")
    print("(1) Facil (2) Médio (3) Díficil")

    nivel = int(input ("Escolha o nível: "))

    if (nivel==1):
        tentativas = 20
    elif(nivel==2):
        tentativas = 10
    else:
        tentativas = 5

    print(numero_secreto)
    #while (rodada <= tentativas):
    for rodada in range(1, tentativas + 1):
        print("voce tem {} de {}".format(rodada,tentativas))
        chute_str = input("Digite um numero : ")

        print("Voce digitou: ", chute_str)
        chute=int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você precisa digitar um número de 0 a 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Voce fez {} pontos".format(pontos))
            print("voce acertou!")
            break
        else:
            if(maior):
                print("Voce errou, o numero digitado esta acima do valor secreto")
            elif (menor):
                print("Voce errou, o numero digitado esta abaixo do valor secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("fim de jogo")

if(__name__ == "__main__"):
    jogar()