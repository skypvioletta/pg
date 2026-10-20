def je_prvocislo(cislo):
    """
    Funkce ověří, zda zadané číslo je nebo není prvočíslo a vrátí True nebo False.

    Prvočíslo je takové číslo větší než 1, které není dělitelné žádným jiným
    číslem než 1 a samo sebou.
    """
    if cislo <= 1:
        return False
    if cislo <= 3:
        return True
    if cislo % 2 == 0:
        return False

    for delitel in range(3, int(cislo ** 0.5) + 1, 2):
        if cislo % delitel == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    maximum = int(maximum)
    seznam = []

    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            seznam.append(cislo)

    return seznam


if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
