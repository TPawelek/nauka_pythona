def calculator(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/' and b != 0:
        return a/b
    return 0


if __name__ == '__main__':
    c = calculator(2, 4, '+')
    print(c)
    d = calculator(10, 0, '/')
    print(d)
