#!/bin/python3

"""Methods to decrypt the secretum."""

import sys


def decrypt(value):
    suma = 0
    for i in value:
        suma = suma + int(i)

    while (suma > 10):
        suma2 = 0
        for i in str(suma):
            suma2 = suma2 + int(i)
            suma = suma2
    return suma

""""
def decrypt(value):
    s = int(value)
    if (s < 10):
        return s
    else:
        suma = 0
        for i in str(value):
            suma = suma + int(i)
    return decrypt(str(suma))
"""

def main():
    """Main function to parse input/output
    and decrypt the secretum."""
    digits = str(sys.argv[1])
    last = int(sys.argv[2])
    result = decrypt(0)
    print('La clau per utilitzar el descodificador és {0}'.format(result))


if __name__ == '__main__':
    main()
