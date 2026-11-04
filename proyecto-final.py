import json

texto_menu_1 = """
=========================================
SISTEMA OPTOGESTIÓN 
========================================= 
1. Registrar paciente 
2. Consultar paciente 
3. Mostrar pacientes registrados 
4. Buscar pacientes con corrección visual 
5. Generar estadísticas 
6. Salir
"""

def id_maximo_pacientes(pacientes):
    maximo_id = 0
    for info_paciente in pacientes:
        if maximo_id < info_paciente["id"]:
            maximo_id = info_paciente["id"]
    return maximo_id

def cargar_pacientes():
    try:
        pacientes = []
        with open("pacientes.json","r",encoding="utf-8") as archivo:
            pacientes = json.load(archivo)
            return pacientes
    except FileNotFoundError:
        print("no se encontro el archivo: pacientes.json creandolo....")
        with open("pacientes.json","w",encoding="utf-8") as archivo:
            json.dump(pacientes,archivo,indent=4)
        return pacientes

def registro_de_pacientes(pacientes):
    id_paciente = id_maximo_pacientes(pacientes) + 1
    nombre_completo = input("favor ingresar nombre completo: ")
    edad = int(input("favor ingrese su edad: "))
    sexo = input("favor ingrese sexo: M/F\n").lower()
    usa_correccion_visual = input("¿usa correccion visual: Si/No\n").lower()
    if (edad >= 1) and (edad <= 120) and ((usa_correccion_visual == "si") or (usa_correccion_visual == "no")):
        paciente = {"id": id_paciente, 
                    "nombre":nombre_completo, 
                    "edad":edad, 
                    "sexo":sexo,
                    "usa_correccion_visual": usa_correccion_visual == "si"
                    }
        pacientes.append(paciente)
        with open("pacientes.json","w",encoding="utf-8") as archivo:
            json.dump(pacientes,archivo,indent=4)
        print("se registro paciente .....")
    elif (usa_correccion_visual != "si") or (usa_correccion_visual != "no"):
        print("ingresa una opcion valida si o no, vuelve a intentarlo")
        print("Volviendo al menu principal")
        print("="*50)

def consulta_de_pacientes(pacientes):
    id_paciente= int(input("favor ingrese el id del paciente que desea consultar: "))
    informacion_completa_paciente = ""
    for info_paciente in pacientes:
        if id_paciente == info_paciente["id"]:
            for llave, valor in info_paciente.items():
                informacion_completa_paciente = informacion_completa_paciente + f"{llave}: {valor}\n"

    if informacion_completa_paciente == "":
        print(f"no existe el id del paciente: {id_paciente}")
    else : 
        print("="*50)
        print(f"la informacion del paciente encontrado es :\n{informacion_completa_paciente}")
        print("="*50)

def mostrar_pacientes_registrados(pacientes):
    print("pacientes registrados")
    for info_paciente in pacientes:
        print("="*50)
        for llave, valor in info_paciente.items():
            print(f"{llave}: {valor}")

def busqueda_de_pacientes(pacientes):
    print("estos son los pacientes que usan correccion visual:")
    contador_pacientes_con_correccion = 0
    for info_paciente in pacientes:
        if info_paciente["usa_correccion_visual"] == True:
            print("="*50)
            contador_pacientes_con_correccion += 1
            for llave, valor in info_paciente.items():
                print(f"{llave}: {valor}")
    if contador_pacientes_con_correccion == 0:
        print("="*50)
        print("no se encontro ningun usuario con correccion visual")
            
def estadisticas_de_la_jornada(pacientes):
    edad_promedio_de_los_pacientes = 0
    contador_pacientes_con_correccion = 0
    for info_paciente in pacientes:
        edad_promedio_de_los_pacientes += info_paciente["edad"]
        if info_paciente["usa_correccion_visual"] == True:
            contador_pacientes_con_correccion += 1

    if len(pacientes) > 0:
        edad_promedio_de_los_pacientes = edad_promedio_de_los_pacientes / len(pacientes)
        print("="*50)
        print("las estadisticas de la jornada son las siguientes:")
        print(f"1.numero total de pacientes: {len(pacientes)}")
        print(f"2.edad promedio de los pacientes: {edad_promedio_de_los_pacientes}")
        if contador_pacientes_con_correccion > 0:
            print(f"3.cantidad de pacientes que utilizan correccion visual: {contador_pacientes_con_correccion}")
        else: 
            print("3.no hay pacientes que utilicen correccion visual")

def sistema_gestion():
    pacientes = cargar_pacientes()
    parar=False
    while not parar:
        print(texto_menu_1)
        opcion = input("Seleccione una opción:")
        if opcion == "1":
            print("ejecutando registrar paciente")
            registro_de_pacientes(pacientes)
        elif opcion == "2":
            print("ejecutando consultar paciente")
            consulta_de_pacientes(pacientes)
        elif opcion == "3":
            print("ejecutando mostrar pacientes registrados")
            mostrar_pacientes_registrados(pacientes)
        elif opcion == "4":
            print("ejecutando buscar pacientes con correccion visual")
            busqueda_de_pacientes(pacientes)
        elif opcion == "5":
            print("ejecutando generar estadisticas")
            estadisticas_de_la_jornada(pacientes)
        elif opcion == "6":
            print("ejecutando salir")
            parar = True
        else:
            print(f"la opcion {opcion} no es valida")

if __name__ == '__main__':
    sistema_gestion()