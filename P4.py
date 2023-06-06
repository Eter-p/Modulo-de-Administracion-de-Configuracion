from telnet import actualizar,cargarArchivo
from tftp import descargarArchivo
import os
import time

IPS_ROUTER_2 = ("30.30.30.1","40.40.40.1","192.168.1.1")
IPS_ROUTER_1 = ("192.168.1.2","10.10.10.1","20.20.20.1")
user_R1 = "rou01"
user_R2 = "rou02"
password = "1234"

if (not os.path.exists("Routers")):
	os.mkdir("Routers")

def comprobar(ip):
	for x in IPS_ROUTER_1:
		if x == ip:
			return 1
		
	for x in IPS_ROUTER_2:
		if x == ip:
			return 2
	return 0

while(True):
	print("\n********** Menu **********\n")
	print("1. Descargar startup-config")
	print("2. Descargar running-config")
	print("3. Cargar startup-config")
	print("4. Cargar running-config")
	print("5. Actualizar (run star)")
	print("6. Salir")

	opcion = input("\nElije una opcion: ")
	if opcion == str(1):
		ip_router = input("IP del router: ")
		n_router = comprobar(ip_router)
		nom_archivo = input("Guardar como: ")
		if(n_router!=0):
			descargarArchivo(ip_router,"rou0"+str(n_router),password,"startup-config",nom_archivo)
			time.sleep(2)
			os.replace(nom_archivo,"Routers/"+nom_archivo)
			print("!!! Archivo Guardado !!!")
		else:
			print("ip no valida")
	elif opcion == str(2):
		ip_router = input("IP del router: ")
		n_router = comprobar(ip_router)
		nom_archivo = input("Guardar como: ")
		if(n_router!=0):
			descargarArchivo(ip_router,"rou0"+str(n_router),password,"running-config",nom_archivo)
			time.sleep(2)
			os.replace(nom_archivo,"Routers/"+nom_archivo)
			print("!!! Archivo Guardado !!!")
		else:
			print("ip no valida")
	elif opcion == str(3):
		listaArchivos = os.listdir("Routers/")
		if len(listaArchivos) == 0:
			print("!!! No exiten Archivos !!!")
			continue
		print("Indice\tAgente")
		i=0
		for archivo in listaArchivos:
			i+=1
			print(str(i)+".\t"+archivo)
		n_archivo = input("Elija un archivo: ")
		ip_router = input("IP del router: ")
		n_router = comprobar(ip_router)
		if(n_router!=0):
			cargarArchivo(ip_router,"rou0"+str(n_router),password,listaArchivos[int(n_archivo)-1],"startup-config")
			print("!!! Archivo Cargado !!!")
		else:
			print("ip no valida")
	elif opcion == str(4):
		listaArchivos = os.listdir("Routers/")
		if len(listaArchivos) == 0:
			continue
		print("Indice\tAgente")
		i=0
		for archivo in listaArchivos:
			i+=1
			print(str(i)+".\t"+archivo)
		n_archivo = input("Elija un archivo: ")
		ip_router = input("IP del router: ")
		n_router = comprobar(ip_router)
		if(n_router!=0):
			cargarArchivo(ip_router,"rou0"+str(n_router),password,listaArchivos[int(n_archivo)-1],"running-config")
			print("!!! Archivo Cargado !!!")
		else:
			print("ip no valida")
	elif opcion == str(5):
		ip_router = input("IP del router: ")
		n_router = comprobar(ip_router)
		if(n_router!=0):
			actualizar(ip_router,"rou0"+str(n_router),password)
			print("!!! Actualizacion Completada !!!")
		else:
			print("ip no valida")
	elif opcion == str(6):
		break
	else:
		print("\n!!! Opcion no valida !!!")

