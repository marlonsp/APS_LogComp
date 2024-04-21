# APS_LogComp

CalvinLang é uma linguagem de programação projetada para simular o ciclo de Calvin, uma importante etapa da fotossíntese nas células vegetais. Inspirada nas equações bioquímicas desse ciclo, CalvinLang oferece uma sintaxe intuitiva e clara para expressar as diferentes etapas do processo, incluindo a fixação do dióxido de carbono (CO2), a redução do ácido 3-fosfoglicérico (PGA) em gliceraldeído-3-fosfato (G3P) e a regeneração do ribulose-1,5-bisfosfato (RuBP). A linguagem permite a declaração de variáveis para representar os diferentes compostos envolvidos, bem como o uso de estruturas de controle de fluxo, como condicionais e loops, para controlar o fluxo das reações e simular as condições necessárias para o funcionamento do ciclo.

![Diagrama do ciclo de Calvin - khanacademy](https://cdn.kastatic.org/ka-perseus-images/4c9fbc7e4f158fd4bf3e1114e9a7ebe47d08f020.png)

CO2 + RuBP -> 2 3-PGA <br>
3-PGA + NADPH + ATP -> G3P + NADP+ + ADP + Pi <br>
5 G3P + 3 ATP -> 3 RuBP + 3 ADP <br>
1 G3P -> 1/2 Glicose <br>

```
programa            ::= instrução*

instrução           ::= declaração | atribuição | estrutura_condicional | loop

declaração          ::= "variáveis" identificador ("," identificador)* "=" expressão

atribuição          ::= identificador "=" expressão

estrutura_condicional ::= "se" expressão "então" bloco ("senão" bloco)?

loop                ::= "enquanto" expressão "faça" bloco

bloco               ::= "{" instrução* "}"

expressão          ::= termo (operador termo)*

termo               ::= número | identificador | chamada_função | "(" expressão ")"

chamada_função      ::= função "(" (expressão ("," expressão)*)? ")"

função              ::= "fixação_CO2" | "redução_3_PGA" | "regeneração_RuBP" | "síntese_glicose"

operador            ::= "+" | "-" | "*" | "/" | ">=" | ">" | "<=" | "<" | "==" | "!="

identificador       ::= "RuBP" | "G3P" | "ATP" | "Glicose" | "NADPH" | "CO2" | "3_PGA" | "variáveis" | "se" | "então" | "senão" | "enquanto" | "faça" | "fixação_CO2" | "redução_3_PGA" | "regeneração_RuBP" | "síntese_glicose"

número              ::= dígito+

letra               ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

dígito              ::= "0" | "1" | ... | "9"
```

Exemplo de código para a linguagem:

```
# Definição das variáveis iniciais
variáveis CO2 = 10, RuBP = 10, NADPH = 10, ATP = 10, Glicose = 0

# Função para a etapa de Fixação do CO2
função fixação_CO2():
    CO2 -= 1
    RuBP -= 1
    3_PGA_produzido = 2
    retorne 3_PGA_produzido

# Função para a etapa de Redução de 3-PGA para G3P
função redução_3_PGA():
    NADPH -= 1
    ATP -= 1
    G3P_produzido = 1
    retorne G3P_produzido

# Função para a etapa de Regeneração de RuBP
função regeneração_RuBP():
    ATP -= 3
    RuBP_produzido = 3
    retorne RuBP_produzido

# Função para a síntese de glicose
função síntese_glicose():
    Glucose_produzida = 0.5
    Glicose += Glucose_produzida

# Loop principal para simular o ciclo de Calvin
enquanto CO2 > 0 e RuBP > 0:
    # Etapa 1: Fixação do CO2
    3_PGA_produzido = fixação_CO2()
    
    # Etapa 2: Redução de 3-PGA para G3P
    G3P_produzido = redução_3_PGA()
    
    # Verificar se há ATP suficiente para a regeneração de RuBP
    se G3P_produzido >= 5 e ATP >= 3:
        # Etapa 3: Regeneração de RuBP
        RuBP_produzido = regeneração_RuBP()
    
    # Verificar se há G3P suficiente para a síntese de glicose
    se G3P_produzido >= 1:
        # Etapa 4: Síntese de glicose
        síntese_glicose()

# Exibição dos resultados finais
exibir("Resultados finais:")
exibir("CO2:", CO2)
exibir("RuBP:", RuBP)
exibir("NADPH:", NADPH)
exibir("ATP:", ATP)
exibir("Glicose:", Glicose)
```

Referencias:

- https://pt.khanacademy.org/science/biology/photosynthesis-in-plants/the-calvin-cycle-reactions/a/calvin-cycle