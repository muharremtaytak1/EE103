x=float(input("Enter a fraction between 0 and 1: "))

binary_str="0."

fraction=x
while fraction>0:
    fraction=fraction*2
    bit=int(fraction)
    binary_str+=str(bit)
    fraction=fraction-bit

print(f"{x} in binary is: {binary_str}")
