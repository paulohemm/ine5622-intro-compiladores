transicoes = {
    "E": [[["T"], ["E'"]]],
    "E'": [[["+"], ["T"], ["E'"]], ["e"]],
    "T": [[["F"], ["T'"]]],
    "T'": [[["*"], ["F"], ["T'"]], [["e"]]],
    "F": [[["("], ["E"], [")"]], [["id"]]]
}

tabela = {
    "E": {
        "id": transicoes["E"][0],
        "(": transicoes["E"][0]
    },
    "E'": {
        "+": transicoes["E'"][0],
        ")": transicoes["E'"][1],
        "$": transicoes["E'"][1]
    },
    "T": {
        "id": transicoes["T"][0],
        "(": transicoes["T"][0]
    },
    "T'": {
        "+": transicoes["T'"][1],
        "*": transicoes["T'"][0],
        ")": transicoes["T'"][1],
        "$": transicoes["T'"][1]
    },
    "F": {
        "id": transicoes["F"][1],
        "(": transicoes["F"][0]
    }
}

entrada = ["id", "+", "id", "*", "id"]
pilha = ["$", "E"]
result = []

x = pilha.pop(-1)
coringa = ""
for token in entrada:
  i = 0
  print(["for", x, token])
  while token != x or coringa != x:
    print(["while", x, token])
    if token != "$":
      if x not in tabela or not tabela[x].get(token, False):
        print([x, token, tabela[x], x in tabela, token not in tabela[x]])
        raise Exception("Erro Sintático, busque comer cimento")
      elif token in tabela[x]:
        producao = tabela[x][token]
        print(f"{x} -> {producao}")
        reverso = producao[::-1]
        for prod in reverso:
          if prod[0] != "e":
            pilha.append(prod[0])
        print(f"pilha: {pilha}")
    x = pilha.pop(-1)
    if x == token:
      print(token)
      result.append(token)
      print(["result", result])
      coringa = x
      x = pilha.pop(-1)
      break


transicoes = {
    "PARAMLISTCALL": [[["ident,"], ["PARAMLISTCALL"]], [["ident"]], [["ε"]]],
    "NUMEXPRESSION": [[["TERM"], ["NUMEXPRESSION'"]]],
    "NUMEXPRESSION'": [[["+"], ["TERM"], ["NUMEXPRESSION'"]], [["-"], ["TERM"], ["NUMEXPRESSION'"]], [["ε"]]],
    "PROGRAM": [[["STATEMENT"]], [["FUNCLIST"]], [["ε"]]],
    "FUNCLIST": [[["FUNCDEF"], ["FUNCLIST"]], [["FUNCDEF"]]],
    "FUNCDEF": [[["def"], ["ident"], ["("], ["PARAMLIST"], [")"], ["{"], ["STATELIST"], ["}"]]],
    "PARAMLIST": [[["TIPO"], ["ident"], [",", "PARAMLIST"]], [["TIPO"], ["ident"]], [["ε"]]],
    "TIPO": [[["int"]], [["float"]], [["string"]]],
    "STATEMENT": [[["VARDECL"], [";"]], [["ATRIBSTAT"], [";"]], [["PRINTSTAT"], [";"]], [["READSTAT"], [";"]], [["RETURNSTAT"], [";"]], [["IFSTAT"]], [["FORSTAT"]], [["{"], ["STATELIST"], ["}"]], [["break"], [";"]], [[";"]]],
    "VARDECL": [[["TIPO"], ["ident"], ["INT'"]]],
    "INT'": [[["["], ["int_constant"], ["]"], ["INT'"]], [["ε"]]],
    "ATRIBSTAT": [[["LVALUE"], ["="], ["EXPRESSION"]], [["LVALUE"], ["="], ["ALLOCEXPRESSION"]], [["LVALUE"], ["="], ["FUNCCALL"]]],
    "FUNCCALL": [[["ident"], ["PARAMLISTCALL"]]],
    "PRINTSTAT": [[["print"], ["EXPRESSION"]]],
    "READSTAT": [[["read"], ["LVALUE"]]],
    "RETURNSTAT": [[["return"]]],
    "IFSTAT": [[["if"], ["("], ["EXPRESSION"], [")"], ["STATEMENT"], ["ELSE"]]],
    "ELSE": [[["else"], ["STATEMENT"]], [["ε"]]],
    "FORSTAT": [[["for"], ["("], ["ATRIBSTAT"], [";"], ["EXPRESSION"], [";"], ["ATRIBSTAT"], [")"], ["STATEMENT"]]],
    "STATELIST": [[["STATEMENT"], ["STATELIST'"]]],
    "STATELIST'": [[["STATELIST"]], [["ε"]]],
    "ALLOCEXPRESSION": [[["new"], ["TIPO"], ["["], ["NUMEXPRESSION"], ["]"], ["VAR2"]]],
    "VAR2": [[["["], ["NUMEXPRESSION"], ["]"]], [["ε"]]],
    "EXPRESSION": [[["NUMEXPRESSION"], ["COMPARADORES"], ["NUMEXPRESSION"]], [["NUMEXPRESSION"]]],
    "COMPARADORES": [[["<"]], [[">"]], [["<="]], [[">="]], [["=="]], [["!="]]],
    "TERM": [[["UNARYEXPR"], ["TERM'"]]],
    "TERM'": [[["OPERACOES"], ["UNARYEXPR"], ["TERM'"]], [["ε"]]],
    "OPERACOES": [[["*"]], [["/"]], [["%"]]],
    "UNARYEXPR": [[["+"], ["FACTOR"]], [["-"], ["FACTOR"]], [["FACTOR"]]],
    "FACTOR": [[["int_constant"]], [["float_constant"]], [["string_constant"]], [["null"]], [["LVALUE"]], [["("], ["NUMEXPRESSION"], [")"]]],
    "LVALUE": [[["ident"], ["LVALUE'"]]],
    "LVALUE'": [[["["], ["NUMEXPRESSION"], ["]"], ["LVALUE'"]], [["ε"]]]
}