import random
print("HELLO ...\nWelcome to the game...!")
print("***INSTRUCTION*** \n1.Rock beats scissor \n2.Paper beat Rock \n3.scissor beat paper\n")


def asking_input():
    while True:
        choice=['rock','paper','scissor']
        user_c=input("\nEnter your choice (rock,paper,scissors):").lower()
        if user_c not in choice:
            print("invalid input..")
            continue
        return user_c
        

user_count=0
sys_count=0

while True:
        print("your score:",user_count)
        print("computer score:",sys_count)
        sys=random.choice(['rock','paper','scissor']).lower()
        c=input("\ndo you want to play (yes/no)..?").lower()
        
        
        if c=='yes':
            user=asking_input()
            print(f"\ncomputer's choice = {sys}")
            print(f"user's choice ={user}")
            
            if sys==user:
                 print("IT IS TIE..")
            elif (sys=='rock' and user=='scissor') or (sys=='paper' and user=='rock') or (sys=='scissor' and user=='paper'):
                 print("COMPUTER WINS!!!")
                 sys_count+=1
            else:
                 print("YOU WINS!!")
                 user_count+=1
        elif c=='no':
            print("thank you !!")
            break
        else:
            print("invalid input...choose again..!!")        
        
        

            