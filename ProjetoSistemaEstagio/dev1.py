"""
Sistema de Controle de Gastos Residenciais

Este programa permite o gerenciamento de pessoas e transações financeiras, com relatórios de saldos.
"""

# Banco de dados em memória
people_db = []          # Lista para armazenar pessoas
transactions_db = []    # Lista para armazenar transações
last_person_id = 0      # Contador para IDs de pessoas
last_transaction_id = 0 # Contador para IDs de transações

def criar_pessoa():
    """
    Cadastra uma nova pessoa no sistema.
    Gera ID automático e valida idade mínima.
    """
    global last_person_id
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    last_person_id += 1
    new_person = {
        'id': last_person_id,
        'nome': nome,
        'idade': idade
    }
    people_db.append(new_person)
    print(f"Pessoa cadastrada com ID: {last_person_id}")

def listar_pessoas():
    """Lista todas as pessoas cadastradas no sistema."""
    print("\n--- PESSOAS CADASTRADAS ---")
    for person in people_db:
        print(f"ID: {person['id']} | Nome: {person['nome']} | Idade: {person['idade']}")

def deletar_pessoa():
    """
    Remove uma pessoa do sistema.
    Apaga todas as transações relacionadas ao ID da pessoa.
    """
    person_id = int(input("Digite o ID da pessoa para excluir: "))
    
    global people_db, transactions_db
    # Remove pessoa
    people_db = [p for p in people_db if p['id'] != person_id]
    # Remove transações relacionadas
    transactions_db = [t for t in transactions_db if t['pessoa'] != person_id]
    print("Pessoa e transações relacionadas removidas!")

def criar_transacao():
    """
    Cadastra uma nova transação financeira.
    Valida existência da pessoa e restrição para menores de idade.
    """
    global last_transaction_id
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    tipo = input("Tipo (receita/despesa): ").lower()
    pessoa_id = int(input("ID da pessoa: "))
    
    # Validação da pessoa
    pessoa = next((p for p in people_db if p['id'] == pessoa_id), None)
    if not pessoa:
        print("Erro: Pessoa não encontrada!")
        return
    
    # Validação para menores de idade
    if pessoa['idade'] < 18 and tipo != 'despesa':
        print("Erro: Menores só podem ter despesas!")
        return
    
    last_transaction_id += 1
    new_transaction = {
        'id': last_transaction_id,
        'descricao': descricao,
        'valor': valor,
        'tipo': tipo,
        'pessoa': pessoa_id
    }
    transactions_db.append(new_transaction)
    print("Transação cadastrada com sucesso!")

def listar_transacoes():
    """Lista todas as transações cadastradas no sistema."""
    print("\n--- TRANSAÇÕES ---")
    for transacao in transactions_db:
        print(f"ID: {transacao['id']} | Desc: {transacao['descricao']} | Valor: R${transacao['valor']:.2f} | Tipo: {transacao['tipo']} | Pessoa ID: {transacao['pessoa']}")

def consultar_totais():
    """
    Gera relatório financeiro com:
    - Totais individuais por pessoa
    - Totais gerais consolidados
    """
    print("\n--- RELATÓRIO FINANCEIRO ---")
    total_geral_receitas = 0
    total_geral_despesas = 0

    for pessoa in people_db:
        receitas = sum(t['valor'] for t in transactions_db 
                    if t['pessoa'] == pessoa['id'] and t['tipo'] == 'receita')
        despesas = sum(t['valor'] for t in transactions_db 
                     if t['pessoa'] == pessoa['id'] and t['tipo'] == 'despesa')
        saldo = receitas - despesas
        
        print(f"\nPessoa: {pessoa['nome']} (ID: {pessoa['id']})")
        print(f"Receitas: R${receitas:.2f}")
        print(f"Despesas: R${despesas:.2f}")
        print(f"Saldo: R${saldo:.2f}")
        
        # Acumula totais gerais
        total_geral_receitas += receitas
        total_geral_despesas += despesas

    print("\n--- TOTAL GERAL ---")
    print(f"Total de Receitas: R${total_geral_receitas:.2f}")
    print(f"Total de Despesas: R${total_geral_despesas:.2f}")
    print(f"Saldo Líquido: R${total_geral_receitas - total_geral_despesas:.2f}")

def menu():
    """Exibe o menu principal e gerencia as opções."""
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Deletar Pessoa")
        print("4. Cadastrar Transação")
        print("5. Listar Transações")
        print("6. Consultar Totais")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            deletar_pessoa()
        elif opcao == '4':
            criar_transacao()
        elif opcao == '5':
            listar_transacoes()
        elif opcao == '6':
            consultar_totais()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()