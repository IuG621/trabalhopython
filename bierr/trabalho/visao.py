from controle import exibir_aluno
from modelo import exibir_cabecalho
from controle import criar_aluno, excluir_aluno, alterar_aluno, exibir_cabecalho


def main():
    while True:
        try:
            escolha = exibir_cabecalho('Adicionar aluno', 'Exibir aluno(s)', 'Excluir aluno', 'Alterar aluno', 'sair')
        except Exception:
            print('Erro!')
        else:
            if escolha == 1:
                criar_aluno()
            elif escolha == 2:
                exibir_aluno()
            elif escolha == 3:
                excluir_aluno()
            elif escolha == 4:
                alterar_aluno()
            elif escolha == 5:
                break
            else:
                print('Opção invalida')