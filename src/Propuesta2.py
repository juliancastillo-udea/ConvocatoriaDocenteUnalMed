print('Favor ingresar la estatura del estudiante en metros: ')
estatura = float(input('-->'))
if estatura >=1.75:
    categoria = "C"
elif estatura >= 1.5:
    categoria = "B"
elif estatura >= 1.0:
    categoria = "A"
else:
    categoria = "NA"
print(f'La categoria del estudiante con estatura {estatura:,.2f}m es:\n\t--> {categoria}')