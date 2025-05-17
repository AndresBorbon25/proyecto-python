"""Este módulo contiene una función para saludar y otra para dividir dos números."""

def saludar(nombre):
    """Imprime un saludo personalizado."""
    print("Hola " + nombre)

def dividir(a, b):
    """Devuelve la división entre a y b. Muestra un error si b es 0."""
    if b == 0:
        print("Error: división por cero")
        return None
    return a / b


if __name__ == "__main__":
    saludar("Mundo")
    print(dividir(10, 0))

