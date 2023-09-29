pila=[]
cadena=input("digite la cadena de invertir")
for i in range(0,len(cadena)):
	pila.append(cadena[i])
	
while(pila):
	print(pila.pop())
