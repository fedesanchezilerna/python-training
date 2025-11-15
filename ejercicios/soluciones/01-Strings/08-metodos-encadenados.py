# Ejercicio 8: Métodos Encadenados (Difícil)
# Crea una variable `texto = "  python programming  "`.
# - Elimina los espacios en blanco con `.strip()`
# - Conviértelo a mayúsculas
# - Reemplaza "PROGRAMMING" por "ROCKS" usando `.replace()`
# - Todo en una sola línea usando encadenamiento de métodos

print("Ejercicio 8: Métodos Encadenados")

textoOriginal = "  python programming  "
print(f"Texto original: '{textoOriginal}'")

# Paso por paso
paso1 = textoOriginal.strip()
print(f"Después de strip(): '{paso1}'")

paso2 = paso1.upper()
print(f"Después de upper(): '{paso2}'")

paso3 = paso2.replace("PROGRAMMING", "ROCKS")
print(f"Después de replace(): '{paso3}'")

# Todo encadenado en una sola línea
textoEncadenado = textoOriginal.strip().upper().replace("PROGRAMMING", "ROCKS")
print(f"\nEncadenado en una línea: '{textoEncadenado}'")

# Verificar textos iguales
print(f"Textos iguales? {paso3 == textoEncadenado}")