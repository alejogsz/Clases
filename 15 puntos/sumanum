def calcular_suma(lista):
    if len(lista) < 2:
        print("La lista debe contener al menos dos números.")
        return None
    
    print("Lista de números disponibles:")
    for i, numero in enumerate(lista):
        print(f"{i + 1}. {numero}")
    
    seleccionados = input("Ingrese los números que desea sumar separados por comas (por ejemplo, '1,3'): ")
    seleccionados_indices = [int(i.strip()) for i in seleccionados.split(",")]
    
    if not all(1 <= idx <= len(lista) for idx in seleccionados_indices):
        print("Índices ingresados inválidos.")
        return None
    
    suma = sum(lista[idx - 1] for idx in seleccionados_indices)
    return suma

calcular_suma()





