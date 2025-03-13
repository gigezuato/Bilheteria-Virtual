from funcionalidades.interface import *
from menu import cadastro


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

    print(f'  - Porcentagem de pessoas', f'\033[{verde}m menores de idade\033[m', 'cadastradas:',
          f'\033[{verde}m{por_menor:.1f} %\033[m')
    print('  - Porcentagem de pessoas', f'\033[{verde}m maiores de idade\033[m', 'cadastradas:',
          f'\033[{verde}m{por_maior:.1f} %\033[m')
    print('  - A ', f'\033[{verde}m menor \033[m', 'idade cadastrada foi: ',
          f'\033[{verde}m{menor}\033[m')
    print('  - A ', f'\033[{verde}m maior \033[m',
          'idade cadastrada foi: ', f'\033[{verde}m{maior}\033[m')


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

    print('   - Porcentagem de pessoas do gênero', f'\033[{verde}mfeminino\033[m', 'cadastradas:',
          f'\033[{verde}m{porc_fem:.1f} %\033[m')
    print('   - Porcentagem de pessoas do gênero', f'\033[{verde}m masculino\033[m', 'cadastradas:',
          f'\033[{verde}m{porc_masc:.1f} %\033[m')
    print('   - Porcentagem de pessoas de', f'\033[{verde}moutro\033[m', 'gênero cadastradas:',
          f'\033[{verde}m{porc_out:.1f} %\033[m')


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
    if cont_fem != 0:
        porc_fem_maior = (fem_maior / cont_fem) * 100
        porc_fem_menor = (fem_menor / cont_fem) * 100
        print('   - Porcentagem de pessoas do gênero', f'\033[{verde}mfeminino maiores de idade\033[m',
              'cadastradas:', f'\033[{verde}m{porc_fem_maior:.2f} %\033[m')
        print('   - Porcentagem de pessoas do gênero', f'\033[{verde}mfeminino menores de idade\033[m',
              'cadastradas:', f'\033[{verde}m{porc_fem_menor:.2f} %\033[m')
    else:
        print('   - Não foram cadastradas pessoas do gênero feminino.')

    if cont_masc != 0:
        porc_masc_maior = (masc_maior / cont_masc) * 100
        porc_masc_menor = (masc_menor / cont_masc) * 100
        print('   - Porcentagem de pessoas do gênero', f'\033[{verde}m masculino maiores de idade\033[m',
              'cadastradas:', f'\033[{verde}m{porc_masc_maior:.2f} %\033[m')
        print('   - Porcentagem de pessoas do gênero', f'\033[{verde}m masculino menores de idade\033[m',
              'cadastradas:', f'\033[{verde}m{porc_masc_menor:.2f} %\033[m')
    else:
        print('   - Não foram cadastradas pessoas do gênero masculino.')


def analise_regioes(dado):
    cont_sud = cont_sul = cont_nord = cont_nort = cont_cent = 0
    cadastros_regioes = []
    for n, i in dado.items():
        if i['Estado'] in ['SP', 'MG', 'ES', 'RJ']:
            cont_sud += 1
        elif i['Estado'] in ['RS', 'PR', 'SC']:
            cont_sul += 1
        elif i['Estado'] in ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']:
            cont_nord += 1
        elif i['Estado'] in ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC']:
            cont_nort += 1
        else:
            cont_cent += 1
    cadastros_regioes.append(cont_sud)
    cadastros_regioes.append(cont_sul)
    cadastros_regioes.append(cont_nort)
    cadastros_regioes.append(cont_nord)
    cadastros_regioes.append(cont_cent)

    cadastros_regioes_ordem = cadastros_regioes.sort()



