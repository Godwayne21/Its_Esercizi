#1
def convert(x:list[tuple])->dict:

    diz = {}

    for i in x:
        key,value = i[0],i[1]
        
        if key in diz:
          diz[key] += value
        
        else:
          diz[key] = value

    return diz

el=[(1,"x"),(2,"Y"),(3,"Z")]
print(convert(el))

