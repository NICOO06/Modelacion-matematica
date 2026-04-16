# 📊 Métodos Numéricos para Ecuaciones Diferenciales

📘 **Materia:** Modelación Matemática

**Nicolas Vargas - Juan Marin**

Este proyecto consiste en un programa en Python que permite resolver ecuaciones diferenciales ordinarias (EDO) de primer orden de la forma:

dy/dx = f(x, y)

utilizando diferentes métodos numéricos.

---

## 🚀 Métodos implementados

El programa incluye los siguientes métodos:

- Método de Euler  
- Método de Euler Mejorado (Heun)  
- Método de Taylor de orden 2  
- Método de Runge-Kutta del punto medio  
- Método de Runge-Kutta de orden 4  

---

## ⚙️ Funcionalidades

El programa permite:

- Ingresar una función f(x, y)
- Definir condiciones iniciales (x0, y0)
- Establecer el tamaño de paso (h)
- Calcular la solución aproximada
- Mostrar resultados en consola
- Graficar la solución
- Comparar todos los métodos en una sola gráfica

---

## 🧪 Ejemplo de uso

Ejemplo de ecuación:

f(x,y) = -y + 70

Valores:

x0 = 0  
y0 = 100  
h = 0.1  
xf = 2  

---

## ▶️ Cómo ejecutar

En la terminal:

```bash
py metodos.py
