from lexer import lexer

def true_table():
    for i in range(0, 16):
        term = str(bin(i))[2:]
        term = ("0"*(4-len(term)))+term 
        print(term)
    

def main():
    '''
    state = ""
    while True:
        print("> ")
        state = input()

        if state == "salir":
            break
    
        print(lexer(state))
    '''
    print(lexer("!ab!c+abc+!a!bc+!a!b!c"))
    #print(lexer("(!a+!b+c)(a+b+c)"))
            

if __name__ == "__main__":
    main()