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

for N in range(100):
    i = convert_base(str(N), 2, 10)
    if N % 2 == 0:
        i = i + '10'
    else:
        i = '1' + i + '01'
    R = convert_base(i, 10, 2)
    if int(R) > 516:
        print(N)