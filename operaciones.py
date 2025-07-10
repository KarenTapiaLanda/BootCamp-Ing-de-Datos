# operaciones.py

def sumar(a, b):
    """
    Suma dos números.
    :param a: Primer número.
    :param b: Segundo número.
    :return: Resultado de la suma.
    """
    return a + b

def restar(a, b):
    """
    Resta el segundo número al primero.
    :param a: Primer número.
    :param b: Segundo número.
    :return: Resultado de la resta.
    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos números.
    :param a: Primer número.
    :param b: Segundo número.
    :return: Resultado de la multiplicación.
    """
    return a * b

def dividir(a, b):
    """
    Divide el primer número por el segundo.
    :param a: Dividendo.
    :param b: Divisor (no debe ser cero).
    :return: Resultado de la división.
    :raises ZeroDivisionError: Si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b
