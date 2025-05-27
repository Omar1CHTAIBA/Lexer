from Token import Token, TokenType


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = -1
        self.read_position = 0
        self.line_n = 1
        self.current_char = None
        self.read_char()
    def read_char(self):
        if self.read_position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.read_position]
        self.position = self.read_position
        self.read_position += 1
    def skip_whitespace(self):
        while self.current_char in ["\t", "\n", " ", "\r"]:
            if self.current_char == '\n':
                self.line_n += 1
            self.read_char()
    def new_token(self, TokenType, literal):
        return Token(type=TokenType, literal=literal, line=self.line_n, pos=self.position)

    def is_digit(self, char):
        return '0' <= char and char <= '9' # return True if 0<=char<=9

    def read_number(self):
        dot_count = 0
        output = ""
        while self.is_digit(self.current_char) or self.current_char == '.':
            if self.current_char ==  '.':
                dot_count += 1
            if dot_count > 1:
                print(f"Too many decimals in number on line {self.line_n}, position {self.position}")
                return self.new_token(TokenType.ILLEGAL, self.current_char)
            output += self.source[self.position]
            self.read_char()
            if self.current_char is None:
                break
        if dot_count == 0:
            return self.new_token(TokenType.INT, int(output))
        else:
            return self.new_token(TokenType.FLOAT, float(output))

    def next_token(self):
        # Token = None
        self.skip_whitespace()
        match self.current_char:
            case '+':
                tok = self.new_token(TokenType.PLUS, self.current_char)
            case '-':
                tok = self.new_token(TokenType.MINUS, self.current_char)
            case '*':
                tok = self.new_token(TokenType.ASTERISK, self.current_char)
            case '/':
                tok = self.new_token(TokenType.SLASH, self.current_char)
            case '^':
                tok = self.new_token(TokenType.POW, self.current_char)
            case '%':
                tok = self.new_token(TokenType.MODULUS, self.current_char)
            case '(':
                tok = self.new_token(TokenType.LPAREN, self.current_char)
            case ')':
                tok = self.new_token(TokenType.RPAREN, self.current_char)
            case ';':
                tok = self.new_token(TokenType.SEMICOLON, self.current_char)
            case None:
                tok = self.new_token(TokenType.EOF, "")
            case _:
                if self.is_digit(self.current_char):
                    tok = self.read_number()
                    return tok
                else:
                    tok = self.new_token(TokenType.ILLEGAL, self.current_char)
        self.read_char()
        return tok




