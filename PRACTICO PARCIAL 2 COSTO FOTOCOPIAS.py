
while True:
		print("INGRESE LA CANTIDAD INICIAL DE IMPRESIONES")
		dato1 = float(input())
		print("INGRESE LA CANTIDAD DE IMPRESIONES FINALES")
		dato2 = float(input())
		if dato2<dato1:
			print("ERROR: EL VALOR FINAL ES MENOR AL VALOR INICIAL")
			dato2 = float(input())
		print("DIGITE EL TIPO DE IMPRESION: BLANCONEGRO O COLOR")
		impresion = input()
		if impresion=="BLANCONEGRO" or impresion=="blanconegro":
			blanconegro = 0.06
			impresiones = dato2-dato1
			print("NUMERO DE IMPRESIONES ES=",impresiones)
			costo = impresiones*0.06
			print("VALOR=","$",costo)
		if impresion=="COLOR" or impresion=="color":
			color = 0.12
			impresiones = dato2-dato1
			print("NUERO DE IMPRESIONES ES=",impresiones)
			costo = impresiones*0.12
			print("VALOR=","$",costo)
		print("DESEA SALIR?")
		salir = input()
		if salir=="SI" or salir=="si": break

