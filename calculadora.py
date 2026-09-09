def calc(a, b, op):
    if op == "soma":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mult":
        return a * b
    elif op == "div":
        return a / b if b != 0 else "Erro: divisão por zero"
    elif op == "pot":
        return a ** b


if __name__ == "__main__":
    print(calc(10, 5, "soma"))
    print(calc(10, 5, "sub"))
    print(calc(10, 5, "mult"))
    print(calc(10, 5, "div"))
    print(calc(10, 0 ,"div"))
    print(calc(5, 2 ,"pot"))