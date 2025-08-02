import sympy as sp
import numpy as np

def spline_cubico_natural_vid(x, y, decimales):
    n = len(x) - 1
    h = [x[i+1] - x[i] for i in range(n)]
    alfa = [0] * (n+1)
    for i in range(1, n):
        alfa[i] = (3/h[i])*(y[i+1] - y[i]) - (3/h[i-1])*(y[i] - y[i-1])
    l = [0]*(n+1)
    u = [0]*(n+1)
    z = [0]*(n+1)
    l[0] = 1
    u[0] = 0
    z[0] = 0
    for i in range(1, n):
        l[i] = 2*(x[i+1]-x[i-1]) - h[i]*u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (alfa[i] - h[i-1]*z[i-1])/l[i]
    l[n] = 1
    z[n] = 0
    c = [0]*(n+1)
    b = [0]*n
    d = [0]*n
    a = y[:n]
    for j in reversed(range(n)):
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (y[j+1]-y[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1]-c[j])/(3*h[j])

    x_sym = sp.Symbol('x')
    print("Splines cúbicos naturales:")
    for j in range(n):
        sx = round(a[j], decimales) + round(b[j], decimales)*(x_sym - x[j]) + round(c[j], decimales)*(x_sym - x[j])**2 + round(d[j], decimales)*(x_sym - x[j])**3
        print(f"S_{j}(x) = {sp.expand(sx)}")

    def evaluar_spline(x_eval):
        y_eval = []
        x_eval = np.atleast_1d(x_eval)
        for xi in x_eval:
            if xi <= x[0]:
                i = 0
            elif xi >= x[-1]:
                i = n - 1
            else:
                for k in range(n):
                    if x[k] <= xi <= x[k+1]:
                        i = k
                        break
            dx = xi - x[i]
            yi = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
            y_eval.append(yi)
        return np.array(y_eval)

    return {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'x': x,
        'evaluar': evaluar_spline
    }
