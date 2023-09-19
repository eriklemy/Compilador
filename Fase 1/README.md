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

**Raspberry Pi 3 Model B**

-Processador Broadcom BCM2837 64bit ARMv8 Cortex-A53 Quad-Core
-Clock 1.2 GHz
-Memória RAM: 1GB
-Adaptador Wifi 802.11n integrado (trabalha na frequência de 2.4 Ghz)
-Bluetooth 4.1 BLE integrado
-Conector de vídeo HDMI
-4 portas USB 2.0
-Conector Ethernet
-Interface para câmera (CSI)
-Interface para display (DSI)
-Slot para cartão microSD
-Conector de áudio e vídeo
-GPIO de 40 pinos
-Número de homologação Anatel: 04908-17-10629
-Dimensões: 85 x 56 x 17mm


## Apresentação da Linguagem

Estética: A linguagem é baseada na sintaxe de Python, com algumas características de C, como a declaração de tipos de dados e necessidade de uso do ";".

TODO: **Apresentação da Linguagem**: Durante a apresentação, destaque as principais características da linguagem, com ênfase nas regras de produção criadas para interação com o hardware.

### TODO: Bloco de Declarações

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
| num        | [0-9]                                 |


Esta tabela apresenta as regras de produção da linguagem, indicando como a gramática da linguagem é estruturada. Certifique-se de adaptar essas regras de produção para sua linguagem específica, adicionando detalhes e funcionalidades conforme necessário.

As mudanças básicas em relação ao bloco fornecido estão relacionadas à expansão da sintaxe para acomodar a criação de funções, a introdução de parâmetros de função, declaração de pinos e instruções específicas para interação com hardware. Aqui estão as principais mudanças em relação ao bloco fornecido:

1. **Adição de Funções e Parâmetros**:
   - A produção `func_decl` foi introduzida para permitir a declaração de funções com parâmetros e tipo de retorno.
   - A produção `params` foi adicionada para definir a lista de parâmetros em uma função.
   - A produção `param` permite a definição de parâmetros de função com seu tipo e nome.

2. **Tipo Básico**:
   - A produção `type` continua a permitir tipos básicos, como `int`, `float16` e `bool`.

3. **Identificadores**:
   - A produção `id` permanece semelhante, permitindo identificadores compostos por letras maiúsculas e minúsculas, bem como dígitos numéricos.

4. **Outras Instruções**:
   - A produção `stmt` foi expandida para acomodar instruções específicas relacionadas ao hardware e funções.

5. **Blocos de Função**:
   - As produções `func_decl` e `block` são usadas para definir o escopo de uma função, incluindo a lista de parâmetros e o corpo da função.


### TODO: Lexema Basico - herman

O lexema básico da linguagem é composto por:

```
stmt -> var = bool ;
            | if ( bool ) { stmt }
            | if ( bool ) { stmt } else { stmt }
            | if ( bool ) { stmt } elif (bool) { stmt }
            | for (var -> num; bool; var -> var +- num) { stmt }
            | while ( bool ) { stmt }
            | do { stmt } while ( bool ) ;
            | break;
            | id (args) { stmt }
            | return bool
            | block
var -> var | id
var -> var [ bool ] | id
func_call -> id(args);
```

- **Identificador**: uma sequência de letras, números e sublinhados, começando com uma letra.
- **Numérico**: um número inteiro ou de ponto flutuante.
- **Operador**: um símbolo que representa uma operação matemática, relacional ou lógica.
- **Delimitador**: um símbolo que separa tokens ou delimita um bloco de código.

| Produção   | Regra de Produção                      |
|------------|----------------------------------------|
| stmt       | assign \| func_decl \| if_stmt \| return_stmt |
| if_stmt    | if ( expr ) { stmts } else { stmts } \| if ( expr ): { stmts }
| return_stmt| return expr ;                          |
| expr       | id \| num \| true \| false \| func_call \| bin_op \| ( expr ) |
| func_call  | id ( args )                            |
| args       | expr \| null |
| bin_op     | expr + expr \| expr - expr \| expr * expr \| expr / expr \| expr == expr \| expr != expr \| expr < expr \| expr <= expr \| expr > expr \| expr >= expr |



### TODO: Regra de Produção para Expressões

### TODO: Tratamento dos numeros e letras - leandro/feito


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
