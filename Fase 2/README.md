# Fase 2 - Verificação de Código – Análise Sintática e Semântica

## Descrição da Fase

Nesta fase você deverá implementar um analisador sintático usando um parser, usando LL1, ou LR1
e uma estrutura baseada em cálculo de sequentes para a verificação dos tipos dos identificadores, 
valores e expressões criadas na sua linguagem. 
Estes dois analisadores, devem ser implementados em Python, ou C++, recebem o texto contendo o
código na linha de comando e devolvem, relatórios de erro contendo o número da linha onde o erro
se encontra, e uma árvore sintática, contendo os lexemas identificados, com suas classes, tipos e
posições definidas.

# Link para rodar o analisador sintatico e lexico
https://replit.com/@matheusherman/Compiladores <br>
**`PARA RODAR É NECESSÁRIO DIGITAR O COMANDO ABAIXO`**<br>
**`python3 main.py testeX.cpy`**<br>
**`OS ARQUIVOS DISPONÍVEIS SÃO TESTE1.CPY, TESTE2.CPY E TESTE3.CPY`**<br>


### Fase 2

TODO: Escrever



## Exemplos de Código Teste

Aqui estão alguns exemplos de código que demonstram as funcionalidades da linguagem criada, abrangendo diferentes aspectos, como declaração de variáveis, expressões matemáticas e interação com hardware

#### 1. Exemplo Basico*.Cpy:
```python
// Este eh um comentario

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

def main() -> int: {
    soma: int = somar(numero, numero);
    return 0;
}

```

#### 2. Interação com Hardware
##### 2.1 - Exemplo 1: Piscar led com intervalo de 1s
```python
// Declara um pino como saída
pin(led, GPIO_2, GPIO_OUT);

def main() -> int: {
    while (true): {
        // Lê o estado atual do LED
        estado_led: int = read(led);
        
        // Inverte o estado do LED
        if (estado_led == 0): {
            write(led, 1);
        } else: {
            write(led, 0);
        }
        
        // Aguarda 1 segundo
        delay(1000);
    }
    return 0;
}
```

##### 2.2 - Exemplo 2: Controle de LED com botão
```python
// Declara um pino como saída para o LED
pin(led, GPIO_2, GPIO_OUT);

// Declara um pino como entrada para o botão
pin(botao, GPIO_3, GPIO_IN);

def main() -> int: {
    while (true): {
        // Lê o estado atual do botão
        estado_botao: int = read(botao);
        
        // Se o botão estiver pressionado, alterna o estado do LED
        if (estado_botao == 1): {
            estado_led = read(led);
            if (estado_led == 0): {
                write(led, 1);
            } else: {
                write(led, 0);
            }
        }
        
        // Aguarda um curto período de tempo para evitar leituras múltiplas do botão
        delay(100);
    }
    return 0;
}
```

#### 2.3 - Exemplo 3: Controle de Intesidade do LED com Potenciometro 
```python
// Declara um pino como saída para o LED
pin(led, GPIO_2, GPIO_OUT);

// Declara um pino como entrada analógica para o potenciômetro (ADC)
pin(potenciometro, ADC_0, GPIO_IN);

def ler_valor_potenciometro() -> int: {
    // Lê o valor analógico do potenciômetro (0-1023)
    valor: int = read(potenciometro);
    return valor;
}

def ajustar_brilho_led(valor_potenciometro: int) -> void: {
    // Converte o valor do potenciômetro para um valor de brilho (0-1)
    brilho: float16 = valor_potenciometro / 1023.0;
    
    // Define o brilho do LED com base no valor do potenciômetro
    write(led, brilho);
}

def main() -> int: {
    while (true): {
        // Lê o valor atual do potenciômetro
        valor_potenciometro: int = ler_valor_potenciometro();
        
        // Ajusta o brilho do LED com base no valor do potenciômetro
        ajustar_brilho_led(valor_potenciometro);
        
        // Aguarda um curto período de tempo antes da próxima leitura
        delay(100);
    }
    return 0;
}
```

