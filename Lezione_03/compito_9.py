#9

def cambio_segno(target:str = '3.14'):

    pi = 0
    denominatore = 1
    segno = 1
    counter = 0

    while True:

        pi += segno* (4/denominatore)

        segno *= -1
        counter += 1
        denominatore += 2

        if str(pi)[:len(target)] == target:

            print(f"le iterazioni per {target} sono: {counter} ")

            break

cambio_segno(target='3.14')
cambio_segno(target='3.141')
cambio_segno(target='3.1415')
cambio_segno(target='3.14159')

