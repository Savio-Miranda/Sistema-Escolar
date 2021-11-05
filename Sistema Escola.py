# IMPORTANDO FUNÇÕES
import funcoes

diretorio_logins = 'banco_de_dados_logins.json'
diretorio_instituicoes = 'banco_de_instituicoes.json'

loop = True
while loop:
    if not funcoes.menu():
        login_do_usuario = {}
        instituicoes = {}
        materias = {}
        turmas = {}
        alunos = {}

        nome = input('Digite seu nome:\n-> ')
        cpf = input('Digite seu cpf:\n-> ')
        senha = input('Digite sua senha:\n-> ')

        funcoes.acesso_ou_geracao_de_login(nome, cpf, senha, login_do_usuario)
        funcoes.insercao_de_instituicoes(login_do_usuario, instituicoes)
        funcoes.inserir_em_json(diretorio_logins, login_do_usuario)
        funcoes.inserir_em_json(diretorio_instituicoes, instituicoes)

    else:
        a = 0

    # ENCERRAR PROGRAMA
    parar_programa = input('Deseja parar? Digite "S" para terminar o programa ou qualquer tecla para revonar.\n-> ')
    if parar_programa == 'S':
        break
    continue
