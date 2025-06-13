from string import ascii_lowercase, punctuation

def count_unique_words(s:str)->dict[str,int]:

    d:dict[str,int] = {}
    s = s.split(" ") #ritorna una lista di stringhe in questo caso saparate da spazi

    for token in s:
        token_lower:str = token.lower()

        clean_token:str = token_lower.strip(punctuation) # punctuation contiene una stringa "!?,.:;..."

        if not clean_token: # or (len(clean_token)%2)=0:
            continue

        if clean_token in d:
            d[clean_token] += 1
        
        else:
            d[clean_token] = 1
    
    return d