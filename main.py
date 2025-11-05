# ======================
#   PROGRAMA PRINCIPAL  
# ======================
from funciones import *

def main(directorio):
    while True:
        print("\n==================")
        print("  MENÚ PRINCIPAL  ")
        print("==================")
        print("1. Ver directorios")
        print("2. Ver equipos")
        print("3. Editar liga")
        print("4. Editar equipo")
        print("5. Eliminar equipo")
        print("6. Agregar equipo")
        print("7. Salir")

        try:
            opc = int(input("Seleccione una opción (1-7): "))
            match opc:
                case 1:
                    print("\n--------------------")
                    print("  Ver directorios:  ")
                    listar_archivos(directorio)
                case 2:
                    print("\n----------------")
                    print("  Ver equipos:  ")
                    mostrar_equipos(directorio)
                case 3:
                    print("\n----------------")
                    print("  Editar liga:  ")
                    editar_liga(directorio)
                case 4:
                    print("\n------------------")
                    print("  Editar equipo:  ")
                    editar_equipo(directorio)
                case 5:
                    print("\n--------------------")
                    print("  Eliminar equipo:  ")
                    eliminar_equipo(directorio)
                case 6:
                    print("\n-------------------")
                    print("  Agregar equipo:  ")
                    agregar_equipo(directorio)
                case 7:
                    print("\n----------------------------")
                    print("  Saliendo del programa...  ")
                    break
                case _:
                    print("❌¡Error! Ingrese una opción válida.")
        except ValueError:
            print("❌¡Error! Ingrese un número entero.")
        except Exception as e:
            print(f'❌¡Error inesperado! {e}.')

if __name__ == "__main__":
    directorios = os.path.dirname(os.path.abspath(__file__))
    futbol_directorio = os.path.join(directorios, "Futbol_argentino")
    main(futbol_directorio)