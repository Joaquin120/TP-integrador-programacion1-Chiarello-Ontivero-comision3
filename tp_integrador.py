# Definimos el nombre del archivo y el encabezado del mismo
nombre_archivo = "paises.csv"
encabezado = "NOMBRE,POBLACIÓN,SUPERFICIE,CONTINENTE\n"

# Definimos los datos de los países
datos_paises = [
    "Argentina,46994384,2780400,América del Sur\n",
    "Brasil,220051512,8515770,América del Sur\n",
    "Japon,123201945,377915,Asia oriental\n",
    "Francia,68374591,643801,Europa occidental\n",
    "Senegal,18847519,196722,África occidental\n",
    "Cuba,10966038,110860,Centroamérica y el Caribe\n",
    "España,47280433,505370,Suroeste de Europa\n",
    "China,1416043270,9596960,Asia oriental\n"
]

try:
    # Abrimos el archivo en modo escritura ('w')
    with open(nombre_archivo, "w") as archivo:
        
        # Escribimos el encabezado primero
        archivo.write(encabezado)
        
        # Escribimos todas las líneas de datos de la lista
        archivo.writelines(datos_paises)
    
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")

except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")


def calcular_promedio(paises, clave): # Calcula el promedio de una clave numérica (Población o Superficie)
    if not paises:
        return 0
    total = 0
    for pais in paises:
        total += pais[clave]
    return total / len(paises)

def calcular_max_min_poblacion(paises): # Encuentra el país con mayor y menor población
    if not paises:
        return None, None

    # Usa las funciones min() y max() con una lambda para establecer cual país tiene el mínimo de población y cuál el máximo
    pais_min = min(paises, key=lambda p: p["Población"])
    pais_max = max(paises, key=lambda p: p["Población"])
    
    return pais_min, pais_max

def contar_paises_por_continente(paises): #Cuenta cuántos países hay por cada continente

    conteo_continentes = {} # Usamos un diccionario vacío para ser dinámicos
    for pais in paises:
        continente = pais["Continente"]
        if continente not in conteo_continentes:
            conteo_continentes[continente] = 0 # Si no existe, lo creamos
        conteo_continentes[continente] += 1
    return conteo_continentes


def mostrar_paises(lista_paises): #Maneja el submenú de la opción 1: Ver los países
    
    opcion_str = input("""
        OPCIONES:
        (1) LISTADO COMPLETO
        (2) FILTRADO ALFABETICAMENTE
        (3) FILTRADO POR CONTINENTE
        (4) FILTRADO POR POBLACIÓN
        (5) FILTRADO POR SUPERFICIE
        Elija una opción: """)
    
    print()
    
    try:
        opcion = int(opcion_str)
    except ValueError:
        print("Opción no válida.")
        return

    match opcion:
        case 1: # LISTADO COMPLETO
            print("-- Listado Completo --")
            for pais in lista_paises:
                print(f" - {pais['Nombre']}")
        
        case 2: # FILTRADO ALFABETICAMENTE
            print("-- Listado Ordenado Alfabéticamente --")
            paises_ordenados = sorted(lista_paises, key=lambda d: d["Nombre"])
            for pais in paises_ordenados:
                print(f" - {pais['Nombre']} ({pais['Continente']})")
        
        case 3: # FILTRADO POR CONTINENTE
            print("-- Países Agrupados por Continente --")
            paises_por_continente = {}
            for pais in lista_paises:
                continente = pais["Continente"]
                if continente not in paises_por_continente:
                    paises_por_continente[continente] = []
                paises_por_continente[continente].append(pais)
            
            for continente, lista_de_paises in paises_por_continente.items():
                print(f"\nContinente: {continente}")
                for pais_individual in lista_de_paises:
                    print(f"  - {pais_individual['Nombre']}")
        
        case 4: # FILTRADO POR POBLACIÓN
            try:
                min_poblacion = int(input("Rango mínimo de poblacion: "))
                max_poblacion = int(input("Rango máximo de población: "))
                paises_filtrados = []
                
                for pais in lista_paises:
                    if min_poblacion <= pais["Población"] <= max_poblacion:
                        paises_filtrados.append(pais)
                
                if not paises_filtrados:
                    print("No hay países dentro de ese rango de población.")
                else:
                    print(f"\n-- Países entre {min_poblacion} y {max_poblacion} --")
                    for pais in paises_filtrados:
                        print(f" - {pais['Nombre']} ({pais['Población']} hab.)")
            except ValueError:
                print("Error: Rango de población debe ser numérico.")
        
        case 5: # FILTRADO POR SUPERFICIE (Lógica similar al case 4, pero con "Superficie")
            print("Función de superficie no implementada.")
        
        case _:
            print("Opción de listado no válida.")

def buscar_pais(lista_paises):
    """Busca un país por nombre y muestra sus detalles."""
    nombre_buscado = input("Ingresa el pais que desea buscar: ").title()
    encontrado = False
    for pais in lista_paises:
        if pais["Nombre"] == nombre_buscado:
            print("\n-- País Encontrado --")
            print(f"Nombre: {pais['Nombre']}")
            print(f"Población: {pais['Población']}")
            print(f"Superficie: {pais['Superficie']} km²")
            print(f"Continente: {pais['Continente']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Error: El país '{nombre_buscado}' no se encontró.")

def mostrar_estadisticas_menu(lista_paises): #Maneja el submenú del case 3: "Ver estadísticas"
    
    opcion_str = input("""
        ESTADÍSTICAS:
        (1) Ver los paises con mayor y menor población
        (2) Ver el promedio de población de los paises
        (3) Ver el promedio de superficie de los paises
        (4) Ver cuantos paises tiene cada continente
        Elija una opción: """)
    
    try:
        opcion = int(opcion_str)
    except ValueError:
        print("Opción no válida.")
        return

    match opcion:
        case 1:
            pais_min, pais_max = calcular_max_min_poblacion(lista_paises)
            print(f"\nPaís con mayor población: {pais_max['Nombre']} ({pais_max['Población']} hab.)")
            print(f"País con menor población: {pais_min['Nombre']} ({pais_min['Población']} hab.)")
        case 2:
            prom = calcular_promedio(lista_paises, "Población")
            print(f"\nEl promedio de población es: {prom:,.0f} habitantes.")
        case 3:
            prom_sup = calcular_promedio(lista_paises, "Superficie")
            print(f"\nEl promedio de superficie es: {prom_sup:,.2f} km².")
        case 4:
            conteo = contar_paises_por_continente(lista_paises)
            print("\n-- Conteo de Países por Continente --")
            for continente, cantidad in conteo.items():
                print(f" - {continente}: {cantidad} país/es")
        case _:
            print("Opción de estadística no válida.")

def cargar_datos_csv(nombre_archivo): # Lee el archivo CSV y lo convierte en una lista de diccionarios.
    
    lista_paises = []
    try:
        with open(nombre_archivo, "r") as archivo:
            # Saltamos la primera línea (el encabezado)
            next(archivo) 
            
            for linea in archivo:
                linea = linea.strip() # Limpiamos saltos de línea
                if linea: # Nos aseguramos que la línea no esté vacía
                    partes = linea.split(',')
                    
                    if len(partes) == 4:
                        try:
                            # Creamos el diccionario convirtiendo los números a int
                            pais_dict = {
                                "Nombre": partes[0],
                                "Población": int(partes[1]),
                                "Superficie": int(partes[2]),
                                "Continente": partes[3]
                            }
                            lista_paises.append(pais_dict)
                        except ValueError:
                            print(f"Advertencia: Omitiendo línea mal formada (no numérico): {linea}")
                    else:
                        print(f"Advertencia: Omitiendo línea mal formada (columnas): {linea}")
                        
    except FileNotFoundError:
        print(f"ERROR FATAL: No se encontró el archivo '{nombre_archivo}'.")
        return None # Devolvemos None para indicar que la carga falló
    
    print(f"Se cargaron {len(lista_paises)} países exitosamente.")
    return lista_paises

def preguntar_continuar():
    """Maneja la lógica de tu función 'final()'."""
    pregunta = input("\n¿Desea realizar otra actividad? (S/N): ").capitalize()
    while pregunta not in ("S", "N"):
        pregunta = input("Valor inválido. Intente (S/N): ").capitalize()
    
    if pregunta == "N":
        return True # Retorna True para "terminar" (permitir = True)
    else:
        return False # Retorna False para "continuar" (permitir = False)

def main():#Función principal que ejecuta el programa
    
    # 1. Cargamos los datos desde el CSV
    lista_paises = cargar_datos_csv("paises.csv")
    
    # Si la carga falla, no continuamos
    if lista_paises is None:
        input("Presione Enter para salir.")
        return

    permitir_salir = False

    while not permitir_salir:
        opcion_menu = input("""
        --- MENÚ PRINCIPAL ---
        (1) Ver los países
        (2) Buscar un país
        (3) Ver estadísticas
        (0) Salir
        Elija una opción: """)
        
        try:
            match opcion_menu:
                case "1":
                    mostrar_paises(lista_paises)
                case "2":
                    buscar_pais(lista_paises)
                case "3":
                    mostrar_estadisticas_menu(lista_paises)
                case "0":
                    permitir_salir = True
                case _:
                    print("Opción no válida, intente de nuevo.")
        
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

        # Preguntamos si desea continuar solo si no eligió salir
        if not permitir_salir and opcion_menu in ("1", "2", "3"):
            permitir_salir = preguntar_continuar()

    print("\nFin del programa")
if __name__ == "__main__":
    main()