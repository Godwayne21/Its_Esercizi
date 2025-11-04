import string

def count_word(liz:list[str]) -> dict[str,int]:

    diz = {}

    for i in liz:
        i = i.lower()
        for x in i:
            if x in string.punctuation:
                x.replace()
        
            x.replace(" ", '""')
        
        liz_clean = i.split()
            
    for word in liz_clean:
        if word not in diz:
            count = 0
            diz[word] = 1
        
        else:
            diz[word]  = count+1
    
    return diz