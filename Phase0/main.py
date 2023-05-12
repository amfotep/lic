from lexer import lexer, strip_str

def main():
    print(lexer("!ab!c+abc+!a!bc+!a!b!c"))
    #print(lexer("(!a+!b+c)(a+b+c)"))


if __name__ == "__main__":
    main()