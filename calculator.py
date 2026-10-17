import math

def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número dado.
    
    Excepciones:
    - TypeError: Si el argumento no es de tipo int o float.
    - ValueError: Si el número es negativo.
    """
    if not isinstance(numero, (int, float)):
        raise TypeError("El valor debe ser un número (entero o flotante).")
    
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        
    return math.sqrt(numero)