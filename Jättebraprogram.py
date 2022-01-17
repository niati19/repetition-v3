grispris = input("Hur mycket kostar en gris? ")
int(grispris)

fågelpris = input("Hur mycket kostar en fågel? ")
int(fågelpris)

if fågelpris > grispris: 
    print("Ja, en fågel är dyrare än en gris")
    print(f"En fågel kostar {fågelpris} kr")
    print(f"En gris kostar {grispris} kr")  

elif grispris > fågelpris:
    print("En gris kostar mer än en fågel")
    print(f"En gris kostar {grispris} kr")
    print(f"En fågel kostar {fågelpris} kr")
elif grispris == fågelpris:
    print(f"De kostar lika mycket, alltså {grispris} kr")