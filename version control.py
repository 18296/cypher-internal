alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def cypher():
    while True:
        try: 
            cypherkey = int(input("enter original cypher key\t"))
            break
    
        except:
            pass

    while True:
        yesno = input("do you want to cypher or decypher\t")
        yesno = yesno.lower()
        if yesno == "decypher":
            cypherkey = -cypherkey
            break
        elif yesno == "cypher":
            break
        else:
            pass
    codein = input("enter word\t")
    codeinlist = list(codein)
    x=0
    char=codeinlist[x]
    if char in alphabet:
            index = alphabet.index(char)
            #print(index)
            while True:
                if (index+cypherkey)>25:
                    index = ((index+cypherkey)-(26+cypherkey))
                else:
                    break
                
    new_letternum = (index+cypherkey)
    new_letter = (alphabet[new_letternum])
    print(new_letter)

cypher()