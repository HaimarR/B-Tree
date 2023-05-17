import time

myArray = []
for i in range(1000):
    myArray.append(i)

start = time.time()
for num in myArray:
    print(num)
check = time.time()
print(check - start)

print(myArray[0:1000])
end = time.time()
print(end - check)