import sympy as sp
def spline_cubico_natural_vid(x, y, decimales):
    """
    ENTRADA: x (lista de valores de x), y (lista de valores de y = f(x)), decimales (precisión)
    SALIDA: impresión de los splines cúbicos para cada segmento con redonceo a decimales propuestos.
    """
    n = len(x) - 1 ; h = [x[i+1] - x[i] for i in range(n)] ; alfa = [0] * (n+1)
    for i in range(1, n):
        alfa[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])
    l = [0] * (n+1) ; u = [0] * (n+1) ; z = [0] * (n+1)
    l[0] = 1 ; u[0] = 0 ; z[0] = 0
    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i] * u[i-1]
        u[i] = h[i] / l[i]
        z[i] = (alfa[i] - h[i-1] * z[i-1]) / l[i]
    l[n] = 1 ; z[n] = 0
    c = [0] * (n+1)
    b = [0] * n
    d = [0] * n
    a = y[:n]
    for j in reversed(range(n)):
        c[j] = z[j] - u[j] * c[j+1]
        b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    x_sym = sp.Symbol('x')
    for j in range(n):
        sx = round(a[j], decimales) + round(b[j], decimales)*(x_sym - x[j]) + round(c[j], decimales)*(x_sym - x[j])**2 + round(d[j], decimales)*(x_sym - x[j])**3
        print(f"S_{j}(x) = {sp.expand(sx)}")
