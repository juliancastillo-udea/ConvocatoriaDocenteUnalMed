# Programa para clasificar estudiantes y asignar silla ergonómica
# Universidad Nacional - Empresa Sillas&Sillas

# Entrada de datos
estatura = float(input("Ingrese la estatura del estudiante en metros (Ej: 1.68): "))

# Clasificación según los rangos de estatura
if 1.00 <= estatura < 1.50:
    categoria = "A"
    silla = "Silla A (1.00 m - 1.50 m)"
elif 1.50 <= estatura < 1.75:
    categoria = "B"
    silla = "Silla B (1.50 m - 1.75 m)"
elif estatura >= 1.75:
    categoria = "C"
    silla = "Silla C (1.75 m en adelante)"
else:
    categoria = None
    silla = "Estatura fuera de rango válido."

# Salida de datos
if categoria:
    print(f"Categoría: {categoria}")
    print(f"Asignación: {silla}")
else:
    print("La estatura ingresada no es válida. Debe ser mayor o igual a 1.00 m.")