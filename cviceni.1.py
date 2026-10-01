def add(a, b):
    c = a + b
    return c 

def mul(a, b, c):
    vysledek = a * b * c
    return vysledek

def div(a, b): 
    if b == 0: 
        # prvni cast, by b je 0
        vysledek = 0
    else:
        # druha cast, by b je  nenulove
        vysledek = a / b
    return vysledek

def je_delitelne_beze_zbytku(a, b):
    x = a % b 
    if x == 0:
        return f"{a}je delitelne beze zbytku{b}"
    else:
        return f"{a}neni delitelne beze zbytku{b}"

def je_delitelne_3(a):
    return je_delitelne_beze_zbytku(a, 3)


if __name__ == "__main__": 
    # x = add(1, 2)
    # x = mul(100, 2, 3)
    # x = div(10, 1) 
    # vysledek = je_delitelne_beze_zbytku(10, 5)
    vysledek = je_delitelne_3(9)
    print(vysledek)
