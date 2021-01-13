from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
sabo = Cheat_Sabo_Dice()
swapper_score = 0
loaded_dice_score = 0
sabo_score = 0
number_of_games = 10
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()
  sabo.roll()
  print(f'{swapper.get_dice()}, {loaded_dice.get_dice()}, {sabo.get_dice()}')
  swapper.cheat()
  loaded_dice.cheat()
  sabo.cheat()
  #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

  print("Cheater 1 rolled" + str(swapper.get_dice()))
  print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  print("Sabo rolled" + str(sabo.get_dice()))
  swap_total = sum(swapper.get_dice())
  load_total = sum(loaded_dice.get_dice())
  sabo_total = sum(sabo.get_dice())
  total = [swap_total, load_total, sabo_total]
  print(total)
  if swap_total == load_total == sabo_total:
 #print("Draw!")
    pass
  elif max(total) == swap_total:
 #print("Dice swapper wins!")
    swapper_score+= 1
  elif max(total) == sabo_total:
    sabo_score += 1
  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Sabo won: " + str(sabo_score))
total_score = [swapper_score, loaded_dice_score, sabo_score]
if swapper_score == loaded_dice_score == sabo_score:
  print("Game was drawn")
elif max(total_score) == swapper_score:
  print("Swapper won most games")
elif max(total_score) == sabo_score:
  print("Sabo won most games")
else:
  print("Loaded dice won most games")

