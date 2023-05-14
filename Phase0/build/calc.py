operators = {
   "(": "LPAREN",
   ")": "RPAREN",
   "!": "NOT",
   "*": "AND",
   "+": "OR"
}

def door(a):
    return "DOOR:N:" + a if "!" not in list(a) else "DOOR:I:" + a[1]

def strip_str(data):
    #return ''.join([x for x in data if x != " "])

    n=""
    for i in data:
        if i == " ":
            continue
        n+= i
    return n

def modify_and_count(input):
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
       

def lexer(input):
    literals, data = modify_and_count(input)
    tokens = []

    for i in data:
        try:
            tokens.append(operators[i])
        except:
            if i in literals:
                literal_char = i

                tokens.append(door(literal_char))
                continue
            
            print('Error: Invalid syntax, operator ' + i + ' not exist')
            return None
    
    return tokens
    


def true_table():
    for i in range(0, 16):
        term = str(bin(i))[2:]
        term = ("0"*(4-len(term)))+term 
        print(term)
    

def main():
    state = ""
    while True:
        print("> ")
        state = input()

        if state == "s":
            break

        print(lexer(state))
        #print(lexer("!ab!c+abc+!a!bc+!a!b!c"))
        #print(lexer("(!a+!b+c)(a+b+c)"))
            


true_table()
#main()
