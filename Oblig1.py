#Oppgave 1 – Hello World

print("Hello World")

#**Oppgave 2 - Navn:**

fornavn = "Kari"
etternavn = "nordmann"
alder = 30

print(f"Hei, jeg heter {fornavn} {etternavn} og er {alder} år gammel.")

#Oppgave 3 - Operatorer

# input() gir tekst, float() gjør det om til et tall (godtar også 2.5)
tall1 = float(input("Skriv inn forste tall: "))
tall2 = float(input("Skriv inn andre tall: "))

print(f"{tall1} * {tall2} = {tall1 * tall2}")
print(f"{tall1} / {tall2} = {tall1 / tall2}")
print(f"{tall1} + {tall2} = {tall1 + tall2}")
print(f"{tall1} - {tall2} = {tall1 - tall2}")
print(f"{tall1} % {tall2} = {tall1 % tall2}")
print(f"{tall1} ** {tall2} = {tall1 ** tall2}")
print(f"{tall1} // {tall2} = {tall1 // tall2}")

if tall2 == 0:
    print("Kan ikke dele på 0")
else:
    print(f"{tall1} / {tall2} = {tall1 / tall2}")
    print(f"{tall1} % {tall2} = {tall1 % tall2}")
    print(f"{tall1} // {tall2} = {tall1 // tall2}")

#**Oppgave 4 - Regnestykker:**

#Lag tre variabler a = 6, b = 3, c = 2.
#Lag et program som regner ut resultatene av følgende regnestykker og skriver ut svaret.

# Oppgave 4 - Regnestykker
# Variablene oppgaven gir
a = 6
b = 3
c = 2

# Gange regnes før pluss: 3 * 2 = 6, så 6 + 6 = 12
print(f"a) a + b * c = {a + b * c}")

# Parentesen regnes først: 6 + 3 = 9, så 9 * 2 = 18
print(f"b) (a + b) * c = {(a + b) * c}")

# Regnes fra venstre: 6 / 3 = 2.0, så 2.0 / 2 = 1.0
print(f"c) a / b / c = {a / b / c}")

# Parentesen regnes først: 3 / 2 = 1.5, så 6 / 1.5 = 4.0
print(f"d) a / (b / c) = {a / (b / c)}")

#**Oppgave 5 - Småkaker:**
# Oppgave 5 - Småkaker
# Antall småkaker hver person har spist (person 3 har spist 2.5, så noen verdier er float)
person1 = 5
person2 = 9
person3 = 2.5
person4 = 21
person5 = 0

# Egen variabel for antall personer, slik oppgaven foreslår
antall_personer = 5

# Totalt antall kaker: 5 + 9 + 2.5 + 21 + 0 = 37.5
totalt = person1 + person2 + person3 + person4 + person5

# Gjennomsnitt: 37.5 / 5 = 7.5
gjennomsnitt = totalt / antall_personer

# int() fjerner desimaldelen, så 7.5 blir 7
print(f"Gjennomsnittlig antall spiste småkaker: {int(gjennomsnitt)}")