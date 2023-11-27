letras_min = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
letras_mai = [letra.upper() for letra in letras_min]
letras = letras_min + letras_mai
digito = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = [
    '(', ')', '[', ']', '{', '}', '=', '>', '<', '+', '-', '*', '/', '&', '|',
    '^', '%', ';', '!', ','
]
simbolos_complexos = ['!=', '>=', '<=', '==']
aceitos = letras + digito + ["_"]

identificadores = {}

def analyze_word(word, row, column):
  reserved = {
      'def': 'DEF',
      'int': 'INT',
      'float': 'FLOAT',
      'string': 'STRING',
      'break': 'BREAK',
      'print': 'PRINT',
      'return': 'RETURN',
      'if': 'IF',
      'else': 'ELSE',
      'for': 'FOR',
      'new': 'NEW',
      'null': 'NULL',
      '=': 'EQUAL',
      '(': 'OPEN_PARENTHESES',
      ')': 'CLOSE_PARENTHESES',
      '[': 'OPEN_BRACKET',
      ']': 'CLOSE_BRACKET',
      '{': 'OPEN_BRACE',
      '}': 'CLOSE_BRACE',
      ';': 'SEMICOLON',
      '+': 'PLUS',
      '-': 'MINUS',
      '*': 'MULTIPLY',
      '/': 'DIVIDE',
      '%': 'MODULO',
      '&': 'AND',
      '|': 'OR',
      '^': 'XOR',
      '>': 'GREATER',
      '<': 'LOWER',
      '<=': 'LOWER_EQUAL',
      '>=': 'GREATER_EQUAL',
      '==': 'EQUAL_EQUAL',
      '!=': 'NOT_EQUAL',
      '!': 'NOT',
      ',': 'COMMA',
  }
  if word in reserved:
    return reserved[word]
  
  if word in identificadores:
    identificadores[word].append({"row": row, "column": column})
  else:
    identificadores[word] = [{"row": row, "column": column}]
  return "IDENT"


def is_letter(char):
  return char in letras


def is_digit(char):
  return char in digito


def is_operator(char):
  return char in ['+', '-']


def is_space(char):
  return char == ' '


def analyze_token(buffer, row, column):
  if buffer[0] in letras or (len(buffer) == 1 and buffer[0] in simbolos):
    return analyze_word(''.join(buffer), row, column)
  elif buffer[0] in digito + ["+", "-"]:
    if '.' in buffer:
      return "FLOAT_CONSTANT"
    else:
      return "INT_CONSTANT"
  elif (len(buffer) == 1 and buffer[0] == ';'):
    return analyze_word(''.join(buffer), row, column)
  elif buffer[0] == '"' and buffer[-1] == '"':
    return "STRING_CONSTANT"
  elif buffer[0] in simbolos:
    return analyze_word(''.join(buffer), row, column)
  else:
    raise Exception(f"Erro léxico linha: {row}, coluna: {column}")


def lexical_analysis(line, row):
  lex_line = []
  buffer = []
  column = 0

  for char in line.strip():
    column += 1

    if not buffer and is_space(char):
      continue

    elif buffer and (is_letter(buffer[0]) and char not in aceitos):
      lex_line.append(analyze_token(buffer, row, column))
      buffer = []
      if not is_space(char):
        buffer.append(char)

    elif buffer and (is_digit(buffer[0]) and char not in aceitos
                     and char != '.'):
      lex_line.append(analyze_token(buffer, row, column))
      buffer = []
      if not is_space(char):
        buffer.append(char)

    elif buffer and (buffer[0] in ["+", "-"] and char not in digito + ["."]):
      lex_line.append(analyze_token(buffer, row, column))
      buffer = []
      if not is_space(char):
        buffer.append(char)

    elif buffer and buffer[0] == '"' and buffer[
        -1] == '"' and char not in aceitos:
      lex_line.append(analyze_token(buffer, row, column))
      buffer = []
      if not is_space(char):
        buffer.append(char)

    elif (buffer and (buffer[0] in simbolos)
          and char not in simbolos + simbolos_complexos + digito + ['.']):

      if len(buffer) == 2 and (buffer[0] + buffer[1]) in simbolos_complexos:
        lex_line.append(analyze_token(buffer, row, column))
      else:
        for i in buffer:
          lex_line.append(analyze_token(i, row, column))
      
      buffer = []
      if not is_space(char):
        buffer.append(char)

    else:
      buffer.append(char)


  if buffer:
    if buffer[0] in simbolos:
      for i in buffer:
        lex_line.append(analyze_token(i, row, column))
    else:
      lex_line.append(analyze_token(buffer, row, column))

  return lex_line


def main():
  lex = []
  for i, line in enumerate(linhas):
    lex_line = lexical_analysis(line, i + 1)
    lex.append(lex_line)
    print(f"Linha {i+1}: {lex_line}")

  format_ident  = '\n'.join('{}\t{}'.format(k, v) for k, v in identificadores.items())
  print(f"\nIdentificadores: \n{format_ident}")

if __name__ == "__main__":
    entrada = input("Digite o numero (1, 2 ou 3) de uma da opcoes abaixo e aperte enter: \n1 - exemplo1.lcc\n2 - exemplo2.lcc\n3 - exemplo3.lcc\n")
    swtich = {
        '1': 'exemplo1.lcc',
        '2': 'exemplo2.lcc',
        '3': 'exemplo3.lcc'
    }
    print(f'\nArquivo selecionado: {swtich[entrada]}\n')
    f = open(swtich[entrada], "r")
    linhas = f.readlines()

    main()