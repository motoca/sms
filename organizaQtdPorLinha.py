with open('diff.txt', 'r') as sms, open('naoenviados.txt', 'w') as smsInLine:
    print("LENDO ARQUIVO DIFF...")
    lines = set(sms.readlines())

    QTDPORLINHA = 20

    print(f"ESCREVENDO {QTDPORLINHA} POR LINHA...")
    cont = 0
    linha = ""
    for line in lines:
        cont+=1
        linha += f"{line.strip()},"

        if cont == QTDPORLINHA:
            print(f"LINHA: {linha[:-1]}")
            smsInLine.write(f"{linha}\n")
            linha = ""
            cont = 0