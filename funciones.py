def crear_sublista(lista, clave):
    sublista = []
    for pregunta in lista:
        sublista.append(pregunta[clave])

    return sublista

def detectar_colision(posicion_mouse, diccionario_boton):
    x_mouse = posicion_mouse[0]
    y_mouse = posicion_mouse[1]
    x = diccionario_boton['x']
    y = diccionario_boton['y']
    ancho = diccionario_boton['ancho']
    alto = diccionario_boton['alto']

    flag_colision_x = x_mouse >= x and x_mouse <= x + ancho
    flag_colision_y = y_mouse >= y and y_mouse <= y + alto

    return flag_colision_x and flag_colision_y