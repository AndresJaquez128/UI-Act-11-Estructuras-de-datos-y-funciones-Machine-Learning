
# ============================================================
# Inicio de codigo: jaquez andres 0074
# Actividad: P8 - Funciones en Python
# Grupo: 3H_IA
# ============================================================

# 1. Funcion basica
def saludar():
    print("Hola, bienvenido a Python")


# 2. Funcion con un parametro
def saludar_persona(nombre):
    print(f"Hola, {nombre}")


# 3. Funcion con dos parametros
def sumar(a, b):
    return a + b


# 4. Funcion para restar
def restar(a, b):
    return a - b


# 5. Funcion para multiplicar
def multiplicar(a, b):
    return a * b


# 6. Funcion para calcular el area de un rectangulo
def area_rectangulo(base, altura):
    return base * altura


# 7. Parametros con valores por defecto
def presentar(nombre="Estudiante"):
    print(f"Mi nombre es {nombre}")


# 8. Parametro por defecto para un saludo
def saludo_personalizado(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")


# 9. Parametros por defecto para una operacion
def potencia(base, exponente=2):
    return base ** exponente


# 10. Funcion que determina si un numero es par
def es_par(numero):
    return numero % 2 == 0


# 11. Funcion que calcula el promedio
def promedio(a, b, c):
    return (a + b + c) / 3


# 12. Funcion que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 13. Funcion que encuentra el mayor de dos numeros
def mayor(a, b):
    return a if a > b else b


# 14. Funcion que cuenta caracteres
def contar_caracteres(texto):
    return len(texto)


# 15. Funcion que convierte texto a mayusculas
def convertir_mayusculas(texto):
    return texto.upper()


# 16. Funcion que calcula el factorial de forma iterativa
def factorial_iterativo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


# 17. Funcion lambda para sumar
sumar_lambda = lambda a, b: a + b


# 18. Funcion lambda para elevar al cuadrado
cuadrado_lambda = lambda numero: numero ** 2


# 19. Funcion lambda para comprobar si un numero es positivo
positivo_lambda = lambda numero: numero > 0


# 20. Funcion recursiva para calcular el factorial
def factorial_recursivo(numero):
    if numero < 0:
        raise ValueError("El numero debe ser positivo")
    if numero <= 1:
        return 1
    return numero * factorial_recursivo(numero - 1)


# 21. Funcion recursiva para calcular Fibonacci
def fibonacci(numero):
    if numero < 0:
        raise ValueError("El numero debe ser positivo")
    if numero <= 1:
        return numero
    return fibonacci(numero - 1) + fibonacci(numero - 2)


# 22. Decorador que muestra un mensaje antes de ejecutar
def mi_decorador(funcion):
    def envoltura():
        print("Iniciando funcion...")
        funcion()
        print("Funcion finalizada.")
    return envoltura


@mi_decorador
def mostrar_mensaje():
    print("Esta funcion utiliza un decorador")


# 23. Funcion para calcular el precio con descuento
def aplicar_descuento(precio, descuento=10):
    return precio - (precio * descuento / 100)


# 24. Funcion para calcular el IMC
def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero")
    return peso / (altura ** 2)


# 25. Funcion para obtener el numero mayor de una lista
def mayor_lista(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacia")
    return max(numeros)


# 26. Funcion para filtrar numeros pares
def filtrar_pares(numeros):
    return [numero for numero in numeros if numero % 2 == 0]


# 27. Funcion para contar palabras
def contar_palabras(texto):
    return len(texto.split())


# 28. Funcion para calcular el total de una compra
def total_compra(precios, impuesto=0):
    return sum(precios) * (1 + impuesto / 100)


# 29. Funcion para verificar una contrasena basica
def contrasena_valida(contrasena):
    return len(contrasena) >= 8


# 30. Funcion para calcular el promedio de una lista
def promedio_lista(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacia")
    return sum(numeros) / len(numeros)


# ============================================================
# Pruebas de las funciones
# ============================================================

if __name__ == "__main__":
    print("\n--- FUNCIONES BASICAS ---")
    saludar()
    saludar_persona("Andres Jaquez")
    print("Suma:", sumar(5, 3))
    print("Resta:", restar(8, 2))
    print("Multiplicacion:", multiplicar(4, 3))
    print("Area del rectangulo:", area_rectangulo(5, 4))

    print("\n--- PARAMETROS POR DEFECTO ---")
    presentar()
    presentar("Andres")
    saludo_personalizado("Andres")
    saludo_personalizado("Andres", "Buenos dias")
    print("Potencia:", potencia(5))
    print("Potencia con exponente:", potencia(5, 3))

    print("\n--- OTROS EJEMPLOS ---")
    print("¿Es par el 8?:", es_par(8))
    print("Promedio:", promedio(8, 9, 10))
    print("25 Celsius a Fahrenheit:", celsius_a_fahrenheit(25))
    print("Mayor:", mayor(10, 20))
    print("Caracteres:", contar_caracteres("Python"))
    print("Mayusculas:", convertir_mayusculas("hola mundo"))
    print("Factorial iterativo:", factorial_iterativo(5))

    print("\n--- FUNCIONES LAMBDA ---")
    print("Suma lambda:", sumar_lambda(4, 6))
    print("Cuadrado lambda:", cuadrado_lambda(5))
    print("¿Es positivo?:", positivo_lambda(7))

    print("\n--- RECURSIVIDAD ---")
    print("Factorial recursivo de 5:", factorial_recursivo(5))
    print("Fibonacci de 6:", fibonacci(6))

    print("\n--- DECORADORES ---")
    mostrar_mensaje()

    print("\n--- EJEMPLOS ADICIONALES ---")
    print("Precio con descuento:", aplicar_descuento(200))
    print("IMC:", round(calcular_imc(70, 1.75), 2))
    print("Mayor de la lista:", mayor_lista([4, 9, 2, 7]))
    print("Numeros pares:", filtrar_pares([1, 2, 3, 4, 5, 6]))
    print("Cantidad de palabras:", contar_palabras("Python es facil de aprender"))
    print("Total de compra:", total_compra([100, 200, 50], 16))
    print("Contrasena valida:", contrasena_valida("python123"))
    print("Promedio de lista:", promedio_lista([8, 9, 10]))


# ============================================================
# Final de codigo: jaquez andres 0074
# ============================================================