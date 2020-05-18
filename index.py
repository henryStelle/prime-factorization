from datetime import datetime
from decimal import Decimal, getcontext

lineLength = 11


def main():
    print("Prime Number Factorization\n")
    num = int(input('Enter a number to factor: '))
    factorizeA(num)


def factorizeA(alpha):
    global lineLength
    primes = getPrimesFromFile()
    print('\nRealtime Progress...')
    if lineLength < len(str(alpha)) + 4: lineLength = len(str(alpha)) + 4
    printLine = lambda: print('+' + '-' * lineLength + '+' + '-' * lineLength + '+')
    printLine()
    print('| Factor ' + ' ' * (lineLength - 8) + '| Remainder ' + ' ' * (lineLength - 11) + '|')
    printLine()
    getcontext().prec = len(str(alpha))
    factor = 1
    lastFactor = 0
    power = 1
    factorsList = []
    squared = int(alpha) ** 0.5
    start = datetime.now()
    while alpha > 1 and factor <= alpha:
        while Decimal(Decimal(alpha) % int(factor ** power)) == 0 and factor != 1:
            power += 1
        else:
            if alpha % factor == 0:
                realPow = power - 1
                alpha = Decimal(Decimal(alpha) / int(factor ** realPow))
                factorsList.append([factor, realPow])
                presentBox(str(factor) + "^" + str(realPow), alpha)
                lastFactor = factor
                power = 1
                squared = int(alpha) ** 0.5
            elif factor < squared:
                current = datetime.now()
                percent = (factor - lastFactor) / (squared - lastFactor)
                print("| Calculating: {:.3%}    ETA: (sec) {:.2f}".format(percent, (
                        current - start).total_seconds() / percent * (1 - percent)), end='')
                print('', end='\r')
            elif factor >= squared:
                factorsList.append([int(alpha), 1])
                presentBox(str(alpha) + "^1", 1)
                alpha = 1
        if factor <= 2:
            factor += 1
        elif factor < 99991:
            factor = primes[primes.index(factor) + 1]
        else:
            factor += 2
    final = datetime.now()
    printLine()
    print("\ntotal time (s): {}".format((final - start).total_seconds()))
    return factorsList


def presentBox(factor, now):
    extraSpace = lambda x: ' ' * int(lineLength - 1 - len(str(x)))
    print('| {}{}| {}{}|'.format(factor, extraSpace(factor), now, extraSpace(now)))


def getPrimesFromFile():
    primes = []
    with open('primes_100k.txt', 'r') as file:
        for line in file:
            primes.append(int(line.strip()))
    return primes


main()
