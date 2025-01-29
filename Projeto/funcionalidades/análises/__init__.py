from colorama import Fore


def analise_idades(dado):
    """
        => Analisa qual a porcentagem de pessoas menores de idade cadastradas, assim como as maiores de idade.
        Analisa também qual foi a menor e a maior idade cadastrada.
    :param dado: dicionário com dados de cadastro
    :return: prints com as informações analisadas
    """
    maior_idade = menor_idade = 0
    maior = menor = cont = 0
    for n, i in dado.items():
        if i['Idade'] < 18:
            menor_idade += 1
        elif i['Idade'] >= 18:
            maior_idade += 1
        if cont == 0:
            maior = menor = i['Idade']
        else:
            if i['Idade'] > maior:
                maior = i['Idade']
            if i['Idade'] < menor:
                menor = i['Idade']
        cont += 1

    por_maior = (maior_idade / len(dado.keys())) * 100
    por_menor = (menor_idade / len(dado.keys())) * 100

    print(f'  - Porcentagem de pessoas', Fore.GREEN + 'menores de idade', Fore.RESET + f'cadastradas:',
          Fore.GREEN + f'{por_menor:.1f} %')
    print(Fore.RESET + '  - Porcentagem de pessoas', Fore.GREEN + 'maiores de idade', Fore.RESET + 'cadastradas:',
          Fore.GREEN + f'{por_maior:.1f} %')
    print(Fore.RESET + '  - A ', Fore.GREEN + 'menor ', Fore.RESET + 'idade cadastrada foi: ',
          Fore.GREEN + f'{menor}')
    print(Fore.RESET + '  - A ', Fore.GREEN + 'maior ',
          Fore.RESET + 'idade cadastrada foi: ', Fore.GREEN + f'{maior}')


def analise_genero(dado):
    """
        => Analisa quais as porcentagens de pessoas dos gêneros feminino, masculino e outro cadastradas.
    :param dado: dicionário com dados de cadastro
    :return: prints com as informações analisadas
    """
    feminino = masculino = outro = 0
    for n, i in dado.items():
        if i['Genero'] == 'F':
            feminino += 1
        elif i['Genero'] == 'M':
            masculino += 1
        else:
            outro += 1
    porc_fem = (feminino / len(dado.keys())) * 100
    porc_masc = (masculino / len(dado.keys())) * 100
    porc_out = (outro / len(dado.keys())) * 100

    print('   - Porcentagem de pessoas do gênero', Fore.GREEN + 'feminino', Fore.RESET + 'cadastradas:',
          Fore.GREEN + f'{porc_fem:.1f} %')
    print(Fore.RESET + '   - Porcentagem de pessoas do gênero', Fore.GREEN + 'masculino', Fore.RESET + 'cadastradas:',
          Fore.GREEN + f'{porc_masc:.1f} %')
    print(Fore.RESET + '   - Porcentagem de pessoas do gênero', Fore.GREEN + 'outro', Fore.RESET + 'cadastradas:',
          Fore.GREEN + f'{porc_out:.1f} %')


def analise_idade_generos(dado):
    """
        => Analisa quais as porcentagens de pessoas com tais características: gênero feminino maiores de idade,
        gênero feminino menores de idade, gênero masculino maiores de idade e gênero masculino menores de idade.
    :param dado: dicionário com dados de cadastro
    :return: prints com as informações analisadas
    """
    fem_maior = masc_maior = fem_menor = masc_menor = 0
    cont_fem = cont_masc = 0
    for n, i in dado.items():
        if i['Genero'] == 'F':
            cont_fem += 1
        elif i['Genero'] == 'M':
            cont_masc += 1

    for n, i in dado.items():
        if i['Genero'] == 'F' and i['Idade'] >= 18:
            fem_maior += 1
        elif i['Genero'] == 'F' and i['Idade'] < 18:
            fem_menor += 1
        if i['Genero'] == 'M' and i['Idade'] >= 18:
            masc_maior += 1
        elif i['Genero'] == 'M' and i['Idade'] < 18:
            masc_menor += 1
    # Tratar o erro de quando não houver cadastros pessoas de um gênero e, por isso a divisão ser um divisão por 0.
    porc_fem_maior = (fem_maior / cont_fem) * 100
    porc_fem_menor = (fem_menor / cont_fem) * 100
    porc_masc_maior = (masc_maior / cont_masc) * 100
    porc_masc_menor = (masc_menor / cont_masc) * 100

    print('   - Porcentagem de pessoas do gênero', Fore.GREEN + 'feminino maiores de idade',
          Fore.RESET + 'cadastradas:',
          Fore.GREEN + f'{porc_fem_maior:.2f} %')
    print(Fore.RESET + '   - Porcentagem de pessoas do gênero', Fore.GREEN + 'feminino menores de idade', Fore.RESET +
          'cadastradas:', Fore.GREEN + f'{porc_fem_menor:.2f} %')
    print(Fore.RESET + '   - Porcentagem de pessoas do gênero', Fore.GREEN + 'masculino maiores de idade', Fore.RESET +
          'cadastradas:', Fore.GREEN + f'{porc_masc_maior:.2f} %')
    print(Fore.RESET + '   - Porcentagem de pessoas do gênero', Fore.GREEN + 'masculino menores de idade', Fore.RESET +
          'cadastradas:', Fore.GREEN + f'{porc_masc_menor:.2f} %')

