valor_casa = float(input("Qual o valor da casa? ")) # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar
mensal = valor_casa / (anos_pagar * 12)
if mensal <= salario * 0.3:
    print("Aprovado")
else:
    print("Desaprovado")