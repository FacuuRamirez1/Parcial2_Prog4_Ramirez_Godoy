# =============
#   FUNCIONES
# =============
import os
import csv

equipos_LP = []
equipos_PN = []
equipos_FA = []

# ==== para mostrar rutas de directorios y archivos ====
def listar_archivos(directorio):
    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                print(f'\nDirectorio: {ruta}')
                print("-------------------------------------------")
                listar_archivos(ruta)
            else:
                print(f'Archivo: {ruta}')

    # Manejo de errores
    except Exception as e:
        print(f'❌Error al listar archivos: {e}.')



# === Mostrar equipos según liga elegida ===
def mostrar_equipos(directorio):
    while True:
        print("\n-------------------")
        print("  Elija una liga:  ")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Todas las ligas")
        print("5. Volver")

        try:
            liga = int(input("Seleccione una opción (1-5): "))
            match liga:
                case 1:
                    print("\n----------------------------------")
                    print("  Equipos de la Liga Profesional  ")
                    print("----------------------------------")
                    most_liga(directorio, "equipos_LP.csv", "Liga Profesional")
                    break
                case 2:
                    print("\n----------------------------------")
                    print("  Equipos de la Primera Nacional  ")
                    print("----------------------------------")
                    most_liga(directorio,"equipos_PN.csv", "Primera Nacional")
                    break
                case 3:
                    print("\n-----------------------------")
                    print("    Equipos del Federal A    ")
                    print("-----------------------------")
                    most_liga(directorio, "equipos_FA.csv", "Federal A")
                    break
                case 4:
                    print("\n-------------------")
                    print("  Todas las ligas  ")
                    print("-------------------")
                    most_liga(directorio, "equipos_LP.csv", "Liga Profesional")
                    most_liga(directorio, "equipos_PN.csv", "Primera Nacional")
                    most_liga(directorio, "equipos_FA.csv", "Federal A")
                    break
                case 5:
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("❌¡Error! Ingrese una opción válida.")

        # Manejo de errores
        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

# Mostrar equipos de la liga seleccionada
def most_liga(directorio, archivo, liga):
    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                most_liga(ruta, archivo, liga)

            elif elemento.lower() == archivo.lower():
                if os.path.getsize(ruta) != 0:
                    print("\n---------------------")
                    print(f' Equipos de {liga}')
                    print("-------------------")
                    with open(ruta, "r", encoding="utf-8") as liga:
                        reader = csv.DictReader(liga, fieldnames=["nombre", "ciudad", "estadio"])
                        next(reader)
                        for equipo in reader:
                            print(f'Nombre: {equipo["nombre"]} | Ciudad: {equipo["ciudad"]} | Estadio: {equipo["estadio"]}')
                else:
                    print("❌¡La liga está vacía!")

    # Manejo de errores
    except FileNotFoundError:
        print("❌¡Error! Archivo no encontrado.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')





# ==== Editar liga (Hacer liga de cero) ====
def editar_liga(directorio):
    while True:
        print("\n-------------------")
        print("  Elija una liga:  ")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Volver")

        try:
            liga = int(input("Seleccione una opción (1-4): "))
            match liga:
                case 1:
                    print("\n------------------------------")
                    print("  Editar Liga Profesional  ")
                    edit_liga(directorio,"equipos_LP.csv")
                case 2:
                    print("\n------------------------------")
                    print("  Editar Primera Nacional  ")
                    edit_liga(directorio,"equipos_PN.csv")
                case 3:
                    print("\n------------------------------")
                    print("  Editar Federal A  ")
                    edit_liga(directorio, "equipos_FA.csv")
                case 4:
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("❌¡Error! Ingrese una opción válida.")

        # Manejo de errores
        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

# Editar liga específica
def edit_liga(directorio, archivo):
    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                edit_liga(ruta, archivo)

            elif elemento == archivo:
                n = int(input("¿Cuántos equipos desea agregar?: "))
                with open(ruta, "w", newline="", encoding="utf-8") as liga:
                    campos = ["nombre", "ciudad", "estadio"]
                    writer = csv.DictWriter(liga, fieldnames=campos)
                    writer.writeheader()
                    for i in range(n):
                        nombre = input("Nombre del equipo: ")
                        ciudad = input("Ciudad del equipo: ")
                        estadio = input("Estadio del equipo: ")
                        writer.writerow({
                            "nombre": nombre,
                            "ciudad": ciudad,
                            "estadio": estadio
                        })
                    print("✅ Liga editada con éxito.")

    # Manejo de errores
    except FileNotFoundError:
        print("❌¡Error! Archivo no encontrado.")
    except ValueError:
        print("❌¡Error! Ingrese un número entero.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')





# ==== Editar información de un equipo ====
def editar_equipo(directorio):
    while True:
        print("\n------------------")
        print("  Elija una liga  ")
        print("------------------")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Volver")

        try:
            liga = int(input("Seleccione una opción (1-4): "))
            match liga:
                case 1:
                    print("\n-------------------------------------")
                    print("  Editar equipo de Liga Profesional  ")
                    print("-------------------------------------")
                    equipos_LP = edit_equipo(directorio,"equipos_LP.csv", [])
                    break
                case 2:
                    print("\n-------------------------------------")
                    print("  Editar equipo de Primera Nacional  ")
                    print("-------------------------------------")
                    equipos_PN = edit_equipo(directorio,"equipos_PN.csv", [])
                    break
                case 3:
                    print("\n------------------------------")
                    print("  Editar equipo de Federal A  ")
                    print("------------------------------")
                    equipos_FA = edit_equipo(directorio, "equipos_FA.csv", [])
                    break
                case 4:
                    print("Volviendo al menú principal...")
                    break
                case _:
                    print("❌¡Error! Ingrese una opción válida.")

        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

# Editar equipo específico
def edit_equipo(directorio, archivo, lista):

    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                edit_equipo(ruta, archivo, lista)

            elif elemento.lower() == archivo.lower():
                with open(ruta, "r", encoding="utf-8") as liga:
                    reader = csv.DictReader(liga)
                    lista = [equipo for equipo in reader]

                    nom_equipo = input("Ingrese el nombre del equipo a editar: ")
                    encontrado = False
                    for equipo in lista:
                        if nom_equipo.lower() == equipo["equipo"].lower():
                            encontrado = True
                            print("Ingrese los nuevos datos:")
                            nuevo_nombre = input("Nuevo equipo: ")
                            nueva_ciudad = input("Nueva ciudad: ")
                            nuevo_estadio = input("Nuevo estadio: ")

                            equipo["equipo"] = nuevo_nombre
                            equipo["ciudad"] = nueva_ciudad
                            equipo["estadio"] = nuevo_estadio
                    if encontrado:
                        with open(ruta, "w", newline="", encoding="utf-8") as liga:
                            campos = ["equipo", "ciudad", "estadio"]
                            writer = csv.DictWriter(liga, fieldnames=campos)
                            writer.writeheader()
                            writer.writerows(lista)
                        print("✅ Equipo editado con éxito.")
                        
                    else:
                        print("❌¡Equipo no encontrado!")
                return lista

    # Manejo de errores
    except FileNotFoundError:
        print("❌¡Error! Archivo no encontrado.")
    except ValueError:
        print("❌¡Error! Ingrese un número entero.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')


# ==== Eliminar equipo según liga elegida ====
def eliminar_equipo(directorio,):
    while True:
        print("\n-------------------")
        print(" ---Elegir liga:--- ")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Volver")

        try:
            elegir_liga = int(input("Elija una opción:"))
            match elegir_liga:
                case 1:
                    print("\n------------------------------")
                    print("Eliminar equipo de la Liga Profesional")
                    elim_equipo(directorio, "equipos_LP.csv")
                    break

                case 2:
                    print("\n------------------------------")
                    print("Eliminar equipo de Primera Nacional")
                    elim_equipo(directorio, "equipos_PN.csv")
                    break

                case 3:
                    print("\n------------------------------")
                    print("Eliminar equipo de Federal A")
                    elim_equipo(directorio, "equipos_FA.csv")
                    break

                case 4:
                    print("---Redirigiendo al menú principal...---")
                    break

                case _:
                    print("❌¡Error! Ingrese una opción válida.")

        #Manejo de errores        
        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

# Eliminar equipo específico
def elim_equipo(directorio, archivo):
    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                elim_equipo(ruta, archivo)

            elif elemento.lower() == archivo.lower():
                equipos = []
                with open(ruta, "r", encoding="utf-8") as liga:
                    reader = csv.DictReader(liga)
                    equipos = [equipo for equipo in reader]

                nom_equipo = input("Ingrese el nombre del equipo a eliminar: ")
                nuevo_lista = [equipo for equipo in equipos if equipo["equipo"].lower() != nom_equipo.lower()]

                if len(equipos) == len(nuevo_lista):
                    print("❌¡Equipo no encontrado!")
                else:
                    with open(ruta, "w", newline="", encoding="utf-8") as liga:
                        campos = ["equipo", "ciudad", "estadio"]
                        writer = csv.DictWriter(liga, fieldnames=campos)
                        writer.writeheader()
                        writer.writerows(nuevo_lista)
                    print("✅ Equipo eliminado con éxito.")

    #Manejo de errores
    except ValueError:
        print("❌¡Error! Ingrese un número entero.")
    except FileNotFoundError:
        print("❌ ¡Error! Archivo no encontrado.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')


# ==== Agregar equipo a una liga ====
def agregar_equipo(directorio):
    while True:
        print("\n---------------")
        print("  Elegir liga  ")
        print("---------------")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Volver")

        try:
            elegir_liga = int(input("Elija una opción:"))
            match elegir_liga:
                case 1:
                    print("\n------------------------------")
                    print(" Agregar equipo a Liga Profesional ")
                    agr_equipo(directorio, "equipos_LP.csv")
                    break

                case 2:
                    print("\n------------------------------")
                    print(" Agregar equipo a Primera Nacional ")
                    agr_equipo(directorio, "equipos_PN.csv")
                    break

                case 3:
                    print("\n------------------------------")
                    print(" Agregar equipo a Federal A ")
                    agr_equipo(directorio, "equipos_FA.csv")
                    break

                case 4:
                    print("\n------------------------------")
                    print(" Volviendo al menú principal... ")
                    break

                case _:
                    print("❌¡Error! Ingrese una opción válida.")

        #Manejo de errores
        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except FileNotFoundError:
            print("❌ ¡Error! Archivo no encontrado.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

def agr_equipo(directorio, archivo):
    for elemento in os.listdir(directorio):
                ruta = os.path.join(directorio, elemento)
                if os.path.isdir(ruta):
                    agr_equipo(ruta, archivo)

                elif elemento == archivo:
                    #Acá se leen los equipos existentes
                    equipos_ex = []
                    with open(ruta, "r", encoding="utf-8") as liga:
                        lector = csv.DictReader(liga)
                        for eq in lector:
                            equipos_ex.append(eq["equipo"].lower())

                    equipo = input("Nombre del equipo:").strip()
                    if equipo.lower() in equipos_ex:
                        print("❌ Ese equipo ya existe en esta liga.")
                        return
                    
                    ciudad = input("Ciudad del equipo:").strip()
                    estadio = input("Estadio del equipo:").strip()

                    with open(ruta, "a", newline="", encoding="utf-8") as liga:
                        campos = ["equipo", "ciudad", "estadio"]
                        writer = csv.DictWriter(liga, fieldnames=campos)
                        writer.writerow({
                            "equipo": equipo,
                            "ciudad": ciudad,
                            "estadio": estadio
                        })

                    print("✅ Equipo agregado con éxito.")