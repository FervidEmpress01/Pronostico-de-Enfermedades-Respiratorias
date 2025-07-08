def minimos_cuadrados_vid(puntos_x, puntos_y, decimales):
    """
    ENTRADA: puntos_x (lista de puntos x_i), puntos_y (lista de puntos y_i), decimales (precisión)
    SALIDA: valor de a y b de la ecuación ajustada y = a + bx con redondeo a los decimales dados
    """
    n = len(puntos_x)
    sum_x = sum(puntos_x)
    sum_y = sum(puntos_y)
    sum_xx = sum(xi**2 for xi in puntos_x)
    sum_xy = sum(puntos_x[i]*puntos_y[i] for i in range(n))
    b = (n*sum_xy - sum_x*sum_y)/(n*sum_xx - sum_x**2)
    a = (sum_y - b*sum_x)/n
    return round(a, decimales), round(b, decimales)
