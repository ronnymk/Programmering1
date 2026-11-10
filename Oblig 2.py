#**Oppgave 1 - If og else**

# Oppgave 1 - If og else
# input() gir tekst, int() gjør det om til et heltall
tall = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall."))

# == sammenligner verdier, mens = gir en variabel en verdi
if tall == 42:
    print("Det stemmer, meningen med livet er 42!")
else:
    print("FEIL!")

if tall == 42:
    print("Det stemmer, meningen med livet er 42!")
# and: begge betingelsene må være sanne samtidig
elif tall > 30 and tall < 50:
    print("Nærme, men feil.")
else:
    print("FEIL!")