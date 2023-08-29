listComp = []
con = 0
acuSubtotal = 0
acuIVA = 0
acuTotal = 0

while True:
    con += 1
    dictProd = {}
    dictProd["Código"] = input(f"Digite el Código del Producto {con}: ")
    dictProd["Producto"] = input(f"Digite el Nombre del Producto {con}: ")
    dictProd["Cantidad"] = int(input(f"Digite la Cantidad a llevar {con}: "))
    dictProd["Valor_Unitario"] = int(input(f"Digite el Valor Unitario del Producto {con}: "))
    dictProd["Tipo_IVA"] = int(input(f"Digite el Tipo de IVA a aplicar para el Producto {con}: \n1. Sin IVA \n2. IVA 5% \n3. IVA 19% "))

    listComp.append(dictProd)

    if input("Desea continuar?: s(si)/n(no): ") != "s":
        break

cadenaImp = "*" * 138 + "\n"
cadenaImp += "*\t Código \t\t Producto \t\t Cantidad \t\t Valor Un \t\t Tipo IVA \t\t SubTotal \t\t\t IVA \t\t\t Total \t\t\t*\n"
cadenaImp += "*" * 138 + "\n"

for producto in listComp:
    producto["SubTotal"] = producto["Cantidad"] * producto["Valor_Unitario"]
    acuSubtotal += producto["SubTotal"]

    if producto["Tipo_IVA"] == 1:
        producto["IVA"] = 0
    elif producto["Tipo_IVA"] == 2:
        producto["IVA"] = producto["SubTotal"] * 0.05
    else:
        producto["IVA"] = producto["SubTotal"] * 0.19

    acuIVA += producto["IVA"]

    producto["Total"] = producto["SubTotal"] + producto["IVA"]

    acuTotal += producto["Total"]

    cadenaImp += f"*\t {producto['Código']} \t\t\t {producto['Producto']} \t\t\t {producto['Cantidad']} \t\t\t\t {producto['Valor_Unitario']} \t\t\t {producto['Tipo_IVA']} \t\t\t\t {producto['SubTotal']} \t\t\t\t {producto['IVA']} \t\t\t {producto['Total']} \t\t *\n"

cadenaImp += "-" * 138 + "\n"
cadenaImp += f"*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t {acuSubtotal} \t\t\t\t {acuIVA} \t\t\t {acuTotal} \t\t *\n"
cadenaImp += "*" * 138 + "\n"

#print(cadenaImp)

with open("factura.txt","w") as archivo:
    archivo.write(cadenaImp)
    
print("factura guardada en el archivo (factura.txt)")