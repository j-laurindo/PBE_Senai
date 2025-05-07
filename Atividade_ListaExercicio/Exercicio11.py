# Declaração dos valores de cada frase
frase1 = "Ana Ana"
frase2 = "1DSTB-SENAI"
frase3 = "Subi no Ônibus"

# Formatação de cada frase para a verificação de parâmetros
frase_formatacao1 = frase1.replace(" ","").replace("-","").lower()
frase_formatacao2 = frase2.replace(" ","").replace("-","").lower()
frase_formatacao3 = frase3.replace(" ","").replace("-","").replace("Ô","O").lower()

# Condicional que verifica os parâmetros entre a frase formatada(original) e a frase invertida(slice)
if frase_formatacao1[::-1] == frase_formatacao1:
    print(f"-> {frase1} é um palíndromo!")
else:
    print(f"-> {frase1} não é um palíndromo!")

if frase_formatacao2[::-1] == frase_formatacao2:
    print(f"-> {frase2} é um palíndromo!")
else:
    print(f"-> {frase2} não é um palíndromo!")

if frase_formatacao3[::-1] == frase_formatacao3:
    print(f"-> {frase3} é um palíndromo!")
else:
    print(f"-> {frase3} não é um palíndromo!")