x = int(input("Inserisci un numero:"))
if x < 0:
	x = 0
	print("Numro negativo cambiato a zero")
elif x==0:
	print("Zero")
elif x==1:
	print("Singolo")
else:
	print("Multipo")
