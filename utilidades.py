"""Este módulo contiene funciones matemáticas básicas: suma, resta, multiplicación, división."""

def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b

def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b

def multiplicar(a, b):
    """Devuelve el producto de a y b."""
    return a * b

def dividir(a, b):
    """Devuelve la división de a entre b. Si b es 0, devuelve un mensaje de error."""
    if b == 0:
        return "Error: división por cero"
    return a / b

def operacion_innecesaria(x):
    """Siempre retorna True. Solo se mantiene para propósitos ilustrativos."""
    return True
