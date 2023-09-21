// Declara uma variável booleana
ligado: bool = true;

// Declara uma variável real
num: int = 69;
PI: float16 = 3.14159;

def main() -> int: {
    if (ligado) : {
        return 1;
    } else: {
        return 0;
    }
    return 0;
}

def soma(a: float16, b: float16) -> float16: {
    return a + b;
}