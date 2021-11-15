import json


def menu():  # ALTERAR O MENU
    print('', 25 * '_', 'MENU', 25 * '_')
    print('| Bem-vindo(a) ao Sistema! Se já estiver cadastrado(a),  |\n'
          '| basta digitar seu login/senha. Se não tiver cadastro,  |\n'
          '| digite "1" para criá-lo agora mesmo.', (17 * ' '), '|\n',
          28 * '==')
    escolha = input('-> ')
    if escolha == '1':
        return False
    return True


def acesso_ou_geracao_de_login(arg_nome, arg_cpf, arg_senha, arg_login_do_usuario):
    login = {'nome de usuario': arg_nome, 'CPF': arg_cpf, 'senha': arg_senha}
    arg_login_do_usuario.update(login)
    return login


def insercao_de_instituicoes():
    lista_de_instituicoes = []
    continuar = True
    while continuar:
        instituicao = input('Digite sua instituição:\n-> ')
        lista_de_instituicoes.append({instituicao: insercao_de_turmas()})
        saida = input('Deseja adicionar mais uma instituição?\n'
                      'Digite qualquer tecla para continuar ou [N] para sair.\n-> ')
        if saida == 'N':
            break
    return lista_de_instituicoes


def insercao_de_turmas():
    lista_de_turmas = []
    continuar = True
    while continuar:
        turma = input('Digite sua turma:\n-> ')
        materia = input('Digite sua materia:\n-> ')
        alunos = insercao_de_alunos()
        lista_de_turmas.append({'turma': turma, 'materia': materia, 'alunos': alunos})
        saida = input('Deseja adicionar mais uma turma?\n'
                      'Digite qualquer tecla para continuar ou [N] para sair.\n-> ')
        if saida == 'N':
            break
    return lista_de_turmas


def insercao_de_alunos():
    lista_de_alunos = []
    qtd_de_alunos = int(input('Digite a quantidade de alunos nesta turma:\n-> '))
    for contador in range(qtd_de_alunos):
        nome_de_aluno = input('Nome: ')
        lista_de_alunos.append({'nome': nome_de_aluno, 'nota': 'S/ nota'})
    return lista_de_alunos


def inserir_em_json(arg_load_arquivo, arg_dicionario):
    with open(arg_load_arquivo, 'r') as banco:
        arquivo_json = json.load(banco)
        arquivo_json.append(arg_dicionario)
    with open(arg_load_arquivo, 'w') as banco:
        json.dump(arquivo_json, banco, indent=4)


def verificar_escolas(arg_dados, arg_contador):
    for b in range(len(arg_dados[arg_contador]['Instituicoes'])):
        instituicoes = arg_dados[arg_contador]['Instituicoes'][b].keys()
        return print(instituicoes)


def verificar_turmas(arg_dados, arg_contador):
    for a in range(len(arg_dados[arg_contador]['Instituicoes'])):
        for b in arg_dados[arg_contador]['Instituicoes'][a]:
            turmas = arg_dados[arg_contador]['Instituicoes'][a][b]
            return print(turmas)


def verificar_alunos(arg_dados, arg_contador, arg_interacao):
    for a in range(len(arg_dados[arg_contador]['Instituicoes'])):
        for b in arg_dados[arg_contador]['Instituicoes'][a]:
            for c in range(len(arg_dados[arg_contador]['Instituicoes'][a][b])):
                for d in range(len(arg_dados[arg_contador]['Instituicoes'][a][b][c]['alunos'])):
                    if arg_interacao == arg_dados[arg_contador]['Instituicoes'][a][b][c]['alunos'][d]['nome']:
                        alunos = arg_dados[arg_contador]['Instituicoes'][a][b][c]['alunos'][d]
                        return print(alunos)
    print('Aluno(a) não encontrado(a).')
