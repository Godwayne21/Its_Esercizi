def compoundInterest(t:int, m:float) -> float:
    if m == 0:
        return 0
    
    if t == 0:
        return m
    
    else:
        return (compoundInterest(t-1, m*1.005))
    
print(compoundInterest(1,3))