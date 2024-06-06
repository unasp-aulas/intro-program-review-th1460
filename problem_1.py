def main(cargo, salario):
    if cargo == "junior":
        novo_salario = salario * 1.1
    elif cargo == "pleno":
        novo_salario = salario * 1.2
    elif cargo == "senior":
        novo_salario = salario * 1.3
    else:
        novo_salario = -1
    return novo_salario