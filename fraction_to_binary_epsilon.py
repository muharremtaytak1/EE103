x=float(input("Enter a fraction between 0 and 1: "))
epsilon=0.00001

binary_str="0."
fraction=x
current_value=0.0
power=1

while abs(current_value - x) > epsilon:
    fraction=fraction*2
    bit=int(fraction)
    binary_str+=str(bit)
    fraction=fraction-bit

    current_value += bit*(2**(-power))
    power+=1

print(f"{x} in binary (approx): {binary_str}")
print(f"Approximated decimal value: {current_value}")
print(f"Error: {abs(current_value - x)}")
