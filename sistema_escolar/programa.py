import classes as c

banco_de_logins = c.banco_de_logins
banco_de_alunos = c.banco_de_alunos

programa_rodando = True
while programa_rodando:
    tem_cadastro = c.menu_de_entrada()

    if not tem_cadastro:

        tipo_de_usuario = input('Coordenador [C], Professor [P], Aluno [A]: ').capitalize()
        c.checar_tipo_de_entrada(tipo_de_usuario, 1)

        nome = input('Nome: ').title()
        cpf = input('Cpf: ')
        senha = input('Senha: ')

        cadastro = {"C": lambda: c.Coordenador(nome, cpf, senha),
                    "P": lambda: c.Professor(nome, cpf, senha),
                    "A": lambda: c.Aluno(nome, cpf, senha)}

        novo_usuario = cadastro[tipo_de_usuario]()
        novo_usuario = c.rodar_usuario(novo_usuario)

        if tipo_de_usuario == 'A':
            c.subir_json(banco_de_alunos, novo_usuario.__dict__)
        else:
            c.subir_json(banco_de_logins, novo_usuario.__dict__)

    else:
        while tem_cadastro:

            tipo_de_usuario = input('Coordenador [C], Professor [P], Aluno [A]: ').capitalize()
            c.checar_tipo_de_entrada(tipo_de_usuario, 1)

            login = input('Nome de usuário ou CPF: ').title().strip()
            c.checar_tipo_de_entrada(login, 1)

            senha = input('Digite sua senha: ')
            c.checar_tipo_de_entrada(login, 4)

            if tipo_de_usuario == 'A':
                arquivo_json = c.carregar_json(banco_de_alunos, 'r')

            else:
                arquivo_json = c.carregar_json(banco_de_logins, 'r')

            for usuario_atual in range(len(arquivo_json)):
                usuario = dict(arquivo_json[usuario_atual])

                login_checado = login in usuario['_nome'] or login in usuario['_cpf']
                senha_checada = senha in usuario['_senha']

                if login_checado and senha_checada:
                    print("*** ACESSO CONCEDIDO ***")

                    usuario = c.rodar_usuario(usuario)
                    c.atualizar_json(banco_de_logins, arquivo_json)
                    break

                else:
                    print("*** LOGIN OU SENHA INCORRETOS ***")

        terminar = input('Você deseja terminar o programa? [S] para sair.\n-> ')
        if terminar == 'S':
            break
        continue

print('*** FIM DO PROGRAMA ***')
