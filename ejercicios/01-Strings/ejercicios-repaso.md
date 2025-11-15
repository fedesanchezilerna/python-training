# Ejercicios Python - Repaso para Examen

## 📝 Ejercicios de Strings

### Ejercicio 1: Métodos Básicos de Cadenas (Fácil)
Crea una variable `mensaje` con el texto "bienvenido a python" y muestra:
- El mensaje con la primera letra en mayúscula
- El mensaje completamente en mayúsculas
- El mensaje completamente en minúsculas
- Si el mensaje comienza con "bien"
- Cuántas veces aparece la letra "n"

### Ejercicio 2: Validación de Datos (Fácil)
Pide al usuario que ingrese un código. Verifica:
- Si el código es numérico usando `isnumeric()`
- Si el código está completamente en mayúsculas
- La longitud del código

### Ejercicio 3: Comparación de Cadenas (Medio)
Crea dos variables: `palabra1 = "Manzana"` y `palabra2 = "manzana"`.
- Compara si son iguales
- Usa el operador `not` para verificar si NO son iguales
- Muestra los códigos ASCII del primer carácter de cada una usando `ord()`
- Explica en un comentario por qué "M" es diferente de "m"

### Ejercicio 4: Operador NOT con Strings (Medio)
Crea una variable `nombre = ""` (cadena vacía).
- Usa `not` para verificar si el nombre está vacío
- Pide al usuario un nombre, y usa `not` para verificar si NO comienza con "A"
- Usa `not` para verificar si el nombre NO contiene solo números

### Ejercicio 5: Análisis de Texto (Medio)
Crea una variable `frase = "Python es genial"`.
- Cuenta cuántas veces aparece la letra "e"
- Verifica si la frase comienza con "Python"
- Convierte la frase a mayúsculas y guárdala en otra variable
- Compara ambas variables usando `==` y `!=`

### Ejercicio 6: Validación con NOT (Medio-Difícil)
Crea un programa que pida una contraseña al usuario. La contraseña es válida si:
- NO está vacía
- NO es completamente numérica
- NO es menor de 6 caracteres
Usa el operador `not` en las validaciones.

### Ejercicio 7: Comparaciones ASCII (Difícil)
Escribe un programa que:
- Pida dos palabras al usuario
- Compare cuál es "mayor" alfabéticamente
- Muestre el código ASCII del primer carácter de cada palabra
- Explique por qué una es mayor que la otra

### Ejercicio 8: Métodos Encadenados (Difícil)
Crea una variable `texto = "  python programming  "`.
- Elimina los espacios en blanco con `.strip()`
- Conviértelo a mayúsculas
- Reemplaza "PROGRAMMING" por "ROCKS" usando `.replace()`
- Todo en una sola línea usando encadenamiento de métodos

### Ejercicio 9: Búsqueda en Texto (Difícil)
Crea una variable con tu nombre completo. Escribe un programa que:
- Cuente cuántas vocales (a,e,i,o,u) hay en tu nombre
- Use el operador `not` para verificar que NO hay números en el nombre
- Muestre el nombre con cada palabra capitalizada

### Ejercicio 10: Comparación Compleja (Difícil)
Crea tres variables: `a = "abc"`, `b = "ABC"`, `c = "abc"`.
- Verifica si `a == c` y `a != b`
- Usa `not` para verificar que `a` NO es mayor que `c`
- Convierte `b` a minúsculas y compárala con `a`
- Muestra los resultados explicando cada comparación

---

## 📋 Ejercicios de Listas

### Ejercicio 1: Creación y Acceso Básico (Fácil)
Crea una lista llamada `frutas` con 5 frutas diferentes.
- Muestra la lista completa
- Muestra el primer elemento
- Muestra el último elemento usando índice negativo
- Muestra la longitud de la lista

### Ejercicio 2: Lista de Números (Fácil)
Crea una lista `numeros = [10, 20, 30, 40, 50]`.
- Accede al tercer elemento
- Accede al penúltimo elemento
- Muestra el tipo de dato de la lista
- Muestra el tipo de dato del primer elemento

### Ejercicio 3: Método count() (Medio)
Crea una lista `valores = [5, 8, 5, 3, 8, 5, 9, 8, 5]`.
- Cuenta cuántas veces aparece el número 5
- Cuenta cuántas veces aparece el número 8
- Muestra la proporción de 5s sobre el total (como porcentaje)

### Ejercicio 4: Desempaquetado Simple (Medio)
Crea una lista `datos = [18, "Juan", "Pérez", True]`.
- Desempaqueta la lista en variables: edad, nombre, apellido, estudiante
- Muestra cada variable con un mensaje descriptivo
- Usa f-strings para crear una frase con toda la información

### Ejercicio 5: Lista Mixta (Medio)
Crea una lista con tu edad, altura, nombre y apellido (como en las actividades).
- Muestra la longitud de la lista
- Accede a cada elemento por su índice
- Desempaqueta la lista en variables apropiadas
- Crea una frase presentándote con esos datos

### Ejercicio 6: Operador NOT con Listas (Medio-Difícil)
Crea dos listas: `lista1 = [1, 2, 3]` y `lista2 = [4, 5, 6]`.
- Usa `not` para verificar si lista1 NO está vacía
- Verifica si lista1 NO es igual a lista2
- Crea una lista vacía y usa `not` para comprobar que está vacía

### Ejercicio 7: Análisis de Lista (Difícil)
Crea una lista `calificaciones = [7, 9, 8, 7, 10, 7, 6, 9, 7]`.
- Cuenta cuántas veces aparece cada calificación (6, 7, 8, 9, 10)
- Calcula qué porcentaje representa cada calificación
- Encuentra la calificación que más se repite

### Ejercicio 8: Desempaquetado Inverso (Difícil)
Crea una lista `persona = [25, 1.70, "Ana", "García"]`.
- Desempaqueta en orden normal
- Desempaqueta en orden inverso usando `[::-1]`
- Desempaqueta solo el nombre y apellido (ignorando edad y altura)

### Ejercicio 9: Lista con Range (Difícil)
- Crea una lista con números del 1 al 20 usando `range()`
- Cuenta cuántos números pares hay (pista: usa un bucle o count con módulo)
- Muestra solo los primeros 5 elementos
- Muestra solo los últimos 5 elementos

### Ejercicio 10: Manipulación Compleja (Difícil)
Crea una lista `numeros = [3, 7, 3, 9, 3, 7, 3, 5]`.
- Cuenta todas las apariciones de cada número único
- Calcula el total de elementos
- Determina qué número es el más frecuente
- Usa el operador `not` para verificar que el número 10 NO está en la lista

---

## 🎯 Ejercicios de Lógica y Operadores

### Ejercicio 1: Operador NOT Básico (Fácil)
Escribe 5 ejemplos usando el operador `not`:
- Con comparación numérica (>, <, ==)
- Con comparación de strings
- Con un valor booleano directo
- Con una cadena vacía
- Con una lista vacía

### Ejercicio 2: Condicionales Simples (Fácil)
Crea una variable `edad = 20`.
- Si edad es menor de 18, imprime "Menor de edad"
- Si edad es entre 18 y 30, imprime "Joven"
- Si edad es mayor de 30, imprime "Adulto"

### Ejercicio 3: Operadores Lógicos AND/OR (Medio)
Crea variables: `edad = 25`, `es_estudiante = True`.
- Verifica si edad es >= 18 AND es_estudiante es True
- Verifica si edad es < 18 OR edad > 65
- Usa `not` para verificar que NO es menor de edad

### Ejercicio 4: Validación de Entrada (Medio)
Pide al usuario un número.
- Verifica que NO esté vacío
- Verifica que sea numérico
- Si es válido, conviértelo a entero y verifica si es par o impar

### Ejercicio 5: Múltiples Condiciones (Medio-Difícil)
Crea un programa que pida edad y altura (en metros).
- Si edad < 18 AND altura < 1.50, imprime "Niño pequeño"
- Si edad >= 18 OR altura >= 1.80, imprime "Adulto o persona alta"
- Usa `not` para verificar alguna condición negativa

### Ejercicio 6: Clasificación Compleja (Difícil)
Pide al usuario tres calificaciones y clasifícalas:
- Si todas son >= 7: "Aprobado con buenas notas"
- Si alguna es < 5: "Reprobado"
- Si el promedio es >= 6 pero < 7: "Aprobado justo"
Usa operadores lógicos y el operador `not` donde sea apropiado.

### Ejercicio 7: Validador de Contraseña (Difícil)
Pide una contraseña y verifica que:
- NO esté vacía
- Tenga al menos 8 caracteres
- NO sea completamente numérica
- NO sea "password" o "12345678"
Usa múltiples condiciones con `not`, `and`, y `or`.

### Ejercicio 8: Comparador de Strings con Lógica (Difícil)
Pide dos palabras al usuario:
- Compara si son iguales (case-insensitive)
- Usa `not` para verificar que NO son exactamente iguales (case-sensitive)
- Compara cuál es mayor alfabéticamente
- Si ninguna comienza con vocal, muestra un mensaje especial

### Ejercicio 9: Analizador de Listas (Difícil)
Crea una lista `datos = [10, 20, 30, 40, 50]`.
- Verifica que la lista NO esté vacía
- Verifica que el primer elemento NO sea cero
- Verifica que la longitud sea exactamente 5
- Si todas las condiciones son True, suma todos los elementos

### Ejercicio 10: Sistema de Decisión Completo (Muy Difícil)
Crea un mini-programa que:
- Pida nombre, edad, y si es estudiante
- Valide que el nombre NO esté vacío y NO sea numérico
- Valide que la edad sea un número entre 0 y 120
- Determine el precio de una entrada:
  - Menores de 12 o mayores de 65: $5
  - Estudiantes entre 12 y 25: $8
  - Otros: $12
- Use `not`, `and`, `or` en las validaciones

---

## 🎁 Ejercicios Integradores (Combinan todos los temas)

### Ejercicio Integrador 1: Registro de Persona (Medio)
Crea un programa que:
- Pida nombre, edad, altura y ciudad al usuario
- Guarde los datos en una lista
- Desempaquete la lista
- Valide que el nombre NO sea numérico
- Muestre un resumen usando f-strings con los datos capitalizados

### Ejercicio Integrador 2: Analizador de Texto (Difícil)
Pide una frase al usuario:
- Cuenta cuántas palabras tiene (pista: usa `.split()`)
- Verifica que NO esté vacía
- Convierte a mayúsculas y cuenta las vocales
- Determina si es una frase corta (<5 palabras), media (5-10) o larga (>10)

### Ejercicio Integrador 3: Sistema de Calificaciones (Muy Difícil)
Crea un programa completo:
- Pide nombre del estudiante y 3 calificaciones
- Guarda los datos en una lista
- Valida que las calificaciones sean números entre 0 y 10
- Calcula el promedio
- Usa condicionales para determinar: Reprobado, Aprobado, Notable, Sobresaliente
- Cuenta cuántas calificaciones son >= 7
- Muestra un reporte completo usando todo lo aprendido

---

**Consejos para el examen:**
1. Recuerda que Python es case-sensitive: "Hola" ≠ "hola"
2. Los índices negativos acceden desde el final: -1 es el último
3. El operador `not` invierte el valor booleano
4. El desempaquetado requiere igual número de variables que elementos en la lista
5. Los métodos de strings como `.upper()`, `.lower()`, `.capitalize()` son muy útiles
6. `count()` es perfecto para contar repeticiones
7. `len()` funciona con strings, listas, tuplas y más
8. `ord()` te da el código ASCII de un carácter
9. Las comparaciones de strings se hacen carácter por carácter usando ASCII
10. Practica combinando `not`, `and`, `or` en condiciones complejas

¡Buena suerte en el examen! 🚀