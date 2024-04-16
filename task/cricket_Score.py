import random

print('======================================  TATA-IPL-2023  ======================================')

print('\nTEAMS : RCB,MI,KKR,CSK')

team = ['MI','GT','CSK','KKR','RCB']

user_choice = input('\nENTER YOUR TEAM :')

if user_choice in team :
    team.remove(user_choice)
else:
    print('TEAM ARE NOT FOUND')
    exit()

computer_team_choice = random.choice(team)

print('\nUSER :',user_choice)
print('\nOOP. :',computer_team_choice)

print('\nTOSS TIME :')

toss = ['head','tail']

user_toss_choice = input('\nENTER YOUR CHOICE :')
random_toss = random.choice(toss)

user_list = []
computer_list = []
#_____________________________________________________________________________________________________________
def user():
    run_list = [1,2,4,6,0,'wicket','no ball','wide']

    noball_list = [1,2,4,'wicket']

    run = 0
    wicket = 0
    balls = 0.0
    count = 1
    for i in range(80):
        
        ch = input()
                
        counter = random.choice(run_list)
        print(counter)
            
        if counter == 1:
            count += 1
            run += 1
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
        
        elif counter == 2:
            count += 1
            run += 2
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")

                
        elif counter == 4:
            count += 1
            run += 4
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('Its a boundry')

        elif counter == 6:
            count += 1
            run += 6
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('Its a SIX')
                
        elif counter == 0:
            count += 1
            run += 0
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                
        elif counter == 'wicket':
            count += 1
            wicket += 1
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('wicket')
            
        elif counter == 'no ball':
            noball_list_choice = random.choice(noball_list)

            if counter == 1:
                run += 1
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Free hit')
                
            elif counter == 2:
                run += 2
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Free hit')
                    
            elif counter == 4:
                run += 4
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Its a boundry')
                print('Free hit')

            elif counter == 'wicket':
                wicket += 1
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Free hit')
    
        elif counter == 'wide':
            balls += 0
            run += 1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('wide')

        if balls==0.6:
            user_list.append(run)
            print(f'\nTOTAL RUNS {user_choice} = {run}')
            break
#_____________________________________________________________________________________________________________
def computer():
    run_list = [1,2,4,6,0,'wicket','no ball','wide']

    noball_list = [1,2,4,'wicket']

    run = 0
    wicket = 0
    balls = 0.0
    count = 1
    for i in range(80):
        
        ch = input()
                
        counter = random.choice(run_list)
        print(counter)
            
        if counter == 1:
            count += 1
            run += 1
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
        
        elif counter == 2:
            count += 1
            run += 2
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")

                
        elif counter == 4:
            count += 1
            run += 4
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('Its a boundry')

        elif counter == 6:
            count += 1
            run += 6
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('Its a SIX')
                
        elif counter == 0:
            count += 1
            run += 0
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                
        elif counter == 'wicket':
            count += 1
            wicket += 1
            balls += 0.1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('wicket')
            
        elif counter == 'no ball':
            noball_list_choice = random.choice(noball_list)

            if counter == 1:
                run += 1
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Free hit')
                
            elif counter == 2:
                run += 2
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Free hit')
                    
            elif counter == 4:
                run += 4
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Its a boundry')
                print('Free hit')

            elif counter == 'wicket':
                wicket += 1
                print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
                print('Free hit')
    
        elif counter == 'wide':
            balls += 0
            run += 1
            print(f"{user_choice} : {run} / {wicket}  Balls:-{balls}")
            print('wide')

        if balls==0.6:
            computer_list.append(run)
            print(f'TOTAL RUNS {computer_team_choice} = {run}')
            break
#______________________________________________________________________________________________________________

if user_toss_choice == random_toss:
    print('\nYOU WON THE TOSS')

    user_choice = input('\nChoose Bat or ball first :')
    if user_choice == 'bat':
        try:
            print("\n============================  start game  ============================ ")
            print(f"\n============================    {user_choice}  ============================  ") 
            user()
            
        except:
            pass
        
        else:
            print("\n============================    {computer_team_choice}  ============================")
            computer()
            
        finally:
            if user_list == computer_list:
                print("\n============================    MATCH TAI  ============================  ")
                
            elif user_list < computer_list:
                print(f"\n============================    {computer_team_choice} won the match  ============================  ")
            else:
                print(f"\n============================  {user_choice} won the match============================  ")
    
    else:
        try:
            print("\n============================    start game  ============================  ")
            print(f"\n============================    {computer_team_choice}  ============================  ")
            computer()
            
        except:
            pass
        
        else:
            print(f"\n============================    {user_choice}  ============================  ")
            user()
            
        finally:
            if user_list == computer_list:
                print("\n============================    MATCH TAI  ============================  ")
                
            elif user_list < computer_list:
                print(f"\n============================   {computer_team_choice} won the match  ============================  ")

            else:
                print(f"\n============================  {user_choice} won the match============================  ")
    
else:
    print('OOP. WON THE TOSS')
    choice = ['bat','ball']
    oop_choice = random.choice(choice)

    if oop_choice == 'bat':
        try:
            print("\n============================    start game  ============================  ")
            print(f"\n============================    {computer_team_choice}  ============================  ")
            computer()
            
        except:
            pass
        
        else:
            print(f"\n============================    {user_choice}  ============================  ")
            user()
            
        finally:
            if user_list == computer_list:
                print("\n============================    MATCH TAI  ============================  ")
                
            elif user_list < computer_list:
                print(f"\n============================    {computer_team_choice} won the match  ============================  ")

            else:
                print(f"\n============================  {user_choice} won the match============================  ")
            
    else:
        try:
            print("\n============================    start game  ============================  ")
            print(f"\n============================    {user_choice}  ============================  ")
            user()
            
        except:
            pass
        
        else:
            print(f"\n============================    {computer_team_choice}  ============================  ")
            computer()
            
        finally:
            if user_list == computer_list:
                print("\n============================    MATCH TAI  ============================  ")
                
            elif user_list < computer_list:
                print(f"\n============================    {computer_team_choice} won the match  ============================  ")
            else:
                print(f"\n============================  {user_choice} won the match============================  ")

