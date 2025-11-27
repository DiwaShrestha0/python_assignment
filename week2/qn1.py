numbers = []
n = int(input("enter the range:"))
for k in range(n):
    element = float(input("Enter element:"))
    numbers.append(element)
for num in numbers:
    if num > 50:
        break
    elif num%5==0:
        continue
    else:
        print(num)

