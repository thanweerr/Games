import random
low=int(input("Enter the lowest\n"))
high=int(input("Enter the highest limit\n"))
n=random.randint(low,high+1)
guss=0
while guss!=n:
    guss=int(input("Guess the number\n"))
    if guss<low or guss>high:
       print("Guess again\n")
    elif guss>n:
        print(f"sorry!! number is smaller than {guss}\n")
    elif guss<n:
        print(f"sorry!! number is higher than {guss}\n")
print(f"Congrats..........You guessed correctly")
