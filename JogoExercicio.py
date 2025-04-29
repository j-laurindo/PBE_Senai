import random

itens = {
    "1" : {"Nome": "Poção de Força", "Efeito": "Ataque+20", "turnos": 2},
    "2" : {"Nome": "Bola de Fogo", "Efeito": "Danos explosivos no inimigo", "turnos": 1},
}
duracao_item_jogador = 0
duracao_item_robo = 0
item_jogador = ""
item_robo = ""

itens_gastos_jogador = []
itens_gastos_robo = []

efeitos = {
    "jogador" :
    "robo" :
}

while True:
    print("----JOGO RPG----")
    print("1. Iniciar o jogo")
    print("2. Multiplayer")
    print("3. Sair")
    opcao = input("Escolha: ")

    if opcao == "2":
        multiplayer = True
    else:
        multiplayer = False

    if opcao == "3":
        break
    elif opcao == "1" or opcao == "2":
        # Declarou as variáveis dos ataques e defesas
        hp = random.randint(200,1000)
        ataque_jogador = random.randint(1,50)
        ataque_robo = random.randint(1,50)
        defesa_robo = random.randint(1,ataque_jogador-1)
        defesa_jogador = random.randint(1,ataque_robo-1)

        # Dicionario de cada jogador
        jogador = {
            "hp" : hp,
            "ataque" : ataque_jogador,
            "defesa" : defesa_jogador
        }

        robo = {
            "hp" : hp,
            "ataque" : ataque_robo,
            "defesa" : defesa_robo
        }

        while jogador['hp'] > 0 and robo['hp'] > 0:
            print(f"Seu HP: {jogador['hp']}")
            print(f"Seu Ataque: {jogador['ataque']}")
            print(f"Sua Defesa: {jogador['hp']}")
            print(f"HP: {robo['hp']}")

            acao= input('[1] Atacar  [2] Curar  [3] Itens')

            if acao == "1":
                dano = max(0, jogador['ataque'] - robo['defesa'])
                # Critico
                if random.random() < 0.1:
                    dano *= 2
                    print("Você causou dano crítico!")
                robo['hp'] -= dano
                print(f"Você causou {dano} de dano!")
                print(f"Deixando o inimigo com {robo['hp']} de vida")
            elif acao == "2":
                cura = 20
                if cura + jogador['hp'] > hp:
                    jogador['hp'] = hp
                else:
                    jogador['hp'] += cura
            elif acao == "3":
                print("Itens disponíveis: ")
                for chave, valor in itens.items():
                    print(f"[{chave}] {valor['Nome']} - {valor['Efeito']}")
                escolha_item = input("Escolha seu item: ")
                if escolha_item == "1" and "1" not in itens_gastos_jogador:
                    jogador['ataque'] += 20
                    duracao_item_jogador = 2
                    item_jogador = "1"
                    itens_gastos_jogador.append("1")
                elif escolha_item == "2" and "2" not in itens_gastos_jogador:
                    robo['hp'] -= 50
                    duracao_item_jogador = 1
                    itens_gastos_jogador.append("2")
            elif acao == "4":
                status = ""
                print("""wewewe
                wewewe
                wewewewe
                wewewew""")

            if duracao_item_jogador > 0:
                duracao_item_jogador -= 1
            elif item_jogador == "1":
                jogador['ataque'] -= 20
                item_jogador = ""

            if robo['hp'] <= 0:
                print("Você venceu!")
                break

            if multiplayer:
                acao = input('[1] Atacar  ou  [2] Curar')
            else:
                acao = random.choices(["1", "2"])

            if acao == "1":
                dano = max(0, robo['ataque'] - jogador['defesa'])
                # Critico
                if random.random() < 0.1:
                    dano *= 2
                    print("Você causou dano crítico!")
                jogador['hp'] -= dano
                print(f"Você sofreu {dano} de dano!")
                print(f"Ficando com {jogador['hp']} de vida!")
            else:
                cura = 20
                robo['hp'] = min(hp,robo['hp'] + cura)
                print(f"O robo foi curado com {robo['hp']} de vida")

            if jogador['hp'] <= 0:
                print("Você perdeu!")
                break