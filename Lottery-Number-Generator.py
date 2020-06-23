import random
def generate(numbers):
    num=random.randint(1,49)
    if num in numbers:
        generate(numbers)
    return num
    
numbers=[]
for count in range(1,7):
    num=generate(numbers)
    numbers.append(num)

bonus=generate(numbers)
print(numbers)

    
user_nums=[]
for count in range(len(numbers)):
    user=int(input("What is ball number "+str(count+1)+"?"))
    user_nums.append(user)
user_bonus=int(input("And what is the bonus ball?"))
correct=0
for count in range(len(user_nums)):
    if user_nums[count]== numbers[count]:
        print("You got ball",count+1,"correct!")
        correct=correct+1
    else:
        print("You got ball",count+1,"wrong")
if user_bonus==bonus:
    print("And you got the bonus ball correct!")
    correct=correct+1
else:
    print("And you got the bonus ball wrong")
    
perball=1/49
probability=perball/correct
print("There was a "+str(probability)+"% chance that you would get this many right")


