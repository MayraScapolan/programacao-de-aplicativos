# importar arquivos
import json
import os

# variavel de alunos
BANCO_DADOS = 'alunos.json'

# funcao cadastrar os alunos
def cadastrar():

    # mostra no terminal "novo cadastro"
    print("\n--- Novo Cadastro ---")
    
    # verifica se o arquivo existe
    if os.path.exists(BANCO_DADOS):

        # abrindo a funcao de ler o arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

            # lendo arquivo
            alunos = json.load(f)

    # se nao, criar uma nova lista        
    else:
        alunos = []

    # criaçao do objeto
        novo_aluno = { # abrir chave do objeto
        "nome": input("Nome: "), # pede nome
        "telefone": input("Telefone: "), # pede o telefone
        "turma": input("Turma: "), # pede a turma
        "idade": int(input("Idade: ")), # pede a idade
        "cpf": input("CPF: ") # pede o cpf
    } # fechar chave do objeto

    # adicionar os alunos ao objeto
    alunos.append(novo_aluno)

    # abrindo a funçao de escrever
    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

        # escreve no arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False)
    
    # mostra ao terminal "aluno cadastrado com sucesso"
    print("Aluno cadastrado com sucesso!")

# funcao listar alunos
def listar():

    # mostra ao terminal "lista de alunos"
    print("\n--- Lista de Alunos ---")
    
    # se o arquivo existir
    if os.path.exists(BANCO_DADOS):

        # abrindo o arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

            # lendo o arquivo 
            alunos = json.load(f)

    # se nao existir alunos     
    else:
        alunos = []

    # se nao for alunos 
    if not alunos:
         
        # mostre nenhum aluno cadastrado
        print("Nenhum aluno cadastrado.")

        # retorne
        return

    # se oque a pessoa digitou estiver na lista 
    for aluno in alunos:

        # mostre o nome, cpf, turma, telefone
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

# funcao atualizar o aluno
def atualizar():

    # abrir no terminal 
    print("\n--- Atualizar Aluno ---")

    # se nao existir no banco de dados
    if not os.path.exists(BANCO_DADOS):

        # mostre que nao tem aluno cadastrado
        print("Nenhum aluno cadastrado no sistema.")

        # retorne
        return

    # abrindo arquivo para ler
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

        # lendo arquivo
        alunos = json.load(f)

    # variavel de cpf para editar o antigo 
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))
    
    # se nome dito, percorra a lista
    for aluno in alunos:

        # se cpf do aluno for igual o cpf da busca
        if aluno['cpf'] == cpf_busca:

            # editando dados do aluno que foi pedido
            print(f"Editando dados de: {aluno['nome']}")

            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            # cadastrando novo nome do aluno, ou deixando nome antigo

            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            # cadastrando novo telefone do aluno, ou deixando telefone antigo

            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            # cadastrando novo turma do aluno, ou deixando turma antigo

            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            # cadastrando novo idade do aluno, ou deixando idade antigo

            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            # cadastrando novo cpf do aluno, ou deixando cpf antigo
            

            # abrindo arquivo para sobescrever
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

                # escrevendo arquivo
                json.dump(alunos, f, indent=4, ensure_ascii=False)

            # mostrando que os dados foram atualizados
            print("Dados atualizados com sucesso!")

            # retorne
            return

    # mostrando que nao tem aluno encontrado
    print("Aluno não encontrado.")

# funcao excluir aluno
def excluir():

    # moatrando que aluno vai ser excluido
    print("\n--- Excluir Aluno ---")

    # se nao existir
    if not os.path.exists(BANCO_DADOS):
  
        # mostrando que nao tem aluno cadastrado
        print("Nenhum aluno cadastrado no sistema.")

        # retorne
        return

    # abrindo arquivo para ler
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

        # lendo arquivo
        alunos = json.load(f)
    
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    # cria uma nova lista que nao tem os alunos com cpf digitado 
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    # se a nova lista for maior, volte a lista antiga
    if len(nova_lista) < len(alunos):

        # abrindo o arquivo para sobrescrever
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

            # escrevendo arquivo
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        
        # mostrando que aluno foi removido
        print("Aluno removido com sucesso!")

    # se nao, mostre que nao tem aluno encontrado
    else:
        print("Aluno não encontrado.")

# funcao de menu
def menu(): 

    # se nao, verifique se existe o arquivo
    if not os.path.exists(BANCO_DADOS):

        # abrindo o arquivo para sobescrever
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

            #escreve a lista nova no arquivo
            json.dump([], f)

    # criando um loop infinito
    while True:
        # mostrando sistema escoa
        print("\n=== SISTEMA ESCOLAR ===")

        # mostrando cadastrar alunp
        print("1. Cadastrar Aluno")

        |# mostrando listar alunos
        print("2. Listar Alunos")

        # mostrando atualizar o aluno
        print("3. Atualizar Aluno")

        # mostrando excluir aluno
        print("4. Excluir Aluno")

        # mostrando sair
        print("5. Sair")
        
        # variavel de escolha de opcao 
        opcao = input("Escolha uma opção: ")
        
         if opcao == '1': cadastrar()
        # se opcao escolhida for 1, mostre cadastrar

        elif opcao == '2': listar()
        # se nao. se escolhida 2, mostre listar

        elif opcao == '3': atualizar()
        # se nao. se escolhida 3, mostre atualizar

        elif opcao == '4': excluir()
        # se nao. se escolhida 4, mostre excluir
        
        elif opcao == '5': break
        # se nao. se escolhida 5, quebrar codigo

        else: print("Opção inválida!")
          # se nao, mostre opcao invalida 

# mostrando menu novamento (loop infinito)
menu()



        
nova_lista = [a for a in alunos if a['id'] != id_busca] # cria uma nova lista onde vai adicionar um novo id e o outro vai ser excluido 
    
    if len(nova_lista) < len(alunos): # o if cria uma nova função e dentro dela tem o len e ele conta quantas pessoas tem dentro da nova_lista 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # salva a lista de alunos no formato json, mantendo o arquivo organizado com recuo e acentos
        print("Aluno removido com sucesso!") # mostra essa mensagem no terminal quando remover um aluno
    else: # se a opção não existir vai para o else
        print("Aluno não encontrado.") # mostra essa mensagem se não encontrar aluno cadastrado

def menu(): # de cria a função, e o nome da função(menu) onde a função vai executar comandos
    if not os.path.exists(BANCO_DADOS): # o comando if not verifica se o arquivo existe ou não dentro da variável
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
            json.dump([], f) # o json.dump aqui armazena uma lista vazia ([]) no arquivo representado por f

    while True:  # laço de repetição que faz ele executar todas as opções
        print("\n=== SISTEMA ESCOLAR ===")  # mostra a mensagem, quebra a lista e começa a mostrar as opções
        print("1. Cadastrar Aluno") # print com a priemira opção
        print("2. Listar Alunos")  # print com a segunda opção 
        print("3. Atualizar Aluno") # print com a terceira opção
        print("4. Excluir Aluno")  # print com a quarta opção
        print("5. Sair") # ultimo print para sair das opções
        
        opcao = input("Escolha uma opção: ") # uma nova variavel, com o input para armazenar ela e para o usuário digitar uma das opções do print
        
        if opcao == '1': cadastrar() # o if cria uma função para o cadastro
        elif opcao == '2': listar() # o elif cria outra função igual a opção para listar
        elif opcao == '3': atualizar() # o elif cria oura função igual para atualizar
        elif opcao == '4': excluir() # o elif cria outra função igual a opção para excluir
        elif opcao == '5': break # o break serve para quebrar o loop
        else: print("Opção inválida!") # cria um else já com a mensagem e com a opção inválida

menu() # criada para mostrar o menu no termina
vao estudadarrrrr(e a amanda)