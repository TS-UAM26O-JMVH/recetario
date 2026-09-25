from recetas import receta_pasta
# AQui se itan importando mas recetas a medida que se agreguen

def mostrar_menu():
	print("recetario disponible:")
	print("1. Pasta al ajo")
	#Agrega aqui tu receta con un numero nuevo

	opcion = input("Elige una receta (numero): ")
	
	if opcion == "1":
		receta_pasta()
	else:
		print("Opcion no valida. Intenta de nuevo")

if __name__ == "__main__":
	mostrar_menu()

---

### recetas.py

# Aqui van las recetas de todos los participantes

def receta_pasta():
    print(" Receta: Pasta al ajo")
    print("Ingredientes: pasta, tomate, ajo, aceite de oliva")
    print("Pasos:")
    print("1. Hervir la pasta.")
    print("2. Freír el ajo y tomate en aceite.")
    print("3. Mezclar todo y servir caliente.")

# Agrega tu receta debajo de esta línea
# Ejemplo:
# def receta_tacos():
#     print(" Receta: Tacos de pollo")
#     print("Ingredientes: tortillas, pollo, cebolla, cilantro")
#     print("Pasos: Cocinar el pollo, calentar las tortillas, armar los tacos.")
