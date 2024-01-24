# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


PLAYER1 = "x"
PLAYER2 = "y"

print("Welcome to the circus!")
print("Definition who starts the game")
option = input("Select player")
print("You have chosen")
import random

randint = random.randint(x,y )
print("The selection completed" + str(randint))
#Ja radom sistēma izvēla PLAYER1, tad viņš veic pirmo soļu spelē, ja nē, tad PLAYER2 veic pirmo soļu
if randint == PLAYER1
print("PLAYERS1 turn")
elif randint == PLAYER2
print("PLAYERS2 turn")

import random 
dice_roll = random.randint(1,6)
new_position = position + dice_roll


player_location = 1
ai_location = 1

def player_move():
    global player_location
    print("Now it is your turn")
    dice=input ()
    #Jā mēs atmētam daisu, tad viņam ir sešas sēnu malas, uz kuriem piezemēties
    if dice == "mest":
        dice = random.randint(1, 6)
        print("Done:", dice)
        player_location = player_location + dice
        #Mūsu spēles laukā ir speciālas zonas, kuri var palidzēt spēlētajām, vai otrādi padarīt sliktāk. Pirmkārt mums ir sarkanie pakāpieni, kuras mums palīdzēt uzvārēt.
        if player_location == 15:
           player_location = 24
            print("Success! You move to 24")
            elif player_location == 33:
                player_location = 52
                print("Success! You move to 52")
            elif player_location == 39
                player_location = 48
                print("Success! You move to 48")
            elif player_location == 87:
                player_location = 96
                print("Success! You move to 96")
        #Bet arī ir zilie pakāpieni, kuri kas traucē spēlētājam iet tālāk, pārnesot uz kaut kādu soļu skaiti atpakaļ.        
        if player _location == 18:
            player_location = 7
            print("Unfortunately, you move to 7")
            elif player_location == 67
                player_location == 46
                print("Unfortunately, you move to 46")
            elif player_location == 80
                player_location = 69
                print("Unfortunately, ypu move to 69")
            elif player_location == 74
            player location = 63
            print("Unfortunately, you move to 63")    

#Valerija Januškeviča 10.B



