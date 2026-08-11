c = 0
i = 0
from collections import Counter
while i == 0:
    avaatiedosto = input("Anna tekstitiedoston nimi: ")
    try:
        with open(avaatiedosto, "r") as f:
            teksti = f.readlines()
            print("1. Merkkien määrä")
            print("2. Sanojen määrä")
            print("3. Yleisimmät sanat")
            print("4. Yleisimmät merkit")
            valinta = input("Valitse näistä: ")
            if valinta == "1":
                for text in teksti:
                    c += sum(1 for z in text if z not in (" ", "\n"))
                print("Merkkien määrä:", c)
                i += 1
            if valinta == "2":
                for text in teksti:
                    c += len(text.split())
                print("Sanojen määrä:", c)
            if valinta == "3":
                count = Counter(text for rivi in teksti for text in rivi.split())
                print(count.most_common(5))
            if valinta == "4":
                for text in teksti:
                    for z in text:
                        count = Counter(z for plong in text for z in plong.split())
                print(count.most_common(5))
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")