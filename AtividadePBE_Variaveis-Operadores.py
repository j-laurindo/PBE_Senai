## Exercicio 1
"""
nome = "João"
print(dobro)
"""

## Exercicio 2
"""
a = 5
b = 10


print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""

## Exercicio 3
"""
valor = 50
desc = 10

ValTotal = 50 - 10

print(ValTotal)
"""

## Exercicio 4
"""
resultado = 10 + 5 * 2
print(resultado)
"""

## Exercicio 5
"""
texto = str(150)
numero = int(str(150))
print(2 * numero)
"""

## Exercício 7

"""
a = int(input("Insira um primeiro valor: "))
b = int(input("Insira um segundo valor: "))

resultado = a + b

print(f"O resultado é igual a: ", resultado)
"""

## Exercício 8

"""
x = float(input("Insira um número: "))
y = float(input("Insira outro número: "))

result = x // y

print(f"O resultado da divisão entre {x} e {y} é: ", result)
"""

## Exercício 9

"""
num1 = int(input("Insira um primeiro número: "))
num2 = int(input("Insira um segundo número: "))

result = num1 > num2

print(f"True - num1 é maior que num2    |   False - num1 é menor que num2: ", result)
"""

## Exercício 10

"""
idade = int(input("Insira a sua idade: "))

calculo = idade * 365

print(f"Você já viveu {calculo} dias!")
"""

## Exercício 11
"""
base = int(input("Insira o valor da base: "))
expoente = int(input("Insira o valor do expoente: "))

result = base ** expoente

print(f"O resultado da potência é: ", result)
"""

## Exercício 12

"""
preco = float(input("Insira um valor/preço: "))
str(preco)

print(f"O precço é R$", str(preco))
"""

## Exercício 13

"""
raio = float(input("Insira o valor de um raio (do círculo): "))

result = 3.14 * (raio ** 2)

print(f"A área do círculo é igual à:", result)
"""

## Exercício 14

"""
a = int(input("Insira um primerio valor: "))
b = int(input("Insira um segundo valor: "))

a,b = b, a

print(f"Valor 1: {a} | Valor 2: {b}")
"""

## Exercício 15

"""
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 * 2) + (nota2 * 3) + (nota3 * 5) / (2 + 3 + 5)

print(f"A média ponderada dessas notas é:", media)
"""

## Exercício 16 - DESAFIO
"""
import math

x1 = float(input("Insira o primeiro ponto x: "))
y1 = float(input("Insira o primeiro ponto y:  "))
x2 = float(input("Insira o segundo ponto x: "))
y2 = float(input("Insira o segundo ponto y:  "))

result = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(f"O resultado da distância desses pontos é: ", result)
"""