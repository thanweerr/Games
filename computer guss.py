import random
low=int(input("input the lower limit\n"))
high=int(input("input the higher limit\n"))
evaluation=""
while evaluation!="correct":
    n=random.randint(low,high)
    print(n)
    evaluation=input(f"Is this the correct number. Or is it smaller or higher than {n}\n")
    if evaluation=="smaller":
        high=n-1
    elif evaluation=="higher":
        low=n+1
print("Computer found the correct number..........")