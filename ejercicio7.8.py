"""
     Inversión de listas
        a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
           deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
        b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista dada para invertirla, sin usar listas auxiliares.

"""

def invertir_lista(lista):

    lista_invertida = []
    longitud = len(lista) - 1

    while longitud>=0:
        lista_invertida.append(lista[longitud])
        longitud-=1

    return lista_invertida


# print(invertir_lista(['Di', 'buen', 'día', 'a', 'papa']))


def invertir_lista_2(lista):

    pass