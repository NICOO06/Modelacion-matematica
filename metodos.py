# Programa de ecuaciones diferenciales
# Métodos numéricos (nivel básico)

import matplotlib.pyplot as plt

# función que evalúa lo que escribe el usuario
def f(x, y, funcion):
    return eval(funcion)

# derivadas aproximadas (para Taylor)
def fx(x, y, funcion):
    h = 0.0001
    return (f(x + h, y, funcion) - f(x, y, funcion)) / h

def fy(x, y, funcion):
    h = 0.0001
    return (f(x, y + h, funcion) - f(x, y, funcion)) / h


# 1. Euler
def euler(funcion, x0, y0, h, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    for i in range(n):
        y0 = y0 + h * f(x0, y0, funcion)
        x0 = x0 + h

        xs.append(x0)
        ys.append(y0)

    return xs, ys


# 2. Euler mejorado
def euler_mejorado(funcion, x0, y0, h, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    for i in range(n):
        k1 = f(x0, y0, funcion)
        k2 = f(x0 + h, y0 + h * k1, funcion)

        y0 = y0 + (h/2)*(k1 + k2)
        x0 = x0 + h

        xs.append(x0)
        ys.append(y0)

    return xs, ys


# 3. Taylor orden 2
def taylor2(funcion, x0, y0, h, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    for i in range(n):
        y0 = y0 + h*f(x0, y0, funcion) + (h**2/2)*(fx(x0, y0, funcion) + fy(x0, y0, funcion)*f(x0, y0, funcion))
        x0 = x0 + h

        xs.append(x0)
        ys.append(y0)

    return xs, ys


# 4. Runge-Kutta punto medio
def rk_punto_medio(funcion, x0, y0, h, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    for i in range(n):
        k1 = f(x0, y0, funcion)
        k2 = f(x0 + h/2, y0 + h*k1/2, funcion)

        y0 = y0 + h*k2
        x0 = x0 + h

        xs.append(x0)
        ys.append(y0)

    return xs, ys


# 5. Runge-Kutta orden 4
def rk4(funcion, x0, y0, h, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    for i in range(n):
        k1 = f(x0, y0, funcion)
        k2 = f(x0 + h/2, y0 + h*k1/2, funcion)
        k3 = f(x0 + h/2, y0 + h*k2/2, funcion)
        k4 = f(x0 + h, y0 + h*k3, funcion)

        y0 = y0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x0 = x0 + h

        xs.append(x0)
        ys.append(y0)

    return xs, ys


# mostrar resultados
def mostrar(xs, ys):
    print("\nResultados:")
    for i in range(len(xs)):
        print("x =", round(xs[i],2), " y =", round(ys[i],5))


# graficar simple
def graficar(xs, ys):
    plt.plot(xs, ys)
    plt.title("Grafica")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()


# =========================
# PROGRAMA PRINCIPAL
# =========================

print("ECUACIONES DIFERENCIALES")
print("------------------------")

funcion = input("Ingrese f(x,y): ")

x0 = float(input("x0: "))
y0 = float(input("y0: "))
h = float(input("h: "))
xf = float(input("xf: "))

n = int((xf - x0)/h)

print("\n1. Usar un metodo")
print("2. Comparar todos los metodos")

modo = int(input("Elija: "))


# =========================
# MODO NORMAL
# =========================
if modo == 1:

    print("\nMetodo:")
    print("1. Euler")
    print("2. Euler mejorado")
    print("3. Taylor orden 2")
    print("4. Runge-Kutta punto medio")
    print("5. Runge-Kutta orden 4")

    op = int(input("Elija: "))

    if op == 1:
        xs, ys = euler(funcion, x0, y0, h, n)

    elif op == 2:
        xs, ys = euler_mejorado(funcion, x0, y0, h, n)

    elif op == 3:
        xs, ys = taylor2(funcion, x0, y0, h, n)

    elif op == 4:
        xs, ys = rk_punto_medio(funcion, x0, y0, h, n)

    elif op == 5:
        xs, ys = rk4(funcion, x0, y0, h, n)

    else:
        print("Opcion no valida")

    mostrar(xs, ys)
    graficar(xs, ys)


# =========================
# MODO COMPARACION 🔥
# =========================
elif modo == 2:

    xs1, ys1 = euler(funcion, x0, y0, h, n)
    xs2, ys2 = euler_mejorado(funcion, x0, y0, h, n)
    xs3, ys3 = taylor2(funcion, x0, y0, h, n)
    xs4, ys4 = rk_punto_medio(funcion, x0, y0, h, n)
    xs5, ys5 = rk4(funcion, x0, y0, h, n)

    plt.plot(xs1, ys1, label="Euler")
    plt.plot(xs2, ys2, label="Euler mejorado")
    plt.plot(xs3, ys3, label="Taylor 2")
    plt.plot(xs4, ys4, label="RK punto medio")
    plt.plot(xs5, ys5, label="RK4")

    plt.title("Comparacion de metodos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()

    plt.show()

else:
    print("Opcion no valida")
    