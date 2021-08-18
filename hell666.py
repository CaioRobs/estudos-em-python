def LEITURASENSOR(sensor):
    parametro_retornado = input(f'insira {sensor}:')
    return parametro_retornado


def EXAUSTOR(estado):
    print(f'EXAUSTOR: {estado}')


def AQUECIMENTO(temperatura):
    print(f'AQUECIMENTO: {temperatura}')


def TIMER(estado):
    print('contando')


def DESUMIDIFICACAO():
    print('Início desumidificação')
    umidade = int(LEITURASENSOR('UMIDADE'))
    temperatura_interna = int(LEITURASENSOR('TEMP_INT'))
    if temperatura_interna >= 15 and umidade >= 40:
        EXAUSTOR('ON')
    if temperatura_interna < 15 and umidade >= 40:
        EXAUSTOR('ON')
        AQUECIMENTO(100)
    if temperatura_interna >= 100:
        AQUECIMENTO('OFF')
    if umidade <= 5:
        EXAUSTOR('OFF')
        AQUECIMENTO('OFF')
        print('desumidificaçao concluida')
        return
    else:
        DESUMIDIFICACAO()


def COCCAO():
    print('Iniciando cocção')
    umidade = int(LEITURASENSOR('UMIDADE'))
    temperatura_interna = int(LEITURASENSOR('TEMP_INT'))
    if umidade > 15:
        EXAUSTOR('ON')
    if umidade <= 5:
        EXAUSTOR('OFF')
    if temperatura_interna <= 200:
        AQUECIMENTO(380)
    if umidade <= 5 and temperatura_interna >= 380:
        print('inserir conteudo para cocção')
        print(' - quando inserir, pressione o botao pronto')
        pronto = LEITURASENSOR('BOTAO')
        if pronto == 'ON':
            AQUECIMENTO(380)
            TIMER('SET')
    else:
        COCCAO()


umidade = int(LEITURASENSOR('UMIDADE'))
temperatura_interna = int(LEITURASENSOR('TEMP_INT'))
temperatura_externa = int(LEITURASENSOR('TEMP_EXT'))

if temperatura_externa <= 20 and umidade >= 40:
    clima = 'inverno'
else:
    clima = 'verao'

if clima == 'inverno':
    DESUMIDIFICACAO()
    COCCAO()
else:
    COCCAO()
