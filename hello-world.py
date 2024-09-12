import random

def hadani_cisla():
    print("Vítej ve hře 'Hádej číslo'!")
    print("Myslím si číslo mezi 1 a 100.")
    
    # Počítač náhodně vybere číslo
    tajne_cislo = random.randint(1, 100)
    
    pokusy = 0
    while True:
        # Hráč zadá číslo
        hadani = input("Hádej číslo: ")

        # Ošetření chybného vstupu
        try:
            hadani = int(hadani)
        except ValueError:
            print("Prosím, zadej platné číslo.")
            continue

        pokusy += 1

        # Porovnání čísla
        if hadani < tajne_cislo:
            print("Moje číslo je větší.")
        elif hadani > tajne_cislo:
            print("Moje číslo je menší.")
        else:
            print(f"Gratuluji! Uhodl jsi správné číslo {tajne_cislo} za {pokusy} pokusů.")
            break

# Spuštění hry
if __name__ == "__main__":
    hadani_cisla()
