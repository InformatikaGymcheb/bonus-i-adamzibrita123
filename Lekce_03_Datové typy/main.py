# ÚLOHA 1: Sčítací past (Cíl: 5 + 3 = 8)
# ---------------------------------------------------------
x = int(input("Zadej první číslo: "))
y = int(input("Zadej druhé číslo: "))

print(f"Výsledek je: {x+y}")
print()

# ÚLOHA 2: Opakovač jména (Cíl: "Honza" a 3 -> "HonzaHonzaHonza")
# ---------------------------------------------------------
jmeno = input("Zadej jméno: ")
pocet = int(input("Zadej počet opakování: "))

print(jmeno * pocet)
print()

# ÚLOHA 3: Rok narození (Cíl: 2026 - věk)
# ---------------------------------------------------------
vek = int(input("Zadej svůj věk: "))
rok = 2026
print(f"Váš přibližný rok narození je {rok - vek}")
print()

# ÚLOHA 4: Výplata (Cíl: mzda * hodiny)
# ---------------------------------------------------------
mzda = int(input("Zadej svou hodinovou mzdu: "))
pocetHodin = int(input("Zadej počet odpracovaných hodin: "))
print(f"Vaše celková odměna je {mzda * pocetHodin} Kč")
print()

# ÚLOHA 5: Magická matematika (Cíl: (x + 10) * 2)
# ---------------------------------------------------------
cislo = int(input("Zadej své číslo: "))
print(f"Výsledek je: {(cislo + 10) * 2}")
