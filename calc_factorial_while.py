num=int(input("Enter a number: "))
result=1
current_num=1

while current_num<=num:
    result*=current_num
    current_num+=1

print(f"The factorial of {num} is {result}")
