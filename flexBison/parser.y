%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* s) {
    fprintf(stderr, "Erro de sintaxe: %s\n", s);
}
%}

%union {
    char *string;
    int integer;
}

%token <string> STRING
%token <integer> NUMBER

%token VARIABLE CUSTOM_VARIABLE ASSIGN SEMICOLON IF ELSE PRINT RUBP GLICOSE RUBP_MIN GLICOSE_MIN
%token PLUS MINUS MULTIPLY DIVIDE EQUAL NOTEQUAL LESS GREATER LESSEQUAL GREATEREQUAL AND OR IDENTIFIER

%left '+' '-'
%left '*' '/'
%nonassoc '<' '>' LESSEQUAL GREATEREQUAL EQUAL NOTEQUAL
%left AND
%left OR

%%

program : statement SEMICOLON
        | program statement SEMICOLON
        ;

statement : variable_declaration
          | custom_variable_declaration
          | assignment_statement
          | operation_statement
          | cycle_of_calvin
          | print_statement
          ;

variable_declaration : VARIABLE identifier ASSIGN NUMBER SEMICOLON
                      ;

custom_variable_declaration : CUSTOM_VARIABLE IDENTIFIER SEMICOLON
                             ;

assignment_statement : variable_or_custom ASSIGN expression SEMICOLON
                     ;

variable_or_custom : identifier
                   | CUSTOM_VARIABLE
                   ;

expression : identifier
           | CUSTOM_VARIABLE
           | NUMBER
           ;

operation_statement : variable_or_custom ASSIGN expression arithmetic_operator expression SEMICOLON
                    ;

cycle_of_calvin : RUBP_MIN '{' statements "fixação_CO2" "redução_3_PGA" conditionals statements '}'
                ;

statements : assignment_statement
           | operation_statement
           ;

conditionals : if_statement else_statement
             ;

if_statement : IF '(' condition ')' '{' function '}'
             ;

else_statement : ELSE '{' function '}'
               ;

function : "regeneração_RuBP" "síntese_glicose"
         ;

condition : IDENTIFIER comparison_operator NUMBER
          | IDENTIFIER logical_operator IDENTIFIER
          | '(' condition ')' logical_operator '(' condition ')'
          ;

assignment_operator : ASSIGN
                    | "+="
                    | "-="
                    | "*="
                    | "/="
                    ;

arithmetic_operator : '+'
                    | '-'
                    | '*'
                    | '/'
                    ;

comparison_operator : EQUAL
                    | NOTEQUAL
                    | LESS
                    | GREATER
                    | LESSEQUAL
                    | GREATEREQUAL
                    ;

logical_operator : AND
                 | OR
                 ;

print_statement : PRINT '(' print_argument ')' SEMICOLON
                ;

print_argument : STRING
               | IDENTIFIER
               ;

identifier : RUBP
           | GLICOSE
           | RUBP_MIN
           | GLICOSE_MIN
           | IDENTIFIER
           ;

custom_identifier : IDENTIFIER
                  ;

%%

int main(int argc, char** argv) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s arquivo_de_entrada\n", argv[0]);
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        perror(argv[1]);
        return 1;
    }

    yyparse();
    fclose(yyin);
    return 0;
}
