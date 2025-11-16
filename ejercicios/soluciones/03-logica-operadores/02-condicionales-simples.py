# Ejercicio 2: Condicionales Simples (Fácil)
# Crea una variable `edad = 20`
# - Si edad es menor de 18, imprime "Menor de edad"
# - Si edad es entre 18 y 30, imprime "Joven"
# - Si edad es mayor de 30, imprime "Adulto"

edad = int(input("Introduce edad: "))


if 0 < edad and edad < 18:
    print("Menor de edad")
elif 18 < edad and edad < 30:
    print("Joven")
elif edad < 0:
    print("Ingresa un número positivo")
else:
    print("Adulto")