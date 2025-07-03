def inv(l:list[int])->None:
    if not l:
        print("vuota")
    
    else:
        print(l[-1])
        inv (l[:-1])

inv([1,2,3,4,5])