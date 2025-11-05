# =============
#   FUNCIONES
# =============
import os
import csv

# ==== ¡EN DUDA SI SE USA O NO! ====
equipos_LP = []
equipos_NP = []
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
                print(f'\nDirectorio padre: {ruta}')
                print("-------------------------------------------")
                listar_archivos(ruta)
            else:
                print(ruta)

    # Manejo de errores
    except FileNotFoundError:
        print("❌¡Error! Archivo no encontrado.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')





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
            liga = int(input("Seleccione una opción (1-4): "))
            match liga:
                case 1:
                    print("\n------------------------------")
                    print("Equipos de la Liga Profesional")
                    most_liga("liga_profesional.csv")
                case 2:
                    print("\n------------------------------")
                    print("Equipos de la Primera Nacional")
                    most_liga(directorio,"primera_nacional.csv")
                case 3:
                    print("\n------------------------------")
                    print("Equipos del Federal A")
                    most_liga(directorio, "federal_a.csv")
                case 4:
                    print("\n-------------------")
                    print("  Todas las ligas  ")
                    most_liga(directorio, "liga_profesional.csv")
                    most_liga(directorio, "primera_nacional.csv")
                    most_liga(directorio, "federal_a.csv")
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
def most_liga(directorio, archivo):
    try:
        for elemento in os.listdir(directorio):
            ruta = os.path.join(directorio, elemento)
            if os.path.isdir(ruta):
                pass
                most_liga(ruta)
            else:
                print("\n---------------------")
                print(f' Equipos de {archivo}')

                ruta_csv = os.path.join(directorio, archivo)
                with open(ruta_csv, "r", encoding="utf-8") as liga:
                    reader = csv.DictReader(liga)
                    for equipo in reader:
                        print(f'Nombre: {equipo["nombre"]} | Ciudad: {equipo["ciudad"]} | Estadio: {equipo["estadio"]}')

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
                    edit_liga(directorio,"liga_profesional.csv")
                case 2:
                    print("\n------------------------------")
                    print("  Editar Primera Nacional  ")
                    edit_liga(directorio,"primera_nacional.csv")
                case 3:
                    print("\n------------------------------")
                    print("  Editar Federal A  ")
                    edit_liga(directorio, "federal_a.csv")
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
                with open(ruta, "w", encoding="utf-8") as liga:
                    writer = csv.DictWriter(liga)
                    for equipo in range(n):
                        nombre = input("Nombre del equipo: ")
                        ciudad = input("Ciudad del equipo: ")
                        estadio = input("Estadio del equipo: ")
                        writer.writerow({
                            "nombre": nombre,
                            "ciudad": ciudad,
                            "estadio": estadio
                        })

    # Manejo de errores
    except FileNotFoundError:
        print("❌¡Error! Archivo no encontrado.")
    except ValueError:
        print("❌¡Error! Ingrese un número entero.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}.')





# ==== Editar información de un equipo ====
def editar_equipo():
    pass





# ==== Eliminar equipo según liga elegida ====
def eliminar_equipo():
    pass





# ==== Agregar equipo a una liga ====
def agregar_equipo():
    pass