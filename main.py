# 1. proměnná pro jméno
jmeno = "Kvido"

# 2. proměnná pro příjmení
prijmeni = "Šamša"

# 3. Výpis obou proměnných
print(jmeno)
print(prijmeni)

# 4. Vytvoření vstupu pro uživatele
vek = input("Zadejte svůj věk (pouze čísla):")

# 9. Kontrola zda je zadána pouze celočíselná hodnota
if vek.isdigit():
    vek = int(vek)  # převedeme vstup na celé číslo
    print("Děkuji")
else:
    print("Zadej jen celočíselnou hodnotu.")
          
# 5. Výpis délky jména a příjmení
print("délka jména: ", len(jmeno))
print("délka příjmení: ", len(prijmeni))

# 6. Vytvoření proměnné s hodnotou 6
cislo = 6

# 7. Vytvoření cyklu který se opakuje 5x
for i in range(5):
    cislo = cislo + 3  # Přičítání 3

# 8. Výsledek cyklu
print("toto je výsledek cyklu s cislem 6: ", cislo)

import random  # pro generování náhodných čísel

# 10. Vytvoření proměnné s náhodnou hodnotou od 1 do 10
nahodne_cislo = random.randint(1, 10)

# Výpis náhodné hodnoty do konzole
print("Náhodné číslo mezi 1 a 10 je:", nahodne_cislo)

