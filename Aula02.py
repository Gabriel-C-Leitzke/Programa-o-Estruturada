# Exercício 1
n=float(input("Digite o 1º número: "))
n2=float(input("Digite o 2º número: "))

if n>n2 :
    print ("O 1º número é o maior!")
elif n==n2:
    print ("Os números são iguais!")
else:
    print ("O 2º número é maior!")
    

# Exercício 2
n = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

if n == n2:
    print("Os números são iguais!")
else:
    print("Os números são diferentes!")

# Exercício 3
n = float(input("Digite um número: "))
if n > 0:
    print("O número é positivo!")
elif n < 0:
    print("O número é negativo!")
else:
    print("O número é zero!")

# Exercício 4
n = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
if n + n2 > 10:
    print("A soma é maior que 10!")
else:
    print("A soma não é maior que 10!")

# Exercício 5
n = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
if n < n2 and n > n3:
    print("O primeiro número é menor que o segundo e maior que o terceiro!")
else:
    print("As condições não foram atendidas!")

# Exercício 6
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Exercício 7
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Exercício 8
n = int(input("Digite um número: "))
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Zero")

# Exercício 9
letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")

# Exercício 10
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
if n1 > n2:
    print(n1, "é o maior número")
elif n2 > n1:
    print(n2, "é o maior número")
else:
    print("Números iguais")

# Exercício 11
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
if n1 > 0 and n2 > 0:
    print("Ambos são positivos")
else:
    print("Nem ambos são positivos")

# Exercício 12
n = float(input("Digite um número: "))
if n > 10 and n < 20:
    print("O número está entre 10 e 20")
else:
    print("O número não está entre 10 e 20")

# Exercício 13
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
if n1 != n2 and n1 != n3 and n2 != n3:
    print("Todos são diferentes")
else:
    print("Nem todos são diferentes")

# Exercício 14
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
if (n1 == 0 or n2 == 0) and (n1 + n2 > 10):
    print("Um dos números é zero e a soma é maior que 10")
else:
    print("Condições não atendidas")

# Exercício 15
letra = input("Digite uma letra: ")
if letra in "AEIOU" and letra.isupper():
    print("É uma vogal maiúscula")
else:
    print("Não é vogal maiúscula")