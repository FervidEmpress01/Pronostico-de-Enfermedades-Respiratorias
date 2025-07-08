def minimos_cuadrados(x_puntos, y_puntos, decimal):
    """
    Calcula la recta de ajuste por mínimos cuadrados.
    ENTRADA: x_puntos (lista), y_puntos (lista), decimal (precisión)
    SALIDA: Un string con la ecuación ajustada y = m·x + c
    """
    N = len(x_puntos)
    sumx = sum(x_puntos)
    sumy = sum(y_puntos)
    sumx2 = sum(x**2 for x in x_puntos)
    sumxy = sum(x*y for x, y in zip(x_puntos, y_puntos))
    denominador = N * sumx2 - sumx**2

    if denominador == 0:
        return "No es posible calcular el ajuste (división por cero)."
    m = (N * sumxy - sumx * sumy) / denominador
    c = (sumy * sumx2 - sumx * sumxy) / denominador

    m = round(m, decimal)
    c = round(c, decimal)
    return f"La recta ajustada es: y = {m}x + {c}"


