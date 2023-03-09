num=1213
agila=num
rev=0
while num > 0:
    rem = num % 10 
    rev= rev * 10 + rem
    num = num // 10

print(rev)
print(f"Original Num= {num}")
print(f"Original Num= {agila}")

if rev == agila:
    print("Palindrome")
else:
    print("Not Palindrome")