num=int(input("Enter a positive integer: "))

if num==0:
    binary_str="0"
else:
    binary_str=""
    current=num
    while current>0:
        remainder=current%2
        binary_str=str(remainder)+binary_str
        current=current//2

print(f"{num} in binary is {binary_str}")
