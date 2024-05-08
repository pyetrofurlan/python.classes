# Exercício 1:
nome = "Maria"
idade = 28
sexo = "Feminino"
status = "Solteira"


print("Nome:", nome)
print("Idade:", idade)
print("Sexo:", sexo)
print("Status:", status)

# Exercício 2:
nome = "João"
idade = 35
sexo = "Masculino"
status = "Casado"

print(f"Nome: {nome}, Idade: {idade}, Sexo: {sexo}, Status: {status}")

# Exercício 3:
nome = "Maria"
sobrenome = "Silva"

nomeCompleto = nome + " " + sobrenome

print("Nome Completo:", nomeCompleto)

# Exercício 4:
nome1 = "João"
nome2 = "Maria"
sobrenome1 = "Silva"
sobrenome2 = "Santos"

nomeCompleto1 = nome1 + " " + sobrenome1
nomeCompleto2 = nome2 + " " + sobrenome2

print("Nome Completo 1:", nomeCompleto1)
print("Nome Completo 2:", nomeCompleto2)

# Exercício 5:
alunos = ["João", "Maria", "Pedro", "Gabriel"]

notas = [8.5, 7.9, 6.3, 9.0]

print("Lista de Alunos:", alunos)
print("Lista de Notas:", notas)

# Exercício 6:
alunos = ["João", "Maria", "Pedro", "Ana"]
notas = [8.5, 7.9, 6.3, 9.0]

print("Alunos e suas respectivas notas:")
for aluno, nota in zip(alunos, notas):
    print(f"Aluno: {aluno}, Nota: {nota}")

# Exercício 7:
num1 = 5
num2 = 10

soma = num1 + num2

subtracao = num1 - num2

multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero."

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
