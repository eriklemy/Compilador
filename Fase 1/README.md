# Fase 1 - Definição da Linguagem e Análise Léxica

## Descrição da Fase

A Fase 1 deste projeto tem como objetivo principal a criação de uma linguagem de programação que permita a criação de programas destinados a sistemas embarcados, como Arduino Mega, Raspberry PI, ou Tiva, baseados na tecnologia ARM. A linguagem será desenvolvida a partir de um esboço inicial, com ênfase na interação com hardware, tipos de dados estáticos, manipulação de números inteiros e de ponto flutuante, além da implementação de operações matemáticas em conformidade com o padrão IEEE-754 de 16 bits, também conhecido como meia precisão.

### Requisitos da Linguagem

A seguir, estão listados os principais requisitos que a linguagem deve atender:

- [] Estrutura do Programa: Um programa na linguagem consiste em um bloco de declarações definidas.

- [] Tipos Básicos: A linguagem deve definir tipos básicos para representar dados, incluindo inteiros e números de ponto flutuante de acordo com o padrão IEEE-754 de 16 bits.

- [] Expressões e Operadores: Deve ser implementada a precedência de operadores e associatividade corretas em expressões matemáticas. Use não-terminais para definir níveis de precedência e um não-terminal "factor" para tratar expressões entre parênteses, identificadores, referências de arranjos e constantes.

- [x] Tipos Estáticos: A linguagem deve ser de tipos estáticos, ou seja, os tipos de variáveis, valores e expressões precisam ser explicitamente definidos no código.

- [] Interção com Hardware: É necessário definir regras de produção para interação com o hardware, permitindo ler e escrever em pinos do microcomputador, portas seriais, e em componentes opcionais, como conversores digital-analógico e analógico-digital.

### Fase 1

**TODO:** COLOCAR AS INFORMAÇÕES DO RASPBERRY AQUI 


## Apresentação da Linguagem

Estética: A linguagem é baseada na sintaxe de Python, com algumas características de C, como a declaração de tipos de dados e necessidade de uso do ";".

TODO: **Apresentação da Linguagem**: Durante a apresentação, destaque as principais características da linguagem, com ênfase nas regras de produção criadas para interação com o hardware.

### TODO: Bloco de Declarações

O bloco de declarações é uma sequência de declarações de variáveis, constantes, funções e declarações para interação com o hardware. O bloco de declarações deve ser encerrado por um ponto-e-vírgula.

Claro, aqui está a sintaxe da linguagem organizada em uma tabela para Markdown:

| Produção   | Regra de Produção                     |
|------------|---------------------------------------|
| program    | block                                 |
| block      | { decls stmts }                       |
| decls      | decls decl \| null                    |
| decl       | type id;                              |
| func_decl  | def id ( parameters ) -> type: block  |
| params     | param, params | params | null         |
| param      | type id                               |
| type       | int \| float16 \| bool                |
| stmts      | stmts stmt \| null                    |
| stmt       | assign \| func_decl \| if_stmt \| return_stmt  |
| assign     | id: type  = expression;               |
| id         | [a-zA-Z-Z0-9]+                        |


Esta tabela apresenta as regras de produção da linguagem, indicando como a gramática da linguagem é estruturada. Certifique-se de adaptar essas regras de produção para sua linguagem específica, adicionando detalhes e funcionalidades conforme necessário.


### TODO: Lexema Basico

O lexema básico da linguagem é composto por:

- **Identificador**: uma sequência de letras, números e sublinhados, começando com uma letra.
- **Numérico**: um número inteiro ou de ponto flutuante.
- **Operador**: um símbolo que representa uma operação matemática, relacional ou lógica.
- **Delimitador**: um símbolo que separa tokens ou delimita um bloco de código.

| Produção   | Regra de Produção                      |
|------------|---------------------------------------|
| stmt       |                             |


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
def somar(a: int, b: int) -> int: {
    return a + b;
}

// Declara uma função para calcular a área de um círculo
def area_circulo(raio: float16) -> float16: {
    return PI * raio * raio;
}
```

#### Interação com Hardware
```C++
// Declara um pino como saída
pin(led, GPIO_2, GPIO_OUT);

// Escreve um valor no pino
write(led, 1);

// Lê um valor do pino
read(led);

// Declara uma função para ligar o LED
def ligar_led() -> void: {
    write(led, 1);
}

def desligar_led() -> void: {
    write(led, 0);
}

def led(estado: int) -> void: {
    if (estado == 1): {
        // liga o LED
        ligar_led();
    }
    else: desligar_led();
}

def main() -> int: {
    if (read(led) == 0): {
        led(1);
    }
    else: led(0);

    return 0;
}

```

## Documentação

TODO: **Documentação**: Forneça documentação completa da linguagem, incluindo a gramática, a descrição de tipos de dados, operadores e funções incorporadas (se houver).

```Python
pin(nome, pino, direcao)
write(nome, valor)
read(nome)
```