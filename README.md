# APS_LogComp

CalvinLang é uma linguagem de programação projetada para simular o ciclo de Calvin, uma importante etapa da fotossíntese nas células vegetais. Inspirada nas equações bioquímicas desse ciclo, CalvinLang oferece uma sintaxe intuitiva e clara para expressar as diferentes etapas do processo, incluindo a fixação do dióxido de carbono (CO2), a redução do ácido 3-fosfoglicérico (PGA) em gliceraldeído-3-fosfato (G3P) e a regeneração do ribulose-1,5-bisfosfato (RuBP). A linguagem permite a declaração de variáveis para representar os diferentes compostos envolvidos, bem como o uso de estruturas de controle de fluxo, como condicionais e loops, para controlar o fluxo das reações e simular as condições necessárias para o funcionamento do ciclo.

![Diagrama do ciclo de Calvin - khanacademy](https://cdn.kastatic.org/ka-perseus-images/4c9fbc7e4f158fd4bf3e1114e9a7ebe47d08f020.png)

3 CO2 + 3 RuBP -> 6 3-PGA <br>
6 3-PGA + 6 NADPH + 9 ATP -> 6 G3P + 6 NADP+ + 9 ADP + 9 Pi <br>
5 G3P -> 3 RuBP + 3 ATP <br>
1 G3P -> 1/2 Glicose <br>

```
// Declaração de variáveis
CO2_disponivel = obterCO2DoAmbiente()
RuBP_disponivel = obterRuBPDaCélula()
glicose_disponivel = obterGlicoseDisponivel()
threshold_glicose = 100 // Exemplo de threshold para glicose disponível
threshold_RuBP = 50 // Exemplo de threshold para RuBP disponível
energia_luminosa = capturarEnergiaLuminosa()

// Fixação do CO2
PGA = fixarCO2(CO2_disponivel, RuBP_disponivel)

// Redução do PGA
se energia_luminosa > 0 então:
    NADPH = obterNADPH()
    ATP = obterATP()
    G3P = reduzirPGA(PGA, NADPH, ATP)
senão:
    abortar("Não há energia suficiente para redução do PGA")

// Regeneração do RuBP
enquanto célulaNecessitaRegenerarRuBP():
    ATP = obterATP()
    RuBP = regenerarRuBP(G3P, ATP)

// Conversão de G3P baseada na disponibilidade de glicose e RuBP
para cada molécula de G3P:
    se glicose_disponivel > threshold_glicose ou RuBP_disponivel < threshold_RuBP então:
        RuBP = RuBP + 3/5
    senão:
        glicose = glicose + 1/2
        
// Fim do ciclo de Calvin
```

Referencias:

- https://pt.khanacademy.org/science/biology/photosynthesis-in-plants/the-calvin-cycle-reactions/a/calvin-cycle