n = int(input("Inserisci un numero: "))

if n%2==0 and n>=0:
    print(f"{n} è positivo e pari")
elif n%2==1 and n>=0:
    print(f" {n} è positivo e dispari")
elif n%2==0 and n<0:
    print(f"{n} è pari e negativo")
elif n%2==1 and n<0:
    print(f"{n} è negativo e dispari")
else:
    print("Nessuna delle precedenti")