def prime_factors(n: int) -> list[int]:
    divisori = []
    
    while n % 2 == 0:
        divisori.append(2)
        n //= 2
        
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            divisori.append(i)
            n //= i
        
    if n > 2:
        divisori.append(n)

    return divisori

 	

print(prime_factors(99999999999999999999))