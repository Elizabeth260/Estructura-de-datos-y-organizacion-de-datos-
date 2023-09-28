class alumno:
	def capAlum(alumnos):    #Metodo para Capturar Alumnos
		resp = 's'
		while resp == 's' or resp == 'S':
			alumTemp = []
			print("-" * 30)
			alumTemp.append(input("-Nombre Completo: "))
			alumTemp.append(input("-Semestre: "))
			alumTemp.append(input("-Carrera: "))
			alumTemp.append(input("-RFC: "))
			alumTemp.append(input("-Num de Control: "))
			alumnos.append(alumTemp)
			print("\n*Alumno agregado exitosamente!!!*")
			print("-" * 30)
			resp = input("> Desea agregar otro alumno s/n? -> ")

	def printAlum(alumnos):   #Metodo para imprimir TODOS los Alumnos
		for alumno in alumnos:
			print("-" * 30)
			print("Nombre Completo:", alumno[0])
			print("Semestre:", alumno[1])
			print("Carrera:", alumno[2])
			print("RFC:", alumno[3])
			print("Num de Control:", alumno[4])
			print("-" * 30)

	def printAlumCarr(alumnos, carrera_buscar):    #Metodo para imprimir los alumnos de una carrera en especifico
		print(f"Alumnos de la carrera '{carrera_buscar}':")
		for alumno in alumnos:
			if alumno[2] == carrera_buscar:
				print("-" * 30)
				print("Nombre Completo:", alumno[0])
				print("Semestre:", alumno[1])
				print("Carrera:", alumno[2])
				print("RFC:", alumno[3])
				print("Num de Control:", alumno[4])
				print("-" * 30)

	def printDATalum(alumnos, num_control_buscar):   #Metodo para imprimir los datos de un alumno en especifico
		for alumno in alumnos:
			if alumno[4] == num_control_buscar:
				print("-" * 30)
				print("Nombre Completo:", alumno[0])
				print("Semestre:", alumno[1])
				print("Carrera:", alumno[2])
				print("RFC:", alumno[3])
				print("Num de Control:", alumno[4])
				print("-" * 30)
				return

	def countAlum(alumnos):                        #Metodo para contar TODOS los alumnos registrados
		cantidad = len(alumnos)
		print("-" * 30)
		print(f"Total de alumnos registrados: {cantidad}")
		print("-" * 30)

op = 0
alumnos = []
while op != 6:
    print("**SISTEMA DE GESTION DE ALUMNOS**\n     ...:::BIENVENIDO :::...\n\t     MENU")
    print("1. Captura Alumnos\n2. Listar todos los alumnos\n3. Buscar por carrera\n4. Buscar por alumno\n5. Cuenta alumnos\n6. Salir")
    op = int(input("->"))
    if op == 1:
        capAlum(alumnos)
    elif op == 2:
        printAlum(alumnos)
    elif op == 3:
        print("*Sistemas\n*Tics\n*Gestion\n*Industrial")
        carreraTfind = input("> Carrera a imprimir -> ")
        printAlumCarr(alumnos, carreraTfind)
    elif op == 4:
        numContFind = input("> Ingrese el Numero de Control a buscar -> ")
        printDATalum(alumnos,numContFind)
    elif op == 5:
        countAlum(alumnos)
