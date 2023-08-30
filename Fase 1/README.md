# Fase 1 - Definição da Linguagem e Análise Léxica

## Descrição da Fase

A Fase 1 deste projeto tem como objetivo principal a criação de uma linguagem de programação que permita a criação de programas destinados a sistemas embarcados, como Arduino Mega, Raspberry PI, ou Tiva, baseados na tecnologia ARM. A linguagem será desenvolvida a partir de um esboço inicial, com ênfase na interação com hardware, tipos de dados estáticos, manipulação de números inteiros e de ponto flutuante, além da implementação de operações matemáticas em conformidade com o padrão IEEE-754 de 16 bits, também conhecido como meia precisão.

### Requisitos da Linguagem

A seguir, estão listados os principais requisitos que a linguagem deve atender:

- [] Estrutura do Programa: Um programa na linguagem consiste em um bloco de declarações definidas.

- [] Tipos Básicos: A linguagem deve definir tipos básicos para representar dados, incluindo inteiros e números de ponto flutuante de acordo com o padrão IEEE-754 de 16 bits.

- [] Expressões e Operadores: Deve ser implementada a precedência de operadores e associatividade corretas em expressões matemáticas. Use não-terminais para definir níveis de precedência e um não-terminal "factor" para tratar expressões entre parênteses, identificadores, referências de arranjos e constantes.

- [] Tipos Estáticos: A linguagem deve ser de tipos estáticos, ou seja, os tipos de variáveis, valores e expressões precisam ser explicitamente definidos no código.

- [] Interção com Hardware: É necessário definir regras de produção para interação com o hardware, permitindo ler e escrever em pinos do microcomputador, portas seriais, e em componentes opcionais, como conversores digital-analógico e analógico-digital.

### Fase 1

**TODO:** COLOCAR AS INFORMAÇÕES DO RASPBERRY AQUI 


## Apresentação da Linguagem

TODO: **Apresentação da Linguagem**: Durante a apresentação, destaque as principais características da linguagem, com ênfase nas regras de produção criadas para interação com o hardware.

### TODO: Bloco de Declarações

### TODO: Lexema Basico

### TODO: Regra de Produção para Expressões

### TODO: Tratamento dos numeros e letras

### TODO: Comunicação com Hardware



## Exemplos de Código

TODO: **Exemplos de Código**: Apresente pelo menos três exemplos de código que demonstrem todas as funcionalidades da linguagem criada. Esses exemplos devem abranger diferentes aspectos da linguagem, como declaração de variáveis, expressões matemáticas, e interação com hardware.


### Exemplo *.Cpy:
```C++
// Declara uma variável inteira
numero: int = 10;
led_on: int = 1;
led_off: int = 0;

// Declara uma variável real
pi: float16 = 3.14159;

// Declara uma variável booleana
ligado: bool = true;

// Declara uma função para somar dois números
def somar(a: int, b: int) -> int:
  return a + b;

// Declara uma função para calcular a área de um círculo
def area_circulo(raio: float16) -> float16:
  return PI * raio * raio;

// Declara uma função para imprimir uma mensagem
def imprimir_mensagem(char *mensagem) -> void:
  printf("%s\n", mensagem);

// exemplo LED serial
def main() -> void:
    while (ligado):
        if led_on:
            printf("%d\n", led_on);
        else:
            printf("%d\n", led_off);
    return 0;
```

#### Exemplo LED embarcado
```C++
// pin(nome, pino, direcao)
// write(nome, valor)
// read(nome)

// Declara um pino como saída
pin(led, GPIO_2, GPIO_OUT);

// Escreve um valor no pino
write(led, 1);

// Lê um valor do pino
read(led);

// Declara uma função para ligar o LED
def ligar_led() -> void:
  write(led, 1);

def desligar_led() -> void:
    write(led, 0);

def led(estado: int) -> void:
  if (estado == 1):
    // liga o LED
    ligar_led();
  else
    // desliga o LED
    desligar_led();

def main() -> void:
    if read(led) == 0:
        led(1);
    else:
        led(0);
    return 0;
```

## Documentação

TODO: **Documentação**: Forneça documentação completa da linguagem, incluindo a gramática, a descrição de tipos de dados, operadores e funções incorporadas (se houver).
