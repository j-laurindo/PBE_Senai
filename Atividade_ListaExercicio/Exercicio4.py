primeira_jogada = 4
segunda_jogada = 7
terceira_jogada = 10
contador = 0

print("== PRIMEIRA JOGADA ==")
if primeira_jogada % 2 == 0:
    print("Você avançou uma casa! :D")
    contador = contador + 1
else:
    print("Você recuou uma casa! :(")
    contador = 0

print("\n== SEGUNDA JOGADA ==")
if segunda_jogada % 2 == 0:
    print("Você avançou uma casa! :D")
    contador = contador + 1
else:
    print("Você recuou uma casa! :(")
    contador = contador - 1

print("\n== TERCEIRA JOGADA ==")
if terceira_jogada % 2 == 0:
    print("Você avançou uma casa! :D")
    contador = contador + 1
else:
    print("Você recuou uma casa! :(")
    contador = contador - 1
    
print(f"\n> Ao total, você avançou {contador} casa(s) nessa partida!")
