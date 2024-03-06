def binary(num, n):

    bin_str = str(bin(abs(eval(num))))[2:]  # 0b111
    l = len(bin_str)

    if (l > n or eval(num) > 2**(n-1)-1 or eval(num) < -2**(n-1)):
        raise Exception("Invalid")

    if (eval(num) >= 0):
        bin_str = "0" * (n-l) + bin_str

    else:

        bin_str = "0" * (n-l) + bin_str

        bin_str = list(bin_str)

        for i in range(len(bin_str)):

            if (bin_str[i] == '1'):
                bin_str[i] = '0'

            else:
                bin_str[i] = '1'

        bin_str = ''.join(bin_str)

        bin_str = int(bin_str, 2) + int("1", 2)

        bin_str = str(bin(bin_str))[2:]

    return bin_str