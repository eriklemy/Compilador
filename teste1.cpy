// Declarando variáveis
numero1: int = 10;
numero2: int = 5;
resultado: int;
pi: float16 = 3.14159;
ligado: bool = true;
desligado: bool = false;

// Realizando operações aritméticas
resultado = numero1 + numero2;
diferenca: int = numero1 - numero2;
produto: int = numero1 * numero2;
quociente: int = numero1 / numero2;

// Realizando comparações
igual: bool = (numero1 == numero2);
diferente: bool = (numero1 != numero2);
menor: bool = (numero1 < numero2);
maior: bool = (numero1 > numero2);
menor_igual: bool = (numero1 <= numero2);
maior_igual: bool = (numero1 >= numero2);

// Imprimindo resultados
write('Soma:', resultado);
write('Diferença:', diferenca);
write('Produto:', produto);
write('Quociente:', quociente);
write('Igual:', igual);
write('Diferente:', diferente);
write('Menor:', menor);
write('Maior:', maior);
write('Menor ou igual:', menor_igual);
write('Maior ou igual:', maior_igual);

