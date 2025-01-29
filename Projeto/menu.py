from funcionalidades.verificações import *
from funcionalidades.análises import *
from time import sleep
from colorama import Fore


print(Fore.MAGENTA + '-=' * 30)
print(f'{'BILHETERIA VIRTUAL': >37}')
print('-=' * 30 + Fore.RESET)
print('Se for sua primeira vez aqui, seja muito bem-vindo! Faça o seu cadastro antes de tudo.')


dados = {}
nome_login = ''


def cadastro():
    """
        => Realiza os cadastros a partir de entradas como: nome, senha, idade, gênero, estado, celular e email.
        => As informações são registradas em dicionários. No dicionário principal cada nome é uma chave, assim, cada
        nome possui seu próprio dicionário em que as chaves são os tipos de entradas (idade, estado, ...)
        e os itens são as informações (19, SP, ...).
    :return: as informações são adicionadas no dicionário dados
    """
    while True:
        nome = validar_nome('Nome completo: ')
        senha = limitar_caracteres('Senha (precisa ter 8 caracteres): ', 8)
        idade = validar_idade('Idade: ')
        genero = validar_genero('Gênero - Feminino [F] / Masculino [M] / Outro [O]: ')
        estado = validar_estado('Estado (Sigla somente!): ')
        celular = limitar_caracteres('Celular:', 11)
        email = validar_email('E-mail: ')

        dados[nome] = {
            'Senha': senha,
            'Idade': idade,
            'Genero': genero,
            'Estado': estado,
            'Celular': celular,
            'Email': email
        }

        resp = str(input('Realizar mais cadastros? [S/N] ')).upper().strip()[0]
        if resp == 'N':
            print('Cadastro(s) finalizado(s)!')
            break


def login(data):
    """
        => Realiza o login a partir do nome completo cadastrado e respectiva senha.
    :param data: dicionário com as informações de cadastros
    :return: valor booleano indicando se o login foi realizado ou falhou
    """
    realizado = False
    global nome_login
    nome_login = str(input('Nome completo: ')).strip().upper()
    senha_login = str(input('Senha: ')).strip()

    for chave, valor in data.items():
        if nome_login == chave:
            if senha_login == valor['Senha']:
                realizado = True
                return realizado


while True:
    print(Fore.MAGENTA + '-' * 40)
    print('CADASTRO [1] / LOGIN [2] / ESTATÍSTICAS [3] / SAIR [4]' + Fore.RESET)
    op = int(input('O que deseja fazer?  '))
    match op:
        case 1:
            cadastro()
        case 2:
            if login(dados):
                print('Login realizado com sucesso!')
                print(Fore.MAGENTA + '-='*30)
                while True:
                    print('INFORMAÇÕES DE CADASTRO [1] / COMPRAR [2] / '
                          'BILHETES ADQUIRIDOS [3] / VOLTAR [4]' + Fore.RESET)
                    op_logado = int(input('O que deseja fazer?  '))
                    match op_logado:
                        case 1:
                            print(Fore.MAGENTA + '-' * 30)
                            print(f'{'INFORMAÇÕES DE CADASTRO': >27}' + Fore.RESET)
                            for dd in dados[nome_login]:
                                print(f'{dd}: {dados[nome_login][dd]}')
                        case 2:
                            print(Fore.MAGENTA + '-' * 30)
                            print(f'{'COMPRE SEU BILHETE': >24}' + Fore.RESET)
                        case 3:
                            print(Fore.MAGENTA + '-' * 30)
                            print(f'{'SEUS BILHETES': >20}' + Fore.RESET)
                        case 4:
                            print(Fore.MAGENTA + '-' * 30 + Fore.RESET)
                            break
            else:
                print('Falha no login!')
        case 3:
            print(Fore.MAGENTA + '-'*30)
            print(f'{'DADOS DE TODOS OS CADASTROS'}')
            print('-' * 30 + Fore.RESET)
            if dados == {}:
                print('Ainda não foram realizados os cadastros!')
            else:
                print('-' * 10, 'DADOS GERAIS', '-' * 10)
                print('   - Foram cadastradas ao todo', Fore.GREEN + f'{len(dados)}', Fore.RESET + 'pessoas.')
                print('-'*10, 'IDADES', '-'*10)
                analise_idades(dados)
                print(Fore.RESET + '-' * 10, 'GÊNEROS', '-' * 10)
                analise_genero(dados)
                print(Fore.RESET + '-' * 10, 'IDADES + GÊNEROS', '-' * 10)
                analise_idade_generos(dados)
        case 4:
            print(Fore.MAGENTA + '-'*40)
            print('SAINDO...' + Fore.RESET)
            sleep(1.5)
            break
print('Finalizado. Volte sempre à Bilheteria Virtual!')
