import sys

# entrada = sys.argv[0]

def longitud_por_secuencia(entrada):
    long = 0
    lista = list()
    lectura = open("/home/jorge/Documentos/2021-1/Genomica_Equipo/GenomicaComputacional/equipo00_p02/data/" +
            str(entrada), "r")

    for linea in lectura:
        if not linea.startswith('@'):
            if linea.startswith('+'):
                continue
            else:
                num_c = cuenta_caracteres(linea)
                long = long + num_c
        lista.append(long)

    return lista

def promedio_lps(lista):
    promedio = sum(lista) / len(lista)
    return promedio

def cuenta_caracteres(cadena):
    n = 0
    for c in cadena:
        n = n + 1
    return n


if __name__ == '__main__':

    entrada = sys.argv[1]

    sec = longitud_por_secuencia(entrada)
    prom = promedio_lps(sec)

    print("El promedio de la longitud de las secuencias es: " + str(prom))
