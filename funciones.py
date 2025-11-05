# =============
#   FUNCIONES
# =============
import os
import csv

# ==== ¡EN DUDA SI SE USA O NO! ====
equipos_LP = []
equipos_PN = []
equipos_FA = []

# ==== ¡EN DUDA SI SE USA O NO! ====
def cargar_datos(directorio, archivo, lista):
    pass

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
                    most_liga(directorio, "equipos_LP.csv", "Liga Profesional")
                    break
                case 2:
                    print("\n----------------------------------")
                    print("  Equipos de la Primera Nacional  ")
                    most_liga(directorio,"equipos_PN.csv", "Primera Nacional")
                    break
                case 3:
                    print("\n-----------------------------")
                    print("    Equipos del Federal A    ")
                    most_liga(directorio, "equipos_FA.csv", "Federal A")
                    break
                case 4:
                    print("\n-------------------")
                    print("  Todas las ligas  ")
                    print("-------------------")
                    most_liga(directorio, "liga_profesional.csv", "Liga Profesional")
                    most_liga(directorio, "primera_nacional.csv", "Primera Nacional")
                    most_liga(directorio, "federal_a.csv", "Federal A")
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
                    print("  Editar equipo de Liga Profesional  ")
                    equipos_LP = edit_equipo(directorio,"equipos_LP.csv", equipos_LP)
                case 2:
                    print("\n------------------------------")
                    print("  Editar equipo de Primera Nacional  ")
                    equipos_PN = edit_equipo(directorio,"equipos_PN.csv", equipos_PN)
                case 3:
                    print("\n------------------------------")
                    print("  Editar equipo de Federal A  ")
                    equipos_FA = edit_equipo(directorio, "equipos_FA.csv", equipos_FA)
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
def edit_equipo(directorio, archivo, lista_liga):

    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                edit_liga(ruta, archivo)

            elif elemento == archivo:
                with open(ruta, "r", encoding="utf-8") as liga:
                    reader = csv.DictReader(liga)
                    for equipo in reader:
                        lista_liga.append({
                            "nombre":equipo["nombre"],
                            "ciudad":equipo["ciudad"],
                            "estadio":equipo["estadio"]
                        })

                        nom_equipo = input("Ingrese el nombre del equipo a editar: ")
                        encontrado = False
                        for equipo in lista_liga:
                            if nom_equipo.lower() == equipo["nombre"].lower():
                                print("Ingrese los nuevos datos:")
                                nuevo_nombre = input("Nuevo nombre: ")
                                nueva_ciudad = input("Nueva ciudad: ")
                                nuevo_estadio = input("Nuevo estadio: ")

                                equipo["nombre"] = nuevo_nombre
                                equipo["ciudad"] = nueva_ciudad
                                equipo["estadio"] = nuevo_estadio

                                with open(ruta, "w", newline="", encoding="utf-8") as liga:
                                    campos = ["nombre", "ciudad", "estadio"]
                                    writer = csv.DictWriter(liga, fieldnames=campos)
                                    writer.writeheader()
                                    writer.writerows(lista_liga)
                                encontrado = True
                                print("✅ Equipo editado con éxito.")
                            
                            if not encontrado:
                                print("❌¡Equipo no encontrado!")
                return lista_liga

    # Manejo de errores
    except FileNotFoundError:
        print("❌¡Error! Archivo no encontrado.")
    except ValueError:
        print("❌¡Error! Ingrese un número entero.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')


# ==== Eliminar equipo según liga elegida ====
def eliminar_equipo(directorio):
    while True:
        print("\n-------------------")
        print(" ---Elegir liga:--- ")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Volver")

        try:
            elegir_liga = int(input("Elija una opción:"))
            if elegir_liga == 1:
                print("\n------------------------------")
                print("Eliminar equipo de la Liga Profesional")
                eliminar_equipo(directorio, "equipos_LP.csv")

            elif elegir_liga == 2:
                print("\n------------------------------")
                print("Eliminar equipo de Primera Nacional")
                eliminar_equipo(directorio, "equipos_PN.csv")

            elif elegir_liga == 3:
                print("\n------------------------------")
                print("Eliminar equipo de Federal A")
                eliminar_equipo(directorio, "equipos_FA.csv")

            elif elegir_liga == 4:
                print("---Redirigiendo al menú principal...---")
                break

            else:
                print("❌¡Error! Ingrese una opción válida.")
        #Manejo de errores        
        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')




# ==== Agregar equipo a una liga ====
def agregar_equipo(directorio, archivo):
    while True:
        print("\n-------------------")
        print(" ---Elegir liga:--- ")
        print("1. Liga profesional")
        print("2. Primera Nacional")
        print("3. Federal A")
        print("4. Volver")

        try:
            for elemento in os.listdir(directorio):
                ruta = os.path.join(directorio, elemento)
                if os.path.isdir(ruta):
                    agregar_equipo(ruta, archivo)

                elif elemento == archivo:
                    #Acá se leen los equipos existentes
                    equipos_ex = []
                    with open(ruta, "r", encoding="utf-8") as liga:
                        lector = csv.DictReader(liga)
                        for eq in lector:
                            equipos_ex.append(eq["nombre"].lower())

                    equipo = input("Nombre del equipo:").strip()
                    if equipo.lower() in equipos_ex:
                        print("❌ Ese equipo ya existe en esta liga.")
                        return
                    
                    ciudad = input("Ciudad del equipo:").strip()
                    estadio = input("Estadio del equipo:").strip()

                    with open(ruta, "a", newline="", encoding="utf-8") as liga:
                        campos = ["nombre", "ciudad", "estadio"]
                        writer = csv.DictWriter(liga, fieldnames=campos)
                        writer.writerow({
                            "nombre": equipo,
                            "ciudad": ciudad,
                            "estadio": estadio
                        })

                    print("✅ Equipo agregado con éxito.")

        #Manejo de errores
        except FileNotFoundError:
            print("❌ ¡Error! Archivo no encontrado.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')
