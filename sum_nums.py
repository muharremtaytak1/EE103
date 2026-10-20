num=int(input("Enter a number: "))

total_sum=0
current_num=0
while current_num<=num:
    total_sum+=current_num
    current_num+=1

sum_gauss=(num*(num+1))/2

if total_sum==sum_gauss:
    print(f"My running sum code works correctly and result is {total_sum}")
else:
    print("My running sum code failed badly")


