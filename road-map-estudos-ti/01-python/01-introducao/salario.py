salario = float(input("Digite o salário: "))
porcentagem = 0.10

def calcula_porcentagem(x: float, y: float) -> float:
    print(f"Calculando {y * 100}% de {x}")
    return x * y
    


def adiciona_aumento(x: float, y: float) -> float:
    print(f"Adicionando aumento de {y * 100}% ao salário de {x}")
    return x + calcula_porcentagem(x, y)

print(f"Salário com aumento: {adiciona_aumento(salario, porcentagem)}")
