def is_fraction_expression(expression):
    if expression.count("/") == 1:
        values = expression.split("/")
        if values[0].isdigit() and values[1].isdigit():
            if int(values[1]) != 0:
                return True
    return False


def gcd(a, b):
    while a % b != 0:
        modulo = a % b
        a = b
        b = modulo
    return b


while True:
    expression = input("Kérem adja meg az egyszerüsíteni kívánt tört kifejezést (vagy 'q' a kilépéshez): ")

    if expression == 'q':
        break

    if is_fraction_expression(expression):
        numerator, denominator = map(int, expression.split("/"))
        
        common_divider = gcd(numerator, denominator)

        if common_divider > 1:
            numerator = numerator // common_divider
            denominator = denominator // common_divider
            if denominator == 1:
                print(f"Egyszerüsített alak: {numerator}/{denominator} ==> {numerator}")
            else:
                print(f"Egyszerüsített alak: {numerator}/{denominator}")
        else:
            print("A tört nem egyszerüsíthető tovább!")
    else:
        print("Kérem tört kifejezést adjon meg! Például: 20/5")