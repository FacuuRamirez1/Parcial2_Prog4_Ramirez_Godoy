# =============
#   FUNCIONES
# =============
import os

# para mostrar rutas
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


# Mostrar equipos según liga elegida
def mostrar_equipos():
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
                    most_liga("primera_nacional.csv")
                case 3:
                    print("\n------------------------------")
                    print("Equipos del Federal A")
                    most_liga("federal_a.csv")
                case 4:
                    print("\n-------------------")
                    print("  Todas las ligas  ")
                    most_liga("liga_profesional.csv")
                    most_liga("primera_nacional.csv")
                    most_liga("federal_a.csv")
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
def most_liga(archivo):
    pass


# Editar liga (Hacer liga de cero)
def editar_liga():
    pass

# Editar información de un equipo
def editar_equipo():
    pass

# Eliminar equipo según liga elegida
def eliminar_equipo():
    pass

# Agregar equipo a una liga
def agregar_equipo():
    pass