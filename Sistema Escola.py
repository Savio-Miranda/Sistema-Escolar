# IMPORTANDO FUNÇÕES
import json
import funcoes

diretorio_logins = 'banco_de_dados_logins.json'
diretorio_instituicoes = 'banco_de_instituicoes.json'

programa_rodando = True
while programa_rodando:
    if not funcoes.menu():
        login_do_usuario = {}
        todas_as_instituicoes = {}

        nome = input('Digite seu nome:\n-> ')
        cpf = input('Digite seu cpf:\n-> ')
        senha = input('Digite sua senha:\n-> ')

        funcoes.acesso_ou_geracao_de_login(nome, cpf, senha, login_do_usuario)
        login_do_usuario.update({'Instituicoes': funcoes.insercao_de_instituicoes()})
        todas_as_instituicoes.update({'Instituicoes': login_do_usuario['Instituicoes']})
        funcoes.inserir_em_json(diretorio_logins, login_do_usuario)
        funcoes.inserir_em_json(diretorio_instituicoes, todas_as_instituicoes)
        programa_rodando = False

    else:
        logado = True
        while logado:
            saida = input('Digite [S] se quiser voltar ou qualquer tecla para prosseguir.\n-> ')
            if saida == 'S':
                break

            acesso = input('Nome de usuário ou CPF:\n-> ')
            senha = input('Digite sua senha:\n-> ')

            with open(diretorio_logins, 'r') as banco_logins:
                dados = json.load(banco_logins)

            for contador2 in range(len(dados)):
                if (acesso in dados[contador2]['nome de usuario'] or acesso in dados[contador2]['CPF']) \
                        and senha in dados[contador2]['senha']:
                    print("Acesso concedido!")

                    interacao = input('| Digite um número para acessar informações no sistema:  |\n'
                                      '| [1] Instituições em que atua;                          |\n'
                                      '| [2] Turmas de alocação;                                |\n'
                                      '| [3] lançar notas;                                      |\n'
                                      '| Ou no caso de acessar o perfil de um aluno, digite seu |\n'
                                      '| nome ou CPF.                                           |\n'
                                      '-> ')

                    if interacao == '1':
                        funcoes.verificar_escolas(dados, contador2)
                    elif interacao == '2':
                        funcoes.verificar_turmas(dados, contador2)
                    elif interacao == '3':
                        print('nada feito')
                    else:
                        funcoes.verificar_alunos(dados, contador2, interacao)

        terminar = input('Você deseja terminar o programa? [S] para sair.\n-> ')
        if terminar == 'S':
            break
        continue

print('Fim do Programa')
