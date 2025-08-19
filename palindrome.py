n = int(input("Enter a no. n : "))
reverseNum = 0
myNum = n

while(n > 0) :
    last_digit = n % 10
    reverseNum = reverseNum * 10 + last_digit
    n = n//10
if(myNum  == reverseNum):
    print(myNum,"=",reverseNum,"This no. is a Palindrome")
else:
    print("no.",myNum,"is NOT a palindrome")