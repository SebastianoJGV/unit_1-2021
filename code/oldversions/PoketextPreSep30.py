#Description : Text based pokemon game with 3 base types of fire water and grass
#Date : 2021-08-16 - today
#Author : Sebastiano GV
#

import time
import sys
import random

#import playsound
#playsound('audio.mp3')
#Variable with start time
start_time = time.ctime()

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    
    
class player:
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.hp = 500
        self.acc_amt = (20, 12, 2)

        
        if element == "fire": 
            #If you are a fire type you have these moves
            self.weakness = "water"
            self.strong = "grass"
            self.moves = {
                #move PP
                "ember" : 25,
                "fire punch" : 15,
                "inferno" : 5
                }
            
            self.move_power = {
                #move power
                "ember" : 40,
                "fire punch" : 75,
                "inferno" : 100
                }
            self.accuracy = {
                "ember" : self.acc_amt[0],
                "fire punch" : self.acc_amt[1],
                "inferno" : self.acc_amt[2]
                }
        elif element == "grass":
            #If you are a grass type you have these moves
            self.weakness = "fire"
            self.strong = "water"
            self.moves = {
                #move PP
                "vine whip" : 25,
                "razor leaf" : 15,
                "petal dance" : 5
                }
            
            self.move_power = {
                #move power
                "vine whip" : 40,
                "razor leaf" : 75,
                "petal dance" : 100
                }
            self.accuracy = {
                "vine whip" : self.acc_amt[0],
                "razor leaf" : self.acc_amt[1],
                "petal dance" : self.acc_amt[2]
                }    
        elif element == "water":
            #If you are a grass type you have these moves
            self.weakness = "grass"
            self.strong = "fire"
            self.moves = {
                #move PP
                "bubble" : 25,
                "bubble beam" : 15,
                "hydro pump" : 5
                }
            
            self.move_power = {
                #move power
                "bubble" : 40,
                "bubble beam" : 75,
                "hydro pump" : 100
                }
            self.accuracy = {
                "bubble" : self.acc_amt[0],
                "bubble beam" : self.acc_amt[1],
                "hydro pump" : self.acc_amt[2]
                }           


def cpu_turn():
    delay_print("It is the CPU's turn!")
    rand_choice = random.randint(0, 2)
    cpu_command = " "
    if player2.element == "fire":
        if rand_choice == 0:
            cpu_command = "ember"
        elif rand_choice == 1:
            cpu_command = "fire punch"
        elif rand_choice == 2:
            cpu_command = "inferno"
    elif player2.element == "grass":
        if rand_choice == 0:
            cpu_command = "vine whip"
        elif rand_choice == 1:
            cpu_command = "razor leaf"
        elif rand_choice == 2:
            cpu_command = "petal dance"
    else:
        if rand_choice == 0:
            cpu_command = "bubble"
        elif rand_choice == 1:
            cpu_command = "bubble beam"
        elif rand_choice == 2:
            cpu_command = "hydro pump"
    if player2.moves[cpu_command] > 0:
        miss_chance = random. randint(0, player2.accuracy.get(cpu_command))
        if miss_chance != 1:
            delay_print(str(player2.name)+" uses " + str(cpu_command)+" against "+str(player1.name)+ ". ")
            if player1.element == player2.strong:
                delay_print(str(cpu_command) + " is super effective! ")
                attack_power = round(player2.move_power.get(cpu_command)*1.5)
                delay_print(str(player1.name) + " takes " + str(attack_power) + " damage! \n")
                player1.hp -= attack_power
#                    
            elif player1.element == player2.weakness:
                delay_print(". It is not very effective...")
                attack_power = round(player2.move_power.get(cpu_command)*0.5)
                delay_print(str(player1.name) + " takes " + str(attack_power) + " damage... \n")
                player1.hp -= attack_power
#                    
            else:
                attack_power = player2.move_power.get(cpu_command)
                delay_print(str(player1.name) + " takes " + str(attack_power) + " damage! \n")
                player1.hp -= attack_power
            #decrease pp by 1 
             
        else:
            delay_print("the attack missed! \n")
            player2.moves[cpu_command] -= 1
           
    else:
         delay_print("You do not have any PP left. \n")   

    

#Function battle checks if someone has lost, and alternates between players
# or between players and the cpu
def battle():
    while True:
        player1_turn()
        if player2.hp <= 0:
            delay_print(str(player2.name) + " fainted...")
            delay_print(str(player1.name) + " is the winner! \n")
            break
        
        if game_type == "pvp":
            player2_turn()
            
        else:
            cpu_turn()
            
        if player1.hp <= 0:
            delay_print(str(player1.name) + " fainted...")
            delay_print(str(player2.name) + " is the winner! \n")
            break
 



def player1_turn():
    delay_print(str(player1.name) +  ", it is your turn! Choose an attack! ")
    delay_print(str(player1.name) + " has " + str(player1.hp) +  " health left. ")
    delay_print("your pokemon knows: " + str(player1.moves))
    p1_command = input(" > ").lower()
    if p1_command in player1.moves:
        
        if player1.moves[p1_command]>0:#make sure we have not run out of pp
            miss_chance = random. randint(0, player1.accuracy.get(p1_command))
            
            if miss_chance!=1:
                delay_print(str(player1.name)+" uses " + str(p1_command)+" against "+str(player2.name)+ ". ")
                
                if player2.element == player1.strong:
                    delay_print(str(p1_command) +" is super effective! ")
                    attack_power = round(player1.move_power.get(p1_command)*1.5)
                    delay_print(str(player2.name) + " takes " + str(attack_power) + " damage! \n")
                    player2.hp -= attack_power
                    
                elif player2.element == player1.weakness:
                    delay_print(". It is not very effective...")
                    attack_power = round(player1.move_power.get(p1_command)*0.5)
                    delay_print(str(player2.name)+ " takes " + str(attack_power) + " damage... \n")
                    player2.hp -= attack_power
                    
                else:
                    attack_power = player1.move_power.get(p1_command)
                    delay_print(str(player2.name) + " takes " + str(attack_power) + " damage! \n")
                    player2.hp -= attack_power
                #decrease pp by 1
                player1.moves[p1_command] -= 1    
                
            else: 
                delay_print("the attack missed! \n")
                player1.moves[p1_command] -= 1
                
        else:
            delay_print("You do not have any PP left. \n")   
            
    else:
        delay_print("You did not choose a valid attack and have forfeited your turn \n")  
   
   
        
def player2_turn():
    delay_print(str(player2.name) + ", it is your turn! Choose an attack! ")
    delay_print(str(player2.name) + " has " + str(player2.hp) + " health left. ")
    delay_print("your pokemon knows " + str(player2.moves))
    p2_command = input(" > ").lower()
    
    if p2_command in player2.moves:
        if player2.moves[p2_command]>0:#make sure we have not run out of pp
            miss_chance = random. randint(0, player2.accuracy.get(p2_command))
            
            if miss_chance!=1:
                delay_print(str(player2.name) + " uses " + str(p2_command) + " against " + str(player1.name) + ". ")
                
                if player1.element == player2.strong:
                    delay_print(str(p2_command) + " is super effective! ")
                    attack_power = round(player2.move_power.get(p2_command)*1.5)
                    delay_print(str(player1.name) + " takes " + str(attack_power) + " damage! \n")
                    player1.hp -= attack_power
                    
                elif player1.element == player2.weakness:
                    delay_print(". It is not very effective...")
                    attack_power = round(player2.move_power.get(p2_command)*0.5)
                    delay_print(str(player1.name) + " takes " + str(attack_power) + " damage... \n")
                    player1.hp -= attack_power
                    
                else:
                    attack_power = player2.move_power.get(p2_command)
                    delay_print(str(player1.name) + " takes " + str(attack_power) + " damage! \n")
                    player1.hp -= attack_power
                #decrease pp by 1
                player2.moves[p2_command] -= 1    
                
            else: 
                delay_print("the attack missed! \n")
                player2.moves[p2_command] -= 1
                
        else:
            delay_print("You do not have any PP left. \n")   
            
    else:
        delay_print("You did not choose a valid attack and have forfeited your turn... \n")  
        
#Bit intimidating, but it just asks for parameters       
while True:
    delay_print("Welcome to Pokemon text edition. ")
    game_type = input("Choose game type: (PvP or PvCPU)").lower()#code works with lowercase letters only
    player_name = input("Player 1, input your name: ")
    
    while True:#select type, this decided moves, strengths, etc
        player_type = input(str(player_name) + " choose a type out of fire, grass, or water: ").lower()
        
        if player_type == "fire" or player_type == "grass" or player_type == "water":
            break
        else:
            delay_print("enter a type correctly, options are fire, grass, or water: ")
    player1 = player(player_name, player_type)#assign player 1 the name and type
    print()#empty space
    
    #If its pvp, repeat for player 2
    if game_type == "pvp":
        player_name = input("Player 2, input your name: ")
        
        while True:
            player_type = input(str(player_name) + " choose a type out of fire, grass, or water: ").lower()
            if player_type == "fire" or player_type == "grass" or player_type == "water":
                break
            else:
                delay_print("enter a type correctly, options are fire, grass, or water: ")
        player2 = player(player_name, player_type)
        print(" ")
    
    #if it is not pvp, randomly assign the cpu a type
    else:
        player_name = "CPU"
        rand_type = random.randint(0, 2)
        if rand_type == 0:
            player_type = "fire"
        elif rand_type == 1:
            player_type = "grass"
        else:
            player_type = "water"
        player2 = player(player_name, player_type)
        print()
                                  
    battle()
    end_time = time.ctime()
    delay_print("Match went from " + str(start_time) + " to " + str(end_time) + " \n")
    yn = input("Do you want to play again? y/n")
    if yn[0] == "n":
        break
    else:
        delay_print("Restarting game! \n")
delay_print("Thank you for playing.")
