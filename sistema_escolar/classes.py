import json


# *** MENUS ***
def menu_de_entrada():  # ALTERAR O MENU
    print(15 * '*', ' BOAS-VINDAS ', 15 * '*')
    menu_entrada = """
Bem-vindo ao Sistema Escolar!
Digite N caso não possua cadastro.
Ou qualquer tecla para prosseguir."""
    print(menu_entrada)

    escolha = input('-> ').capitalize()
    if escolha == 'N':
        return False
    return True


def voltar_ao_menu_de_entrada():
    voltar = input("[S] para voltar ao menu de entrada\n"
                   "ou qualquer tecla para continuar\n"
                   "-> ")

    if voltar == "S":
        return True

    return False


def menu_principal_coordenador():
    print('', 25 * '_', 'MENU', 25 * '_')
    menu_prp = """
    [1] Inserir instituicao
    [2] Remover instituicao
    [3] Inserir turma
    [4] Remover turma
    [5] Inserir alunos em turma
    [6] Remover alunos específicos
    """

    print(menu_prp)
    escolha = int(input('-> '))

    return escolha


def menu_principal_professor():
    print('', 25 * '_', 'MENU', 25 * '_')
    menu_prp = """
    [1] Inserir instituição
    [2] Remover instituição
    [3] Encarregar turma ao professor
    [4] Retirar professor de turma
    [5] Inserir alunos em turma
    [6] Remover alunos específicos
    [7] Inserir notas gerais
    [8] Reiniciar notas da turma
    [9] Editar/remover notas individuais
    """

    print(menu_prp)
    escolha = int(input('-> '))

    return escolha


def menu_principal_aluno():
    print('', 25 * '_', 'MENU', 25 * '_')
    menu_prp = """
    [1] Inserir nova instituição
    [2] Remover instituição
    [3] Ver notas
    """

    print(menu_prp)
    escolha = int(input('-> '))

    return escolha


# *** FUNÇÕES JSON ***
def carregar_json(load_arquivo: str, forma: str) -> str:
    """
    Função utilizada para deserializar dados.
    :param forma: Forma como será aberto o arquivo. Ex. read, write, append.
    :param load_arquivo: Diretório do arquivo json a se carregar os dados.
    :return: Variável contendo os dados deserializados.
    """

    with open(load_arquivo, forma) as banco:
        arquivo_json = json.load(banco)
        return arquivo_json


def subir_json(load_arquivo: str, dados: object) -> str:
    """
    Função utilizada para serializar dados.
    :param load_arquivo: Diretório do arquivo json a se inserir os dados.
    :param dados: Objeto com informações a serem inseridas.
    :return: Mensagem de sucesso.
    """

    with open(load_arquivo, 'r') as banco:
        usuario_formatado = json.dumps(dados)
        usuario_formatado = usuario_formatado.replace("_Usuario", "")

        arquivo_json = json.load(banco)
        arquivo_json.append(json.loads(usuario_formatado))

    with open(load_arquivo, 'w') as banco:
        json.dump(arquivo_json, banco, indent=4)
        return '*** DADOS ENVIADOS COM SUCESSO ***'


def atualizar_json(load_arquivo, dados):
    json_string = json.dumps(dados)
    json_object = json.loads(json_string)
    with open(load_arquivo, 'w') as banco:
        json.dump(json_object, banco, indent=4)


# *** FUNÇÕES AUXILIARES ***
def checar_tipo_de_entrada(entrada, chave: int):
    entrada_filtrada = entrada
    if type(entrada_filtrada) is str:
        entrada_filtrada = entrada.replace(' ', '')

    entradas_possiveis = {
        1: lambda text: text.isalpha(),
        2: lambda text: text.isnumeric(),
        3: lambda text: text.isalpha() or text.isnumeric(),
        4: lambda text: text.isalnum()
    }
    frases_possiveis = {1: 'alfabética.',
                        2: 'numérica.',
                        3: 'alfabética ou numérica.',
                        4: 'alfanumérica.'}

    verificacao_de_entrada = entradas_possiveis[chave](entrada_filtrada)
    if verificacao_de_entrada is False:
        while verificacao_de_entrada is False:
            print(f'Entrada incorreta. É possível apenas entrada {frases_possiveis[chave]}')
            correcao = input("Corrija a entrada: ")

            if chave in entradas_possiveis:
                checar_correcao = entradas_possiveis[chave](correcao.replace(" ", ""))
                if checar_correcao is False:
                    continue

            return correcao

    return entrada


def printar_iteraveis(titulo: str, iteravel: list):
    print(titulo)
    num = 0
    if type(iteravel) is list:
        for item in range(len(iteravel)):
            num += 1
            print(f'-->  [{num}] {iteravel[item]}')


def rodar_usuario(usuario):
    coordenador = isinstance(usuario, Coordenador)
    professor = isinstance(usuario, Professor)
    aluno = isinstance(usuario, Aluno)
    print('aluno:', aluno, 'professor:', professor, 'coord:', coordenador)
    if coordenador:
        while coordenador:
            escolha = menu_principal_coordenador()
            interacao = {1: lambda: usuario.inserir_instituicao(),
                         2: lambda: usuario.remover_instituicao(),
                         3: lambda: usuario.inserir_turma(),
                         4: lambda: usuario.remover_turma(),
                         5: lambda: usuario.inserir_alunos_em_turma(),
                         6: lambda: usuario.remover_alunos_especificos()}

            interacao[escolha]()

            retornando_ao_menu_de_entrada = voltar_ao_menu_de_entrada()
            if retornando_ao_menu_de_entrada:
                coordenador = False

        return usuario

    elif professor:
        while professor:
            escolha = menu_principal_professor()
            interacao = {1: lambda: usuario.inserir_instituicao(),
                         2: lambda: usuario.remover_instituicao(),
                         3: lambda: usuario.encarregar_turma_ao_professor(),
                         4: lambda: usuario.retirar_professor_de_turma(),
                         5: lambda: usuario.inserir_alunos_em_turma(),
                         6: lambda: usuario.remover_alunos_especificos(),
                         7: lambda: usuario.inserir_notas_gerais(),
                         8: lambda: usuario.reiniciar_notas_da_turma(),
                         9: lambda: usuario.editar_ou_remover_notas_individuais()}

            interacao[escolha]()

            retornando_ao_menu_de_entrada = voltar_ao_menu_de_entrada()
            if retornando_ao_menu_de_entrada:
                professor = False

        return usuario

    elif aluno:
        while aluno:
            escolha = menu_principal_aluno()
            interacao = {1: lambda: usuario.inserir_instituicao(),
                         2: lambda: usuario.remover_instituicao(),
                         3: lambda: usuario.consultar_notas()}

            interacao[escolha]()

            retornando_ao_menu_de_entrada = voltar_ao_menu_de_entrada()
            if retornando_ao_menu_de_entrada:
                aluno = False

        return usuario

    # *** CLASSES DE ALUNOS, PROFESSORES E COORDENADORES ***


class Aluno:
    def __init__(self, nome, cpf, senha, titulo="Aluno", instituicoes=None, turmas=None):
        self._nome = nome.title().strip()
        self._cpf = cpf
        self._senha = senha
        self.titulo = titulo
        self.instituicoes = [] if instituicoes is None else instituicoes
        self.turmas = [] if turmas is None else turmas

    def inserir_instituicao(self):
        arquivo_json = carregar_json(banco_de_escolas, 'r')
        entrada = input('Digite o nome ou código da escola: ')
        entrada = checar_tipo_de_entrada(entrada, 3)

        for escola in range(len(arquivo_json)):
            codigo_escola = dict(arquivo_json[escola])
            if (entrada == codigo_escola["codigo"]) or (entrada == codigo_escola["escola"]):
                self.instituicoes.append(codigo_escola)
                return '*** MATRÍCULA REALIZADA COM SUCESSO ***'

        return '*** INSTITUIÇÃO INEXISTENTE ***'

    def remover_instituicao(self):
        entrada = input('Digite o nome ou código da escola: ')
        entrada = checar_tipo_de_entrada(entrada, 3)
        for escola in range(len(self.instituicoes)):
            codigo_escola = self.instituicoes[escola]
            if (entrada == codigo_escola["codigo"]) or (entrada == codigo_escola["escola"]):
                self.instituicoes.remove(codigo_escola)

                turmas_pendentes = True
                while turmas_pendentes:
                    turmas_pendentes = self.remocao_de_turmas_pendentes(codigo_escola)

                return '*** INSTITUIÇÃO REMOVIDA COM SUCESSO ***'

        return '*** INSTITUIÇÃO INEXISTENTE ***'

    def remocao_de_turmas_pendentes(self, codigo_escola):
        for key, value in self.turmas.items():
            if value == codigo_escola:
                del self.turmas[key]
                return True

        return False

    def consultar_notas(self):
        for turma in range(len(self.turmas)):
            turma_do_aluno = self.turmas[turma]['turmas']
            print(turma_do_aluno)


class Coordenador(Aluno):
    def __init__(self, _nome, _cpf, _senha, titulo="Coordenador(a)", instituicoes=None):
        super().__init__(_nome, _cpf, _senha, titulo, instituicoes)
        self.titulo = titulo
        self.instituicoes = [] if instituicoes is None else instituicoes

    def retorna_lista_de_instituicoes(self):
        lista_de_instituicoes = []
        for escola_atual in range(len(self.instituicoes)):
            lista_de_instituicoes.append(self.instituicoes[escola_atual]['escola'])

        return lista_de_instituicoes

    @staticmethod
    def retorna_lista_de_turmas(BD_turmas, instituicao, estado=None):
        lista_de_turmas = []
        for turma in range(len(BD_turmas)):
            verificar_escola = instituicao in BD_turmas[turma]['instituicao_referente']['escola']
            verificar_ocupacao = BD_turmas[turma]['professor(a)'] == estado
            if verificar_escola and verificar_ocupacao:
                turma_verificada = BD_turmas[turma]['turma']
                lista_de_turmas.append(turma_verificada)

        return lista_de_turmas

    @staticmethod
    def retorna_lista_de_alunos(BD_alunos, instituicao):
        lista_de_alunos = []
        for aluno in range(len(BD_alunos)):
            if instituicao == BD_alunos[aluno]['instituicoes'][0]['escola']:
                nome = BD_alunos[aluno]['_nome']
                cpf = BD_alunos[aluno]['_cpf']

                lista_de_alunos.append({'nome': nome, 'cpf': cpf})

        return lista_de_alunos

    def retorna_instituicao_escolhida(self):
        lista_de_instituicoes = self.retorna_lista_de_instituicoes()
        titulo = '** LISTA DE INSTITUIÇÕES DISPONÍVEIS **'
        printar_iteraveis(titulo, lista_de_instituicoes)

        escolher_escola = int(input('Escolha uma das escolas acima digitando o número: '))
        escolher_escola -= 1

        instituicao = lista_de_instituicoes[escolher_escola]
        return instituicao

    def retorna_turma_escolhida(self, BD_turmas, instituicao_escolhida, estado=None):
        lista_de_turmas = self.retorna_lista_de_turmas(BD_turmas, instituicao_escolhida, estado)
        titulo = '** LISTA DE TURMAS DISPONÍVEIS NA INSTITUIÇÃO ESCOLHIDA **'
        printar_iteraveis(titulo, lista_de_turmas)

        escolher_turma = int(input('Escolha uma das turmas acima digitando o número: '))
        escolher_turma -= 1

        turma = lista_de_turmas[escolher_turma]

        return turma

    def inserir_turma(self):
        turma = input('Digite o nome da turma: ')
        turma = checar_tipo_de_entrada(turma, 1)
        instituicao_referente = self.instituicoes[0]
        turma_inserida = {"turma": turma,
                          "instituicao_referente": instituicao_referente,
                          "professor(a)": None,
                          "alunos": []}

        subir_json(banco_de_turmas, turma_inserida)

        return '*** TURMA INSERIDA COM SUCESSO ***'

    @staticmethod
    def remover_turma():
        nome_da_turma = input('Digite o nome da turma: ')
        nome_da_turma = checar_tipo_de_entrada(nome_da_turma, 1)

        BD_turmas = list(carregar_json(banco_de_turmas, 'r'))

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']
            if nome_da_turma in turma_atual:
                del BD_turmas[turma]
                atualizar_json(banco_de_turmas, BD_turmas)

                return '*** TURMA REMOVIDA COM SUCESSO ***'

        return '*** TURMA INEXISTENTE ***'

    def inserir_alunos_em_turma(self):
        instituicao_escolhida = self.retorna_instituicao_escolhida()
        BD_turmas = carregar_json(banco_de_turmas, 'r')

        # TESTE DE ESTADO INDICA SE ESTAMOS USANDO ESTA FUNÇÃO NA CLASSE COORDENADOR OU NA CLASSE PROFESSOR,
        # O ESTADO COMO 'NONE' É CARACTERÍSTICO DA COORDENAÇÃO, POIS ELA NÃO PRECISA ESTAR ENCARREGADA DA TURMA,
        # PARA INSERIR ALUNOS NELA, DIFERENTEMENTE DO PROFESSOR.
        estado = self._nome
        teste_de_estado = isinstance(self, Coordenador)
        if teste_de_estado:
            estado = None

        turma_escolhida = self.retorna_turma_escolhida(BD_turmas, instituicao_escolhida, estado)

        BD_alunos = carregar_json(banco_de_alunos, 'r')

        lista_de_alunos = self.retorna_lista_de_alunos(BD_alunos, instituicao_escolhida)
        titulo = '** LISTA DE ALUNOS DISPONÍVEIS PARA A TURMA ESCOLHIDA **'
        printar_iteraveis(titulo, lista_de_alunos)

        print('Escolha alunos digitando seus nomes ou cpf: ')

        saida = True
        while saida:
            if not lista_de_alunos:
                break

            escolher_aluno = input('Nome ou cpf do(a) aluno(a): ')

            # COMPARA A ESCOLHA DO USUÁRIO COM AS OPÇÕES EXISTENTES NA LISTA DE ALUNOS
            for aluno in range(len(lista_de_alunos)):
                nome_do_aluno = lista_de_alunos[aluno]['nome']
                cpf_do_aluno = lista_de_alunos[aluno]['cpf']
                verificar_nome = escolher_aluno in nome_do_aluno
                verificar_cpf = escolher_aluno in cpf_do_aluno

                # INSERE O ALUNO NA TURMA
                if verificar_nome or verificar_cpf:
                    aluno_atual = {'nome': nome_do_aluno, 'cpf': cpf_do_aluno, 'notas': []}
                    atualizacao_aluno = {turma_escolhida: {"notas": []}}

                    for turma in range(len(BD_turmas)):
                        turma_atual = BD_turmas[turma]['turma']

                        if turma_escolhida in turma_atual:
                            BD_turmas[turma]['alunos'].append(aluno_atual)

                            # TESTE
                            BD_alunos[aluno]['turmas'].append(atualizacao_aluno)

            # DELETA AS OPÇÕES ESCOLHIDAS PELO USUÁRIO DA LISTA DE ALUNOS
            for aluno in range(len(lista_de_alunos)):
                nome_do_aluno = lista_de_alunos[aluno]['nome']
                cpf_do_aluno = lista_de_alunos[aluno]['cpf']
                verificar_nome = escolher_aluno == nome_do_aluno
                verificar_cpf = escolher_aluno == cpf_do_aluno

                if verificar_nome or verificar_cpf:
                    del lista_de_alunos[aluno]
                    printar_iteraveis(titulo, lista_de_alunos)
                    break

        atualizar_json(banco_de_turmas, BD_turmas)
        atualizar_json(banco_de_alunos, BD_alunos)
        return '*** ALUNOS INSERIDOS COM SUCESSO ***'

    @staticmethod
    def remover_alunos_especificos():
        nome_do_aluno = input('Digite o nome do aluno: ')
        nome_do_aluno = checar_tipo_de_entrada(nome_do_aluno, 1)

        nome_da_turma = input('Digite a turma que deseja removê-lo(a): ')
        nome_da_turma = checar_tipo_de_entrada(nome_da_turma, 3)

        BD_turmas = carregar_json(banco_de_turmas, 'r')

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']
            if nome_da_turma in turma_atual:
                alunos = BD_turmas[turma]['alunos']

                for aluno in range(len(alunos)):
                    if nome_do_aluno in alunos[aluno]['nome']:
                        del BD_turmas[turma]['alunos'][aluno]
                        atualizar_json(banco_de_turmas, BD_turmas)

                        return '*** ALUNO(A) REMOVIDO(A) COM SUCESSO ***'

                if not alunos:
                    return '*** NÃO FORAM INSERIDOS ALUNOS NESTA TURMA'

        if not BD_turmas:
            return '*** NÃO FORAM CRIADAS TURMAS NESTA INSTITUIÇÃO ***'


class Professor(Coordenador):
    def __init__(self, _nome, _cpf, _senha, titulo="Professor(a)", instituicoes=None, turmas=None, alunos=None):
        super().__init__(_nome, _cpf, _senha, titulo, instituicoes)
        self.titulo = titulo
        self.instituicoes = [] if instituicoes is None else instituicoes
        self.turmas = {} if turmas is None else turmas
        self.alunos = {} if alunos is None else alunos

    def encarregar_turma_ao_professor(self):
        instituicao_escolhida = self.retorna_instituicao_escolhida()
        BD_turmas = carregar_json(banco_de_turmas, 'r')
        turma_escolhida = self.retorna_turma_escolhida(BD_turmas, instituicao_escolhida)

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']
            if turma_escolhida in turma_atual:
                BD_turmas[turma]['professor(a)'] = self._nome

                # TESTE
                self.turmas.append(turma_escolhida)

                atualizar_json(banco_de_turmas, BD_turmas)

                return '*** PROFESSOR ENCARREGADO COM SUCESSO ***'

        return '*** ESCOLHA FORA DO ESCOPO ***'

    def retirar_professor_de_turma(self):
        instituicao_escolhida = self.retorna_instituicao_escolhida()
        BD_turmas = carregar_json(banco_de_turmas, 'r')
        turma_escolhida = self.retorna_turma_escolhida(BD_turmas, instituicao_escolhida)

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']
            if turma_escolhida in turma_atual:
                BD_turmas[turma]['professor(a)'] = None

                # TESTE
                for teste in range(len(self.turmas)):
                    print('TESTE: self.turmas:', self.turmas)
                    print('TESTE: self.turmas[teste]:', self.turmas[teste])
                    if turma_escolhida in self.turmas[turma]:
                        del self.turmas[turma]

                atualizar_json(banco_de_turmas, BD_turmas)

                return '*** PROFESSOR ENCARREGADO COM SUCESSO ***'

        return '*** ESCOLHA FORA DO ESCOPO ***'
        pass

    def inserir_notas_gerais(self):
        instituicao_escolhida = self.retorna_instituicao_escolhida()
        BD_turmas = carregar_json(banco_de_turmas, 'r')
        turma_escolhida = self.retorna_turma_escolhida(BD_turmas, instituicao_escolhida, self._nome)

        qtd_de_notas = int(input('Digite a quantidade de avaliações: '))

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']

            if turma_escolhida in turma_atual:
                alunos = BD_turmas[turma]['alunos']

                for aluno in range(len(alunos)):
                    nome_do_aluno = alunos[aluno]['nome']
                    print(f'Notas do(a) aluno(a) {nome_do_aluno}:')
                    notas_do_aluno = []

                    for nota in range(qtd_de_notas):
                        dar_nota = float(input(f'{nota + 1}ª Avaliação: '))
                        notas_do_aluno.append(dar_nota)
                        BD_turmas[turma]['alunos'][aluno]['notas'] = notas_do_aluno

        atualizar_json(banco_de_turmas, BD_turmas)
        return '*** NOTAS INSERIDAS COM SUCESSO ***'

    def reiniciar_notas_da_turma(self):
        instituicao_escolhida = self.retorna_instituicao_escolhida()
        BD_turmas = carregar_json(banco_de_turmas, 'r')
        turma_escolhida = self.retorna_turma_escolhida(BD_turmas, instituicao_escolhida, self._nome)

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']
            if turma_escolhida in turma_atual:
                for aluno in range(len(BD_turmas[turma]['alunos'])):
                    notas_do_aluno = []
                    BD_turmas[turma]['alunos'][aluno]['notas'] = notas_do_aluno

        atualizar_json(banco_de_turmas, BD_turmas)
        return '*** NOTAS INSERIDAS COM SUCESSO ***'

    def editar_ou_remover_notas_individuais(self):
        instituicao_escolhida = self.retorna_instituicao_escolhida()
        BD_turmas = carregar_json(banco_de_turmas, 'r')
        turma_escolhida = self.retorna_turma_escolhida(BD_turmas, instituicao_escolhida, self._nome)

        qtd_de_notas = int(input('Digite a quantidade de avaliações: '))

        for turma in range(len(BD_turmas)):
            turma_atual = BD_turmas[turma]['turma']
            if turma_escolhida in turma_atual:

                lista_de_alunos = []
                for aluno in range(len(BD_turmas[turma]['alunos'])):
                    nome_do_aluno = BD_turmas[turma]['alunos'][aluno]['nome']
                    lista_de_alunos.append(nome_do_aluno)

                titulo = '** LISTA DE ALUNOS DISPONÍVEIS NA TURMA ESCOLHIDA **'
                printar_iteraveis(titulo, lista_de_alunos)

                escolher_aluno = int(input('Escolha um dos alunos acima digitando o número: '))
                escolher_aluno -= 1

                for aluno in range(len(BD_turmas[turma]['alunos'])):
                    if lista_de_alunos[escolher_aluno] in BD_turmas[turma]['alunos'][aluno]['nome']:
                        notas_do_aluno = []
                        for nota in range(qtd_de_notas):
                            dar_nota = float(input(f'{nota + 1}ª Avaliação: '))
                            notas_do_aluno.append(dar_nota)
                            BD_turmas[turma]['alunos'][aluno]['notas'] = notas_do_aluno

                atualizar_json(banco_de_turmas, BD_turmas)
                return '*** NOTAS MODIFICADAS COM SUCESSO ***'


diretorio_principal = r'C:\Users\Sávio Miranda\PycharmProjects\Estudos\Elielson\Projeto_escola\bancos_de_dados'
banco_de_logins = diretorio_principal + r'\logins.json'
banco_de_escolas = diretorio_principal + r'\escolas_por_webscrapping\escolas.json '
banco_de_turmas = diretorio_principal + r'\turmas.json'
banco_de_alunos = diretorio_principal + r'\alunos.json'
