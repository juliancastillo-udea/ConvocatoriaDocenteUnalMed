def asignar_silla(estatura_metros):
  """
  Clasifica a un estudiante en una categoría de silla (A, B o C) según su estatura.

  Args:
    estatura_metros: La estatura del estudiante en metros.

  Returns:
    Una cadena de texto indicando la categoría de la silla asignada.
    "Estatura no válida" si la estatura es menor que 1.00 m.
  """
  if estatura_metros < 1.00:
    return "Estatura no válida"
  elif 1.00 <= estatura_metros < 1.50:
    return "Silla A"
  elif 1.50 <= estatura_metros < 1.75:
    return "Silla B"
  else:  # 1.75 m o más
    return "Silla C"

# Ejemplos de uso del algoritmo
estudiante1 = 1.45
estudiante2 = 1.68
estudiante3 = 1.80
estudiante4 = 0.95

print(f"Al estudiante con una estatura de {estudiante1} m se le asigna la: {asignar_silla(estudiante1)}")
print(f"Al estudiante con una estatura de {estudiante2} m se le asigna la: {asignar_silla(estudiante2)}")
print(f"Al estudiante con una estatura de {estudiante3} m se le asigna la: {asignar_silla(estudiante3)}")
print(f"Al estudiante con una estatura de {estudiante4} m se le asigna la: {asignar_silla(estudiante4)}")