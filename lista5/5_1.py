l = [4, "alfa", 2.75, "pies"]
print(l[1], l[-1], l[-2])
print("program wyswietla po wpisaniu liczby calkowitej element odpowiadajacy indeksowi elementu z listy, a gdy podajemy ujemna to jest to liczone od konca, nie mozna wyjsc poza zakres")
l2 = l
print(l)
print(l2)
l2[0] = 7
print(l)
print(l2)
l3 = l.copy()
l3[0] = 2
print(l)
print(l3)
