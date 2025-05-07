# Declaração dos valores dos produtos
produto1 = 50
produto2 = 120
produto3 = 200

# Variáveis dos produtos com 10% desconto
desconto_prod1 = produto1 - (produto1 * (10 / 100))
desconto_prod2 = produto2 - (produto2 * (10 / 100))
desconto_prod3 = produto3 - (produto3 * (10 / 100))

# Saída dos valores com desconto
print(f"-> PRODUTO 1 COM 10% DE DESCONTO: de R${produto1:.2f} para R${desconto_prod1:.2f}")
print(f"-> PRODUTO 2 COM 10% DE DESCONTO: de R${produto2:.2f} para R${desconto_prod2:.2f}")
print(f"-> PRODUTO 3 COM 10% DE DESCONTO: de R${produto3:.2f} para R${desconto_prod3:.2f}")