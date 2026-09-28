print("Welcome to Quize Game")
playing = input("Do You Want To Play The Quiz Game ")
score =0

if playing.lower() != "yes":
    quit()
answer = input("What is national Animal ")
if answer.lower() == "lion":
    score += 1
    print("coorect! " +"Your Score is "+ str(score))
   
else:
    print("Incorrect")

answer = input("What is national Bird  ")
if answer.lower() == "peacock":
    score += 1
    print("coorect! " +"Your Score is "+ str(score))
   
else:
    print("Incorrect")
    
answer = input("What is national River ")
if answer.lower() == "Ganga":
    score += 1
    print("coorect! " +"Your Score is "+ str(score))
   
else:
    print("Incorrect")
    
answer = input("What is national Flag ")
if answer.lower() == "Tiranga":
    score += 1
    print("coorect! " +"Your Score is "+ str(score))
   
else:
    print("Incorrect")
    
answer = input("What is national Festival ")
if answer.lower() == "Deepawali":
    score += 1
    print("coorect! " +"Your Score is "+ str(score))
   
else:
    print("Incorrect")
    
answer = input("What is national Anthum ")
if answer.lower() == "janman Gan":
    score += 1
    print("coorect! " +"Your Score is "+ str(score))
   
else:
    print("Incorrect")
    
print("Your Total Score is "+ str(score))