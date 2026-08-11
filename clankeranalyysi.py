from collections import Counter

while True:
    tiedoston_nimi = input("Anna tekstitiedoston nimi: ")

    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            teksti = tiedosto.read()
        break
    except FileNotFoundError:
        print("Tiedostoa ei löydy")

# Merkkien määrä
merkkien_maara = len(teksti)
print(f"Tekstissä on {merkkien_maara} merkkiä.")

# Sanojen määrä
sanat = teksti.split()
sanojen_maara = len(sanat)
print(f"Tekstissä on {sanojen_maara} sanaa.")

# 5 yleisintä sanaa
sanat_pienilla = [sana.lower() for sana in sanat]
yleisimmat_sanat = Counter(sanat_pienilla).most_common(5)

sanat_lista = [sana for sana, maara in yleisimmat_sanat]

if len(sanat_lista) > 1:
    sanat_teksti = ", ".join(sanat_lista[:-1]) + " ja " + sanat_lista[-1]
else:
    sanat_teksti = sanat_lista[0]

print(f"Yleisimmät sanat ovat {sanat_teksti}.")

# 5 yleisintä merkkiä, välilyönnit pois
merkit = [merkki.lower() for merkki in teksti if not merkki.isspace()]
yleisimmat_merkit = Counter(merkit).most_common(5)

merkit_lista = [merkki for merkki, maara in yleisimmat_merkit]

if len(merkit_lista) > 1:
    merkit_teksti = ", ".join(merkit_lista[:-1]) + " ja " + merkit_lista[-1]
else:
    merkit_teksti = merkit_lista[0]

print(f"Yleisimmät merkit ovat {merkit_teksti}.")