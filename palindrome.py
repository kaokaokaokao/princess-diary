from sys import exit

print("palindrome? or not?")
s = input("say something\n")
n = len(s)-1
i = 0
while i < len(s) and s[i] == s[n]:
    i+=1
    n-=1
    if i == n or i - n == 1:
        print("yes, it's a palindrome")
        exit(0)
else:
    print("nope, it's not a palindrome")
    exit(1)
