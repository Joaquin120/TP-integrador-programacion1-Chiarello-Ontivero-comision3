paises = [  #creacion de lista con diccionarios dentro que continen informacion de paises
    {"Nombre":"Argentina","Poblacion":46994384,"Superficie":2780400,"Continente":"América del Sur"},
    {"Nombre":"Brasil","Poblacion":220051512 ,"Superficie":8515770,"Continente":"América del Sur"},
    {"Nombre":"Japon","Poblacion":123201945,"Superficie":377915,"Continente":"Asia oriental"},
    {"Nombre":"Francia","Poblacion":68374591,"Superficie":643801,"Continente":"Europa occidental"},     
    {"Nombre":"Senegal","Poblacion":18847519,"Superficie":196722,"Continente":"África occidental"},
    {"Nombre":"Cuba","Poblacion":10966038,"Superficie":110860,"Continente":"Centroamérica y el Caribe"},
    {"Nombre":"España","Poblacion":47280433,"Superficie":47280433,"Continente":"suroeste de Europa"},
    {"Nombre":"China","Poblacion":1416043270,"Superficie":9596960,"Continente":"Asia oriental"}
]

permitir = False

while permitir == False:
    print ("ingresa 1 para ver los paises")
    print ("ingresa 2 para buscar un pais")
    print ("otro para salir")
    permitir_w=input("")    #para elegir una opcion
    if permitir_w == "1":
        for pais in paises:
            print(pais["Nombre"])
    
    if permitir_w == "2":
        usuario=input("ingresa el pais que buscar:").title()
        for pais in paises:
            if usuario == pais["Nombre"]:
                print (pais)
        
    
    permitir=True