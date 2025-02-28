vermelho = '31'
roxo = '35'
azul = '36'
laranja = '34'
amarelo = '33'
verde = '32'
rosa = '31'
branco = '97'
preto = '30'
cinza = '37'


def titulo(msg, tam=42, simbolo='-', cor=vermelho, dupla_linha = True):
    print(f'\033[{cor}m{simbolo}\033[m' * tam)
    print(f'\033[{cor}m{msg.center(tam * len(simbolo))}\033[m')
    if dupla_linha:
        print(f'\033[{cor}m{simbolo}\033[m' * tam)

