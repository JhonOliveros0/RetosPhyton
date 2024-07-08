def comprar(inventario, cantidad, capacidad_maxima, descuento_umbral):
    # Aplica descuento en compras grandes
    if cantidad > descuento_umbral:
        cantidad *= 0.9
    # Actualiza el inventario
    inventario += cantidad
    return inventario

def vender(inventario, cantidad, capacidad_maxima, limite_ventas_diarias):
    # Verifica límite de ventas diarias
    if cantidad > limite_ventas_diarias:
        print("Se ha alcanzado el límite de ventas diarias.")
        return inventario
    # Verifica restricción de ventas según stock
    if inventario < capacidad_maxima * 0.3:
        cantidad = min(cantidad, inventario * 0.5)
    # Actualiza el inventario
    inventario -= cantidad
    return inventario

def mostrar_inventario(inventario):
    print(f"Inventario actual: {inventario} unidades")

# Ejemplo de uso:
capacidad_maxima = 100
inventario_actual = 20
descuento_umbral = 15
limite_ventas_diarias = inventario_actual * 0.1

inventario_actual = comprar(inventario_actual, 20, capacidad_maxima, descuento_umbral)
inventario_actual = vender(inventario_actual, 10, capacidad_maxima, limite_ventas_diarias)
mostrar_inventario(inventario_actual)
