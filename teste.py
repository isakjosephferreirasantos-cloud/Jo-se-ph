preco = float(input("digite seu precor$: "))
def calcular_desconto(preco, pct=0.1):
 valor_desconto=preco*pct
 preco_final = preco - valor_desconto
 return preco_final
resultado = calcular_desconto(100.0)
print(f"valor: r${resultado:.2f}")