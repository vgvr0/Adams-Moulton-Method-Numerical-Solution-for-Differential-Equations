def adams_moulton_integration(f, x0, y0, h, n):
    """
    Función para realizar la integración numérica utilizando el método de Adams-Moulton de paso múltiple.

    Parámetros:
    - f: La función que describe la ecuación diferencial dy/dx = f(x, y).
    - x0: El valor inicial de x.
    - y0: El valor inicial de y.
    - h: El tamaño del paso.
    - n: El número de iteraciones.

    Retorna:
    - Dos listas: una con los valores de x y otra con los valores de y.
    """
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x = x_values[-1]
        y = y_values[-1]

        if i < 2:
            # Usar el método de Euler para los primeros dos pasos
            y_new = y + h * f(x, y)
        else:
            # Utilizar el método de Adams-Moulton de paso múltiple
            y_pred = y + (h / 24) * (
                9 * f(x_values[-1], y_values[-1]) + 19 * f(x, y) - 5 * f(x_values[-2], y_values[-2]) + f(x_values[-3], y_values[-3])
            )
            y_new = y + (h / 24) * (
                f(x_values[-1], y_values[-1]) + 4 * f(x, y_new) + f(x_values[-2], y_values[-2])
            )

        x_new = x + h

        x_values.append(x_new)
        y_values.append(y_new)

    return x_values, y_values


def equation(x, y):
    """
    La función que describe la ecuación diferencial dy/dx = x^2.
    """
    return x ** 2


# Parámetros de integración
x0 = 0  # Valor inicial de x
y0 = 0  # Valor inicial de y
h = 0.1  # Tamaño del paso
n = 10  # Número de iteraciones

# Realiza la integración
x_values, y_values = adams_moulton_integration(equation, x0, y0, h, n)

# Imprime los resultados
for x, y in zip(x_values, y_values):
    print(f"x = {x}, y = {y}")
