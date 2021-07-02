prime = "Prime"

num = int(input("Enter Number: "))

for i in range(2, num):
  if num % i == 0:
    prime = "Not Prime"
    break
print(prime)
