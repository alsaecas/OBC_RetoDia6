import operator

operaciones = {
    "suma": operator.add,
    "súmale": operator.add,
    "multiplica": operator.mul,
    "multiplícalo": operator.mul,
    "resta": operator.sub,
    "réstale": operator.sub,
    "divide": operator.floordiv,
    "divídelo": operator.floordiv
}

numeros = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9
}


def numero_to_letras(numero):
    indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
    entero = int(numero)
    decimal = int(round((numero - entero) * 100))
    # print 'decimal : ',decimal
    contador = 0
    numero_letras = ""
    while entero > 0:
        a = entero % 1000
        if contador == 0:
            en_letras = convierte_cifra(a, 1).strip()
        else:
            en_letras = convierte_cifra(a, 0).strip()
        if a == 0:
            numero_letras = en_letras + " " + numero_letras
        elif a == 1:
            if contador in (1, 3):
                numero_letras = indicador[contador][0] + " " + numero_letras
            else:
                numero_letras = en_letras + " " + indicador[contador][0] + " " + numero_letras
        else:
            numero_letras = en_letras + " " + indicador[contador][1] + " " + numero_letras
        numero_letras = numero_letras.strip()
        contador = contador + 1
        entero = int(entero / 1000)
    numero_letras = numero_letras
    print(numero_letras.lower())
    print(numero)


def convierte_cifra(numero, sw):
    lista_centana = ["", ("CIEN", "CIENTO"), "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS",
                     "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    lista_decena = ["", (
        "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"),
                    ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y "), ("CUARENTA", "CUARENTA Y "),
                    ("CINCUENTA", "CINCUENTA Y "), ("SESENTA", "SESENTA Y "),
                    ("SETENTA", "SETENTA Y "), ("OCHENTA", "OCHENTA Y "),
                    ("NOVENTA", "NOVENTA Y ")
                    ]
    lista_unidad = ["", ("UN", "UNO"), "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
    centena = int(numero / 100)
    decena = int((numero - (centena * 100)) / 10)
    unidad = int(numero - (centena * 100 + decena * 10))
    # print "centena: ",centena, "decena: ",decena,'unidad: ',unidad

    texto_centena = ""
    texto_decena = ""
    texto_unidad = ""

    # Validad las centenas
    texto_centena = lista_centana[centena]
    if centena == 1:
        if (decena + unidad) != 0:
            texto_centena = texto_centena[1]
        else:
            texto_centena = texto_centena[0]

    # Valida las decenas
    texto_decena = lista_decena[decena]
    if decena == 1:
        texto_decena = texto_decena[unidad]
    elif decena > 1:
        if unidad != 0:
            texto_decena = texto_decena[1]
        else:
            texto_decena = texto_decena[0]
    # Validar las unidades
    # print "texto_unidad: ",texto_unidad
    if decena != 1:
        texto_unidad = lista_unidad[unidad]
        if unidad == 1:
            texto_unidad = texto_unidad[sw]

    return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)


if __name__ == '__main__':
    while True:
        entrada = input()
        if len(entrada.split(" ")) == 4:
            try:
                numero1 = numeros[entrada.split(" ")[1]]
            except:
                numero1 = -1
                print("Primer numero no reconocido")
            try:
                numero2 = numeros[entrada.split(" ")[3]]
            except:
                numero2 = -1
                print("Segundo numero no reconocido")
            if numero1 != -1 and numero2 != -1:
                try:
                    resultado = operaciones[entrada.split(" ")[0]](numero1, numero2)
                    numero_to_letras(resultado)
                except:
                    print("Operacion no reconocida")
        elif len(entrada.split(" ")) == 7 or len(entrada.split(" ")) == 8:
            try:
                numero1 = numeros[entrada.split(" ")[1]]
            except:
                numero1 = -1
                print("Primer numero no reconocido")
            try:
                numero2 = numeros[entrada.split(" ")[3]]
            except:
                numero2 = -1
                print("Segundo numero no reconocido")
            try:
                numero3 = numeros[entrada.split(" ")[len(entrada.split(" "))-1]]
            except:
                numero3 = -1
                print("Segundo numero no reconocido")
            if numero1 != -1 and numero2 != -1 and numero3 != -1:
                try:
                    resultado = operaciones[entrada.split(" ")[0]](numero1, numero2)
                    resultado = operaciones[entrada.split("y")[2].split(" ")[1]](resultado, numero3)
                    numero_to_letras(resultado)
                except:
                    print("Operacion no reconocida")
        else:
            print("Imposible realizar la operación")
