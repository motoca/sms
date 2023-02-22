numerosEnviados = []
fileSMS = open('arquivo/diferenca.csv', 'w')

with open('enviados.txt', 'r') as enviados:
    for enviado in enviados:
        numerosEnviados.append(enviado.strip())
        print("\033[K", f"Enviados: {len(numerosEnviados)}", end="\r")

contTodos = 0
contNaoEnviados = 0

with open('todosSMS.csv', 'r') as todos:
    for numero in todos:
        contTodos+=1
        print("\033[K", f"TRATANDO ENVIADOS: {contTodos}", end="\r")
        if numero.strip() not in numerosEnviados:
            fileSMS.write(numero)
            contNaoEnviados+=1
            msg = f"Enviados: {len(numerosEnviados)} - Não Enviados: {contNaoEnviados}"
            print("\033[K", msg, end="\r")


print(f"Total SMS {contTodos} - Total Não Enviados {contNaoEnviados} => DIF {contTodos - contNaoEnviados}")

fileSMS.close()