import os
import requests
from concurrent.futures import ProcessPoolExecutor, as_completed #ThreadPoolExecutor
from suds.client import Client

MAX_CPU = 7

SMS_URL = 'https://sms.correios.com.br/smsWS/smsService/smsWS?wsdl'
MESSAGE = 'Detectamos possível acesso indevido ao seu nº de celular cadastrado, protocolo LGPD foi acionado. Considere alterar sua senha. Acesse https://c.correios.com.br/lgpd'
RECIPIENTS = []
USERNAME = ''
PASSWORD = ''

with open('arquivo/naoenviados.txt', 'r') as sms:
    RECIPIENTS = set(sms.readlines())
    print(f"TOTAL SMS = {len(RECIPIENTS)}")

def send_sms(phones):
    mensagens = []
    phones = phones[:-1]
    print(f"Phones: {phones}")
    listaPhones = phones.split(",")

    for p in listaPhones:
        mensagens.append({'numero': f'{p}', 'remetente': 'Meu Correios', 'texto': MESSAGE})
    
    try:
        client = Client(SMS_URL, username=USERNAME, password=PASSWORD)
        response = client.service.enviarMensagens(mensagens, '00008')
    except Exception as e:
        print(f'Error Sending SMS - {e}')

def send_smsCustom(mensagens, msg):
    try:
        client = Client(SMS_URL, username='11831', password='123456')
        response = client.service.enviarMensagens(mensagens, '00008')
    except Exception as e:
        print(f'Error Sending SMS - {e}')

fileErrors = open('arquivo/errosSMS.csv', 'w')


if __name__ == '__main__':
    USERNAME = os.environ.get('ppn_user')
    PASSWORD = os.environ.get('ppn_pass')

    if USERNAME is None or PASSWORD is None:
        raise Exception("Usuário Inválido para conexão com o componente.")
        exit

    contTotalSucesso = 0
    contTotalErro = 0
    with ProcessPoolExecutor(max_workers=MAX_CPU) as executor:
        futures = {executor.submit(send_sms, phone.strip()): phone for phone in RECIPIENTS}
        for future in as_completed(futures):
            phones = futures[future]
            try:
                # response = future.result()
                contTotalSucesso+=10
                print(f'SMS Sent - {contTotalSucesso}')
            except Exception as e:
                contTotalErro+=10
                print(f'Error Sending SMS - {contTotalSucesso}\n{e}')
                fileErrors.write(f"{phones}")

    msg = f"Total de SMS: SUCESSO: {contTotalSucesso} - ERRO: {contTotalErro}"

    mensagens = []
    mensagens.append({'numero': f'5561992984818', 'remetente': 'Meu Correios', 'texto': msg})
    mensagens.append({'numero': f'5561984868787', 'remetente': 'Meu Correios', 'texto': msg})
    result = send_smsCustom(mensagens, msg)

    print(msg)