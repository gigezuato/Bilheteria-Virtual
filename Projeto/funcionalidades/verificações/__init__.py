from funcionalidades.interface import vermelho


def limitar_caracteres(prompt, tamanho):
    """
        => Verifica se o texto digitado tem a mesma quantidade de caracteres passados de parâmetro.
    :param prompt: mensagem que será exibida ao usuário para a entrada de dado
    :param tamanho: quantidade de caracteres que o dado informado terá que possuir
    :return: o texto digitado pelo usuário sem espaços
    """
    while True:
        texto = str(input(prompt)).strip().split()
        texto_sem_espacos = ''.join(texto)
        if len(texto_sem_espacos) == tamanho:
            return texto_sem_espacos
        else:
            print(f'\033[{vermelho}mErro: Você digitou {len(texto_sem_espacos)} caracteres. O texto deve ter {tamanho} '
                  f'caracteres. '
                  f'Tente novamente!\033[m')


def validar_nome(prompt):
    """
        => Verifica se o texto informado como nome tem mais de 2 caracteres e se possui duas palavras pelo menos,
        caracterizando nome e sobrenome.
    :param prompt: mensagem que será exibida ao usuário para entrada de dado
    :return: o nome informado pelo usuário depois de verificado
    """
    while True:
        nome = str(input(prompt)).strip().upper()
        nome_divisao = nome.split()
        if len(nome) > 2 and len(nome_divisao) > 1:
            return nome
        else:
            print(f'\033[{vermelho}mErro: nome não válido. Certifique-se de colocar nome e sobrenome!\033[m')


def validar_idade(prompt):
    """
        => Verifica se o valor informado como idade é maior que 0.
    :param prompt: mensagem que será exibida ao usuário para a entrada de dado
    :return: a idade informada depois de ser verificada
    """
    while True:
        idade = int(input(prompt))
        if idade > 0:
            return idade
        else:
            print(f'\033[{vermelho}mErro: Você digitou {idade}. A idade deve ser um valor positivo. Tente '
                  f'novamente!\033[m')


def validar_genero(prompt):
    """
        => Verifica se o texto informado pelo usuário como gênero está de acordo com as opções F - feminino,
        M - masculino e O - outro
    :param prompt: mensagem que será exibida ao usuário para a entrada de dado
    :return: o gênero depois de verificado
    """
    while True:
        genero = str(input(prompt)).upper().strip()[0]
        if genero in 'FMO':
            return genero
        else:
            print(f'\033[{vermelho}mErro: Opção inválida! Você digitou {genero} e as opções são: '
                  f'Feminino [F] / Masculino [M] / Outro [O]. Tente novamente!\033[{vermelho}m')


def validar_estado(prompt):
    """
        => Verifica se a sigla informada do estado está na lista de estados brasileiros.
    :param prompt: mensagem que será exibida ao usuário para a entrada de dado
    :return: a sigla do estado caso ela esteja na lista
    """
    estados_brasileiros = {'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
                           'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
                           'Centro-oeste': ['DF', 'GO', 'MT', 'MS'], 'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
                           'Sul': ['PR', 'RS', 'SC']}
    while True:
        estado = str(input(prompt)).strip().upper()
        for regiao, siglas in estados_brasileiros.items():
            if estado in siglas:
                return estado

        print(f'\033[{vermelho}mErro: o estado {estado} não existe. Tente novamente!\033[m')


def validar_email(prompt):
    """
        => Verifica se o email informado possui os caracteres '@' e '.'
    :param prompt: mensagem que será exibida ao usuário para a entrada de dado
    :return: o email caso ele tenha os caracteres obrigatórios
    """
    while True:
        email = str(input(prompt)).strip()
        if '@' and '.' in email:
            return email
        else:
            print(f'\033[{vermelho}mErro: esse não é um e-mail válido. Tente novamente!\033[m')