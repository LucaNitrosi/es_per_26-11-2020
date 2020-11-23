x = int(input("Quanti voti ha ricevuto il primo candidato? "))
y = int(input("Quanti voti ha ricevuto il secondo candidato? "))

pc = (x + y)/100

if x > y:
    print("ha vinto il primo con ", x/pc)
elif x == y:
    print("sono pari")
else:
    print("ha vinto il secondo con ",  y/pc)