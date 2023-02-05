import random
user=input("Choose your option\nr for rock\np for papper\ns for scissors\n")
comp=random.choice(['r','p','s'])
print(f"computer choise: {comp}\n")
if user==comp:
    print("tie")
elif user=='r' and comp=='p':
    print("Sorry!!!You lost")
elif user=='r' and comp=='s':
    print("Congrats!! You win")
elif user=='p' and comp=='r':
    print("Congrats!! You win")
elif user=='p' and comp=='s':
    print("Sorry!!!You lost")
elif user=='s' and comp=='r':
     print("Sorry!!!You lost")
elif user=='s' and comp=='p':
     print("Congrats!! You win")