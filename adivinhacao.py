import random
def jogar():
    numero = random.randint(0,10)
    #print(numero)
    tentativa = 1
    while(tentativa <= 3):
        print("Adivinhe o número que estou pensando, de 0 a 10")
        chute = int(input("Digite o seu chute:"))
        if (numero == chute):
            print("Acertou!")
            break
        else:
            print("Errou :c")

        tentativa = tentativa + 1
    # 1 - MOSTRAR O NÚMERO QUE FOI SORTEADO QUANDO TERMINA O JOGO
    # 2 - DIZER PARA O USUÁRIO SE O SORTEIO É MAIOR OU MENOR
   