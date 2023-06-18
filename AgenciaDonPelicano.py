
tours= []
clientes= []
vehiculos= []
reservartour = []
espaciosOcupados = []

print("Bienvenido al sistema de tours Don Pelicano")
print("-----------------------------------------------")

usuario="DonPelicano" #se crea un usuario para el inicio del programa
contra="12345" #contraseña para el programa 
usuario1=input("Digite su usuario: ")
contra1=input("Digite su contraseña :")
if(usuario1==usuario and contra1==contra):
      print("Bienvenido al sistema",usuario)
      print() #Menu a continuacion:
      def menu():
        print("------------MENU------------")
        print("\n")
        print("1) Registrar tour")
        print("2) Registrar cliente")
        print("3) Registrar vehiculo")
        print("4) Reservacion del vehiculo")
        print("5) Reservacion del tour")
        print("6) Reportes")
        print("7) Salir")
        print("\n")

else:
    print("Su usuario no es correcto,por favor contactarse con su servidor")
#Tuve que hacer cambios en las funciones de tour y cliente
def regisTour():
      toursDisponibles = open("toursDisponibles.txt","w")
      tour= {}
      #datos del tour
      nombreT=str(input("Ingrese el nombre del Tour: "))
      precioTour= int(input("Ingrese el precio del Tour: "))
      precioTransp= int(input("Ingrese el precio del Transporte: "))
      lugar=str(input("Ingrese el lugar del Tour: "))
      salida=str(input("Ingrese el lugar de salida del Tour: "))
      dias=int(input("Indique la cantidad de dias del Tour: "))
      actividades= str(input("Ingrese las actividades que tiene el Tour: "))
      comida= str(input("Ingrese los servicios de alimentacion del Tour: "))
      #guardar datos del tour
      tour["nombreTour"]=nombreT
      tour["precioTour"]=precioTour
      tour["precioTransporte"]=precioTransp
      tour["lugar"]=lugar
      tour["salida"]=salida
      tour["dias"]=dias
      tour["espacio"]=10
      tour["actividades"]=actividades
      tour["alimentacion"]=comida
      tours.append(tour)
      toursDisponibles.write("\n=========================================\n")
      toursDisponibles.write("Tours Disponibles: \n")
      toursDisponibles.write(str(tours))
      toursDisponibles.close()
      import pprint
      pprint.pprint(tours)    

#se ejecuta la variable cliente
def regisCliente():         
      cliente= {}
      #datos del cliente
      nombre=str(input("Ingrese el nombre del cliente: "))
      apellidos=str(input("Ingrese el apellido del cliente: "))
      identificacion=int(input("Digite su numero de identificacion: "))
      correo=str(input("Ingrese el correo electronico del cliente: "))
      telefono=int(input("Ingrese el numero de telefono del cliente: "))
      #guardar datos cliente
      cliente["nombreCliente"]=nombre
      cliente["apellidos"]=apellidos
      cliente["identificacion"]=identificacion
      cliente["correo"]=correo
      cliente["telefono"]=telefono
      clientes.append(cliente)
      import pprint
      pprint.pprint(clientes)
#la funcion vehiculo,Nos pide los datos del vehiculo,y nos manda la restriccion
def obtenerRes(placa):
      ultimoNum= placa%10
      if(ultimoNum==1 or ultimoNum==2):
            dia=1
            print("Este vehiculo tiene restriccion el lunes")
      elif(ultimoNum==3 or ultimoNum==4):
            dia=2
            print("Este vehiculo tiene restriccion el martes")
      elif(ultimoNum==5 or ultimoNum==6):
            dia=3
            print("Este vehiculo tiene restriccion el miercoles")
      elif(ultimoNum==7 or ultimoNum==8):
            dia=4
            print("Este vehiculo tiene restriccion el jueves")
      elif(ultimoNum==9 or ultimoNum==0):
            dia=5
            print("Este vehiculo tiene restriccion el viernes")
      return dia
#Cambio en la funcion hice un arregle para meter los vehiculos
def regisVehiculo():
    vehiculo= {}
    marca=str(input("Ingrese la marca de su vehiculo: "))
    modelo=str(input("Ingrese el modelo de su vehiculo: "))
    placa=int(input("Digite su placa: "))
    restriccion=obtenerRes(placa)
    capac=int(input("Cual es la capacidad del vehiculo: "))
    #Aqui se guardan los datos del arreglo
    vehiculo["marca"]=marca
    vehiculo["modelo"]=modelo
    vehiculo["placa"]=placa
    vehiculo["restriccion"]=restriccion
    vehiculo["capacidad"]=capac
    vehiculo["disponibilidad"] = True
    #esto hace que se comparta con la de reservar vehiculo en esa aparece los vehiculos
    vehiculos.append(vehiculo)
#Funcion para reservar el vehiculo
#se obtienen datos mediante otras funciones para la funcion de reservar
def obtTour(tourN):
      for tour in tours:
            if (tour["nombreTour"] == tourN):
                  return tour

def rvehiculoAux(quitar):
      for vehiculo in vehiculos:
            if (vehiculo == quitar):
                  vehiculo["disponibilidad"] = False

def reserVehiculo():
      vehiculosDisponibles = []
      tourN = str(input("Ingrese el nombre del Tour: "))
      tour = obtTour(tourN)
      opcion = str(input("La salida/llegada es en San José y es entre semana?(si/no): "))
      if(opcion == "si" or opcion == "Si" or opcion == "SI"):
            print("\nQue dia es la salida?")
            print("1) Lunes")
            print("2) Martes")
            print("3) Miercoles")
            print("4) Jueves")
            print("5) Viernes")
            salida = int(input("Ingrese el numero: "))
            print("\nQue dia es la llegada?")
            print("1) Lunes")
            print("2) Martes")
            print("3) Miercoles")
            print("4) Jueves")
            print("5) Viernes")
            llegada = int(input("Ingrese el numero: "))
            for vehiculo in vehiculos:
                  if(vehiculo["disponibilidad"] == True and (vehiculo["restriccion"] != salida and vehiculo["restriccion"] != llegada)):
                        if(vehiculo["capacidad"] >= tour["espacio"]):
                              vehiculosDisponibles.append(vehiculo)
      else:
            for vehiculo in vehiculos:
                  if(vehiculo["disponibilidad"] == True and vehiculo["capacidad"] >= tour["espacio"]):
                        vehiculosDisponibles.append(vehiculo)
      print("Elija uno de los siguientes vehiculos: ")
      print("| Posicion | Marca | Modelo | Placa | Capacidad |")
      pos= 1
      for vehiculo in vehiculosDisponibles:
            print("| "+str(pos)+" | "+vehiculo["marca"]+" | "+vehiculo["modelo"]+" | "+str(vehiculo["placa"])+" | "+str(vehiculo["capacidad"])+" |")
            pos +=1
      opcion = int(input("Ingrese la posicion de carro que desea reservar: "))
      rvehiculoAux(vehiculosDisponibles[opcion-1])
      import pprint
      pprint.pprint(vehiculos)

#funcion para leer la identificacion en la matriz de clientes
def obtClie(idClie):
      for cliente in clientes:
            if (cliente["identificacion"] == idClie):
                  return cliente
#funcion para leer la cantidad de personas por tour en la matriz tours
def obtEsp(cantPers):
      for tour in tours:
            if (tour["espacio"] == cantPers):
                  return tour

def reserTour():
      reservas = open("reservas.txt","w")
      resertour={}
      idClie = int(input("Ingrese la identificacion del cliente: "))
      cliente = obtClie(idClie)
      tourN = str(input("Ingrese el nombre del tour: "))
      tour = obtTour(tourN)
      cantPers = int(input("Cantidad de personas que asistiran al tour: "))
      tour = obtEsp(cantPers)
      transp = str(input("Requiere transporte: "))
      if (transp == "si" or transp == "Si" or transp == "SI"):
            vehicasig = int(input("Indique la placa del vehiculo asignado para el tour: "))
      
      espaciosOcupados.append(cantPers)

      
      
      print("Reserva de tour completada con exito!")
      print("\n=========================================\n")


      for tour in tours:

            if (cantPers > tour["espacio"]):
                  print("Tour sin espacios disponibles! Pruebe con menor cantidad de personas o reserve otro tour.")
            else:        
                  print("Reserva realizada con exito!")
                  print("Cliente: "+cliente["nombreCliente"]+" "+cliente["apellidos"])
                  print("Tour: "+tourN)
                  print("Personas: "+str(cantPers))
                  print("Transporte: "+transp)
                  print("Dias: "+str(tour["dias"]))
                  print("Actividades: "+tour["actividades"])
                  print("Alimentacion: "+tour["alimentacion"])
                  print("Precio: "+str(tour["precioTour"]))
                  print("\n")
                  reservas.write("\n=========================================\n")
                  reservas.write("Nombre: "+cliente["nombreCliente"]+" "+cliente["apellidos"]+"\n")
                  reservas.write("Tour: "+tourN+"\n")
                  reservas.write("Personas: "+str(cantPers)+"\n")
                  reservas.write("Transporte: "+transp+"\n")
                  reservas.write("Dias: "+str(tour["dias"])+"\n")
                  reservas.write("Alimentacion: "+tour["alimentacion"]+"\n")
                  reservas.write("Precio: "+str(tour["precioTour"])+"\n")
                  reservas.write("\n=========================================\n")
                  reservas.close()



def reports():
      #proceso de creacion d rports sobre tours llenos y disponibles
      print("Para ver tour llenos escriba a y para ver tours disponibles escriba b")
      tipreport = str(input("Indique que tipo de reporte desea generar: "))
      if (tipreport == "a" or tipreport == "A"):
            print("\nTours llenos: \n")
            reservas = open("reservas.txt","r")
            contenido = reservas.read()
            print(contenido)
            reservas.close()


      elif (tipreport == "b" or tipreport == "B"):
            print("\nTour con espacios disponibles\n")
            toursDisponibles = open("toursDisponibles.txt","r")
            contenido1 = toursDisponibles.read()
            print(contenido1)
            toursDisponibles.close()
      else: 
            print("Opcion invalida!")
      

            
#lo coloque en diferentes prints, porque si creo una tabla con un solo print, se va a desordenar dependiendo de la cantidad de caracteres que se coloquen en algun dato.

      
#se crea la ejecucion del menu
def menuAux():
      nav=True
      while nav:
            print(menu())
            opcion = int((input("Elija una opcion: ")))
            if opcion == 1:
                  regisTour()
            elif opcion == 2:
                  regisCliente()
            elif opcion == 3:
                  regisVehiculo()
            elif opcion == 4:
                  reserVehiculo()
            elif opcion == 5:
                  reserTour()
            elif opcion == 6:
                  reports()
            elif opcion == 7:
                  quit()
            else:
                  print("Opcion invalida")
            print("=========================================\n")
      print("Gracias por usar el sistema de tours Don Pelicano")
print(menuAux())
     

    

        
