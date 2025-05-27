from Lexer import Lexer

LEXER_DEBUG = True

if __name__ == '__main__':
    with open("lexer.opl", "r") as f:
        code = f.read()

    if LEXER_DEBUG:
        debug_lex = Lexer(code)
        while debug_lex.current_char is not None:
            print(debug_lex.next_token())