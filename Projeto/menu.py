from funcionalidades.interface import *
from funcionalidades.verificações import *
from funcionalidades.análises import *
from time import sleep
from colorama import Fore


titulo('BILHETERIA VIRTUAL', 30, '-=', roxo)
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
    titulo('CADASTRO', 30, '-', verde)
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

        resp = str(input('>> Realizar mais cadastros? [S/N] ')).upper().strip()[0]
        if resp == 'N':
            print('Cadastro(s) finalizado(s)!')
            break


def login(data):
    """
        => Realiza o login a partir do nome completo cadastrado e respectiva senha.
    :param data: dicionário com as informações de cadastros
    :return: valor booleano indicando se o login foi realizado ou falhou
    """
    titulo('LOGIN', 30, '-', verde)
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
    titulo('CADASTRO [1] / LOGIN [2] / ESTATÍSTICAS [3] / SAIR [4]', 60, '-', roxo, False)
    op = int(input('>> O que deseja fazer?  '))
    if op not in range(1, 5):
        print('Opção inválida!')
        continue
    match op:
        case 1:
            cadastro()
        case 2:
            if login(dados):
                print(f'\033[{azul}mLogin realizado com sucesso!\033[m')
                while True:
                    titulo('INFORMAÇÕES DE CADASTRO [1] / COMPRAR [2] / BILHETES ADQUIRIDOS [3] / VOLTAR [4]', 60,
                           '-', roxo, False)
                    op_logado = int(input('>> O que deseja fazer?  '))
                    if op_logado not in range(1, 5):
                        print('Opção inválida!')
                        continue
                    match op_logado:
                        case 1:
                            titulo('INFORMAÇÕES DE CADASTRO', 30, '-', verde)
                            for dd in dados[nome_login]:
                                print(f'{dd}: {dados[nome_login][dd]}')
                        case 2:
                            titulo('COMPRE SEU BILHETE', 30, '-', verde)
                        case 3:
                            titulo('SEUS BILHETES', 30, '-', verde)
                        case 4:
                            break
            else:
                print('Falha no login!')
        case 3:
            titulo('DADOS DE TODOS OS CADASTROS', 30, '-', verde)
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
            titulo('SAINDO...', 30, '-', roxo, False)
            sleep(1.5)
            break
titulo('Volte sempre à Bilheteria Virtual!', 30, '-=', roxo)
