paises = [  #Creacion de lista con diccionarios dentro que continen informacion de paises
    {"Nombre":"Argentina","Población":46994384,"Superficie":2780400,"Continente":"América del Sur"},
    {"Nombre":"Brasil","Población":220051512 ,"Superficie":8515770,"Continente":"América del Sur"},
    {"Nombre":"Japon","Población":123201945,"Superficie":377915,"Continente":"Asia oriental"},
    {"Nombre":"Francia","Población":68374591,"Superficie":643801,"Continente":"Europa occidental"},     
    {"Nombre":"Senegal","Población":18847519,"Superficie":196722,"Continente":"África occidental"},
    {"Nombre":"Cuba","Población":10966038,"Superficie":110860,"Continente":"Centroamérica y el Caribe"},
    {"Nombre":"España","Población":47280433,"Superficie":47280433,"Continente":"Suroeste de Europa"},
    {"Nombre":"China","Población":1416043270,"Superficie":9596960,"Continente":"Asia oriental"}
]

#Añado el listado de países al archivo "paises.csv"

with open("paises.csv" , "w") as archivo: 
    archivo.write("NOMBRE,POBLACIÓN,SUPERFICIE,CONTINENTE \n")

lista_paises = []
for pais in paises:
    pais_sin_keys = f"{pais['Nombre']},{pais['Población']},{pais['Superficie']},{pais['Continente']}"
    lista_paises.append(pais_sin_keys)

with open("paises.csv" , "a") as archivo:
    
    for pais in lista_paises:
        archivo.writelines(f"{pais}\n")

permitir2 = False

def final(permiso):
    pregunta = input("¿Desea realizar otra actividad? (S/N)  ").capitalize()
    print()
    while pregunta != "S" and pregunta != "N":
        
        pregunta = input("""Valor inválido, intente nuevamente:
                            
                            
                            
                            """)
        
    if pregunta == "S":
        permiso = False
    elif pregunta == "N":
        permiso = True

    return permiso

permitir = False

while permitir == False:
    permitir_w=(input("""
            Ingresa 1 para ver los paises
            Ingresa 2 para buscar un pais
            Ingresa 3 para ver los paises con mayor y menor poblacion
            Ingresa otro número para salir
            
            """))     #Optimizé el menú
    try:
        permitir_w=int(permitir_w)     #try para validar numeros       #y un if para salir del programa si el usuario lo decidio previamente
        if permitir_w>3 or permitir_w<1:
            break
        
    except:
        print ("")
        print ("            *Opcion no valida")
    

    
    match permitir_w:
        case 1: #CASO 1 PRINCIPAL: Visualización de lista completa con diferentes opciones organizacionales
            opcion = input("""
                                
                                    OPCIONES:
                                (1) LISTADO COMPLETO
                                (2) FILTRADO ALFABETICAMENTE
                                (3) FILTRADO POR CONTINENTE
                                (4) FILTRADO POR POBLACIÓN
                                (5) FILTRADO POR SUPERFICIE (Ascendente y Descendente)
                                
                                """) #OPCIONES DE LISTADO
            try:
                opcion=int(opcion)
            except:
                print ("Opcion no valida")
            
            print()
            match opcion: #MATCH PARA LAS OPCIONES DEL CASO 1 PRINCIPAL (ver los países)
                
                case 1: #Para ver el listado completo de países tal cual está
                    for pais in paises:
                        print(pais["Nombre"])
                    permitir = final(permitir2) #Una llamada a la funcion para ver si el usuario quiere realizar alguna otra actividad (se repite en todos los casos)
                    
                case 2: #Para ver el listado de países ordenado alfabeticamente
                    paises_ordenados = sorted(paises, key=lambda d: d["Nombre"]) #Funcion lambda y sorted para ordenar alfabeticamente
                    for elemento in paises_ordenados:                        
                        print(elemento)
                    permitir = final(permitir2)
                
                case 3: #Para ver el listado de países agrupados por continente
                    paises_por_continente = {} #Creo una nueva lista para almacenar los paises agrupados por continente
                    
                    for pais in paises:
                        continente = pais["Continente"]
                        if continente not in paises_por_continente:#Si es que el continente no está ya integrado en el diccionario se crea
                            paises_por_continente[continente] = [] #un nuevo diccionario
                        
                        paises_por_continente[continente].append(pais) #Se añade el país con sus datos al diccionario
                        
                    print("-- Países Agrupados por Continente --")
                    for continente,paises in paises_por_continente.items():
                        print(f"Continente: {continente}")
                        for pais in paises:
                            print(f"  - {pais["Nombre"]}")
                    
                    permitir = final(permitir2)
                
                case 4: #Para ver el listado de países filtrados por un rango mínimo y un rango máximo de población definido por el usuario
                    min_poblacion = int(input("Rango mínimo de poblacion:  ")) #Se establecen el rango mínimo y el máximo
                    max_poblacion = int(input("Rango máximo de población:  "))
                    paises_filtrados_poblacion = [] #Se crea una nueva lista para contener los paises filtrados en el rango establecido
                    print()
                    
                    for pais in paises: #Se evalua si la poblacion del país dentro de la variable "pais" está dentro del rango o no
                        poblacion = pais["Población"] #Si está dentro del rango, lo añade a la lista
                        if poblacion >= min_poblacion and poblacion <= max_poblacion:
                            paises_filtrados_poblacion.append(pais)
                    
                    if not paises_filtrados_poblacion: #Validación de si 
                        print("No hay países dentro de ese rango de población.")
                    else:
                        print(f"-- Países entre {min_poblacion} y {max_poblacion} --")
                        for pais in paises_filtrados_poblacion:
                            print(f"{pais}\n")
                    
                    permitir = final(permitir2)
                case 5: #Para ver el listado de países filtrados por un rango mínimo y un rango máximo de superficie definido por el usuario
                    min_superficie = int(input("Rango mínimo de superficie: "))
                    max_superficie = int(input("Rango máximo de superficie: "))
                    paises_filtrados_superficie = []
                    print()
                    
                    for pais in paises: #Se evalua si la poblacion del país dentro de la variable "pais" está dentro del rango o no
                        superficie = pais["Superficie"] #Si está dentro del rango, lo añade a la lista
                        if superficie >= min_superficie and superficie <= max_superficie:
                            paises_filtrados_superficie.append(pais)
                    
                    if not paises_filtrados_superficie: #Validación de si 
                        print("No hay países dentro de ese rango de superficie.")
                    else:
                        print(f"-- Países entre {min_superficie} y {max_superficie} --")
                        for pais in paises_filtrados_superficie:
                            print(f"{pais}\n")
                        
                    permitir = final(permitir2)
            
        case 2: #CASO 2 PRINCIPAL: Buscador de países
            usuario=input("Ingresa el pais que desea buscar:").title()
            for pais in paises:
                if usuario == pais["Nombre"]:
                    print (pais)    
            
        case 3: #CASO 3 PRINCIPAL: Los países con mayor y menor poblacion registrados
            población_menor=99999999999
            población_mayor=0
            for pais in paises:  #bucle para comparar la poblacion de todos los paises registrados
                if pais["Población"]<población_menor:   #if para asignarle a las variables de poblacion el valor de la menor y mayor de poblacion de cada pais-
                    n_menor=pais["Nombre"]
                    población_menor=pais["Población"]
                if pais["Población"]>población_mayor:
                    n_mayor=pais["Nombre"]
                    población_mayor=pais["Población"]
            print (f"el pais con mayor población es {n_mayor} con {población_mayor} habitantes")
            print (f"el pais con menor población es {n_menor} con {población_menor} habitantes")
