n = 1
soma = 0
while True:
    x = int(input(f"Digite o {n} número: "))
    if x == 0:
        break
    soma += x
    n += 1
print(soma)