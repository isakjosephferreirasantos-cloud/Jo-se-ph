def analisar_notas(notas):
    media = sum(notas) / len(notas)
    acima = []
    for n in notas:
        if n > media:
            acima.append(n)

    aprovados = 0
    for n in notas:
        if n >= 7.0:
            aprovados += 1

    return media, acima, aprovados


dados = [5.5, 8.0, 9.5, 6.0, 7.5, 4.0]
media, acima, aprovados = analisar_notas(dados)
print(f"media: {media:.2f}")
print(f"notas acima da media: {acima}")
print(f"quantidade de aprovados: {aprovados}")