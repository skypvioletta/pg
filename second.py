def cislo_text(cislo):
    cislo = int(cislo)

    if not 0 <= cislo <= 100:
        raise ValueError("Číslo musí být v rozmezí od 0 do 100.")

    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři", "pět",
        "šest", "sedm", "osm", "devět"
    ]

    nacta = {
        10: "deset",
        11: "jedenáct",
        12: "dvanáct",
        13: "třináct",
        14: "čtrnáct",
        15: "patnáct",
        16: "šestnáct",
        17: "sedmnáct",
        18: "osmnáct",
        19: "devatenáct"
    }

    desitky = {
        2: "dvacet",
        3: "třicet",
        4: "čtyřicet",
        5: "padesát",
        6: "šedesát",
        7: "sedmdesát",
        8: "osmdesát",
        9: "devadesát"
    }

    if cislo < 10:
        return jednotky[cislo]
    if cislo < 20:
        return nacta[cislo]
    if cislo < 100:
        deset = cislo // 10
        jednotka = cislo % 10

        if jednotka == 0:
            return desitky[deset]
        return f"{desitky[deset]} {jednotky[jednotka]}"

    return "sto"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
