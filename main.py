from datetime import datetime

NOME_SISTEMA = 'IndustrialLog'
VERSAO = "0.1.1-alpha"

escolha = 5

def registrar_ocorrencias():
    ocorrencia = input('Descreva a ocorrência: ').strip()
    while ocorrencia == '':
        ocorrencia = input('O campo não pode estar vazio!\nDescreva a ocorrência: ').strip()
    responsavel = input('Responsável pelo registro: ').strip()
    while responsavel == '':
        responsavel = input('O campo não pode estar vazio!\nResponsável pelo registro: ').strip()
    agora = datetime.now()
    data = agora.strftime('%d/%m/%Y')
    hora = agora.strftime('%H:%M:%S')
    try:
        with open('ocorrencia.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Ocorrência: {ocorrencia}\nData: {data}\nHora: {hora}\nResponsavel: {responsavel}\n\n')
    except OSError:
        print('\nFalha ao registrar a ocorrência!')
    else:
        print('\nOcorrência registrada com sucesso!')

def consultar_historico():
    try:
        with open('ocorrencia.txt', 'r', encoding='utf-8') as arquivo:
            historico = arquivo.read()
    except FileNotFoundError:
        print('\nO arquivo ainda não foi criado!')
    else:
        if historico == '':
            print('\nAinda não houveram ocorrências registradas!')
        else:
            print('')
            print(historico)

def consultar_por_responsavel(responsavel: str):
    try:
        with open('ocorrencia.txt', 'r', encoding='utf-8') as arquivo:
            historico = arquivo.read()
    except FileNotFoundError:
        print('\nO arquivo ainda não foi criado!')
    else:
        if historico == '':
            print('\nAinda não houveram ocorrências registradas!')
        else:
            historico_do_responsavel = []
            repositorio = historico.split('\n\n')

            for ocorrencia in repositorio:
                responsavel_comparacao = 'responsavel: ' + responsavel.casefold()
                if responsavel_comparacao in ocorrencia.casefold():
                    historico_do_responsavel.append(ocorrencia)

            if not historico_do_responsavel:
                print('\nNão há um histórico de ocorrências registrado por esse responsável!')
            else:
                ocoresp = '\n\n'.join(historico_do_responsavel)
                print('')
                print(ocoresp)

def exibir_versao():
    print(f'{NOME_SISTEMA} - Versão: {VERSAO}')

while escolha != 0:
    try:
        print(f'\n=== {NOME_SISTEMA} ===\n')
        escolha = int(input('1- Registrar ocorrência\n2- Consultar histórico\n3- Consultar histórico por responsável\n4- Exibir versão\n0- Sair do programa\n\n'))
    except ValueError:
        print('\nDigite apenas números!')
        continue
    else:
        if escolha not in (0, 1, 2, 3, 4):
            print('\nFunção não encontrada, tente novamente!')
            continue
        elif escolha == 1:
            registrar_ocorrencias()
        elif escolha == 2:
            consultar_historico()
        elif escolha == 3:
            responsavel = str(input('\nDeseja verificar o histórico de qual responsável? ')).strip()
            if responsavel == '':
                print('\nO campo de responsável está vazio!')
            else:
                consultar_por_responsavel(responsavel)
        elif escolha == 4:
            exibir_versao()
        else:
            break

print('\nPrograma encerrado com sucesso!')

# Projeto IndustrialLog - versão inicial
