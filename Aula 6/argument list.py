def Churrascaria(pontoCarne, *arguments, **keywords):
    print("Voces servem carne", pontoCarne, "?")
    print("Sim, servimos em qualquer ponto, inclusive")
    print("Que pecas de carne voces possuem?")
    print("Possuimos as seguintes")
    for arg in arguments:
        print(arg)

    print("E como voces classificam essas carnes?")
    keys = sorted(keywords)
    for key in keys:
        print(keywords[key], "eh ", key)

Churrascaria("ao ponto", "Picanha", "Alcatra", "Javali", nobre = "Picanha", normal = "Alcatra", ruim = "Javali")