def promedio(paises,x):    #x es el parametro al que queremos descubrir el promedio por ejemplo poblacion
    cant_paises=len(paises) #calculo de promedio
    promedio=0
    for pais in paises:
        promedio+=pais[x]
    promedio/=cant_paises
    return promedio


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
            Ingresa 3 para ver estadisticas
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
        case 1:
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
            match opcion:
                case 1:
                    for pais in paises:
                        print(pais["Nombre"])
                    final(permitir)#Una llamada a la funcion para ver si el usuario quiere realizar alguna otra actividad (se repite en todos los casos)
                
                case 2:
                    paises_ordenados = sorted(paises, key=lambda d: d["Nombre"]) #Funcion lambda y sorted para ordenar alfabeticamente
                    for elemento in paises_ordenados:                        
                        print(elemento)
                    final(permitir)
                
                case 3:
                    paises_por_continente = {} #Creo una nueva lista para almacenar los paises filtrados por continente
                    
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
                    
                    final(permitir)
                
                case 4: #Mismo procedimiento que con el case 3 pero con poblacion
                    min_poblacion = int(input("Rango mínimo de poblacion:  "))
                    max_poblacion = int(input("Rango máximo de población:  "))
                    paises_filtrados = []
                    print()
                    
                    for pais in paises:
                        poblacion = pais["Población"]
                        if poblacion >= min_poblacion and poblacion <= max_poblacion:
                            paises_filtrados.append(pais)
                    
                    print(f"-- Países entre {min_poblacion} y {max_poblacion} --")
                    print(paises_filtrados)
                    
                    final(permitir)
                case 5:
                    pass
            
        case 2:
            usuario=input("Ingresa el pais que desea buscar:").title()
            for pais in paises:
                if usuario == pais["Nombre"]:
                    print (pais)            
                    
        case 3:
            print ("ingresa 1 para ver los paises con mayor y menor población")
            print ("ingresa 2 para ver el promedio de poblacion de los paises")
            print ("ingresa 3 para ver el promedio de superficcie de los paises")
            opcion=input("")
            try:
                opcion=int(opcion)
            except:
                print("")
            
            match opcion:
                case 1:   #en este bloque se van a mostrar los paises con mayor y menor poblacion registrados
                    población_menor=99999999999
                    población_mayor=0
                    for pais in paises:  #bucle para comparar la poblacion de todos los paise registrados
                        if pais["Población"]<población_menor:   #if para asignarle a las varibles de poblacion el valor de la menor y mayor de poblacion de cada pais-
                            n_menor=pais["Nombre"]
                            población_menor=pais["Población"]
                        if pais["Población"]>población_mayor:
                            n_mayor=pais["Nombre"]
                            población_mayor=pais["Población"]
                    print ("")
                    print ("")
                    print (f"el pais con mayor población es {n_mayor} con {población_mayor} habitantes")
                    print ("/")
                    print (f"el pais con menor población es {n_menor} con {población_menor} habitantes")
                    print ("")
                    print ("")
                case 2:
                    print (f"el promedio de poblacion es {promedio(paises,"Población")} de personas")
                case 3:
                    print (f"el promedio de superficie es {promedio(paises,"Superficie")} KM cuadrados")