palavra = "KENNEDY"
letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]
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