from time import sleep

print('-=' * 30)
print(f'{'BILHETERIA VIRTUAL': >37}')
print('-=' * 30)
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
    print('CADASTRO [1] / LOGIN [2] / ESTATÍSTICAS [3]/ SAIR [4]')
    op = int(input('O que deseja fazer?  '))
    match op:
        case 1:
            cadastro()
        case 2:
            if login(dados):
                print('Login realizado com sucesso!')
                print('-='*30)
                while True:
                    print('INFORMAÇÕES DE CADASTRO [1] / COMPRAR [2] / BILHETES ADQUIRIDOS [3] / SAIR [4]')
                    op_logado = int(input('O que deseja fazer?  '))
                    match op_logado:
                        case 1:
                            print('-' * 30)
                            print(f'{'INFORMAÇÕES DE CADASTRO': >27}')
                            for dd in dados[nome_login]:
                                print(f'{dd}: {dados[nome_login][dd]}')
                        case 2:
                            print('-' * 30)
                            print(f'{'COMPRE SEU BILHETE': >24}')
                        case 3:
                            print('-' * 30)
                            print(f'{'SEUS BILHETES': >20}')
                        case 4:
                            print('-' * 30)
                            break
            else:
                print('Falha no login!')
        case 3:
            print('-'*30)
            print(f'{'DADOS DE TODOS OS CADASTROS'}')
            print('-' * 30)
        case 4:
            print('-'*40)
            print('SAINDO...')
            sleep(1.5)
            break
print('Finalizado. Volte sempre à Bilheteria Virtual!')