interes_mensual = interes_anual / 100 / 12

numero_pagos = anios * 12

if interes_mensual == 0:
    cuota_mensual = capital / numero_pagos
else:
    cuota_mensual = (interes_mensual * capital) / (1 - (1 / (1 + interes_mensual)) ** numero_pagos)

total_pagar = cuota_mensual * numero_pagos

print("La cuota mensual a pagar es: ${:.2f}".format(cuota_mensual))
print("El total a pagar al final del préstamo es: ${:.2f}".format(total_pagar))