# Dicionário de classificação de cada nível de dificuldade do RPG
classificacoes = {
    "1" : {
        "Dificuldade" : "Pequeno",
        "Valor" : 3
    },
    "2" : {
        "Dificuldade" : "Médio",
        "Valor" : 9
    },
    "3" : {
        "Dificuldade" : "Grande",
        "Valor" : 12
    }
} 

# Saída dos itens do dicionário (dificuldade e valor)
print("---------- RPG ----------")
for dicionario, dados in classificacoes.items():
    print(f"Dificuldade: {dados['Dificuldade']}")
    print(f"Valor: {dados['Valor']}\n")
