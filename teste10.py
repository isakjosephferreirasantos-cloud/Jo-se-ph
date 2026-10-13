secreto = 7
for t in range(1, 4):
 chute = int(input("chute: "))
 if chute == secreto:
  print("voce acertou!")
  break
 elif chute < secreto:
  print("tente um MAIOR!")
 else:
  print("tente um MENOR!")
  if chute != secreto:
   print("fim de jogo!")
