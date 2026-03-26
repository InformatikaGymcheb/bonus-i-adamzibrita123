# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:
cislo += 10
print(f"Váš výsledek je {cislo}")


# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():
total = celkem * lidi
print(f"Celková útrata je {round(total, 2)}")


# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
plocha = 3.14 * r * r
print(f"Plocha kruhu je {round(plocha)}")
