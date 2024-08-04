dados = [7, 5, 4, 10, 3]

repetir = True

while repetir:

    repetir = False

    for i in range(len(dados) - 1):
        if(dados[i] > dados[i+1]):
            dados[i], dados[i+1] = dados[i+1], dados[i]
            repetir = True

print(dados)