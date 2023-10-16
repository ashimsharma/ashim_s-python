import random

print("A 1-over Cricket Match.")

bat_ball_choices = [1,2,3,4,6,"out"]
loop_control = 0 
match_stopped = 0
choice_control = 0
total = 0
total1 = 0


while loop_control < 2:
    
    if choice_control != 1:
        print()
        print("""[1] : Bat
[2] : Bowl
[3] : Quit""")
        print()
        choice1 = int(input("What do you want to do: "))
        print()

        choice_control = 1

    else:
        if choice1 == 1:
            count = 1  
            print(f"""Batting Instructions
[1] : Play the ball
[2] : Stop the match""")


            while count <= 6:
                print()
                
                bat = int(input(f"Play {count} ball? "))

                if bat == 1:
                    pass
 
                elif bat == 2:
                    print("Match Stopped!")
                    loop_control = 2
                    match_stopped = 1 
                    break

                else:
                    print("Try Again, Enter respective integer value as per in instructions!")
                    continue

                choice = random.choice(bat_ball_choices)

                print(f"{count} Ball: {choice}")

                if choice == "out":
                    print("You are out.")
                    print()
                    break
                else:
                    if choice == 6 or choice == 4:
                        print(f"Wow!You scored a boundary. Its a {choice}.")
                        total += choice
                    else:
                        total += choice

                if loop_control > 0:
                    if total > total1:
                        count = 7
                        loop_contol = 2
     
                count += 1
    
            loop_control += 1

            if match_stopped != 1:
                print()    
                print(f"Your total score is: {total}")
                print()
                if loop_control == 0 or loop_control == 1:
                    print("Its your turn to bowl now.")
                else:
                    print("Match Ended. Well played.")
                print()

                choice1 = 2    
                
        elif choice1 == 2:
            count = 1
            print("""Bowling Instructions
[1] : Bowl
[2] : Stop the match""")

            while count <= 6:
                print()
                ball = int(input(f"Bowl {count} ball? "))
                if ball == 1:
                    pass
                elif ball == 2:
                    print("Match Stopped!")
                    loop_control = 2
                    match_stopped = 1
                    break
                else:
                    print("Try Again, Enter respective integer value as per in instructions!")
                    continue

                choice = random.choice(bat_ball_choices)

                print(f"{count} Ball: {choice}")
                if choice == "out":
                    print("Wow!! You took a wicket.")
                    break
                else:
                    if choice == 6 or choice == 4:
                        print(f"Oops!! Its a boundary, Its {choice}.")
                        total1 += choice
                    else:
                        total1 += choice

                if loop_control > 0:
                    if total1 > total:
                        count = 7
                        loop_contol = 2   

                count += 1
            loop_control += 1

            if match_stopped != 1:
                print()    
                print(f"The other team's total score is: {total1}.")
                print()
            
                if loop_control == 0 or loop_control == 1:
                    print("Its your turn to bat now.")
                else:
                    print("Match Ended. Well played.")
                print()
                choice1 = 1

        elif choice1 == 3:
            print("Game Quitted")
            break

        else:
            print("Invalid Input. Try again. Enter respective integer values(1,2 or 3).")
            choice_control = 0
        


if match_stopped != 1:        
    if choice1 > 0 and choice1 < 3:
        if total > total1:
            print(f"Congratulations! You won the match.")
        elif total < total1:
            print(f"You lost the match with {total1 - total} runs. Better luck next time.")
        else:
            print("Its a draw!")

                
    

    

