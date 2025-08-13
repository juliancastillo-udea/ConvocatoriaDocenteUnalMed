print('Bienvenido a la Cafetería Central'.center(60))
print('Ingresa el valor comprado: ')
compra = int(input('--> '))
print('Comprado-->', compra)
print('*'*60 + '\n') 

if compra > 200_000:
    descuento = 0.8
elif compra > 100_000:
    descuento = 0.85
elif compra > 50_000:
    descuento = 0.90
elif compra > 25_000:
    descuento = 0.95
elif compra > 0:
    descuento = 1
else:
    descuento = 0

subtotal = compra
valor_descuento = compra - (compra * descuento)
total = compra * descuento
print(f'Subtotal--> ${subtotal:,.0f}')
print(f'Descuento--> ${valor_descuento:,.0f}')
print(f'Total a Pagar--> ${total:,.0f}')


# Solucion Reto

from datetime import datetime
import pytz
# Captura de fecha
# Zona horaria de Bogotá
bogota_tz = pytz.timezone('America/Bogota')
# Fecha actual en esa zona
fecha_bogota = datetime.now(bogota_tz)
# Formato corto: dd/mm/aaaa o similar
fecha_corta = fecha_bogota.strftime('%d/%m/%Y %H:%M')
print('*'*60)
print('Bienvenido a Cafetería Central'.center(60))
print('Nit 123456789'.center(60))
print(fecha_corta.center(60))
print('*'*60)
print(' Subtotal'.ljust(30),f'${compra:,.0f}'.rjust(30), sep='')
print(' Valor Descuento'.ljust(30),f'${valor_descuento:,.0f}'.rjust(30), sep='')
print('_'*60)
print(' Total a pagar'.ljust(30),f'${total:,.0f}'.rjust(30), sep='')
print('*'*60)
print('Gracias por su compra'.center(60))
print('*'*60)
