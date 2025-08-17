from projeto_final import Logavel, IdentificavelMixin, AuditavelMixin, Pessoa, Ingresso, Cliente, Funcionario, Palco, Festival, EmpresaEventos, Auditor

#Página de Testes (PYTEST)

pessoa1 = Pessoa("Bruno", "12345")
print(pessoa1.nome)
print(pessoa1.__str__())

print("-" * 50)

ingresso1 = Ingresso("89", "VIP", 59)
ingresso2 = Ingresso("456", "VIP", 200)
print(ingresso1.__str__())
print(ingresso2.__str__())

print("-" * 50)

cliente1 = Cliente(pessoa1, pessoa1, "eubrunosena2@gmail.com")
cliente1.comprar_ingresso(ingresso1)
cliente1.comprar_ingresso(ingresso2)
cliente1.listar_ingressos()

print("-" * 50)

pessoa2 = Pessoa("Alessandro", "3456")
funcionario1 = Funcionario(pessoa2, pessoa2, "Limpador", "6")
funcionario1.exibir_dados()
funcionario1.logar_entrada()

print("-" * 50)

palco1 = Palco("Palco principal", 5000)
print(palco1.resumo())

print("-" * 50)

festival1 = Festival("FINECAP", 10000, "12/09", "Pau dos Ferros")
festival1.vender_ingresso(cliente1, ingresso1, 2000)
festival1.adicionar_funcionario(funcionario1)
festival1.listar_clientes()
festival1.listar_equipe()
festival1.listar_ingressos()

print("-" * 50)

empresa1 = EmpresaEventos("ZERO UM Bet")
empresa2 = EmpresaEventos("FT")
empresa1.adicionar_festival(festival1)
empresa1.listar_festivais()

print("-" * 50)

auditor1 = Auditor("Bruno", "Bruno")
auditor1.logar_entrada()
print(auditor1.__str__())

print("-" * 50)

fest = Festival("Rock In Python Sem Rio", 3, "14/07", "labs do if")
print(fest.palco.resumo())

func1 = Funcionario("Carlão", "12345678900", "segurança", "R01")
func2 = Funcionario("Ana T", "98765432100", "cantora", "R02")   

fest.adicionar_funcionario(func1)
fest.adicionar_funcionario(func2)

print("Equipe do festival:")
fest.listar_equipe()

print("Informações do palco:")
print(fest.palco.resumo())
