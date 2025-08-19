N = int(input("Enter a no. : "))

if N == 0:
    print(1)
elif(N < 0):
     print("Please Enter a positive Number")
else : 
    count = 0
    while N > 0:
            last_digit = N % 10  
            count += 1
            N = N // 10
    print(count)