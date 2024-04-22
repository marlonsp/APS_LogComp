# APS_LogComp

CalvinLang é uma linguagem de programação projetada para simular o ciclo de Calvin, uma importante etapa da fotossíntese nas células vegetais. Inspirada nas equações bioquímicas desse ciclo, CalvinLang oferece uma sintaxe intuitiva e clara para expressar as diferentes etapas do processo, incluindo a fixação do dióxido de carbono (CO2), a redução do ácido 3-fosfoglicérico (PGA) em gliceraldeído-3-fosfato (G3P) e a regeneração do ribulose-1,5-bisfosfato (RuBP). A linguagem permite a declaração de variáveis para representar os diferentes compostos envolvidos, bem como o uso de estruturas de controle de fluxo, como condicionais e loops, para controlar o fluxo das reações e simular as condições necessárias para o funcionamento do ciclo.

![Diagrama do ciclo de Calvin - khanacademy](https://cdn.kastatic.org/ka-perseus-images/4c9fbc7e4f158fd4bf3e1114e9a7ebe47d08f020.png)

CO2 + RuBP -> 2 3-PGA <br>
3-PGA + NADPH + ATP -> G3P + NADP+ + ADP + Pi <br>
5 G3P + 3 ATP -> 3 RuBP + 3 ADP <br>
1 G3P -> 1/2 Glicose <br>

```
program = { statement };

statement = variable_declaration
          | custom_variable_declaration
          | assignment_statement
          | operation_statement
          | cycle_of_calvin
          | print_statement
          | comment;

variable_declaration = "variable", (RuBP | glicose | RuBP_min | glicose_min), "=", expression, ";";  // Declaração de variáveis padrão

custom_variable_declaration = "custom_variable", identifier, ";";  // Declaração de variáveis personalizadas

assignment_statement = (identifier | custom_variable), assignment_operator, expression, ";";  // Declaração de atribuição

operation_statement = (identifier | custom_variable), assignment_operator, (identifier | custom_variable | number), arithmetic_operator, (identifier | custom_variable | number), ";";  // Declaração de operação

cycle_of_calvin = "calvin_cycle", "{", before_statements, function, function, function, function, conditionals, after_statements, "}";  // Ciclo de Calvin com condições

before_statements = { assignment_statement | operation_statement };

after_statements = { assignment_statement | operation_statement };

conditionals = if_statement, else_statement;

if_statement = "if", "(", condition, ")", "{", function, "}";

else_statement = "else", "{", function, "}";

function = "fixação_CO2", "redução_3_PGA", "regeneração_RuBP", "síntese_glicose";

condition = identifier, comparison_operator, expression
          | identifier, logical_operator, identifier
          | "(", condition, ")", logical_operator, "(", condition, ")";

expression = term, { ( "+" | "-" ), term };  // Expressão aritmética

term = factor, { ( "*" | "/" ), factor };

factor = identifier
       | number
       | "(", expression, ")";

assignment_operator = "=" | "+=" | "-=" | "*=" | "/=";  // Operadores de atribuição

arithmetic_operator = "+" | "-" | "*" | "/";  // Operadores aritméticos

comparison_operator = "==" | "!=" | "<" | ">" | "<=" | ">=";

logical_operator = "and" | "or";

print_statement = "print", "(", print_expression, ")", ";";  // Comando de impressão

print_expression = expression
                  | string_literal
                  | identifier;

comment = "//", { all_characters_except_newline };

identifier = RuBP | glicose | RuBP_min | glicose_min;

RuBP = "RuBP";

glicose = "glicose";

RuBP_min = "RuBP_min";

glicose_min = "glicose_min";

number = digit, { digit };

string_literal = '"', { all_characters_except_quotes }, '"';

letter = "a" | "b" | ... | "z" | "A" | "B" | ... | "Z";

digit = "0" | "1" | ... | "9";

all_characters_except_newline = any_visible_character | space;

all_characters_except_quotes = all_characters_except_newline | '"';

space = " ";
```

Exemplo de código para a linguagem:

```
// Declaração de variáveis padrão
variable RuBP = 0;
variable glicose = 0;
variable RuBP_min = 3;  // Valor mínimo de RuBP
variable glicose_min = 0.5;  // Valor mínimo de glicose

// Declaração de variáveis personalizadas
custom_variable luminosidade = 50;
custom_variable pH = 6;

// Execução do ciclo de Calvin
calvin_cycle {

    // Execução das funções fixação_CO2 e redução_3_PGA em ordem
    fixação_CO2;
    redução_3_PGA;

    // Condicional para regeneração_RuBP
    if (RuBP < RuBP_min and glicose > glicose_min) {
        regeneração_RuBP;
    } else {
        síntese_glicose;
    }

    // Condicional para execução de novo ciclo
    if (RuBP > RuBP_min and glicose > glicose_min) {
        // Alterações de valores de variáveis após as funções
        luminosidade -= 5;
        pH += 0.1;
        calvin_cycle;
    }
}
```

Referencias:

- https://pt.khanacademy.org/science/biology/photosynthesis-in-plants/the-calvin-cycle-reactions/a/calvin-cycle