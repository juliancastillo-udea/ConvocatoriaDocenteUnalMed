print('Favor ingresar la estatura del estudiante en metros: ')
estatura = float(input('-->'))
if estatura > 1.0 and estatura < 1.5:
    categoria = "A"
elif estatura >= 1.5 and estatura < 1.75:
    categoria = "B"
elif estatura >= 1.75:
    categoria = "C"
else:
    categoria = "NA"
print(f'La categoria del estudiante con estatura {estatura:,.2f}m es:\n\t--> {categoria}')

