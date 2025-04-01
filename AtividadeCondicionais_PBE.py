## EXERCÍCIO 1

"""num = int(input("Insira um valor para verificar se é ímpar ou par: "))

if num % 2 == 0:
    print(f"{num} é par!")
else:
    print(f"{num} é ímpar!")"""

## EXERCÍCIO 2

"""num = int(input("Insira um número: "))

if num > 10:
    print(f"{num} é maior que 10")
else:
    print(f"{num} não é maior que 10")"""

## Exercício 3

"""idade = int(input("Digite a sua idade: "))

if idade >=18 18:
    print(f"Você é maior de idade")
else:
    print(f"Você é menor de idade")"""

## Exercício 4

"""idade = int(input("Digite a sua idade: "))

if idade >= 16:
    if idade >= 70 or idade < 18:
        print(f"Seu voto é: OPCIONAL")
    else:
        print(f"Seu voto é: OBRIGATÓRIO")
else:
    print(f"Seu voto é: NÃO VOTA")"""

## Exercício 5

"""num = int(input("Insira um número: "))

if num > 0:
    print(f"{num} é positivo!")
elif num < 0:
    print(f"{num} é negativo!")
else:
    print(f"{num} é igual a 0!")"""

## Exercício 6

"""nota = float(input("Insira uma nota: "))

if nota >= 9:
    print(f"Classificação de nota: A")
elif nota >= 7:
    print(f"Classificação de nota: B")
elif nota >= 5:
    print(f"Classificação de nota: C")
elif nota >= 3:
    print(f"Classificação de nota: D")
elif nota <=2:
    print(f"Classificação de nota: E")"""

## Exercício 7

"""idade = int(input("Digite a sua idade: "))

if idade >= 13 and idade < 60:
    print(f"Você não tem desconto")
else:
    print(f"Você tem desconto")"""

## Exercício 8

"""n1 = int(input("Insira o valor do primeiro lado: "))
n2 = int(input("Insira o valor do segundo lado: "))
n3 = int(input("Insira o valor do terceiro lado: "))

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    if n1 == n2 and n1 == n3:
        print(f"Os lados indicam um triângulo equilátero!")
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print(f"Os lados indicam um triângulo escaleno!")
    else:
        print(f"Os lados indicam um triângulo isóceles")
else:
    print(f"Os lados não indicam um triângulo")"""

## Exercício 9

"""total = float(input("Insira o valor total da compra: "))

if total >= 500:
    desc = (total * 15) / 100
    final = total - desc
    print(f"O valor com desconto é de: R${final}")
elif total < 500:
    if total >= 100:
        desc = (total * 10) / 100
        final = total - desc
        print(f"O valor com desconto é de: R${final}")
    else:
        desc = (total * 5) / 100
        final = total - desc
        print(f"O valor com desconto é de: R${final}")"""

## Exercício 10

"""ano = int(input("Digite um ano: "))

if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 4 != 0) and (ano % 400 == 0)) or ((ano % 4 == 0) and (ano % 400 == 0)):
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")"""

## Exercício 11

"""peso = float(input("Insira o seu peso (kg): "))
altura = float(input("Insira sua altura (m): "))

imc = peso / altura ** 2

if imc >= 30:
    print(f"Resultado: Obesidade")
elif imc >= 25:
    print(f"Resultado: Sobrepeso")
elif imc >= 18.5:
    print(f"Resultado: Peso Normal")
else:
    print(f"Resultado: Abaixo do Peso")"""

## Exercício 12

"""num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 == num2 and num1 == num3 and num2 == num3:
    print("Ordem dos números: Iguais")
elif num1 > num2 and num1 > num3 and num2 > num3:
    print("Ordem dos números: Crescente")
elif num1 < num2 and num1 < num3 and num2 < num3:
    print("Ordem dos números: Decrescente")
else:
    print("Ordem dos números: Desordenado")"""

## Exercício 13

"""temp = float(input("Insira a temperatura atual (em Cº): "))

if temp > 40:
    print(f"Clima: Muito Quente")
elif temp >= 25:
    print(f"Clima: Quente")
elif temp >= 10:
    print(f"Clima: Aconchegante")
else:
    print("Clima: Frio")"""

## Exercício 14

"""from datetime import date, datetime

data = input("Insira uma data no formato (dd/mm/aaaa): ")

dataFormatada = datetime.strptime(data, '%d/%m/%Y').date()

print(data)
print(dataFormatada)
"""
## Exercício 15

# Bilioteca RE https://blog.rocketseat.com.br/untitled-2/ https://awari.com.br/funcao-len-python-como-usar-a-funcao-len-para-contar-caracteres-em-python/ 

## Exercício 16
"""import math

print("--> CALCULADORA DE RAÍZ QUADRADA <--\n")
radic = float(input("Insira o radicando(número): "))

if radic < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo")
elif radic > 100:
    print("Número muito grande, reduza para um valor abaixo de 100")
else:
    raiz = math.sqrt(radic)
    raiz_formatada = "%.2f" % raiz
    print("A raíz de {radic} é: ",raiz_formatada)"""

## Exercício 17
from datetime import date, datetime

data = input("Insira uma data no formato (dd/mm/aaaa): ")
dataFormatada = datetime.strptime(data, '%d/%m/%Y').date()
print(data)
print(dataFormatada)


