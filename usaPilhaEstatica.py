import PilhaEstatica

p = PilhaEstatica.PilhaEstatica()

p.push("A")
p.push("B")
p.push("C")
p.push("D")
p.push("E")
p.show()
print()
print(p.getTopo())
print(p.estaVazia())
print(p.estaCheia())
