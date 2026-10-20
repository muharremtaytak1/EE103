found=False 

for a in range(11):
    for b in range(11):
        for c in range (11):
            if b==a-2 and c==2*a and (a+b+c)==10:
                print(f"Alyssa sold {a} tickets.")
                print(f"Ben sold {b} tickets.")
                print(f"Cindy sold {c} tickets.")
                found=True
                break
        if found:
            break
    if found:
        break
    