# Crear el diccionario
informacion_personal= {
    "Mi nombre es": "Yaritza Lilibeth Arboleda",
    "Mi edad es": "26 años",
    "Vivo en la ciudad": "Esmeraldas",
    "Mi profesion es": "Doctora"
}

#Modificar el valor de la clave "ciudad"
informacion_personal["Vivo en la ciudad"] = "Guayaquil"

#Modificar el valor de la clave "profesion"
informacion_personal["Mi profesion es"] = "Ingeniera en TIC"

#Comprobar si existe la clave-valor "telefono"
if "Numero de telefono" not in informacion_personal:
    informacion_personal["Numero de telefono"] = "0981898227"

#Eliminar la clave-valor edad
del(informacion_personal["Mi edad es"])

#Imprimir los resultados finales del diccionario
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
