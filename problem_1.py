def main(cargo, salario):
    if cargo == "junior":
        novo_salario = salario * 1.15
    elif cargo == "pleno":
        novo_salario = salario * 1.26
    elif cargo == "senior":
        novo_salario = salario * 1.34
    else:
        novo_salario = -1
    return novo_salario