
# vraag de gebruiker het tempo en de maatsoort
def choose_settings():
    # BPM kiezen
    while True:
        try:
            bpm = int(input("Kies tempo in BPM (40–240): "))
            if 40 <= bpm <= 240:
                print(f"Gekozen BPM: {bpm}")
                break
            else:
                print("BPM moet tussen 40 en 240 liggen.")
        except ValueError:
            print("Typ een getal, geen tekst.")

    # maatsoort kiezen
    while True:
        choice = input("Kies maatsoort (5 of 7): ")
        if choice in ("5", "7"):
            numerator = int(choice)
            break
        else:
            print("Ongeldige invoer. Typ '5' of '7'. Probeer opnieuw.")

    denominatorDur = 60 / bpm
    def totalDuration(numerator, denominatorDur):
        totalDur = numerator * denominatorDur
        return totalDur
    
    print(f"Gekozen maat: {numerator}/4  → totale duur = {totalDuration(numerator, denominatorDur)} seconds")

    return numerator, bpm, totalDuration(numerator, denominatorDur)
