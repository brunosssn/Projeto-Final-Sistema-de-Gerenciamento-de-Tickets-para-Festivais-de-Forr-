from abc import ABC, abstractmethod
import uuid
from datetime import datetime

# -------------------------------------------------
# 1) Interface                                    🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass

# -------------------------------------------------
# 2) Mixins                                       🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine o com outras classes."""
    def __init__(self, gerar):
        gerar = self.get_id()
        self.gerar = gerar

    def get_id(self):
        return uuid.uuid4()

class AuditavelMixin:
    """Fornece logs simples ao console."""
    # TODO: imprimir no formato  [LOG] <evento>
    def log_evento(self, evento: str):
        print(f"[LOG]: <{evento}>")

# -------------------------------------------------
# 3) Classe base Pessoa                           🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f"{self._nome} ({self._cpf})"
                    

# -------------------------------------------------
# 4) Ingresso — classe simples                    🡇
# -------------------------------------------------
class Ingresso:
    def __init__(self, codigo: str, tipo: str, preco: float):
        self.codigo = codigo
        self.tipo = tipo 
        self.preco = preco
    def __str__(self):
        return f"[{self.codigo}] {self.tipo} – R$ {self.preco:.2f}"
    
# -------------------------------------------------
# 5) Cliente                                      🡇
# -------------------------------------------------
class Cliente(Pessoa):
    """Herda de Pessoa e possui ingressos."""
    def __init__(self, nome: str, cpf: str, email: str):
        super().__init__(nome, cpf)
        self.email = email
        self.ingressos = []
        # TODO: chamar super().__init__ e criar lista vazia de ingressos
    
    def comprar_ingresso(self, ingresso: Ingresso):
        self.ingressos.append(ingresso)
        print(f"ingressos comprados")
        # TODO: adicionar ingresso à lista
    
    def listar_ingressos(self):
        # TODO: imprimir os ingressos
        for ingresso in self.ingressos:
            print(ingresso)

# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)      🡇
# -------------------------------------------------
# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, registro
# - Métodos:
#   • exibir_dados()    → imprime nome, cargo, registro e ID
#   • logar_entrada()   → registra no log
class Funcionario(Pessoa, IdentificavelMixin, Logavel, AuditavelMixin):#ver se está funcionando audi
    def __init__(self, nome: str, cpf: str, cargo: str, registro: str):
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.registro = registro
        self.gerar = self.get_id()

    def exibir_dados(self):
        print(f"{self.nome} / {self.cargo} / {self.registro} // {self.gerar}")

    def logar_entrada(self):
        print(f"o {self.nome}, entrou às {datetime.now()}") 


# -------------------------------------------------
# 7) Palco (objeto de composição)                 🡇
# -------------------------------------------------
class Palco:
    """Objeto que compõe o Festival."""
    def __init__(self, nome: str, capacidade: int):
        # TODO: armazenar nome e capacidade
        self.nome = nome
        self.capacidade = capacidade

    def resumo(self):
        # TODO: retornar string "Palco X – cap. Y pessoas"
        return f"Palco {self.nome} - cap {self.capacidade} pessoas"
    
# -------------------------------------------------
# 8) Festival (composição com Palco)              🡇
# -------------------------------------------------
# TODO: Implementar a classe Festival
# - Atributos: nome, data, local, palco
# - Listas: clientes, equipe, ingressos
# - Métodos:
#   • vender_ingresso(cliente, ingresso)  (checar duplicidade & capacidade)
#   • adicionar_funcionario(func)
#   • listar_clientes()
#   • listar_equipe()
#   • listar_ingressos()

class Festival:
    def __init__(self, nome, capacidade, data, local):
        self.nome = nome
        self.data = data
        self.local = local
        self.palco = Palco(nome, capacidade)
        self.cliente = []
        self.equipe = []
        self.ingressos_ven = []

    def vender_ingresso(self, cliente: Cliente, ingresso: Ingresso, capacidade_rest: int):
        print(f"Cliente {cliente} comprou ingresso {ingresso}")
        if cliente in self.cliente:
            print(f"Cliente {cliente} já comprou antes. Mas foi add")
        self.cliente.append(cliente)
        self.ingressos_ven.append(ingresso)
        capacidade_rest -= len(self.ingressos_ven)
        print(f"capacidade restante: {capacidade_rest}")

    def adicionar_funcionario(self, func: Funcionario):
        self.equipe.append(func)
        print(f"funcionário: {func.nome} adicionado a equipe ")

    def listar_clientes(self):
        for i in self.cliente:
            print(i)

    def listar_equipe(self):
        for i in self.equipe:
            print(i)

    def listar_ingressos(self):
        for ingresso in self.ingressos_ven:
            print(ingresso)

    def __eq__(self, other):
        if isinstance(other, Festival):
            return self.nome == other.nome
        return False
    
    def __lt__(self, other):
        if isinstance(other, Festival):
            return self.palco.capacidade < other.palco.capacidade
        return False

# -------------------------------------------------
# 9) EmpresaEventos                               🡇
# -------------------------------------------------
class EmpresaEventos:
    """Agrupa seus festivais (has-a)."""
    def __init__(self, nome: str):
        # TODO: validar nome (≥ 3 letras) e criar lista vazia de festivais
        self._nome = nome 
        self.festivais = []
        if len(nome) >= 3:
            print("nome validado")
        else: 
            print("nome nao validado")
            breakpoint
    @property
    def nome(self):
        # TODO: retornar nome
        return self.nome
    @nome.setter
    def nome(self, novo_nome: str):
        # TODO: validar + atualizar nome
        if len(novo_nome) >= 3:
            print("novo nome validado")
        else: 
            print("novo nome nao validado")
            novo_nome = "aaa"

    def adicionar_festival(self, festival: Festival):
        # TODO: adicionar festival à lista
        self.festivais.append(festival)

    def buscar_festival(self, nome: str):
        # TODO: retornar festival ou None
        for festival in self.festivais:
            if festival == nome:
                return festival.nome
        return None
    
    def listar_festivais(self):
        # TODO: imprimir todos os festivais
        for e in self.festivais:
            print(f"{e.nome} // {e.data} // {e.local} // {e.palco.resumo()}")


# -------------------------------------------------
# 10) Auditor (Identificável + Logável)           🡇
# -------------------------------------------------
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_festival(fest) → verifica:
#         ▸ Nº de clientes ≤ capacidade do palco
#         ▸ existe ao menos 1 funcionário
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"

class Auditor(IdentificavelMixin, Logavel, Festival):
    def __init__(self, gerar, nome):
        super().__init__(gerar)
        self.nome = nome

    def logar_entrada(self):
        print(f"o {self.nome}, entrou às {datetime.now()}")
    
    def auditar_festival(self):
        if len(self.cliente) <= self.palco.capacidade:
            print(f"funcionário adicionado a equipe {self.equipe}")
        else:
            print("palco lotado, com mais clientes do que devia")
        if len(self.equipe) > 0:
            print("existe ao menos 1 funcionário")
        else:
            print("não existem funcionários")
                
    def __str__(self):
        return f"Auditor <{self.nome}> (ID:{self.gerar})"


# -------------------------------------------------
# 11) Bloco de teste                              🡇
# -------------------------------------------------

    a = Pessoa("Bruno", "3456")
    print(a.nome)
    print(a.__str__())

    empresa = EmpresaEventos("Vai de bet")
    festival1 = Festival("MCJ", 50000, "01/01", "Mossoró")
    festival2 = Festival("FINECAP", 10000, "08/09", "PDF")

    cliente1 = Cliente("Bruno", "12345", "eubrunosena2@gmail.com")
    cliente2 = Cliente("Gabriela", "5678", "gabrielaalmeida@gmail.com")
    cliente3 = Cliente("Alessandro", "45678", "alessandroh@gmail.com")

    funcionario1 = Funcionario("Allan", "9876", "Faxineiro", "2345")
    funcionario2 = Funcionario("Bolsonaro", "0987", "Limpa vasos", "preso")


    empresa = EmpresaEventos("Vai de bet")

    empresa.adicionar_festival(festival1)
    empresa.adicionar_festival(festival2)
    print(empresa.buscar_festival(festival1))
    empresa.listar_festivais()


