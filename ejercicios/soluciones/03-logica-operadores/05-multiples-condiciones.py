# Ejercicio 5: Múltiples Condiciones (Medio-Difícil)
# Crea un programa que pida edad y altura (en metros).
# - Si edad < 18 AND altura < 1.50, imprime "Niño pequeño"
# - Si edad >= 18 OR altura >= 1.80, imprime "Adulto o persona alta"
# - Usa `not` para verificar alguna condición negativa

edad = int(input("Introduce edad: "))
altura = float(input("Introduce altura en m: "))

if edad < 18 and altura < 1.50:
    print("Niño pequeño")
    
if edad >= 18 or not altura <= 1.80:
    print("Adulto o persona alta")