# Jeldrik Hemme
# ETS 2021
# 08.12.2021

# Hardware: es wird keine Hardware benötigt
# Sodtware: es wird keine zusätzliche Software benötigt 
# Version: 0.1

erste_zahl = (int(input('Bitte eine Zahl eingeben:')))
letzte_zahl = (int(input('Bitte eine Zahl eingeben:')))

zahlen_ausgeben = []

for i in range (erste_zahl,letzte_zahl):
    if i % 9 == 0:
        zahlen_ausgeben.append(i)
    if i == 0:
        zahlen_ausgeben.remove(0)

for zahlen_ausgeben1 in zahlen_ausgeben:
    print(zahlen_ausgeben1)


