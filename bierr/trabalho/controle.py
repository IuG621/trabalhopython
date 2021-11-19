from modelo import MENU_INICIAL
import banco as bd
from estilo import cor
from modelo import exibir_cabecalho
from exececoes import leia_nome, leia_nota1, leia_nota2, leia_nota3, leia_notaAvd, leia_notaAvds, leia_numero

def exibir_aluno():
    for dado in bd.get_aluno():
        condicao = u'\u2713' if dado[2] >= 6 else '\U0001F40D'
        imprime = '- [{:>4}] {:<32} {:>4} {:^3} {:^3} {:^3} {:^3} {:^3}'.format(dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6], condicao)
        print(imprime)

def criar_aluno():
    try:
        nome = leia_nome(cor(txt='Digite o nome: ', cor='verde'))
        av1 = leia_nota1(cor(txt='Digite o nota AV1: ', cor='verde'))
        av2 = leia_nota2(cor(txt='Digite o nota AV2: ', cor='verde'))
        av3 = leia_nota3(cor(txt='Digite o nota av3: ', cor='verde'))
        avd = leia_notaAvd(cor(txt='Digite o nota avd: ', cor='verde'))
        avds = leia_notaAvds(cor(txt='Digite o nota avds: ', cor='verde'))
        

        
        
        
        
        print('Adcionando aluno -> ' + str(nome))
    except Exception as e:
        print("Erro ao cria o aluno, {}".format(e))
    else:
        if nome != str(MENU_INICIAL) and (av1, av2, av3, avd, avds) != str(MENU_INICIAL):
            bd.add_aluno(nome, av1, av2, av3, avd, avds)

def excluir_aluno():
    for dado in bd.get_aluno():
        condicao = u'\u2713' if dado[2] >= 6 else '\0001F48D'
        imprime = '- [{:>4}] {:<32} {:>4} {:^3} {:^3} {:^3} {:^3} {:^3}'.format(
            dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6], condicao)
        print(imprime)
    try:
        id_aluno = leia_numero(cor(txt='Digite a id do aluno: ', cor='amarelo'))
        print('Excluindo aluno -> ' + str(id_aluno))
    except Exception as e:
        print("Erro: Ao excluir o aluno: {}".format(e))
    else:
        if id_aluno != MENU_INICIAL:
            bd.excluir_aluno(id_aluno)

def alterar_aluno():
    for dado in bd.get_aluno():
        condicao = u'\u2713' if dado[2] >= 6 else '\0001F48D'
        imprime = '- [{:>4}] {:<32} {:>4} {:^3} {:^3} {:^3} {:^3} {:^3}'.format(
            dado[0], dado[1], dado[2], dado[3], dado[4], dado[5], dado[6], condicao)
        print(imprime)
    try:
        id_aluno = leia_numero(cor(txt='Digite a id do aluno: ', cor='amarelo'))
        print('Alterando aluno -> ' + str(id_aluno) + ' ' + str(dado[1]) )
    except Exception as e:
        print("Erro: Ao alterar o aluno: {}".format(e))
    else:
        nome = leia_nome(cor(txt='Digite o novo nome para {}: '.format(dado[1]), cor='verde'))
        if id_aluno != MENU_INICIAL:
            bd.alterar_aluno(id_aluno, nome)
