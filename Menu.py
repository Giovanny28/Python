# Programa: Menú interactivo de notas
# Simulación de un bucle "do while" usando while True

notas = []  # Lista para guardar las notas

while True:
    print("\n- MENÚ PRINCIPAL -")
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")
    
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        try:
            nota = float(input("Ingrese la nota: "))
            notas.append(nota)
            print("✅ Nota agregada correctamente.")
        except ValueError:
            print("⚠️ Error: debe ingresar un número válido.")

    elif opcion == "2":
        if notas:
            print("\n📋 Todas las notas:")
            for i, n in enumerate(notas, start=1):
                print(f"{i}. {n}")
        else:
            print("Aún no hay notas registradas.")

    elif opcion == "3":
        if notas:
            promedio = sum(notas) / len(notas)
            mayor = max(notas)
            menor = min(notas)
            print(f"\n📊 Promedio: {promedio:.2f}")
            print(f"🔺 Nota mayor: {mayor}")
            print(f"🔻 Nota menor: {menor}")
        else:
            print("No hay notas para calcular estadísticas.")

    elif opcion == "4":
        print("👋 Programa terminado. ¡Hasta luego!")
        break  # Sale del bucle (como el 'do while' al cumplir condición)

    else:
        print("❌ Opción no válida, intenta de nuevo.")
