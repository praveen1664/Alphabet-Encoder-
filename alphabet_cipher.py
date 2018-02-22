#!/usr/bin/python
def alphabet_encode(number, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Converts an integer to an alphabet equivilent"""
    if not isinstance(number, (int, long)):
        raise TypeError("number must be an integer")

    if 0 <= number - 1 < len(alphabet):
        return alphabet[number - 1]

    base = ''
    while number != 0:
        number, r = divmod(number, len(alphabet))
        if r == 0:
            number = number - 1
        base = alphabet[r - 1] + base
    return base


def alphabet_decode(value, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    value.isalpha()
    value = value.upper()[::-1]
    number = 0
    for i in range(len(value)):
        number = ((len(alphabet) ** i) * (alphabet.index(value[i]) + 1)) + number
    return number


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="encode/decode alphabet (base26)")
    parser.add_argument(
        "type", metavar="T", nargs=1, help="'encode' or 'decode")
    parser.add_argument(
        "item", metavar="N", nargs=1, help="The item to encode/decode")

    args = parser.parse_args()
    item = args.item[0]
    code = args.type[0]
    if code.lower() == "encode":
        print alphabet_encode(int(item))
    elif code.lower() == "decode":
        print alphabet_decode(item)
