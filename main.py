from recetas import receta_pasta, receta_ensalada, receta_hotcakes
# Aqui se iran importando mas recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    print("Ensalada")
    print("Hotcakes caseros")

    # Agrega aqui tu receta con un numero nuevo

    opcion = input("Elige una receta (numero): ")

    if opcion == "1":
        receta_pasta()
    elif opcion == "2":
        receta_ensalada()
    elif opcion == "3":
        recetas_hotcakes()
    else:
        print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
