# Exercício 1
nome_funcionario = "Pyetro"
idade = 18
salario = 3000.00
cargo = "Analista de Dados"
turno = "matutino"
setor = "RH"

# Exercício 2
nome_escola = "Escola Estadual De Cruzeiro do Oeste"
estado = "Paraná"
numero_professores = 15
cidade = "Cruzeiro do Oeste"
numero_militares = 4
logradouro = "Rua das Escolas"
numero_endereco = 123
numero_alunos = 1000
colegio_militar = True
disciplinas = ["Matemática", "Português", "História", "Ciências"]

# Exercício 3
valor1 = 10
valor2 = 5
valor3 = "2"
valor4 = 8
valor5 = -5

print(valor1 + valor2)
print(valor1 + valor2 + valor4)
print(valor1 + valor2 - valor5)
print(valor1 + int(valor3))
print(valor1 * valor2)
print((valor4 * valor2) / 2)
print((valor1 + valor2 + valor4 + valor5) / 4)

# Exercício 4
v1 = 2
v2 = 3
v3 = 5
v4 = 6

soma_valores = v1 + v2 + v3 + v4
media_valores = soma_valores / 4

print("Soma dos valores:", soma_valores)
print("Média dos valores:", media_valores)

# Exercício 5
nota1 = 64
nota2 = 45
nota3 = 60

media_notas = (nota1 + nota2 + nota3) / 3

if media_notas >= 60:
    print("Aprovado")
else:
    print("Reprovado")

# Exercício 6
certificado = False

if media_notas >= 60:
    if nota1 >= 60 and nota2 >= 60 and nota3 >= 60:
        certificado = True

if certificado:
    print("Aluno foi aprovado com certificado")
elif media_notas >= 60:
    print("Aluno apenas aprovado")
else:
    print("Aluno reprovado")
