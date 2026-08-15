from smoperacoes.banco import Banco
from smutilitarios.expections import SaldoInsuficienteError, ContaInexistenteError

def menu_principal():
    print("\n--- Banco Facco ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    return input("Escolha uma opcao: ")

def menu_conta(banco):

    try:

        num_conta = int(input("Digite o numero da conta:"))

        conta = banco.buscar_conta(num_conta)

        while True:
            print(f"\n---Operacoes da conta - {conta._numero} ---")
            print(f" {conta._cliente.nome} | Saldo: {conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver extrato")
            print("4. Voltar ao Menu Principal")

            opcao = input("Escolha uma opcao: ")

            if opcao == '1':
                valor = float(input("Digite o valor do depósito:"))
                conta.depositar(valor)

            elif opcao == '2':
                try:
                 valor = float(input("Digite o valor do saque:"))
                 conta.sacar(valor) 
                except SaldoInsuficienteError as e:
                    print(f"Erro na operacao: {e}")

            elif opcao == '3':
                conta.extrato()

            elif opcao == '4':
                break

            else:
                print("Opcao Invalida. Tente novamente.")

    except ContaInexistenteError as e:
        print(f"Erro: {e}")

    except ValueError:
        print("Erro: Entrada invalida. Por favor, digite um numero.")

def main():

    banco = Banco("Banco Digital Facco")

    while True:

        opcao = menu_principal()

        if opcao == '1':
            nome = input("Digite o nome do cliente:")
            cpf = input("Digite o cpf do cliente:")
            banco.adicionar_cliente(nome,cpf)

        elif opcao == '2':
            cpf = input("Digite o cpf do cliente para o cadastro:")
            cliente = banco._clientes.get(cpf)

            if cliente:

                tipo = input("Digite o tipo de conta(corrente/poupanca):")
                banco.criar_conta(cliente,tipo)

            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")

        elif opcao == '3':
            menu_conta(banco)

        elif opcao == '4':
            print("\n Sistema encerrado")
            break
        else:
            print("Opcao invalida")

if __name__ == "__main__":
    main()

        