from abc import ABC, abstractmethod
from datetime import datetime
from smutilitarios.expections import SaldoInsuficienteError

class Conta(ABC):

    _total_contas = 0

    def __init__(self, numero:int,cliente):
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = []
        Conta._total_contas += 1

    @property
    def saldo(self):
     return self._saldo

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas

    @abstractmethod
    def sacar(self, valor: float):
        pass

    def depositar(self, valor:float):
        if valor>0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Deposito de R${valor:.2f}"))
            print(f"Deposito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor do deposito invalido.")

    def extrato(self):
        print(f"---- Extrato da conta N {self._numero}----")
        print(f"Cliente: {self._cliente}")
        print(f"Saldo: R${self._saldo:.2f}")
        print("Historico de transacoes:")

        if not self._historico:
            print("Nenhuma transacao registrada.")

        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%y %M:%M:%S')}: {transacao}" )
            print("__________________________________________\n")



#tipos de contas

class ContaCorrente(Conta):

    def __init__(self, numero:int,cliente,limite:float = 500.00):

        super().__init__(numero,cliente)

        self.limite = limite

    def sacar(self, valor:float):

        if valor <= 0:
            print("Valor de saque invalido")
            return

        saldo_disponivel = self._saldo + self.limite

        if valor>saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel,valor,"Saldo e limite insuficientes.")

        self._saldo -= valor

        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de {valor:.2f} realizado com sucesso.")

class ContaPoupanca(Conta):
    def __init__(self, numero:int, cliente):
         super().__init__(numero, cliente)

    def sacar(self, valor:float):
        if valor<=0:
            print("Valor de saque inválido")
            return

        if valor>self._saldo:
            raise SaldoInsuficienteError(self._saldo,valor, "Saldo e limite insuficiente.")

        self._saldo -=valor

        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

        
            

    
