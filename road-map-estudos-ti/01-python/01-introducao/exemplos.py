nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))

novo_salario = salario * 0.10

print()
print(f"Olá, {nome}!")
print(f"Você tem {idade} anos.")
print(f"Seu novo salário será R$ {novo_salario:.2f}")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")