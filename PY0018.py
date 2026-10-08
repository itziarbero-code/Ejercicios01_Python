#PY0018
cadena = "zeréP nauJ,01"
NombreApellido, nota = cadena.split(",");

NombreApellido = NombreApellido[::-1]
nota = nota[::-1]

print(f"{NombreApellido} ha sacado un Nota de {nota}")