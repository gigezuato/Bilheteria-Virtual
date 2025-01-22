from time import sleep
from colorama import Fore

print(Fore.MAGENTA + '-=' * 30)
print( f'{'BILHETERIA VIRTUAL': >37}')
print('-=' * 30 + Fore.RESET)
print('Se for sua primeira vez aqui, seja muito bem-vindo! Faça o seu cadastro antes de tudo.')

dados = {}
nome_login = ''


def limitar_caracteres(prompt, tamanho):
    while True:
        texto = str(input(prompt)).strip().split()
        texto_sem_espacos = ''.join(texto)
        if len(texto_sem_espacos) == tamanho:
            return texto_sem_espacos
        else:
            print(f'Erro: Você digitou {len(texto_sem_espacos)} caracteres. O texto deve ter {tamanho} caracteres. '
                  f'Tente novamente! ')


def validar_nome(prompt):
    while True:
        nome = str(input(prompt)).strip().upper()
        nome_divisao = nome.split()
        if len(nome) > 2 and len(nome_divisao) > 1:
            return nome
        else:
            print('Erro: nome não válido. Certifique-se de colocar nome e sobrenome!')


def validar_idade(prompt):
    while True:
        idade = int(input(prompt))
        if idade > 0:
            return idade
        else:
            print(f'Erro: Você digitou {idade}. A idade deve ser um valor positivo. Tente novamente! ')


def validar_genero(prompt):
    while True:
        genero = str(input(prompt)).upper().strip()[0]
        if genero in 'FMO':
            return genero
        else:
            print(f'Erro: Opção inválida! Você digitou {genero} e as opções são: '
                  f'Feminino [F] / Masculino [M] / Outro [O]. Tente novamente!')


def validar_estado(prompt):
    estados_brasileiros = {'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
                           'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
                           'Centro-oeste': ['DF', 'GO', 'MT', 'MS'], 'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
                           'Sul': ['PR', 'RS', 'SC']}
    while True:
        estado = str(input(prompt)).strip().upper()
        for regiao, siglas in estados_brasileiros.items():
            if estado in siglas:
                return estado

        print(f'Erro: o estado {estado} não existe. Tente novamente!')


def validar_email(prompt):
    while True:
        email = str(input(prompt)).strip()
        if '@' and '.' in email:
            return email
        else:
            print('Erro: esse não é um e-mail válido. Tente novamente!')


def analise_idades(dado):
    maior_idade = menor_idade = 0
    if dado == {}:
        print('Ainda não foram realizados os cadastros!')
    else:
        for n, i in dado.items():
            if i['Idade'] < 18:
                menor_idade += 1
            elif i['Idade'] >= 18:
                maior_idade += 1
        por_maior = (maior_idade / len(dado.keys())) * 100
        por_menor = (menor_idade / len(dado.keys())) * 100

        print(f'  - Porcentagem de pessoas', Fore.GREEN + 'maiores de idade',
              Fore.RESET + f'cadastradas: {por_maior:.1f} %')
        print(f'  - Porcentagem de pessoas', Fore.GREEN + 'menores de idade',
              Fore.RESET + f'cadastradas: {por_menor:.1f} %')


def cadastro():
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
    print('CADASTRO [1] / LOGIN [2] / ESTATÍSTICAS [3]/ SAIR [4]' + Fore.RESET)
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
            analise_idades(dados)
        case 4:
            print(Fore.MAGENTA + '-'*40)
            print('SAINDO...' + Fore.RESET)
            sleep(1.5)
            break
print('Finalizado. Volte sempre à Bilheteria Virtual!')
