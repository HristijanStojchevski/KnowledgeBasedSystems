__operators = ('+', '-', '/', '//', '*', '**', '%')


def calculator():
    x = eval(input())
    operator = input()
    y = eval(input())

    # print(str(x) + operator + str(y))

    # your code here
    rezultat = 0
    if operator in __operators:
        if operator == '+':
            rezultat = x + y
        if operator == '-':
            rezultat = x - y
        if operator == '/':
            rezultat = x/y
        if operator == '//':
            rezultat = x//y
        if operator == '*':
            rezultat = x*y
        if operator == '**':
            rezultat = x**y
        if operator == '%':
            rezultat = x%y
        print(rezultat)
        return
    print("greshka")

if __name__ == "__main__":
    calculator()