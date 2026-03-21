import random as r
li=["Rock","Scissor","Paper"]

win={
    "Rock":"Scissor",
    "Scissor":"Paper",
    "Paper":"Rock"
}
userScore=0;
ComputerScore=0;
while True:
    s=r.choice(li);
    u=input("Enter Your Choice:\nScissor\nPaper \nRock\nclose\n");
    if u=="close":
        break;
    
    elif u not in li:
        print("Enter a Valid choice\n");
        continue
    
    elif u==s:
        print("Game Draw!");
        
    elif win[u]==s:
        print("You win")
        userScore+=1;
    
    else :
        print("You lose");
        ComputerScore+=1;
        
    
    print("computer "+s);
    print("\n")

print("Your Score: ",userScore);
print("Computer's Score: ",ComputerScore);

        
        
    


