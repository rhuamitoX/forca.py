import random
def jogar():
    palavras = []    
    print("1 - dbz")
    print("2 - jogos")
    print("3 - sonic")
    opcao = int(input("Digite a opção desejada (1 a 3)"))

    if opcao == 1:
        arquivo = open("dbz.txt", "r")
    elif opcao == 2:
        arquivo = open("jogos.txt", "r")
    elif opcao == 3:
        arquivo = open("sonic.txt", "r")
    
    for linha in arquivo:
        palavras.append(linha.strip())
    palavra = random.choice(palavras)

    
    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("_")

    acertou = False
    enforcou = False
    tentativa = 1
    limite_tentativas = len(palavra) + 6
    def mostrarPalavra():
        for letra in letras_acertadas:
            print(letra, end=" ")
        print("")
    while(not acertou and not enforcou):
        mostrarPalavra()
        chute = input("Digite uma letra:")
        indice = 0
        for letra in palavra:
            if (chute.upper() == letra):
                letras_acertadas[indice] = letra
            indice = indice + 1

        if (tentativa == limite_tentativas):
            print("Você perdeu :(\nA palavra era:", palavra)
            enforcou = True

        if (letras_acertadas.count("_")== 0):
            print("Parabéns! Você descobriu a palavra!")
            mostrarPalavra()
            acertou = True

        tentativa = tentativa + 1                   