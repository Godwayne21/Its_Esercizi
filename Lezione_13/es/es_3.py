def recursiveFactorial(n:int) ->int:

    if n == 1:
        return n * 1
    if n == 0:
        return n * 1

    else:
        return n*recursiveFactorial(n-1)

print(recursiveFactorial(6))