# Script para clasificar estudiantes y asignar sillas ergonómicas
# Universidad Nacional - Sillas&Sillas

print("=== CLASIFICADOR DE SILLAS ERGONÓMICAS ===")
print("Grupo A - Silla A: 1.00m a 1.50m")
print("Grupo B - Silla B: 1.50m a 1.75m") 
print("Grupo C - Silla C: 1.75m en adelante")
print("-" * 45)

# Solicitar la estatura del estudiante
estatura = float(input("Ingrese la estatura del estudiante en metros: "))

# Clasificación usando condicionales
if estatura < 1.0:
    print(f"Estatura {estatura}m está fuera del rango mínimo")
    print("No hay silla disponible para esta estatura")

elif estatura >= 1.0 and estatura < 1.5:
    print(f"Estatura: {estatura}m")
    print("Grupo: A")
    print("Silla asignada: Silla A")
    print("Rango: Entre 1.00m y 1.50m")

elif estatura >= 1.5 and estatura < 1.75:
    print(f"Estatura: {estatura}m")
    print("Grupo: B") 
    print("Silla asignada: Silla B")
    print("Rango: Entre 1.50m y 1.75m")

else:  # estatura >= 1.75
    print(f"Estatura: {estatura}m")
    print("Grupo: C")
    print("Silla asignada: Silla C")
    print("Rango: De 1.75m en adelante")