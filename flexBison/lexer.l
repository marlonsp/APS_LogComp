%{
#include "parser.tab.h"
%}

%%

"variable"               { return VARIABLE; }
"custom_variable"        { return CUSTOM_VARIABLE; }
"="                      { return ASSIGN; }
";"                      { return SEMICOLON; }
"if"                     { return IF; }
"else"                   { return ELSE; }
"print"                  { return PRINT; }
"RuBP"                   { return RUBP; }
"glicose"                { return GLICOSE; }
"RuBP_min"               { return RUBP_MIN; }
"glicose_min"            { return GLICOSE_MIN; }
"+"                      { return PLUS; }
"-"                      { return MINUS; }
"*"                      { return MULTIPLY; }
"/"                      { return DIVIDE; }
"=="                     { return EQUAL; }
"!="                     { return NOTEQUAL; }
"<"                      { return LESS; }
">"                      { return GREATER; }
"<="                     { return LESSEQUAL; }
">="                     { return GREATEREQUAL; }
"and"                    { return AND; }
"or"                     { return OR; }
\"[^"]*\"                { yylval.string  = strdup(yytext); return STRING; }
[0-9]+                   { yylval.integer  = atoi(yytext); return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]*   { yylval.string  = strdup(yytext); return IDENTIFIER; }
[ \t\n]                  ; // Ignore whitespace and newline characters
.                        { return yytext[0]; } // Any other character is treated as itself

%%

int yywrap(void) {
    return 1;
}
