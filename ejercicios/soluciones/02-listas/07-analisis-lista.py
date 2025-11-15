# Ejercicio 7: Análisis de Lista (Difícil)
# Crea una lista `calificaciones = [7, 9, 8, 7, 10, 7, 6, 9, 7]`.
# - Cuenta cuántas veces aparece cada calificación (6, 7, 8, 9, 10)
# - Calcula qué porcentaje representa cada calificación
# - Encuentra la calificación que más se repite

print("Ejercicio 7: Análisi de Lista")

calificaciones = [7, 9, 8, 7, 10, 7, 6, 9, 7]

print(f"""
      Número de veces que aparece cada nota:
      6:  {calificaciones.count(6)}
      7:  {calificaciones.count(7)}
      8:  {calificaciones.count(8)}
      9:  {calificaciones.count(9)}
      10: {calificaciones.count(10)}""")

def porcentaje_nota(lista, num):
    return ((lista.count(num) * 100) / len(lista))

print(f"""
      Porcentaje de aparición cada nota:
      6:  {porcentaje_nota(calificaciones, 6):.2f}%
      7:  {porcentaje_nota(calificaciones, 7):.2f}%
      8:  {porcentaje_nota(calificaciones, 8):.2f}%
      9:  {porcentaje_nota(calificaciones, 9):.2f}%
      10: {porcentaje_nota(calificaciones, 10):.2f}%""")

nota_mas_repetida = max(set(calificaciones), key=calificaciones.count)
veces_repetida = calificaciones.count(nota_mas_repetida)

print(f"""
    La calificación que más se repite:
    Nota: {nota_mas_repetida} (aparece {veces_repetida} veces)""")
