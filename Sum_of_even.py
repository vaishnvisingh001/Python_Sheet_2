A = int(input("Enter a no. : "))

i = 1
sum = 0
while i <= A :
    if i%2 == 0 :
        sum += i
    i += 1
print(sum)