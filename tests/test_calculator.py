import pytest
from calculator import raiz_cuadrada

# 1. Caso correcto
def test_raiz_cuadrada_correcto():
    assert raiz_cuadrada(25) == 5.0  # <--- Valor corregido
    assert raiz_cuadrada(9) == 3.0

# 2. Caso límite
def test_raiz_cuadrada_limite():
    assert raiz_cuadrada(0) == 0.0

# 3. Caso error (Excepciones)
def test_raiz_cuadrada_error():
    # Validar que lance ValueError para números negativos
    with pytest.raises(ValueError):
        raiz_cuadrada(-16)
        
    # Validar que lance TypeError para entradas no numéricas
    with pytest.raises(TypeError):
        raiz_cuadrada("texto")