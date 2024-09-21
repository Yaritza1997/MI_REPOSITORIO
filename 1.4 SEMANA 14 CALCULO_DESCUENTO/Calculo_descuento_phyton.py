      #Definir la funcion
def calcular_descuento(monto_total, porcentaje_de_descuento = 25):
    descuento = monto_total * porcentaje_de_descuento / 100
    return descuento, porcentaje_de_descuento

        #Ingreso del monto de compra
monto_total = float(input("Ingrese el valor total de la compra: "))

        #Calcular el descuento correspondiente
descuento, porcentaje_de_descuento  = calcular_descuento(monto_total)

        #Calcular valor final a pagar de la compra
valor_final= monto_total - descuento

print (f"El descuento aplicado sera de:{porcentaje_de_descuento}%")
print(f"El valor del descuento es de: {descuento}")
print(f"Su valor final a pagar es de: {valor_final}")

print("**********Segunda compra**********")
  #Ingreso del monto de compra
monto_total = float(input("Ingrese el valor total de la compra: "))

        #Calcular el descuento correspondiente
descuento, porcentaje_de_descuento  = calcular_descuento(monto_total,50)

        #Calcular valor final a pagar de la compra
valor_final= monto_total - descuento

print (f"El descuento aplicado sera de:{porcentaje_de_descuento}%")
print(f"El valor del descuento es de: {descuento}")
print(f"Su valor final a pagar es de: {valor_final}")

print("---------GRACIAS POR SU COMPRA, VUELVA PRONTO-----------")