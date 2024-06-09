def main(dist):
    if dist <= 200:
        preco = dist * 0.5
    elif (dist > 200) & (dist <= 400):
        preco = dist * 0.45
    elif dist > 400:
        preco = dist * 0.35
    return preco