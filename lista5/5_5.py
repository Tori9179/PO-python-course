lista = []
for i in range(100, 151):
    lista.append(i)
usuniete = 0
for i in range(1, len(lista) - 1):
    if i % 5 == 0:
        del lista[i - usuniete]
        usuniete += 1
print(lista)
