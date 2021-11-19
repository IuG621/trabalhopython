from typing import Text
from estilo import cor

def leia_numero(numero):
    while True:
        try:
            valor = int(input(numero))
        except (ValueError, TypeError):
            print(cor(txt = 'ERRO: Por favor, digite um inteiro válido.', cor = 'vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um inteiro válido. {}'.format(ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt = f'ERRO: {e.__cause__}', cor = 'vermelho'))
        else:
            return valor

def leia_nota1(av1):
    while True:
        try:
            valor = float(input(av1))
            while valor < 0 or valor > 10:
                print(cor(txt='ERRO: Por favor digite uma nota valida', cor = 'vermelho'))
                valor = float(input(av1))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite uma nota válida.', cor='vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nota válida. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor

            
def leia_nota2(av2):
    while True:
        try:
            valor = float(input(av2))
            while valor < 0 or valor > 10:
                print(cor(txt='ERRO: Por favor digite uma nota valida', cor = 'vermelho'))
                valor = float(input(av2))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite uma nota válida.', cor='vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nota válida. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor

            
def leia_nota3(av3):
    while True:
        try:
            valor = float(input(av3))
            while valor < 0 or valor > 10:
                print(cor(txt='ERRO: Por favor digite uma nota valida', cor = 'vermelho'))
                valor = float(input(av3))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite uma nota válida.', cor='vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nota válida. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor

            
def leia_notaAvd(avd):
    while True:
        try:
            valor = float(input(avd))
            while valor < 0 or valor > 10:
                print(cor(txt='ERRO: Por favor digite uma nota valida', cor = 'vermelho'))
                valor = float(input(avd))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite uma nota válida.', cor='vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nota válida. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor

            
def leia_notaAvds(avds):
    while True:
        try:
            valor = float(input(avds))
            while valor < 0 or valor > 10:
                print(cor(txt='ERRO: Por favor digite uma nota valida', cor = 'vermelho'))
                valor = float(input(avds))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite uma nota válida.', cor='vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nota válida. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor


def leia_nome(nome):
    while True:
        try:
            nome = str(input(nome))
            while not nome.isalpha():
                print(cor(txt='ERRO: Por favor, digite um nome válido.', cor='vermelho'))
                nome = str(input(nome))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nota válida. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return nome

            
            
            
            
            
            

