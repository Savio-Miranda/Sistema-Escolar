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


def adicionar_ao_perfil(dicionario, chave, valor):
    dicionario.update({chave: valor})
    return dicionario


def insercao_de_instituicoes(arg_login_do_usuario, arg_instituicoes):
    lista_de_instituicoes = []

    afirmacao = True
    while afirmacao:
        instituicao_atual = input("Digite o nome da INSTITUIÇÃO em que leciona:\n-> ")
        var_auxiliar = insercao_de_turmas_materias(instituicao_atual)
        lista_de_instituicoes.append({instituicao_atual: {"turmas": var_auxiliar}})
        negacao = input('Digite "S" para interromper a inserção de INSTITUIÇÕES ou qualquer tecla para continuar: ')
        if negacao == 'S':
            break
    adicionar_ao_perfil(arg_login_do_usuario, "Instituicoes_do_professor(a)", lista_de_instituicoes)
    adicionar_ao_perfil(arg_instituicoes, "Instituicoes", lista_de_instituicoes)

    return arg_login_do_usuario


def insercao_de_turmas_materias(arg_instituicao_atual):
    lista_de_materias = []

    afirmacao = True
    while afirmacao:
        lista_de_turmas = []

        materia_atual = input("Digite a MATÉRIA que leciona na escola {}:\n-> ".format(arg_instituicao_atual))

        turma_atual = input("Digite o nome da TURMA em que leciona a matéria {}:\n-> ".format(materia_atual))

        lista_de_turmas.append({turma_atual: {"alunos": insercao_de_alunos(turma_atual)}})

        lista_de_materias.append({"materia": {materia_atual: lista_de_turmas}})

        negacao = input('Digite "S" para interromper a inserção de TURMAS ou qualquer tecla para continuar: ')
        if negacao == 'S':
            break

    return lista_de_materias


def insercao_de_alunos(arg_turma_atual):
    lista_de_alunos = []

    qtd_de_alunos = int(input("Quantos alunos existem na turma {}?\n-> ".format(arg_turma_atual)))

    print("Digite o nome de cada um deles:")

    for contador in range(qtd_de_alunos):
        aluno = {}
        nome_do_aluno = input("-> ")
        aluno.update({nome_do_aluno: {"notas": "Sem nota"}})
        lista_de_alunos.append(aluno)

    return lista_de_alunos


def insercao_de_notas():
    lista_de_notas_da_avaliacao = []

    qtd_de_avaliacoes = int(input("Digite a quantidade de avaliacoes feitas pelo(a) aluno(a) no ano:\n-> "))

    print("Digite as notas do(a) aluno(a): ")

    for contador in range(qtd_de_avaliacoes):
        nota = int(input("-> "))
        lista_de_notas_da_avaliacao.append(nota)

    return lista_de_notas_da_avaliacao


def inserir_em_json(arg_load_arquivo, arg_login_do_usuario):
    with open(arg_load_arquivo, "r") as banco:
        temp = json.load(banco)
    temp.append(arg_login_do_usuario)
    with open(arg_load_arquivo, "w") as banco:
        json.dump(temp, banco, indent=4)


def acesso_concedido():
    print("Acesso concedido!")
    interacao = input('| Digite um número para acessar informações no sistema:  |\n'
                      '| [1] Local de cadastro;                                 |\n'
                      '| [2] Turma de alocação;                                 |\n'
                      '| [3] lançar notas;                                      |\n'
                      '| Ou no caso de acessar o perfil de um aluno, digite seu |\n'
                      '| nome ou CPF.                                           |\n'
                      '-> ')
    if interacao == '1':
        verificar_escola()
    elif interacao == '2':
        verificar_turmas()
    elif interacao == '3':
        lancar_editar_notas()
    else:
        verificar_aluno()


def verificar_escola():
    a = 0
    return a


def verificar_turmas():
    a = 0
    return a


def verificar_aluno():
    a = 0
    return a


def lancar_editar_notas():
    a = 0
    return a
