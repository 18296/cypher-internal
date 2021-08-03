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
    codein = codein.lower()
    codeinlist = list(codein)
    x=0
    wordlen = len(codein)
    new_word = ''
    
    while 0<wordlen:
        char=codeinlist[x]
        if char in alphabet:
            index = alphabet.index(char)
            #print(index)
            x = x+1
            wordlen = wordlen-1
            while True:
                if (index+cypherkey)>25:
                    index = ((index+cypherkey)-(26+cypherkey))
                else:
                    break
                
            new_letternum = (index+cypherkey)
            new_letter = (alphabet[new_letternum]) 
            new_word = (new_word+new_letter)

        else:
            wordlen = wordlen-1
            char=codeinlist[x]            
            new_word = (new_word+char)
            x = x+1                        
    print(new_word)

cypher()