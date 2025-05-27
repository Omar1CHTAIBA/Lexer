from enum import Enum

class TokenType(Enum):
    # Special Tokens
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    # Data types
    INT = "INT"
    FLOAT = "FLOAT"

    # Arithmetic symbols
    PLUS = "PLUS"
    MINUS = "MIMUS"
    ASTERISK = "ASTERISK"
    SLASH = "SLASH"
    POW = "POW"
    MODULUS = "MODULUS"

    # Symbols
    SEMICOLON = "SEMICOLON"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"


class Token:
    def __init__(self, type, literal, line, pos):
        self.type = type
        self.literal = literal
        self.line = line
        self.pos = pos
    def __str__(self):
        return f"Token[{self.type} : {self.literal} : {self.line} : {self.pos}]"
    def __repr__(self):
        return self.__str__()


