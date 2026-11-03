from time import sleep
from datetime import datetime

NOME_SISTEMA = 'IndustrialLog'
VERSAO = "0.1.0-alpha"

escolha = 5

def registrar_ocorrencias():
    agora = datetime.now()
    data = agora.strftime('%d/%m/%Y')
    hora = agora.strftime('%H:%M:%S')
    ocorrencia = input('Descreva a ocorrência: ')
    responsavel = input('Responsável pelo registro: ')
    with open('ocorrencia.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Ocorrência: {ocorrencia}\nData: {data}\nHora: {hora}\nResponsavel: {responsavel}\n\n')
        sleep(1)
        print('ocorrencia registrada com sucesso!')
        sleep(1)

def consultar_historico():
    try:
        with open('ocorrencia.txt', 'r', encoding='utf-8') as arquivo:
            historico = arquivo.read()
            sleep(1)
    except FileNotFoundError:
        print('O arquivo ainda não foi criado!')
        sleep(1)
    else:
        if historico == '':
            print('Ainda não houveram ocorrências registradas!')
            sleep(1)
        else:
            print(historico)
            sleep(1)

def exibir_versao():
    print(f'{NOME_SISTEMA} - Versão: {VERSAO}')
    sleep(1)

while escolha != 0:
    try:
        print(f'=== {NOME_SISTEMA} ===\n\n')
        escolha = int(input('1- Registrar ocorrência\n2- Consultar histórico\n3- Exibir versão\n0- Sair do programa\n'))
        sleep(1)
    except ValueError:
        print('Digite apenas números!')
        continue
    else:
        if escolha not in (0, 1, 2, 3):
            print('Função não encontrada, tente novamente!')
            sleep(1)
            continue
        elif escolha == 1:
            registrar_ocorrencias()
        elif escolha == 2:
            consultar_historico()
        elif escolha == 3:
            exibir_versao()
        else:
            sleep(1)
            break

print('Programa encerrado com sucesso!')

# Projeto IndustrialLog - versão inicial

# Funcionalidade em desenvolvimento: consulta por responsável
