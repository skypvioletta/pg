def je_prvocislo(cislo):
    """
    Funkce ověří, zda zadané číslo je nebo není prvočíslo a vrátí True nebo False.

    Prvočíslo je takové číslo větší než 1, které není dělitelné žádným jiným
    číslem než 1 a samo sebou.
    """
   if cislo < 2:
        return False

    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum
    a vrati je jako seznam.
    """
    maximum = int(maximum)
    prvocisla = []

    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)

    return prvocisla


if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
