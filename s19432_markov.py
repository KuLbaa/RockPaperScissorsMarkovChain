import random
import datetime
won = lose = tie = 0.0

MatrixW = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
MatrixL = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
MatrixT = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}

r = 3
p = 3

tMatrix = [[0] * p for i in range(r)]
tMatrixL = [[0] * p for i in range(r)]
tMatrixT = [[0] * p for i in range(r)]

probabilities = [1 / 3, 1 / 3, 1 / 3]


def checkWin(user, machine):
    win = False
    tie = False
    if (user == 0):
        if (machine == 2):
            win = True
            tie = False
        elif (machine == 1):
            win = False
            tie = False
        elif (machine == 0):
            tie = True
        else:
            print("ERROR")
    elif (user == 1):
        if (machine == 0):
            win = True
            tie = False
        elif (machine == 2):
            win = False
            tie = False
        elif (machine == 1):
            tie = True
        else:
            print("ERROR")
    else:
        if (machine == 1):
            win = True
            tie = False
        elif (machine == 0):
            win = False
            tie = False
        elif (machine == 2):
            tie = True
        else:
            print("ERROR")

    if (tie == True):
        checkStats(2)
        return "Tied!"
    elif (win):
        checkStats(0)
        return "Win!"
    else:
        checkStats(1)
        return "Lose!"




def Game():
  global probabilities
  choices = ["Rock","Paper","Scissors"]
  pick = ['r','p','s']
  playing = True
  prevChoice = ""
  choice = 3
  probRock = 0
  probPaper = 0
  probScissors = 0

  try:
      choice = int(input("Pick one: 0 - Rock, 1 - Paper, 2 - Scissors \n"))
  except ValueError:
    print("you must enter an integer \n")
  if((choice > 2 or choice < 0)):
    print("you must enter 0, 1 or 2 \n")
    while((choice > 2 or choice < 0)):
      try:
        choice = int(input("Pick one: 0 - Rock, 1 - Paper, 2 - Scissors \n"))
      except ValueError:
        print("you must enter an integer \n")

  computerChoice = random.randint(0, 2)
  result = checkWin(choice, computerChoice)
  print ("You chose %s" % choices[choice])
  print ("The Computer chose %s" % choices[computerChoice])
  print("You %s" % result)
  print("User score: ", won)
  print("Computer score: ", lose, "\n")
  prevChoice = choice

  while(playing):
    choice = 3
    if (won == 5 or lose == 5):
        print("Thanks for Playing!\n")
        playing = False
    else:
        try:
          choice = int(input("Pick one: 0 - Rock, 1 - Paper, 2 - Scissors \n"))
        except ValueError:
          print("you must enter 0, 1 or 2 \n")
        if ((choice > 2 or choice < 0)):
            print("you must enter 0, 1 or 2 \n")
            while ((choice > 2 or choice < 0)):
                try:
                    choice = int(input("Pick one: 0 - Rock, 1 - Paper, 2 - Scissors \n"))
                except ValueError:
                    print("you must enter an integer \n")
        else:
          transMatrix = TransProbabilities(prevChoice, choice, result)
          computerChoice = random.randint(1, 100)
          probabilities[0] = transMatrix[prevChoice][0]
          probabilities[1] = transMatrix[prevChoice][1]
          probabilities[2] = transMatrix[prevChoice][2]
          rangeR = probabilities[0] * 100
          rangeP = probabilities[1] * 100 + rangeR
          if (computerChoice <= rangeR):
            computerChoice = 1
          elif (computerChoice <= rangeP):
            computerChoice = 2
          else:
            computerChoice = 0

          result = checkWin(choice, computerChoice)
          prevChoice = choice
          print ("You chose %s" % choices[choice])
          print ("The Computer chose %s" % choices[computerChoice])
          print("You %s" % result)
          print("User score: ", won)
          print("Computer score: ", lose, "\n")

def TransProbabilities(pC, c, result):
  global MatrixW
  global MatrixL
  global MatrixT
  pick = ['r','p','s']

  if result == "Win!":
    for i, x in MatrixW.items():
      if ('%s%s' % (pick[pC],pick[c]) == i):
        MatrixW['%s%s' % (pick[pC], pick[c])] += 1
  elif result == "Tied!":
    for i, x in MatrixT.items():
      if ('%s%s' % (pick[pC],pick[c]) == i):
        MatrixT['%s%s' % (pick[pC], pick[c])] += 1
  else:
    for i, x in MatrixL.items():
      if ('%s%s' % (pick[pC],pick[c]) == i):
        MatrixL['%s%s' % (pick[pC], pick[c])] += 1

  return TransMatrix(result)

def TransMatrix(result):
  global tMatrix
  global tMatrixL
  global tMatrixT

  if result == "Win!":
    rock = MatrixW['rr'] + MatrixW['rs'] + MatrixW['rp']
    paper = MatrixW['pr'] + MatrixW['ps'] + MatrixW['pp']
    scissors = MatrixW['sr'] + MatrixW['ss'] + MatrixW['sp']
    pick = ['r', 'p', 's']
    for i_row, row in enumerate(tMatrix):
      for i_column, item in enumerate(row):
          a = int(MatrixW['%s%s' % (pick[i_row], pick[i_column])])
          if (i_row == 0):
            c = a/rock
          elif (i_row == 1):
            c = a/paper
          else:
            c = a/scissors
          row[i_column] = float(c)
    return (tMatrix)
  elif result == "Tied!":
    rock = MatrixT['rr'] + MatrixT['rs'] + MatrixT['rp']
    paper = MatrixT['pr'] + MatrixT['ps'] + MatrixT['pp']
    scissors = MatrixT['sr'] + MatrixT['ss'] + MatrixT['sp']
    pick = ['r', 'p', 's']
    for i_row, row in enumerate(tMatrixT):
      for i_column, item in enumerate(row):
          a = int(MatrixT['%s%s' % (pick[i_row], pick[i_column])])
          if (i_row == 0):
            c = a/rock
          elif (i_row == 1):
            c = a/paper
          else:
            c = a/scissors
          row[i_column] = float(c)
    return (tMatrixT)

  else:
    rock = MatrixL['rr'] + MatrixL['rs'] + MatrixL['rp']
    paper = MatrixL['pr'] + MatrixL['ps'] + MatrixL['pp']
    scissors = MatrixL['sr'] + MatrixL['ss'] + MatrixL['sp']
    pick = ['r', 'p', 's']
    for i_row, row in enumerate(tMatrixL):
      for i_column, item in enumerate(row):
          a = int(MatrixL['%s%s' % (pick[i_row], pick[i_column])])
          if (i_row == 0):
            c = a/rock
          elif (i_row == 1):
            c = a/paper
          else:
            c = a/scissors
          row[i_column] = float(c)
    return (tMatrixL)


def showstats(wmode, lmode):
  x = datetime.datetime.now()
  if (lmode > wmode):
      line = 'Computer Won! with %s' % lmode, ' You scored %s' % wmode
      with open('s19432_markov_result.txt', 'a') as f:
          f.write(x.strftime("%m/%d/%Y, %H:%M:%S "))
          for l in line:
              f.write(l)
          f.write('\n')

      print("Computer Won!")
  else:
      line2 = 'You Won! with %s' % wmode, ' Computer scored %s' % lmode
      with open('s19432_markov_result.txt', 'a') as f:
          f.write(x.strftime("%m/%d/%Y, %H:%M:%S "))
          for l in line2:
              f.write(l)
          f.write('\n')
      print("You Won!")



def main():
  playAgain = True


  while (playAgain):

    playAgain = False
    Game()
    showstats(won, lose)




def checkStats(result):
  global won
  global lose
  global tie

  if (result == 0):
      won += 1
  elif (result == 1):
      lose += 1
  else:
      tie += 1

main()