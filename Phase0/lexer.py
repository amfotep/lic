# =====================================
#         LOGIC CIRCUITS LEXER
# =====================================

operators = {
   "(": "LPAREN",
   ")": "RPAREN",
   "!": "NOT",
   "*": "AND",
   "+": "OR",
   "DOOR": lambda a : f"DOOR:N:{a}" if "!" not in list(a) else f"DOOR:I:{a[1]}", 
}

def strip_str(data):
    return ''.join([x for x in data if x != " "])

    n=""
    for i in data:
        if i == " ":
            continue
        n+= i
    return n

def modify_and_count(input: str):
    literals=[]
    count_rec=-1
    new_input=""
    data = strip_str(input)

    for i in data:
        count_rec+=1
        
        new_input+=i

        if ord(i) in range(97, 123) and i not in literals:
            literals.append(i)

        if data[count_rec] in ["(", "!"]:
            continue

        if count_rec < len(data)-1 and (data[count_rec+1] not in ["+", ")"]):
            if data[count_rec] != "+":
                new_input+="*"
                continue
        

    
    return [literals, new_input]
       

def lexer(input: str):
    literals, data = modify_and_count(input)
    tokens = []

    for i in data:
        try:
            tokens.append(operators[i])
        except:
            if i in literals:
                literal_char = i

                tokens.append(operators["DOOR"](literal_char))
                continue
            
            print(f'Error: Invalid syntax, operator "{i}" not exist')
            return None
    
    return tokens
    
