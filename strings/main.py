# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

#PART 1
# 1.1 Players that scored at match Sovjet-Union - The Netherlands
player1 = "Ruud Gullit"
player2 = "Marco van Basten"

# 1.2 Minute of scored goals
goal_0 = 32
goal_1 = 54

# 1.3 print: <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = player1 + " " + str(goal_0) + ", " + player2 + " " + str(goal_1)
print(scorers)

# 1.4 Add extra info
firstGoal = player1 + " scored in the " + str(goal_0) + "nd minute"
secondGoal = player2 + " scored in the " + str(goal_1) + "th minute"
report = (firstGoal + "\n" + secondGoal)
print(report)

#PART 2
# 2.1 Choose player
player = "Hans van Breukelen"
print("Mijn gekozen voetbalspeler is: " + player)

#2.2 Slice first_name
first_name = player[0:player.find(" ")]
print("En zijn voornaam is: " + first_name)

#2.3 Last_name
last_name = player[player.find(" ")+1:]
print("En zijn achternaam is: " + last_name)

last_name_len = len(last_name)
print("Lengte achternaam: " + str(last_name_len) + " karakters")

#2.4 Name short
first_initial = player[0]
name_short = first_initial + ". " + last_name
print(name_short)

#2.5 Chant
first_name_len = len(first_name)
chant_single = first_name + "! "
chant = (f'{chant_single}' * first_name_len) [:-1]
print(chant)

#2.6 Good Chant
good_chant = (chant[-1:] != " ")
print(good_chant)