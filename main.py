import sys

reserved_words = ['print', 'variable']
standard_variables = ['RuBP', 'glicose', 'ATP', 'ADP', 'G3P', 'RuBP_min', 'glicose_min', 'CO2', 'PGA', 'NADPH', 'NADP', 'Pi']

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def get(self, symbol):
        if symbol in reserved_words:
            raise Exception(f'"{symbol}" é uma palavra reservada e não pode ser usado como identificador.')
        return self.symbols[symbol][0], self.symbols[symbol][1]

    def set(self, symbol, value, data_type):
        if symbol in reserved_words:
            raise Exception(f'"{symbol}" é uma palavra reservada e não pode ser usado como identificador.')
        self.symbols[symbol] = (value, data_type)
        # print(self.symbols)
        
    def create(self, symbol):
        if symbol in reserved_words:
            raise Exception(f'"{symbol}" é uma palavra reservada e não pode ser usado como identificador.')
        self.symbols[symbol] = (None, None)

class FuncTable:
    def __init__(self):
        self.functions = {}

    def get(self, function):
        return self.functions[function]

    def create(self, function, block):
        self.functions[function] = block

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'{self.type}: {self.value}'

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None
    
    def select_next(self):
        if self.position >= len(self.source):
            self.next = Token('EOF', None)
            # print(self.next)
            return
        if self.source[self.position] == '\n':
            self.next = Token('LB', '\n')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == ' ' or self.source[self.position] == '\t':
            self.position += 1
            self.select_next()
            return
        if self.source[self.position:self.position+12] == 'calvin_cycle':
            self.next = Token('CALVIN_CYCLE', 'calvin_cycle')
            self.position += 12
            # print(self.next)
            return
        if self.source[self.position:self.position+6] == 'return':
            self.next = Token('RETURN', 'return')
            self.position += 6
            # print(self.next)
            return
        if self.source[self.position] == ',':
            self.next = Token('COMMA', ',')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position:self.position+5] == 'print':
            self.next = Token('PRINT', 'print')
            self.position += 5
            # print(self.next)
            return
        # tokens para variable
        if self.source[self.position:self.position+8] == 'variable':
            self.next = Token('VAR', 'variable')
            self.position += 8
            # print(self.next)
            return
        if self.source[self.position:self.position+15] == 'custom_variable':
            self.next = Token('CUSTOM_VAR_DECL', 'custom_variable')
            self.position += 15
            # print(self.next)
            return
        # token fixacao_CO2
        if self.source[self.position:self.position+11] == 'fixacao_CO2':
            self.next = Token('FIXACAO_CO2', 'fixacao_CO2')
            self.position += 11
            # print(self.next)
            return
        # token reducao_3_PGA
        if self.source[self.position:self.position+13] == 'reducao_3_PGA':
            self.next = Token('REDUCAO_3_PGA', 'reducao_3_PGA')
            self.position += 13
            # print(self.next)
            return
        # token regeneracao_RuBP
        if self.source[self.position:self.position+16] == 'regeneracao_RuBP':
            self.next = Token('REGENERACAO_RUBP', 'regeneracao_RuBP')
            self.position += 16
            # print(self.next)
            return
        # token sintese_glicose
        if self.source[self.position:self.position+15] == 'sintese_glicose':
            self.next = Token('SINTESE_GLICOSE', 'sintese_glicose')
            self.position += 15
            # print(self.next)
            return
        if self.source[self.position:self.position+2] == '..':
            self.next = Token('CONCAT', '..')
            self.position += 2
            # print(self.next)
            return
        # tokens booleanos
        if self.source[self.position:self.position+2] == '==':
            self.next = Token('EQ', '==')
            self.position += 2
            # print(self.next)
            return
        if self.source[self.position] == '>':
            self.next = Token('GT', '>')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '<':
            self.next = Token('LT', '<')
            self.position += 1
            # print(self.next)
            return
        # token para not
        if self.source[self.position:self.position+3] == 'not':
            self.next = Token('NOT', 'not')
            self.position += 3
            # print(self.next)
            return
        # token para while
        if self.source[self.position:self.position+5] == 'while':
            self.next = Token('WHILE', 'while')
            self.position += 5
            # print(self.next)
            return
        # token para do
        if self.source[self.position:self.position+2] == 'do':
            self.next = Token('DO', 'do')
            self.position += 2
            # print(self.next)
            return
        # token para if
        if self.source[self.position:self.position+2] == 'if':
            self.next = Token('IF', 'if')
            self.position += 2
            # print(self.next)
            return
        # token para then
        if self.source[self.position:self.position+4] == 'then':
            self.next = Token('THEN', 'then')
            self.position += 4
            # print(self.next)
            return
        # token para else
        if self.source[self.position:self.position+4] == 'else':
            self.next = Token('ELSE', 'else')
            self.position += 4
            # print(self.next)
            return
        # token para end
        if self.source[self.position:self.position+3] == 'end':
            self.next = Token('END', 'end')
            self.position += 3
            # print(self.next)
            return
        # token para or
        if self.source[self.position:self.position+2] == 'or':
            self.next = Token('OR', 'or')
            self.position += 2
            # print(self.next)
            return
        # token para and
        if self.source[self.position:self.position+3] == 'and':
            self.next = Token('AND', 'and')
            self.position += 3
            # print(self.next)
            return
        # token para read
        if self.source[self.position:self.position+4] == 'read' and (not self.source[self.position+4] == '_' and not self.source[self.position+4].isalpha()):
            self.next = Token('READ', 'read')
            self.position += 4
            # print(self.next)
            return  
        if self.source[self.position].isalpha():
            start = self.position
            while self.position < len(self.source) and (self.source[self.position].isalpha() or self.source[self.position].isdigit() or self.source[self.position] == '_'):
                self.position += 1
            self.next = Token('IDEN', self.source[start:self.position])
            # print(self.next)
            return
        if self.source[self.position] == '=':
            self.next = Token('ASSIGN', '=')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '+':
            self.next = Token('PLUS', '+')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '-':
            self.next = Token('MINUS', '-')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '*':
            self.next = Token('MULT', '*')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '/':
            self.next = Token('DIV', '/')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position].isdigit():
            start = self.position
            while self.position < len(self.source) and self.source[self.position].isdigit():
                self.position += 1
            self.next = Token('INT', int(self.source[start:self.position]))
            # print(self.next)
            return
        if self.source[self.position] == '{':
            self.next = Token('LCURLY', '{')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '}':
            self.next = Token('RCURLY', '}')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '(':
            self.next = Token('LPAREN', '(')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == ')':
            self.next = Token('RPAREN', ')')
            self.position += 1
            # print(self.next)
            return
        if self.source[self.position] == '"':
            start = self.position
            self.position += 1
            while self.position < len(self.source) and self.source[self.position] != '"':
                self.position += 1
            if self.position >= len(self.source):
                raise Exception('String não fechada')
            self.position += 1
            self.next = Token('STRING', self.source[start + 1:self.position - 1])
            # print(self.next)
            return
        # token ";"
        if self.source[self.position] == ';':
            self.next = Token('SEMICOLON', ';')
            self.position += 1
            # print(self.next)
            return
        raise Exception(f'Caractere inválido: inicio-{self.source[self.position]}-Fim')



class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    @staticmethod
    def parse_relexpr():
        resultado = Parser.parse_expression()
        while Parser.tokenizer.next.type in ['EQ', 'GT', 'LT']:
            if Parser.tokenizer.next.type == 'EQ':
                Parser.tokenizer.select_next()
                resultado = BinOp('==', [resultado, Parser.parse_expression()])
            elif Parser.tokenizer.next.type == 'GT':
                Parser.tokenizer.select_next()
                resultado = BinOp('>', [resultado, Parser.parse_expression()])
            elif Parser.tokenizer.next.type == 'LT':
                Parser.tokenizer.select_next()
                resultado = BinOp('<', [resultado, Parser.parse_expression()])
            else:
                raise Exception('Esperado um operador ==, > ou <')
        return resultado

    @staticmethod
    def parse_boolterm():
        resultado = Parser.parse_relexpr()
        while Parser.tokenizer.next.type == 'AND':
            if Parser.tokenizer.next.type == 'AND':
                Parser.tokenizer.select_next()
                resultado = BinOp('and', [resultado, Parser.parse_relexpr()])
            else:
                raise Exception('Esperado um operador and')
        return resultado
    
    @staticmethod
    def parse_boolexp():
        resultado = Parser.parse_boolterm()
        while Parser.tokenizer.next.type == 'OR':
            if Parser.tokenizer.next.type == 'OR':
                Parser.tokenizer.select_next()
                resultado = BinOp('or', [resultado, Parser.parse_boolterm()])
            else:
                raise Exception('Esperado um operador or')
        return resultado
    
    @staticmethod
    def parse_statement():
        current_token = Parser.tokenizer.next
        if current_token.type == 'LB':
            Parser.tokenizer.select_next()
            return NoOp('nop')
        elif current_token.type == 'PRINT':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LPAREN':
                raise Exception('Esperado um "("')
            Parser.tokenizer.select_next()
            result = Print('print', [Parser.parse_boolexp()])
            if Parser.tokenizer.next.type != 'RPAREN':
                raise Exception('Esperado um ")"')
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LB':
                raise Exception('Esperado um "\n"')
            Parser.tokenizer.select_next()
            return result
        elif current_token.type == 'IDEN':
            iden = current_token.value
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == 'ASSIGN':
                Parser.tokenizer.select_next()
                result = BinOp('=', [IntVal(iden), Parser.parse_boolexp()])
                if Parser.tokenizer.next.type != 'SEMICOLON':
                    raise Exception('Esperado um ";"')
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type != 'LB':
                    raise Exception(f'Esperado um "\n", mas foi encontrado "{Parser.tokenizer.next.type}"')
                Parser.tokenizer.select_next()
                return result
            else:
                raise Exception('Esperado uma atribuição ou uma chamada de função')
        elif current_token.type == 'CUSTOM_VAR_DECL':
            Parser.tokenizer.select_next()
            current_token = Parser.tokenizer.next
            if current_token.type == 'IDEN':
                # checa se é uma variável padrão
                if current_token.value in standard_variables:
                    raise Exception(f'Variável "{current_token.value}" é uma variável padrão')
                iden = current_token.value
                Parser.tokenizer.select_next()
                current_token = Parser.tokenizer.next
                if current_token.type == 'LB':
                    # Declaração sem atribuição
                    result = VarDec('variable', [IntVal(iden)])
                    Parser.tokenizer.select_next()
                    return result
                elif current_token.type == 'ASSIGN':
                    # Declaração com atribuição
                    Parser.tokenizer.select_next()
                    expression = Parser.parse_boolexp()
                    result = VarDec('variable', [IntVal(iden), expression])
                    if Parser.tokenizer.next.type != 'SEMICOLON':
                        raise Exception('Esperado um ";"')
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type != 'LB':
                        raise Exception('Esperado um "\n"')
                    Parser.tokenizer.select_next()
                    return result
                else:
                    raise Exception('Esperado uma atribuição ou uma quebra de linha')
        elif current_token.type == 'VAR':
            Parser.tokenizer.select_next()
            current_token = Parser.tokenizer.next
            if current_token.type == 'IDEN':
                # checa se é uma variável padrão
                if current_token.value not in standard_variables:
                    raise Exception(f'Variável "{current_token.value}" não é uma variável padrão')
                iden = current_token.value
                Parser.tokenizer.select_next()
                current_token = Parser.tokenizer.next
                if current_token.type == 'LB':
                    # Declaração sem atribuição
                    result = VarDec('variable', [IntVal(iden)])
                    Parser.tokenizer.select_next()
                    return result
                elif current_token.type == 'ASSIGN':
                    # Declaração com atribuição
                    Parser.tokenizer.select_next()
                    expression = Parser.parse_boolexp()
                    result = VarDec('variable', [IntVal(iden), expression])
                    if Parser.tokenizer.next.type != 'SEMICOLON':
                        raise Exception('Esperado um ";"')
                    Parser.tokenizer.select_next()
                    if Parser.tokenizer.next.type != 'LB':
                        raise Exception('Esperado um "\n"')
                    Parser.tokenizer.select_next()
                    return result
                else:
                    raise Exception('Esperado uma atribuição ou uma quebra de linha')
        elif current_token.type == 'WHILE':
            #ler while, chamar parse_boolexp, ler do, loopar em pass ou statement, ler end, retornar While
            Parser.tokenizer.select_next()
            condition = Parser.parse_boolexp()
            if Parser.tokenizer.next.type != 'DO':
                raise Exception('Esperado um "do"')
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LB':
                raise Exception('Esperado um "\n"')
            Parser.tokenizer.select_next()
            resultado = Block('block')
            while Parser.tokenizer.next.type != 'END':
                resultado.children.append(Parser.parse_statement())
            if Parser.tokenizer.next.type != 'END':
                raise Exception('Esperado um "end"')
            Parser.tokenizer.select_next()
            #LB depois do end]
            if Parser.tokenizer.next.type != 'LB':
                raise Exception('Esperado um "\n"')
            Parser.tokenizer.select_next()
            return While('while', [condition, resultado])
        elif current_token.type == 'IF':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LPAREN':
                raise Exception('Esperado um LPAREN após "if"')
            Parser.tokenizer.select_next()
            condition = Parser.parse_boolexp()
            if Parser.tokenizer.next.type != 'RPAREN':
                raise Exception('Esperado um RPAREN após a condição do "if"')
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LCURLY':
                raise Exception(f'Esperado um LCURLY após RPAREN do "if": {Parser.tokenizer.next.type}')
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LB':
                raise Exception('Esperado um "\n"')
            Parser.tokenizer.select_next()
            if_block = Block('block')
            while Parser.tokenizer.next.type != 'RCURLY':
                if_block.children.append(Parser.parse_statement())
            if Parser.tokenizer.next.type != 'RCURLY':
                raise Exception(f'Esperado um "RCURLY" após bloco do "if": {Parser.tokenizer.next.type}')
            Parser.tokenizer.select_next()
            if_childs = [condition, if_block]
            if Parser.tokenizer.next.type == 'ELSE':
                else_block = None
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type != 'LCURLY':
                    raise Exception('Esperado um LCURLY após "else"')
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type != 'LB':
                    raise Exception('Esperado um "\n"')
                Parser.tokenizer.select_next()
                else_block = Block('block')
                while Parser.tokenizer.next.type != 'RCURLY':
                    else_block.children.append(Parser.parse_statement())
                if Parser.tokenizer.next.type != 'RCURLY':
                    raise Exception(f'Esperado um "RCURLY" após bloco do "else": {Parser.tokenizer.next.type}')
                Parser.tokenizer.select_next()
                if_childs.append(else_block)
            if Parser.tokenizer.next.type != 'SEMICOLON':
                raise Exception('Esperado um ";" após bloco do "if" ou "else"')
            Parser.tokenizer.select_next()
            return If('if', if_childs)
        elif current_token.type == 'RETURN':
            Parser.tokenizer.select_next()
            result = Parser.parse_boolexp()
            if Parser.tokenizer.next.type != 'LB':
                raise Exception('Esperado um "\n"')
            Parser.tokenizer.select_next()
            return Return(result)
        elif current_token.type == 'CALVIN_CYCLE':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type == 'LCURLY':
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type != 'LB':
                    raise Exception('Esperado um "\n"')
                Parser.tokenizer.select_next()
                cycle_block = Block('block')
                while Parser.tokenizer.next.type != 'RCURLY':
                    cycle_block.children.append(Parser.parse_statement())
                if Parser.tokenizer.next.type != 'RCURLY':
                    raise Exception('Esperado um "}"') 
                Parser.tokenizer.select_next()
                if Parser.tokenizer.next.type != 'SEMICOLON':
                    raise Exception('Esperado um ";"')
                Parser.tokenizer.select_next()
                calvin_cycle = CalvinCycleDec('calvin_cycle', [cycle_block])
                return CalvinCycleCall('calvin_cycle', [calvin_cycle])
            elif Parser.tokenizer.next.type == 'SEMICOLON':
                Parser.tokenizer.select_next()
                return CalvinCycleCall('calvin_cycle')
            else:
                raise Exception(f'Esperado um LCURLY: {Parser.tokenizer.next.type}')
        elif current_token.type == 'FIXACAO_CO2':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'SEMICOLON':
                raise Exception('Esperado um ";"')
            Parser.tokenizer.select_next()
            return FixacaoCO2('fixacao_CO2')
        elif current_token.type == 'REDUCAO_3_PGA':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'SEMICOLON':
                raise Exception('Esperado um ";"')
            Parser.tokenizer.select_next()
            return Reducao3PGA('reducao_3_PGA')
        elif current_token.type == 'REGENERACAO_RUBP':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'SEMICOLON':
                raise Exception('Esperado um ";"')
            Parser.tokenizer.select_next()
            return RegeneracaoRuBP('regeneracao_RuBP')
        elif current_token.type == 'SINTESE_GLICOSE':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'SEMICOLON':
                raise Exception('Esperado um ";"')
            Parser.tokenizer.select_next()
            return SinteseGlicose('sintese_glicose')
        else:
            raise Exception(f'Declaração inválida: {current_token.type}')
        
    @staticmethod
    def parse_factor():
        current_token = Parser.tokenizer.next

        if current_token.type == 'INT':
            Parser.tokenizer.select_next()
            return IntVal(current_token.value)
        elif current_token.type == 'STRING':
            Parser.tokenizer.select_next()
            return StringVal(current_token.value)
        if current_token.type == 'IDEN':
            iden = current_token.value
            Parser.tokenizer.select_next()
            # chamada de função
            return IntVal(iden)
        elif current_token.type == 'LPAREN':
            Parser.tokenizer.select_next()
            result = Parser.parse_boolexp()
            if Parser.tokenizer.next.type != 'RPAREN':
                raise Exception('Esperado um ")"')
            Parser.tokenizer.select_next()
            return result
        elif current_token.type in ['PLUS', 'MINUS', 'NOT']:
            op = current_token.type
            Parser.tokenizer.select_next()
            operand = Parser.parse_factor()
            if op == 'PLUS':
                return UnOp('+', operand)
            elif op == 'MINUS':
                return UnOp('-', operand)
            elif op == 'NOT':
                return UnOp('not', operand)
        elif current_token.type == 'READ':
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'LPAREN':
                raise Exception('Esperado um "("')
            Parser.tokenizer.select_next()
            if Parser.tokenizer.next.type != 'RPAREN':
                raise Exception('Esperado um ")"')
            Parser.tokenizer.select_next()
            return Read()
        else:
            raise Exception('Fator inválido')

        
    @staticmethod
    def parse_term():
        resultado = Parser.parse_factor()
        while Parser.tokenizer.next.type in ['MULT', 'DIV']:
            if Parser.tokenizer.next.type == 'MULT':
                Parser.tokenizer.select_next()
                resultado = BinOp('*', [resultado, Parser.parse_factor()])
            elif Parser.tokenizer.next.type == 'DIV':
                Parser.tokenizer.select_next()
                resultado = BinOp('/', [resultado, Parser.parse_factor()])
            else:
                raise Exception('Esperado um operador + ou -')
        return resultado
    
    @staticmethod
    def parse_expression():
        resultado = Parser.parse_term()
        while Parser.tokenizer.next.type in ['PLUS', 'MINUS', 'CONCAT']:
            if Parser.tokenizer.next.type == 'PLUS':
                Parser.tokenizer.select_next()
                resultado = BinOp('+', [resultado, Parser.parse_term()])
            elif Parser.tokenizer.next.type == 'MINUS':
                Parser.tokenizer.select_next()
                resultado = BinOp('-', [resultado, Parser.parse_term()])
            elif Parser.tokenizer.next.type == 'CONCAT':
                Parser.tokenizer.select_next()
                resultado = BinOp('..', [resultado, Parser.parse_term()])
            else:
                raise Exception('Esperado um operador +, - ou ..')
        return resultado
    
    @staticmethod
    def parse_block():
        Parser.tokenizer.select_next()
        resultado = Block('block')
        while Parser.tokenizer.next.type != 'EOF':
            resultado.children.append(Parser.parse_statement())
        return resultado
    
    @staticmethod
    def run(source):
        source = PrePro.filter(source)
        Parser.tokenizer = Tokenizer(source)
        resultado = Parser.parse_block()
        if Parser.tokenizer.next.type != 'EOF':
            print(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            raise Exception('Esperado EOF')
        return resultado

class PrePro:
    @staticmethod
    def filter(source):
        lines = source.split('\n')
        filtered_lines = []
        for line in lines:
            if '//' in line:
                parts = line.split('//', 1)
                line = parts[0].rstrip()
            filtered_lines.append(line)
        return '\n'.join(filtered_lines)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def evaluate(self, symbol_table=SymbolTable()):
        pass

class BinOp(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        left_value, left_type = self.children[0].evaluate(symbol_table)
        try:
            right_value, right_type = self.children[1].evaluate(symbol_table)
        except:
            raise Exception(f"right: {self.children[1]}")

        if self.value == '+':
            return left_value + right_value, 'int'
        elif self.value == '-':
            return left_value - right_value, 'int'
        elif self.value == '*':
            return left_value * right_value, 'int'
        elif self.value == '/':
            return left_value // right_value, 'int'
        elif self.value == '=':
            # verifica se a variável já foi declarada
            try:
                symbol_table.get(self.children[0].value)
            except:
                raise Exception(f'Variável "{self.children[0].value}" não declarada')
            # print(f"right value: {right_value}")
            symbol_table.set(self.children[0].value, right_value, 'int')  # Passa 'int' como tipo
            # print(symbol_table.symbols)
            return (right_value, 'int')
        elif self.value == 'or':
            return int(left_value or right_value), 'int'
        elif self.value == 'and':
            return int(left_value and right_value), 'int'
        elif self.value == '==':
            #check if the types are the same
            if left_type != right_type:
                raise Exception(f'Tipos incompatíveis: "{left_type}" e "{right_type}"')
            return int(left_value == right_value), 'int'
        elif self.value == '>':
            if left_type != right_type:
                raise Exception(f'Tipos incompatíveis: "{left_type}" e "{right_type}"')
            return int(left_value > right_value), 'int' 
        elif self.value == '<':
            if left_type != right_type:
                raise Exception(f'Tipos incompatíveis: "{left_type}" e "{right_type}"')
            return int(left_value < right_value), 'int' 
        elif self.value == '..':
            return str(left_value) + str(right_value), 'string'
        
class UnOp(Node):
    def __init__(self, value=None, operand=None):
        super().__init__(value)
        if operand is not None:
            self.children.append(operand)

    def evaluate(self, symbol_table=SymbolTable()):
        if self.value == '+':
            return (self.children[0].evaluate(symbol_table)[0], 'int')
        elif self.value == '-':
            return (-(self.children[0].evaluate(symbol_table)[0]), 'int')
        elif self.value == 'not':
            if self.children[0].evaluate(symbol_table)[0] == 0:
                return (1, 'int')
            else:
                return (0, 'int')

class IntVal(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def evaluate(self, symbol_table=SymbolTable()):
        if isinstance(self.value, int):
            return (self.value, 'int')
        else:
            return (symbol_table.get(self.value))
        
class StringVal(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def evaluate(self, symbol_table=SymbolTable()):
        if isinstance(self.value, str):
            return (self.value, 'string')
        else:
            return (symbol_table.get(self.value), 'string')

class NoOp(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def evaluate(self, symbol_table=SymbolTable()):
        pass

class Block(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def evaluate(self, symbol_table=SymbolTable()):
        for child in self.children:
            if isinstance(child, Return):
                return child.evaluate(symbol_table)
            child.evaluate(symbol_table)

class Print(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        print(self.children[0].evaluate(symbol_table)[0])

class If(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        if len(self.children) == 2:
            if self.children[0].evaluate(symbol_table)[0]:
                self.children[1].evaluate(symbol_table)
        else:
            if self.children[0].evaluate(symbol_table)[0]:
                self.children[1].evaluate(symbol_table)
            else:
                self.children[2].evaluate(symbol_table)

class While(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        while self.children[0].evaluate(symbol_table)[0]:
            self.children[1].evaluate(symbol_table)

class VarDec(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        variable_name = self.children[0].value
        if variable_name in symbol_table.symbols:
            raise Exception(f'A variável "{variable_name}" já foi declarada anteriormente.')
        if len(self.children) == 1:
            symbol_table.create(variable_name)
        else:
            symbol_table.create(variable_name)
            value = self.children[1].evaluate(symbol_table)
            symbol_table.set(variable_name, value[0], value[1])
        return symbol_table.get(variable_name)
        
class Read(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def evaluate(self, symbol_table=SymbolTable()):
        return (int(input()), 'int')
    
class CalvinCycleDec(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        symbol_table.create('calvin_cycle')
        symbol_table.set('calvin_cycle', self.children[0], 'calvin_cycle')
        return self
    
class CalvinCycleCall(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        if len(self.children) == 1:
            self.children[0].evaluate(symbol_table)
        function = symbol_table.get('calvin_cycle')[0]
        return function.evaluate(symbol_table)

class FixacaoCO2(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        CO2_now = symbol_table.get('CO2')[0]
        RuBP_now = symbol_table.get('RuBP')[0]
        PGA_now = symbol_table.get('PGA')[0]
        symbol_table.set('CO2', CO2_now - 1, 'int')
        symbol_table.set('RuBP', RuBP_now - 1, 'int')
        symbol_table.set('PGA', PGA_now + 2, 'int')

class Reducao3PGA(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        PGA_now = symbol_table.get('PGA')[0]
        NADPH_now = symbol_table.get('NADPH')[0]
        ATP_now = symbol_table.get('ATP')[0]
        G3P_now = symbol_table.get('G3P')[0]
        NADP_now = symbol_table.get('NADP')[0]
        ADP_now = symbol_table.get('ADP')[0]
        Pi_now = symbol_table.get('Pi')[0]
        symbol_table.set('PGA', PGA_now - 1, 'int')
        symbol_table.set('NADPH', NADPH_now - 1, 'int')
        symbol_table.set('ATP', ATP_now - 1, 'int')
        symbol_table.set('G3P', G3P_now + 1, 'int')
        symbol_table.set('NADP', NADP_now + 1, 'int')
        symbol_table.set('ADP', ADP_now + 1, 'int')
        symbol_table.set('Pi', Pi_now + 1, 'int')

class RegeneracaoRuBP(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        RuBP_now = symbol_table.get('RuBP')[0]
        ATP_now = symbol_table.get('ATP')[0]
        G3P_now = symbol_table.get('G3P')[0]
        ADP_now = symbol_table.get('ADP')[0]
        symbol_table.set('RuBP', RuBP_now + 3, 'int')
        symbol_table.set('ATP', ATP_now - 3, 'int')
        symbol_table.set('G3P', G3P_now - 5, 'int')
        symbol_table.set('ADP', ADP_now + 3, 'int')

class SinteseGlicose(Node):
    def __init__(self, value=None, children=None):
        super().__init__(value)
        if children is not None:
            self.children = children

    def evaluate(self, symbol_table=SymbolTable()):
        G3P_now = symbol_table.get('G3P')[0]
        glicose_now = symbol_table.get('glicose')[0]
        symbol_table.set('G3P', G3P_now - 2, 'int')
        symbol_table.set('glicose', glicose_now + 1, 'int')

class Return(Node):
    def __init__(self, value=None):
        super().__init__(value)

    def evaluate(self, symbol_table=SymbolTable()):
        return self.value.evaluate(symbol_table)

def main(file_path):
    with open(file_path, 'r') as file:
        expressao = file.read()
    resultado = Parser.run(expressao)
    symbol_table = SymbolTable()
    resultado.evaluate(symbol_table)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py input.pr")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)