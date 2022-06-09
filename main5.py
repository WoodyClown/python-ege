def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

for N in range(1000):
    i = convert_base(str(N), 5, 10)
    if N % 5 == 0 or N % 5 == 2 or N % 5 == 4:
        i = i + '2'
    else:
        i = '2' + i + '3'

    if int(convert_base(i, 10, 5)) < 1000:
        print(N)