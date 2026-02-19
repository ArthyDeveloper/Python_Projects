import random, os

def main():
  choices = ('X', 'O')
  board = {
    'A1':'-',
    'A2':'-',
    'A3':'-',
    'B1':'-',
    'B2':'-',
    'B3':'-',
    'C1':'-',
    'C2':'-',
    'C3':'-',
  }
  
  def checkCombinations(player):
    symbol = '-'
    if player:
      symbol = 'X'
    else:
      symbol = 'O'

    combinations = [
      # Horizontal
      (board['A1'], board['B1'], board['C1']),
      (board['A2'], board['B2'], board['C2']),
      (board['A3'], board['B3'], board['C3']),

      # Vertical
      (board['A1'], board['A2'], board['A3']),
      (board['B1'], board['B2'], board['B3']),
      (board['C1'], board['C2'], board['C3']),

      # Diagonal
      (board['A1'], board['B2'], board['C3']),
      (board['A3'], board['B2'], board['C1'])
    ]
    
    for combination in combinations:
      if combination[0] == combination[1] == combination[2] and combination[0] != '-' and combination[1] != '-' and combination[2] != '-':
        print(f'{symbol} is the winner!')
        return True
      else:
        continue
    
    return False

  def getFirstPlayer():
    isX = True
    symbol = random.choice(choices)
    if symbol != 'X':
      isX = False
    return isX
  
  def turn(playerX):
    if playerX:
      print(f'It\'s X turn.')
    else:
      print(f'It\'s O turn.')

    cell = input('Cell to change: ')
    return cell
    #isPlayerX = not playerX
    #return isPlayerX
  
  def drawBoard():
    #os.system('cls')
    '''
      A   B   C
    '   |   |   \n',
    ' - | - | - \n',
    '___|___|___\n',
    '   |   |   \n',
    ' - | - | - \n',
    '___|___|___\n',
    '   |   |   \n',
    ' - | - | - \n',
    '   |   |   \n')
    '''
    print(
      f'    |   |   \n',
      f' {board['A1']} | {board['B1']} | {board['C1']} \n',
      f'___|___|___\n',
      f'   |   |   \n',
      f' {board['A2']} | {board['B2']} | {board['C2']} \n',
      f'___|___|___\n',
      f'   |   |   \n',
      f' {board['A3']} | {board['B3']} | {board['C3']} \n',
      f'   |   |   \n')
  
  def changeBoard(change, isPlayerX):
    try:
      if board[change.upper()] == '-':
        if isPlayerX:
          board[change.upper()] = 'X'
        else:
          board[change.upper()] = 'O'
        
        return True
      else:
        return False
    except(KeyError):
      return False
  
  isPlayerX = getFirstPlayer()
  drawBoard()
  while True:
    #isPlayerX = turn(isPlayerX)
    cell = turn(isPlayerX)
    changed = changeBoard(cell, isPlayerX)
    if changed:
      finish = checkCombinations(isPlayerX)
      if finish:
        break
      else:
        isPlayerX = not isPlayerX
      drawBoard()
    else:
      drawBoard()

if __name__ == '__main__':
  main()
