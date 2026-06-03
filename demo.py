def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

def main():
    print(saludar("Mundo"))
    print(f"2 + 3 = {sumar(2, 3)}")

if __name__ == "__main__":
    main()
